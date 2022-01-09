# Original License from https://github.com/athul/waka-readme

# The MIT License (MIT)

# Copyright (c) 2020 ATHUL CYRIAC AJAY

# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import re
import os
import progress

START_COMMENT = "<!--START_SECTION:progress-->"
END_COMMENT = "<!--END_SECTION:progress-->"
GRAPH_LENGTH = 25
listReg = f"{START_COMMENT}[\\s\\S]+{END_COMMENT}"

WORKSPACE = os.getenv("GITHUB_WORKSPACE")
blocks = "░▒▓█"


def make_graph(percent: float, block: str) -> str:
    divs = len(block) - 1
    graph = block[-1] * int(percent / 100 * GRAPH_LENGTH + 0.5 / divs)
    remainder_block = int(
        (percent / 100 * GRAPH_LENGTH - len(graph)) * divs + 0.5
    )
    if remainder_block > 0:
        graph += block[remainder_block]
    graph += block[0] * (GRAPH_LENGTH - len(graph))
    return graph


def get_stats() -> str:
    lang_data = progress.get_progress()
    data_list = []
    for lang, percent in lang_data.items():
        # following line provides a neat finish
        fmt_percent = format(percent, "0.2f").zfill(5)
        data_list.append(
            f"{lang}{' '*(16-len(lang))}{make_graph(float(percent), blocks)}  "
            f" {fmt_percent} % "
        )
    data = "\n".join(data_list)

    return "```text\n" + data + "\n```"


def read_readme() -> str:
    with open(f"{WORKSPACE}/README.md", "r") as file:
        content = file.read()
    return content


def update_readme(content: str):
    with open(f"{WORKSPACE}/README.md", "w") as file:
        file.write(content)


def generate_new_readme(stats: str, readme: str) -> str:
    stats_in_readme = f"{START_COMMENT}\n{stats}\n{END_COMMENT}"
    return re.sub(listReg, stats_in_readme, readme)


if __name__ == "__main__":
    rmdm = read_readme()
    new_readme = generate_new_readme(stats=get_stats(), readme=rmdm)
    if new_readme != rmdm:
        update_readme(content=new_readme)
