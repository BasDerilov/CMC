import os
import json
import shutil
import requests
from pathlib import Path
from tqdm.auto import tqdm

import lib.utils.logging as log

from lib.utils.env import CURSEFORGE_API_KEY
from modules.palmsbet_mc.scripts.env import (
    CURSE_API, GAME_VERSION, MODULE_DIR, SERVER_DIR, SERVER_PLUGINS_DIR)




def download_bin(url: str, location: Path, name: str):
    
    if not os.path.exists(location):
        os.makedirs(location)

    with requests.get(url, stream=True) as response:
        
        total_length = int(response.headers.get("Content-Length"))

        if response.status_code != 200:
            log.failure(f"response code for {url} was {response.status_code}")
            return
            
        print(name)
        with tqdm.wrapattr(response.raw, "read", total=total_length, desc=f"Downloading ")as raw:
            
            file_path = location.joinpath(name)
            with open(file_path, 'wb') as file:
                shutil.copyfileobj(raw, file)

    log.success(f"wrote file {file_path}")

def download_curse_resource(slug: str):

    log.started(f"fetching {slug}")

    headers = {
        'Accept': 'application/json',
        'x-api-key': CURSEFORGE_API_KEY
    }

    responese = requests.get(f'{CURSE_API}/v1/mods/search', params={
        'gameId': '432',
        "slug": slug
    }, headers=headers)

    if responese.status_code != 200:
        log.failure(
            f"curse resource {slug} returned status code {responese.status_code}")
        return

    responese = responese.json()['data'][0]

    mod_id = responese["id"]
    files_index: list = responese["latestFilesIndexes"]
    file_id = next(
        (x for x in files_index if x['gameVersion'] == GAME_VERSION), None)["fileId"]

    responese = requests.get(
        f'{CURSE_API}/v1/mods/{mod_id}/files/{file_id}', headers=headers)

    if responese.status_code != 200:
        log.failure(
            f"curse resource file for {slug} returned status code {responese.status_code}")
        return

    responese = responese.json()
    download_url = responese['data']['downloadUrl']
    file_name = responese['data']["fileName"]
    
    download_bin(download_url, SERVER_PLUGINS_DIR, file_name)


def download_deps(config_path=MODULE_DIR.joinpath("server.json")):

    log.started("reading palmsbet-mc dependencies")

    with open(config_path, "r") as f:
        deps = json.load(f)

        download_bin(deps["server"], SERVER_DIR, "server.jar")

        plugins = deps["plugins"]

        for plugin in plugins:
            download_curse_resource(plugin)
