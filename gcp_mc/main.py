import os
from modules.palmsbet_mc.scripts.download_bins import download_deps
from modules.palmsbet_mc.scripts.dynmap import configure_dynmap
import lib.utils.env as env
import lib.utils.logging as log
from pick import pick


def main():
    
    action = pick(["start-locally", "deploy-to-cloud"], "Choose server deployment action", default_index=0)
    
    log.success(f"Action: {action}")
    log.started("Reading data from json")
    exit_code = env.set_vars_from_json(f"{env.ENV_DIR}/lcl.json")
    if exit_code == 0 : {log.success("Successfully read environment from file")}
    
    # download_bin("https://api.papermc.io/v2/projects/paper/versions/1.19.3/builds/409/downloads/paper-1.19.3-409.jar", f"{os.path.curdir}/server.mc.jar")
    download_deps()
    configure_dynmap("palmsbet-123", "dynmap", "localhost", "3306", "dynamp-t")
    
    print("gcp_mc WORKS!")
