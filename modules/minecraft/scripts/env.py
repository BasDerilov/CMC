from utils import env
from .config import Config


def filter_ports(config: dict):
    ports = []
    for i in config:
        if str.find(i, "port") != -1 and config[i].isnumeric():
            ports.append(config[i])

    return ports


def as_tcp_ports(ports: list) -> dict:
    tcp_ports = {}
    for port in ports:
        tcp_ports[f"{port}/tcp"] = port

    return tcp_ports


# Directory variables
MODULE_DIR = env.MODULES_DIR.joinpath("minecraft")
SERVER_DIR = MODULE_DIR.joinpath("server")
SERVER_PLUGINS_DIR = SERVER_DIR.joinpath("plugins")
CONFIG_DIR = MODULE_DIR.joinpath("config")

# Minecraft specific variables
CURSE_API = "https://api.curseforge.com"
GAME_VERSION = "1.19.3"
MINECRAFT_SERVER_IMAGE = "openjdk:17.0.1-jdk-slim"
CURSEFORGE_API_KEY = env.require_var("CURSE_API_KEY")

# Database variables
DATABASE_IMAGE = "mysql:oracle"
MYSQL_SETTINGS = {"MYSQL_ROOT_PASSWORD": env.require_var("MYSQL_ROOT_PASSWORD")}

PORTS = set()

mc = filter_ports(Config.get_data(CONFIG_DIR.joinpath("server.properties.json")))
dynmap = filter_ports(
    Config.get_data(CONFIG_DIR.joinpath("dynmap.configuration.json"))["storage"]
)

for i in [*mc, *dynmap]:
    PORTS.add(i)
