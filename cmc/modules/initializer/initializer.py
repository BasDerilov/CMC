import json
from pathlib import Path
from ..exceptions import CmcConfigExists, CmcPackageExist
from .console import err_console, console


class Initializer:

    package_state: dict
    config_state: dict

    DEFAULT_SERVER_JAR = "https://api.papermc.io/v2/projects/paper/versions/1.19.3\
/builds/431/downloads/paper-1.19.3-431.jar"

    def __init__(self, name: str) -> None:

        self.package_state = {
            "name": name,
            "server-jar": self.DEFAULT_SERVER_JAR,
            "plugins": [],
        }

        self.config_state = {"minecraft": {}, "plugins": {"dynmap": {}}}

    def initialize_new_server(self):
        console.rule(f'Initializing "{self.package_state["name"]}"', style="info")

        cmc_package = Path("cmc-package.json")
        cmc_config = Path("cmc-config.json")

        if cmc_package.is_file():
            err_console.print("You already have a cmc-package file", style="warning")
            raise CmcPackageExist

        with open(cmc_package, "w+") as f:
            json.dump(self.package_state, f, indent=4)

        console.log("cmc-package created successfully", style="info")

        if cmc_config.is_file():
            err_console.print("You already have a cmc-config file", style="warning")
            raise CmcConfigExists

        with open(cmc_config, "w+") as f:
            json.dump(self.config_state, f, indent=4)

        console.log("cmc-config created successfully", style="info")
