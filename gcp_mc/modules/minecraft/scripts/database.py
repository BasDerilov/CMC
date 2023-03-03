from utils import logging as log
from docker import DockerClient
from ..env import DATABASE_IMAGE


def start_db_docker(client: DockerClient):

    databse_container = client.containers.run(
        DATABASE_IMAGE,
        environment={
            "MYSQL_ROOT_PASSWORD": "123",
            "MYSQL_DATABASE": "dynmap",
            "MYSQL_USER": "dynmap",
            "MYSQL_PASSWORD": "dynmap123",
        },
        detach=True,
        network_mode="host",
    )

    log.started(f"container started with id: {databse_container.short_id}")
