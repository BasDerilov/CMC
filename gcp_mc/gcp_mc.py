from pick import pick
import docker
from lib.utils.env import MINECRAFT_SERVER_IMAGE
import lib.utils.logging as log

from modules.palmsbet_mc.scripts.configure import configure_plugins, configure_server
from modules.palmsbet_mc.scripts.download_bins import download_deps
from modules.palmsbet_mc.scripts.env import SERVER_DIR


def main():

    action = pick(["start-locally", "deploy-to-cloud"],
                  "Choose server deployment action", default_index=0)

    download_deps()
    configure_server()
    configure_plugins()

    print(action)
    if action[1] == 0:
        client = docker.from_env()
        container = client.containers.run(MINECRAFT_SERVER_IMAGE,"java -Dcom.mojang.eula.agree=true -jar server.jar", volumes=[
                                          f"{SERVER_DIR.absolute().resolve()}:/minecraft:rw"], ports={"25565/tcp": 25565}, detach=True, network_mode="bridge", working_dir="/minecraft")
        
        log.success(f"container started with id: {container.short_id}") 

    print("gcp_mc WORKS!")
