DEFAULT_SERVER_JAR = "https://api.papermc.io/v2/projects/paper/versions/1.19.3\
/builds/448/downloads/paper-1.19.3-448.jar"
DEFAULT_GAME_VERSION = "1.19.3"
CURSE_API = "https://api.curseforge.com"


class CmcPackage:

    name: str
    game_version: str
    server_jar: str
    curse_plugins: list[str]
    url_plugins: dict[str, str]

    def __init__(
        self,
        name: str,
        game_version: str = DEFAULT_GAME_VERSION,
        api: str = CURSE_API,
        curse_plugins: list[str] = None,
        url_plugins: dict[str, str] = None,
        server_jar: str = DEFAULT_SERVER_JAR,
    ) -> None:

        self.name = name
        self.game_version = game_version
        self.api = api
        self.server_jar = server_jar

        if curse_plugins is None:
            self.curse_plugins = []
        else:
            self.curse_plugins = curse_plugins

        if url_plugins is None:
            self.url_plugins = {}
        else:
            self.url_plugins = url_plugins
