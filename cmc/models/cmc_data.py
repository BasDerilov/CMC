from typing import Any
from pydantic import BaseModel


class CmcConfigModel(BaseModel):
    minecraft: dict[str, str]
    plugins: dict[str, Any]


class CmcPackageModel(BaseModel):
    name: str
    game_version: str
    api: str
    server_jar: str
    curse_plugins: list[str]
    url_plugins: dict[str, str]
