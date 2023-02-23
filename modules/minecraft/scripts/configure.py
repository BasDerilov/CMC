import os
from pathlib import Path
from .env import CONFIG_DIR, SERVER_DIR, SERVER_PLUGINS_DIR
from .config import Config


def configure_server():
    ensure_dirs(SERVER_DIR)

    conf_src = CONFIG_DIR.joinpath("server.properties.json")
    conf_tgt = SERVER_DIR.joinpath("server.properties")

    Config.write_properties(conf_src, conf_tgt)


def configure_plugins():
    ensure_dirs(SERVER_DIR, SERVER_PLUGINS_DIR.joinpath("dynmap"))

    conf_src = CONFIG_DIR.joinpath("dynmap.configuration.json")
    conf_tgt = SERVER_PLUGINS_DIR.joinpath("dynmap").joinpath("configuration.txt")

    Config.write_yml(conf_src, conf_tgt)


def ensure_dirs(*args: Path):
    for path in args:
        if not os.path.exists(path):
            os.makedirs(path)
