from pathlib import Path

from .utils import ensure_dirs
from ..env import dynmap_config, minecraft_config


def configure_server(server_config_path: Path):
    ensure_dirs(server_config_path)

    minecraft_config.write_as_config(server_config_path)


def configure_plugins(plugin_config_path: Path):
    ensure_dirs(plugin_config_path)

    dynmap_config.write_as_yml(plugin_config_path)
