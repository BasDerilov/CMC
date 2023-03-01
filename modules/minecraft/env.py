from .scripts.Dynmap_config import Dynmap
from .scripts.Minecraft_config import Minecraft
from utils.home_env import MODULES_DIR, require_var


# Directory variables
MODULE_DIR = MODULES_DIR.joinpath("minecraft")
SERVER_DIR = MODULE_DIR.joinpath("server")
SERVER_PLUGINS_DIR = SERVER_DIR.joinpath("plugins")
CONFIG_DIR = MODULE_DIR.joinpath("config")

# Minecraft specific variables
CURSE_API = "https://api.curseforge.com"
GAME_VERSION = "1.19.3"
MINECRAFT_SERVER_IMAGE = "openjdk:17.0.1-jdk-slim"
CURSEFORGE_API_KEY = require_var("CURSE_API_KEY")
minecraft_config = Minecraft.from_env()

# Database variables
DATABASE_IMAGE = "mysql:oracle"
dynmap_config = Dynmap.from_env()
