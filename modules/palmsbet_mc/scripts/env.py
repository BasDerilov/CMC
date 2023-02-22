from lib.utils import env

MODULE_DIR = env.MODULES_DIR.joinpath("palmsbet_mc")
SERVER_DIR = MODULE_DIR.joinpath("server")
SERVER_PLUGINS_DIR = SERVER_DIR.joinpath("plugins")
CONFIG_DIR = MODULE_DIR.joinpath("config")
CURSE_API = "https://api.curseforge.com"
GAME_VERSION = "1.19.3"