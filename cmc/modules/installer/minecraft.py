import json
from pathlib import Path
from cmc.models import CmcConfigModel, CmcPackageModel
from cmc.modules.utils import (
    ensure_dirs,
    deep_update,
    write_as_yml,
    write_as_config,
    Downloader,
)
from .console import err_console, console


class Minecraft:

    package = CmcPackageModel
    conf: CmcConfigModel
    server_dir: Path
    downloader: Downloader

    # MINECRAFT_SERVER_IMAGE = "openjdk:17.0.1-jdk-slim"
    # # Database constants
    # DATABASE_IMAGE = "mysql:oracle"

    # TODO Rework this entire pile of garbage to install only minecraft
    # NOTE Should need only a package and config data models
    # NOTE Wont need a curse API key, for this migraine check installer/plugin.py
    # NOTE No need for dynamic file path handling bananza. Just use relative paths

    # NOTE The syntax errors are expected, I am too tired to finish this now

    def __init__(self, package: CmcPackageModel, config: CmcConfigModel) -> None:
        self.package = package
        self.conf = config
        self.server_dir = Path(package.name)
        self.downloader = Downloader(package, console, err_console)

    def install(self):
        console.rule(f'Installing "{self.package.name}"', style="info")
        ensure_dirs(self.server_dir)
        self.downloader.download([self.package.server_jar], self.server_dir)
        write_as_config(
            self.server_dir.joinpath("server.properties"), self.conf.minecraft
        )

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
