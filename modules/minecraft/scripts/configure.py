import json
from pathlib import Path
from .utils import deep_update, write_as_config, write_as_yml


def configure_server(server_config_path: Path, server_dir: Path, **kwargs):

    with open(server_config_path, "r") as properties:

        configuration_object: dict = json.load(properties)
        configuration_object = deep_update(configuration_object, kwargs)
        stripped_suffix_file = server_config_path.with_suffix("").name
        destinatio_path = server_dir.joinpath(stripped_suffix_file)

        write_as_config(destinatio_path, configuration_object)


def configure_plugin(plugin_config_path: Path, server_dir: Path, **kwargs):

    with open(plugin_config_path, "r") as config:

        configuration_object: dict = json.load(config)
        configuration_object = deep_update(configuration_object, kwargs)
        destination_path = server_dir.joinpath(
            Path(
                plugin_config_path.parts[-3],
                plugin_config_path.parts[-2],
                plugin_config_path.parts[-1],
            )
        )

        destination_path = destination_path.with_suffix("")
        write_as_yml(destination_path, configuration_object)
