from pathlib import Path
from utils import logging as log


class Minecraft:
    """A class represented configuration for a minecraft server

    Returns:
        Minecraft: A minecraft configuration object
    """

    configuration: dict

    def __init__(self, *args, **kwargs):
        """Create a minecraft configuration manually"""
        self.configuration = kwargs
        self.configuration.storage = args

        return self

    @classmethod
    def from_env(self, cls, **kwargs):
        """creates a minecraft configuration from the current environment

        Returns:
            minecraft: minecraft configuration object
        """

        conf_dict = {
            "rcon.port": kwargs.pop("RCON_PORT", "25575"),
            "gamemode": kwargs.pop("GAME_MODE", "25575"),
            "level-name": kwargs.pop("LEVEL_NAME", "world"),
            "enable-query": kwargs.pop("ENABLE_QUERY", "false"),
            "query.port": kwargs.pop("QUERY_PORT", "25565"),
            "pvp": kwargs.pop("ENABLE_PVP", "true"),
            "difficulty": kwargs.pop("DIFFICULTY", "easy"),
            "max-players": kwargs.pop("MAX_PALYERS", "20"),
            "online-mode": kwargs.pop("ONLINE_MODE", "true"),
            "view-distance": kwargs.pop("VIEW_DISTANCE", "10"),
            "server-port": kwargs.pop("SERVER_PORT", "25565"),
            "enable-rcon": kwargs.pop("ENABLE_RCON", "false"),
            "white-list": kwargs.pop("ENABLE_WHITELIST", "false"),
            "max-world-size": kwargs.pop("MAX_WORLD_SIZE", "29999984"),
            "rcon_password": kwargs.pop("RCON_PASSWORD"),
        }

        return cls(
            conf_dict,
            *kwargs,
        )

    @classmethod
    def write_as_config(self, destination: Path):
        log.started(f"generating {destination}")

        with open(destination, "w+") as file:
            data: dict = self.configuration

            for prop in data:
                print(f"{prop}={data[prop]}")

                file.write(f"{prop}={data[prop]}\n")

        log.success(f"generated file {destination} with success")
