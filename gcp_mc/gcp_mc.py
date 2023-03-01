"""gcp_mc is a tool for quicly spooling up minecraft servers locally or on Google Cloud
Platform

"""


import docker
from minecraft import start_minecraft_docker
from minecraft import start_db_docker
from pick import pick
from modules.minecraft import (
    download_deps,
)


def main():
    """The main entrypoint of gcp_mc"""
    action = pick(
        ["start-locally", "deploy-to-cloud"],
        "Choose server deployment action",
        default_index=0,
    )

    download_deps()

    print(action)
    if action[1] == 0:
        client = docker.from_env()
        start_minecraft_docker(client)
        start_db_docker(client)

    print("gcp_mc WORKS!")
