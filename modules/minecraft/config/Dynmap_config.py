from pathlib import Path
from utils import logging as log
import yaml


class Dynmap:
    configuration: dict

    def __init__(self, *args, **kwargs):
        """Create a dynmap configuration manually"""
        self.configuration = kwargs
        self.configuration.storage = args

        return self

    @classmethod
    def from_env(self, cls, **kwargs):
        """creates a dynmap configuration from the current environment

        Returns:
            Dynmap: dynmap configuration object
        """
        db_name = kwargs.pop("DB_NAME", "dynmap")
        host = kwargs.pop("HOST", "localhost")
        password = kwargs.pop("DB_PASSWORD")
        port = kwargs.pop("PORT", "3306")
        db_type = kwargs.pop("DB_TYPE", "mysql")
        user = kwargs.pop("DB_USER", "dynmap")

        return cls(
            database=db_name,
            hostname=host,
            password=password,
            port=port,
            type=db_type,
            userid=user,
            *kwargs,
        )

    @classmethod
    def write_as_yml(self, destination: Path):
        log.started(f"generating {destination}")

        with open(destination, "w+") as file:
            data: dict = self.configuration
            yaml.dump(data, file)

        log.success(f"generated file {destination} with success")
