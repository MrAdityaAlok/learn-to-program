#!/usr/bin/env python3

import argparse
import json
import subprocess
from json import load as json_load
from pathlib import Path
from typing import Dict, List, NewType, Union

PackageName = NewType("PackageName", str)
SHA256Sum = NewType("SHA256Sum", str)
Dependencies = NewType("Dependencies", List[PackageName])

DepInfo = Dict[PackageName, Dict[str, Union[SHA256Sum, Dependencies]]]

TERMUX_AVAILABLE_PKGS = list()


class DependencyInfo:
    def __init__(self, cabal_plan: Path, cabal_file: Path) -> None:
        """Parse dependencies of cabal package by reading it's plan.json.

        Args:
            cabal_plan: path to cabal's plan.json for the package.
        """

        def read_cabal_plan() -> Dict:
            if not cabal_plan.exists():
                raise ValueError(f"{cabal_plan}: No such file or directory.")
            with open(cabal_plan) as f:
                plan = json_load(f)
            return plan["install-plan"]

        self._deps_info: DepInfo = dict()
        self._cabal_file = cabal_file
        self._extract_deps_info(read_cabal_plan())

    @property
    def dependencies_info(self) -> DepInfo:
        """Returns package's dependencies info."""

        return self._deps_info

    def _extract_external_dep(self, dep: Dict):
        def is_external_dependency(dependency_id: str) -> bool:
            # Every external dependency has a hash appended at last to it's id.
            # So we check if last string is a valid hash then it must be an external pkg.
            hash = dependency_id.split("-")[-1]
            if len(hash) == 64 and len(bytes.fromhex(hash)) == 32:
                return True
            return False

        def pkg_name_from_id(dependency_id: str) -> str:
            dep_name_version = dependency_id[
                :-65
            ]  # Format: <dep_name>-<dep_version>
            return dep_name_version[: dep_name_version.rfind("-")]

        def extract_depends() -> List[PackageName]:
            dependencies = list()
            if "depends" in dep:
                for dep_id in dep["depends"]:
                    if is_external_dependency(dep_id):
                        # Id is in format: <pkg-name>-<pkg-version>-<sha256 hash>
                        dependencies.append(
                            PackageName(pkg_name_from_id(dep_id))
                        )
            else:
                try:
                    for dep_id in dep["components"]["lib"]["depends"]:
                        if is_external_dependency(dep_id):
                            # Id is in format: <pkg-name>-<pkg-version>-<sha256 hash>
                            dep_name_version = dep_id[:-65]
                            dep_name = dep_name_version[
                                : dep_name_version.rfind("-")
                            ]
                            dependencies.append(dep_name)
                except KeyError:
                    pass
            return dependencies

        self._deps_info[PackageName(dep["pkg-name"])] = {
            "src_sha256": SHA256Sum(dep["pkg-src-sha256"]),
            "depends_on": Dependencies(extract_depends()),
        }

    def _extract_deps_info(self, build_plan: Dict) -> None:
        def already_in_termux(dep_name: str) -> bool:
            # print("checking if", dep_name, "is already in termux")
            if dep_name.lower() in TERMUX_AVAILABLE_PKGS:
                # print(f"{dep_name} is already in Termux.")
                return True
            return False

        def is_local_package(dep) -> bool:
            pkg_type = dep["pkg-src"]["type"]
            if pkg_type == "local":
                return True
            return False

        for dep in build_plan:
            if dep["type"] == "configured":
                if is_local_package(dep) or already_in_termux(dep["pkg-name"]):
                    continue
                self._extract_external_dep(dep)
            elif dep["type"] == "pre-existing":
                continue
            else:
                raise ValueError(f"Unknown dependency type: {dep['type']}")


def write_build_file(dependencies_info: DepInfo, termux_packages_dir: Path):
    for dep in dependencies_info:
        subprocess.run(
            args=[
                "./write-haskell-build.sh",
                dep,
                dependencies_info[dep]["src_sha256"],
                f"{','.join(['haskell-' + p for p in dependencies_info[dep]['depends_on']])}",
                termux_packages_dir.as_posix(),
            ]
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extracts dependencies info from cabal plan."
    )
    parser.add_argument(
        "cabal_plan",
        type=Path,
        help="Path to cabal plan file.",
    )
    parser.add_argument(
        "termux_packages_dir",
        type=Path,
        help="Path to directory containing termux packages.",
    )

    parser.add_argument(
        "cabal_file", type=Path, help="Path to .cabal file of package."
    )

    args = parser.parse_args()

    TERMUX_AVAILABLE_PKGS = list(
        pkg.name[8:]  # Remove "haskell-" prefix.
        for pkg in args.termux_packages_dir.glob("haskell-*")
        if pkg.is_dir()
    )

    deps = DependencyInfo(args.cabal_plan, args.cabal_file)
    write_build_file(deps.dependencies_info, args.termux_packages_dir)
    print(json.dumps(deps.dependencies_info, indent=4))
