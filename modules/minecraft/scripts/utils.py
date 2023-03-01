import logging
import os
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)


def as_tcp_ports(ports: list) -> dict:
    tcp_ports = {}
    for port in ports:
        tcp_ports[f"{port}/tcp"] = port

    return tcp_ports


def ensure_dirs(*args: Path):
    for path in args:
        if not os.path.exists(path):
            os.makedirs(path)


def write_as_config(destination: Path, configuration_object: dict):
    logger.info(f"generating {destination}")

    with open(destination, "w+") as file:

        for prop in configuration_object:
            print(f"{prop}={configuration_object[prop]}")

            file.write(f"{prop}={configuration_object[prop]}\n")

    logger.info(f"generated file {destination} with success")


def write_as_yml(destination: Path, configuration_object: dict):
    logger.started(f"generating {destination}")

    with open(destination, "w+") as file:
        data: dict = configuration_object
        yaml.dump(data, file)

    logger.success(f"generated file {destination} with success")
