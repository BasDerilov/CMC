"""gcp_mc is a tool for quicly spooling up minecraft servers locally or on Google Cloud
Platform

"""


import docker
from pick import pick
from modules.minecraft import (
    configure_plugins,
    configure_server,
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
    configure_server()
    configure_plugins()

    print(action)
    if action[1] == 0:
        client = docker.from_env()

    print("gcp_mc WORKS!")
