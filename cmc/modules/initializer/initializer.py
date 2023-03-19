import json
from pathlib import Path
from .console import err_console, console
from .config import CmcConfig
from .package import CmcPackage


class Initializer:

    package_state: CmcPackage
    config_state: CmcConfig

    def __init__(self, package: CmcPackage, config: CmcConfig) -> None:

        self.package_state = package
        self.config_state = config

    def initialize_new_server(self):
        console.rule(f'Initializing "{self.package_state.name}"', style="info")

        cmc_package = Path("cmc-package.json")
        cmc_config = Path("cmc-config.json")

        if cmc_package.is_file():
            err_console.log("You already have a cmc-package.json file", style="warning")
        else:
            with open(cmc_package, "w+") as f:
                json.dump(self.package_state.__dict__, f, indent=4)

            console.log("cmc-package created successfully", style="info")

        if cmc_config.is_file():
            err_console.log("You already have a cmc-config.json file", style="warning")

        else:
            with open(cmc_config, "w+") as f:
                json.dump(self.config_state.__dict__, f, indent=4)

            console.log("cmc-config created successfully", style="info")
