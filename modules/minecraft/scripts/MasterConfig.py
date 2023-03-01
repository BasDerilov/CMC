import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class MasterConfig:
    def __init__(self, **kwargs):

        self.configuration = kwargs

    @classmethod
    def from_env(cls, **kwargs):

        conf_dict = {
            "rcon.port": kwargs.pop("rcon_port", "25575"),
            "gamemode": kwargs.pop("game_mode", "survival"),
            "level-name": kwargs.pop("level_name", "world"),
            "enable-query": kwargs.pop("enable_query", "false"),
            "query.port": kwargs.pop("query_port", "25565"),
            "pvp": kwargs.pop("enable_pvp", "true"),
            "difficulty": kwargs.pop("difficulty", "easy"),
            "max-players": kwargs.pop("max_palyers", "20"),
            "online-mode": kwargs.pop("online_mode", "true"),
            "view-distance": kwargs.pop("view_distance", "10"),
            "server-port": kwargs.pop("server_port", "25565"),
            "enable-rcon": kwargs.pop("enable_rcon", "false"),
            "white-list": kwargs.pop("enable_whitelist", "false"),
            "max-world-size": kwargs.pop("max_world_size", "29999984"),
            "rcon_password": kwargs.pop("rcon_password", ""),
        }

        return cls(*conf_dict, *kwargs)

    def write_as_config(self, destination: Path):
        logger.info(f"generating {destination}")

        with open(destination, "w+") as file:

            for prop in self.configuration:
                print(f"{prop}={self.configuration[prop]}")

                file.write(f"{prop}={self.configuration[prop]}\n")

        logger.info(f"generated file {destination} with success")
