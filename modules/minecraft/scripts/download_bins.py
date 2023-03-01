import json
import logging
import shutil
from .utils import ensure_dirs
import requests
from pathlib import Path
from tqdm.auto import tqdm

from ..env import (
    CURSE_API,
    GAME_VERSION,
    SERVER_DIR,
    SERVER_PLUGINS_DIR,
    CURSEFORGE_API_KEY,
)

logger = logging.getLogger(__name__)


def download_bin(url: str, file_path: Path):

    ensure_dirs(file_path)

    with requests.get(url, stream=True) as response:

        total_length = int(response.headers.get("Content-Length"))

        if response.status_code != 200:
            logger.error(f"response code for {url} was {response.status_code}")
            return

        print(file_path)
        with tqdm.wrapattr(
            response.raw, "read", total=total_length, desc="Downloading "
        ) as raw:
            with open(file_path, "wb") as file:
                shutil.copyfileobj(raw, file)

    logger.info(f"downloaded file {file_path}")


def download_curse_resource(slug: str):
    logger.info(f"fetching {slug}")

    headers = {"Accept": "application/json", "x-api-key": CURSEFORGE_API_KEY}

    responese = requests.get(
        f"{CURSE_API}/v1/mods/search",
        params={"gameId": "432", "slug": slug},
        headers=headers,
        timeout=1000,
    )

    if responese.status_code != 200:

        logger.error(
            f"curse resource {slug} returned status code {responese.status_code}"
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
        logger.error(
            f"curse resource file for {slug}\
                returned status code {responese.status_code}"
        )
        return

    responese = responese.json()
    download_url = responese["data"]["downloadUrl"]
    file_name = responese["data"]["fileName"]

    download_bin(download_url, SERVER_PLUGINS_DIR, file_name)


def download_deps(source_json: Path):
    logger.info("reading palmsbet-mc dependencies")

    with open(source_json, "r") as required_bins:
        deps = json.load(required_bins)

        download_bin(deps["server"], SERVER_DIR, "server.jar")

        plugins = deps["plugins"]

        for plugin in plugins:
            download_curse_resource(plugin)
