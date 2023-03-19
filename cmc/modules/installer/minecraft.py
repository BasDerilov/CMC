import json
import requests
from pathlib import Path
from cmc.models import CmcConfigModel, CmcPackageModel
from cmc.modules.utils import (
    ensure_dirs,
    require_var,
    deep_update,
    write_as_yml,
    write_as_config,
)
from rich.progress import Progress
from .console import err_console, console


class Minecraft:

    CURSE_API_KEY: str
    package = CmcPackageModel
    conf: CmcConfigModel

    # MINECRAFT_SERVER_IMAGE = "openjdk:17.0.1-jdk-slim"
    # # Database constants
    # DATABASE_IMAGE = "mysql:oracle"

    # TODO Rework this entire pile of garbage to install only minecraft
    # NOTE Should need only a package and config data models
    # NOTE Wont need a curse API key, for this migraine check installer/plugin.py
    # NOTE No need for dynamic file path handling bananza. Just use relative paths

    # NOTE The syntax errors are expected, I am too tired to finish this now

    def __init__(
        self,
    ) -> None:
        CONFIG_DIR = Path(".").joinpath("config")
        self.CONFIG_DIR = CONFIG_DIR
        self.PLUGINS_CONFIG_DIR = CONFIG_DIR.joinpath("plugins")
        self.SERVER_PLUGINS_DIR = server_dir.joinpath("plugins")
        self.BINS_SOURCE = CONFIG_DIR.joinpath("server.json")
        self.SERVER_DIR = server_dir
        self.SERVER_CONF_OBJ = server_conf_obj
        self.PLUGIN_CONFIGURATION_OBJS = kwargs

    def install(self):
        console.rule(f'Installing "{self.SERVER_DIR.name}"', style="info")
        ensure_dirs(self.SERVER_DIR, self.SERVER_PLUGINS_DIR)
        self.download_deps(self.BINS_SOURCE)
        self.configure_server(
            self.CONFIG_DIR.joinpath("server.properties.json"),
        )

    def download_bin(self, url: str, file_path: Path):

        with requests.get(url, stream=True) as response:

            total_length = int(response.headers.get("Content-Length"))

            if response.status_code != 200:
                err_console.print(
                    f"response code for {url} was {response.status_code}", style="error"
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

    def download_curse_resource(self, slug: str):
        CURSEFORGE_API_KEY = require_var("CURSE_API_KEY")
        headers = {"Accept": "application/json", "x-api-key": CURSEFORGE_API_KEY}

        responese = requests.get(
            f"{self.CURSE_API}/v1/mods/search",
            params={"gameId": "432", "slug": slug},
            headers=headers,
            timeout=1000,
        )

        if responese.json()["pagination"]["resultCount"] == 0:

            err_console.print(
                f'Curse resource "{slug}" returned 0\
                    matches. Is this the correct name?',
                style="warning",
            )
            return

        responese = responese.json()["data"][0]

        mod_id = responese["id"]
        files_index: list = responese["latestFilesIndexes"]
        file_id = next(
            (x for x in files_index if x["gameVersion"] == self.GAME_VERSION), None
        )["fileId"]

        responese = requests.get(
            f"{self.CURSE_API}/v1/mods/{mod_id}/files/{file_id}",
            headers=headers,
            timeout=10000,
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

        console.log(f"resource url: {download_url}", style="curse")
        self.download_bin(
            download_url, self.SERVER_DIR.joinpath("plugins").joinpath(file_name)
        )

    def download_deps(self, source_json: Path):

        with open(source_json, "r") as required_bins:
            deps = json.load(required_bins)

            console.log("downloading minecraft server binary", style="info")
            try:
                self.download_bin(
                    deps["server"], self.SERVER_DIR.joinpath("server.jar")
                )
            except Exception:
                pass

            plugins = deps["plugins"]

            console.log("downloading curse resources", style="curse")
            for plugin in plugins:
                self.download_curse_resource(plugin)

    def configure_server(self, defaul_config: Path, **kwargs):

        with open(defaul_config, "r") as properties:

            configuration_object: dict = json.load(properties)

            configuration_object = deep_update(configuration_object, kwargs)

            stripped_suffix_file = defaul_config.with_suffix("").name
            destinatio_path = self.SERVER_DIR.joinpath(stripped_suffix_file)

            write_as_config(destinatio_path, configuration_object)

    def configure_plugin(self, plugin_config_path: Path, server_dir: Path, **kwargs):

        with open(plugin_config_path, "r") as config:

            configuration_object: dict = json.load(config)
            configuration_object = deep_update(configuration_object, kwargs)
            destination_path = server_dir.joinpath(
                Path(
                    plugin_config_path.parts[-3],
                    plugin_config_path.parts[-2],
                    plugin_config_path.parts[-1],
                )
            )

            destination_path = destination_path.with_suffix("")
            write_as_yml(destination_path, configuration_object)
