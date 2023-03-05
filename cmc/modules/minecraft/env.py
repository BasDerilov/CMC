from ..utils import require_var


# Minecraft specific constants
CURSE_API = "https://api.curseforge.com"
GAME_VERSION = "1.19.3"
MINECRAFT_SERVER_IMAGE = "openjdk:17.0.1-jdk-slim"
CURSEFORGE_API_KEY = require_var("CURSE_API_KEY")


# Database constants
DATABASE_IMAGE = "mysql:oracle"
