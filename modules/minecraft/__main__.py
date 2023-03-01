from pathlib import Path
from .scripts.download_bins import download_deps
from .scripts.configure import configure_plugins, configure_server


def main():

    download_deps(Path())
    configure_server()
    configure_plugins()


if __name__ == "__main__":
    main()
