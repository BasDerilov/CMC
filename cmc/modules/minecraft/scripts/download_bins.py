import json
import requests
from pathlib import Path
from rich.progress import Progress
from ..env import (
    CURSE_API,
    GAME_VERSION,
    CURSEFORGE_API_KEY,
)
from ..console import console, err_console


def download_bin(url: str, file_path: Path):

    with requests.get(url, stream=True) as response:

        total_length = int(response.headers.get("Content-Length"))

        if response.status_code != 200:
            console.print(
                f"response code for {url} was {response.status_code}", style="warning"
            )
            return

        with Progress() as progress:
            console.print(file_path.name, style="info")
            download_task = progress.add_task("", total=total_length)

            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    progress.update(download_task, advance=1024)
                    if chunk:
                        file.write(chunk)

    console.line()


def download_curse_resource(slug: str, server_dir: Path):
    headers = {"Accept": "application/json", "x-api-key": CURSEFORGE_API_KEY}

    responese = requests.get(
        f"{CURSE_API}/v1/mods/search",
        params={"gameId": "432", "slug": slug},
        headers=headers,
        timeout=1000,
    )

    if responese.json()["pagination"]["resultCount"] == 0:

        err_console.print(
            f'Curse resource "{slug}" returned 0 matches. Is this the correct name?',
            style="warning",
        )
        return

    responese = responese.json()["data"][0]

    mod_id = responese["id"]
    files_index: list = responese["latestFilesIndexes"]
    file_id = next((x for x in files_index if x["gameVersion"] == GAME_VERSION), None)[
        "fileId"
    ]

    responese = requests.get(
        f"{CURSE_API}/v1/mods/{mod_id}/files/{file_id}", headers=headers, timeout=10000
    )

    if responese.status_code != 200:
        err_console.print(
            f"curse resource file for {slug}\
                returned status code {responese.status_code}"
        )
        return

    responese = responese.json()
    download_url = responese["data"]["downloadUrl"]
    file_name = responese["data"]["fileName"]

    download_bin(download_url, server_dir.joinpath("plugins").joinpath(file_name))


def download_deps(source_json: Path, server_dir: Path):

    with open(source_json, "r") as required_bins:
        deps = json.load(required_bins)

        console.log("downloading minecraft server binary", style="info")
        download_bin(deps["server"], server_dir.joinpath("server.jar"))

        plugins = deps["plugins"]

        console.log("downloading curse resources", style="curse")
        for plugin in plugins:
            download_curse_resource(plugin, server_dir)
