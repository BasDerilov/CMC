from typing import Any


class CmcConfig:
    minecraft: dict[str, str]
    plugins: dict[str, Any]

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
