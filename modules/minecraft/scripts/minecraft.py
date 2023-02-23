from .env import MINECRAFT_SERVER_IMAGE, PORTS, SERVER_DIR, as_tcp_ports
from utils import logging as log


def start_minecraft_docker(client):
    minecraft_container = client.containers.run(
        MINECRAFT_SERVER_IMAGE,
        "java -Dcom.mojang.eula.agree=true -jar server.jar",
        volumes=[f"{SERVER_DIR.absolute().resolve()}:/minecraft:rw"],
        ports=as_tcp_ports(PORTS),
        detach=True,
        working_dir="/minecraft",
    )

    log.started(f"container started with id: {minecraft_container.short_id}")
