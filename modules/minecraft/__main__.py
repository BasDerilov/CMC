from .scripts.utils import ensure_dirs
from .env import CONFIG_DIR, PLUGINS_CONFIG_DIR, SERVER_DIR, SERVER_PLUGINS_DIR
from .scripts.download_bins import download_deps
from .scripts.configure import configure_plugin, configure_server


def main():

    # TODO Clear this mess up and parametrize the containers

    # SERVER_DIR = SERVER_DIR
    ensure_dirs(SERVER_DIR, SERVER_PLUGINS_DIR, SERVER_PLUGINS_DIR.joinpath("dynmap"))

    BINS_SOURCE = CONFIG_DIR.joinpath("server.json")

    download_deps(BINS_SOURCE, SERVER_DIR)

    server_custom_configuration = {"rcon.password": input("Choose rcon password:  ")}

    configure_server(
        CONFIG_DIR.joinpath("server.properties.json"),
        SERVER_DIR,
        **server_custom_configuration
    )

    dynmap_custom_configuration = {
        "storage": {"password": input("Choose dynmap database password:  ")}
    }
    configure_plugin(
        PLUGINS_CONFIG_DIR.joinpath("dynmap").joinpath("configuration.txt.json"),
        SERVER_DIR,
        **dynmap_custom_configuration
    )


if __name__ == "__main__":
    main()
