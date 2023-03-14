import collections
import json
import os
from pathlib import Path

import yaml
from ..exceptions import MissingEnvVariable


def set_vars_from_json(file: str):
    with open(file) as env_file:
        data = json.load(env_file)

        for var in data:
            print(f"setting {var}={data[var]}")
            os.environ.setdefault(var, data[var])

    return 0


def require_var(var_name: str) -> str:
    env_var = os.environ.get(var_name)

    if env_var is None:
        print(f"Enter a value for: {var_name}")

        raise MissingEnvVariable(f"Missing environment variable ${var_name}")

    return env_var


def ensure_dirs(*args: Path):
    for path in args:
        if not os.path.exists(path):
            os.makedirs(path)


def as_tcp_ports(ports: list) -> dict:
    tcp_ports = {}
    for port in ports:
        tcp_ports[f"{port}/tcp"] = port

    return tcp_ports


def write_as_config(destination: Path, configuration_object: dict):

    with open(destination, "w+") as file:
        for prop in configuration_object:
            file.write(f"{prop}={configuration_object[prop]}\n")


def write_as_yml(destination: Path, configuration_object: dict):

    with open(destination, "w+") as file:
        data: dict = configuration_object
        yaml.dump(data, file)


def deep_update(disctionary, new_data):
    for k, v in new_data.items():
        if isinstance(v, collections.abc.Mapping):
            disctionary[k] = deep_update(disctionary.get(k, {}), v)
        else:
            disctionary[k] = v
    return disctionary
