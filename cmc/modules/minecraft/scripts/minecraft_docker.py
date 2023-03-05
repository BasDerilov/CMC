from ..env import MINECRAFT_SERVER_IMAGE, SERVER_DIR
from ..console import console


def start_minecraft_docker(client):
    minecraft_container = client.containers.run(
        MINECRAFT_SERVER_IMAGE,
        "java -Dcom.mojang.eula.agree=true -jar server.jar",
        volumes=[f"{SERVER_DIR.absolute().resolve()}:/minecraft:rw"],
        detach=True,
        working_dir="/minecraft",
        network_mode="host",
    )

    console.log(
        f"container started with id: {minecraft_container.short_id}", style="info"
    )
