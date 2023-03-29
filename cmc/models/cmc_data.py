from typing import Any
from pydantic import BaseModel


class PluginConfigModel(BaseModel):
    config_file_name: str
    config: dict[str, Any]


class CmcConfigModel(BaseModel):
    minecraft: dict[str, str]
    plugins: dict[str, PluginConfigModel]


class CmcPackageModel(BaseModel):
    name: str
    game_version: str
    api: str
    server_jar: str
    curse_plugins: list[str]
    url_plugins: list[str]
