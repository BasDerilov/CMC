import os
from pathlib import Path
from .scripts.utils import ensure_dirs
from .scripts.download_bins import download_deps
from .scripts.configure import configure_plugin, configure_server


def create_server(SERVER_DIR: Path, server_conf_obj: dict, **kwargs):
    """The function that generates the entire minecaft server environment

    Args:
        SERVER_DIR (Path): the directory under which you wish the server to be created

        server_conf_obj (dict): the configuration object for the server.properties

        kwargs:
            every keyword argument should be named after the thing you wish to
            configure with a configuration object, for example: \n
            dynmap={
                "storage":{
                    "passwrod":"my-strong-password"
                    }
            }\n
            This configuration object will be merged with the existing default one in
            the config folder effectively updating it\n\n
            Make sure the configuration objects comply with the
            structure of the plugin you are trying to configure
    """

    # TODO Clear this mess up and parametrize the containers
    CONFIG_DIR = Path(".").joinpath("config")
    PLUGINS_CONFIG_DIR = CONFIG_DIR.joinpath("plugins")
    SERVER_PLUGINS_DIR = SERVER_DIR.joinpath("plugins")
    BINS_SOURCE = CONFIG_DIR.joinpath("server.json")

    # SERVER_DIR = SERVER_DIR
    ensure_dirs(SERVER_DIR, SERVER_PLUGINS_DIR, SERVER_PLUGINS_DIR.joinpath("dynmap"))
    download_deps(BINS_SOURCE, SERVER_DIR)

    configure_server(
        CONFIG_DIR.joinpath("server.properties.json"), SERVER_DIR, **server_conf_obj
    )

    for plugin, config in kwargs.items():
        config_dir = PLUGINS_CONFIG_DIR.joinpath(plugin)
        config_files = os.listdir(config_dir)

        if len(config_files) > 1:
            raise NotImplementedError(
                "Functionality for more than one \
                    config per plugin hasn't been implemented"
            )

        for config in config_files:
            configure_plugin(config_dir.joinpath(config), SERVER_DIR)


if __name__ == "__main__":
    create_server(Path("server"), {})
