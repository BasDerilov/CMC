import json
import os
import requests
import lib.utils.logging as log

MODULE_DIR=os.path.join(os.path.curdir, os.path.pardir)
SERVER_DIR=MODULE_DIR+"/server"
SERVER_PLUGINS_DIR=SERVER_DIR+"/plugins"

def download_bin(url:str, location:str, name:str):
    
    response = requests.get(url)

    if response.status_code == 200:
        with open(f"{location}/{name}", 'wb') as f:
            f.write(response.content)
            log.success(f"wrote file {location}")
    else:
        log.failure(f"response code for {url} was {response.status_code}")
    
def download_deps(config_path=MODULE_DIR):
    
    log.started("reading palmsbet-mc dependencies")
    print(config_path)
    with open(config_path, "r") as f:
        deps = json.load(f)
        
        download_bin(deps["server"], SERVER_DIR, "server.jar")
        
        plugins = vars(deps["plugins"]).items
        
        for plugin in plugins:
            download_bin(deps["plugins"][plugin], SERVER_PLUGINS_DIR, f"{plugin}.jar")
        