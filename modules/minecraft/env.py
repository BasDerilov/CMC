from utils.home_env import MODULES_DIR, require_var


# Module constants
MODULE_DIR = MODULES_DIR.joinpath("minecraft")
CONFIG_DIR = MODULE_DIR.joinpath("config")
PLUGINS_CONFIG_DIR = CONFIG_DIR.joinpath("plugins")

# Minecraft specific constants
CURSE_API = "https://api.curseforge.com"
GAME_VERSION = "1.19.3"
MINECRAFT_SERVER_IMAGE = "openjdk:17.0.1-jdk-slim"
CURSEFORGE_API_KEY = require_var("CURSE_API_KEY")
SERVER_DIR = MODULE_DIR.joinpath("server")
SERVER_PLUGINS_DIR = SERVER_DIR.joinpath("plugins")


# Database constants
DATABASE_IMAGE = "mysql:oracle"
