from json import loads as jsonLoads

from bs4 import BeautifulSoup
from requests import get

DATA = {}


def _get_total_num_of_exercises(track_name: str) -> int:
    track_name = track_name.replace(" ", "")
    return len(
        get(
            f"https://exercism.org/api/v2/tracks/{track_name}/exercises"
        ).json()["exercises"]
    )


def _set_data():
    tracks_data = jsonLoads(
        BeautifulSoup(
            get("https://exercism.io/profiles/MrAditya/solutions").text,
            "html.parser",
        ).find(
            "div",
            class_=(
                "c-react-component"
                " c-react-wrapper-profile-community-solutions-list"
            ),
        )[
            "data-react-data"
        ]
    )["tracks"]
    # print(tracks_data)

    for data in tracks_data:
        track_name = data["slug"]
        if track_name == None:  # All tracks field have 'None' slug.
            continue
        # print(f"Using: {track_name}", end=" ")
        total_exercises = _get_total_num_of_exercises(track_name)
        solved_exercises = data["num_solutions"]
        # print(f"{solved_exercises}/{total_exercises}")
        DATA[track_name.capitalize()] = solved_exercises / total_exercises * 100


def get_progress():
    _set_data()
    return dict(sorted(DATA.items(), key=lambda item: item[1], reverse=True))
