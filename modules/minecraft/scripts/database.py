from docker import DockerClient
from .minecraft_env import DATABASE_IMAGE, PORTS, as_tcp_ports


def start_db_docker(client: DockerClient):
    port_dict = as_tcp_ports(PORTS)

    databse_container = client.containers.run(
        DATABASE_IMAGE, ports=port_dict, detach=True, working_dir="/minecraft"
    )
