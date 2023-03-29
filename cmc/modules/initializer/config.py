from typing import Any


class PluginConfig:
    config_file_name: str
    config: dict[str, Any]

    def __init__(
        self, config_file_name: str = None, config: dict[str, Any] = None
    ) -> None:

        if config_file_name is None:
            self.config_file_name = {}
        else:
            self.config_file_name = config_file_name

        if config is None:
            self.config = {}
        else:
            self.config = config


class CmcConfig:
    minecraft: dict[str, str]
    plugins: dict[str, PluginConfig]

    def __init__(
        self, minecraft: dict[str, str] = None, plugins: dict[str, Any] = None
    ) -> None:

        if minecraft is None:
            self.minecraft = {}
        else:
            self.minecraft = minecraft

        if plugins is None:
            self.plugins = {}
        else:
            self.plugins = plugins
