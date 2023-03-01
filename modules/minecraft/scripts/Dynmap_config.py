from pathlib import Path
from utils import logging as log
import yaml


class Dynmap:
    configuration: dict

    def __init__(self, **kwargs):
        """Create a dynmap configuration manually"""
        self.configuration = kwargs

    @classmethod
    def from_env(cls, **kwargs):
        """creates a dynmap configuration from the current environment

        Returns:
            Dynmap: dynmap configuration object
        """

        storage = {
            "database": kwargs.pop("db_name", "dynmap"),
            "host": kwargs.pop("host", "localhost"),
            "password": kwargs.pop("db_password", "dynmap123"),
            "port": kwargs.pop("port", "3306"),
            "type": kwargs.pop("db_type", "mysql"),
            "userid": kwargs.pop("db_user", "dynmap"),
        }

        return cls(storage=storage, **kwargs)

    def write_as_yml(self, destination: Path):
        log.started(f"generating {destination}")

        with open(destination, "w+") as file:
            data: dict = self.configuration
            yaml.dump(data, file)

        log.success(f"generated file {destination} with success")
