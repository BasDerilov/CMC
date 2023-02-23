import docker
from pick import pick
from utils import MINECRAFT_SERVER_IMAGE
from utils import logging as log

from modules.minecraft import (
    configure_plugins,
    configure_server,
    download_deps,
    SERVER_DIR,
)


def main():
    action = pick(
        ["start-locally", "deploy-to-cloud"],
        "Choose server deployment action",
        default_index=0,
    )

    download_deps()
    configure_server()
    configure_plugins()

    print(action)
    if action[1] == 0:
        client = docker.from_env()

    print("gcp_mc WORKS!")
