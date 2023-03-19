"""cmc is a tool for quicly spooling up minecraft servers locally or on Google Cloud
Platform

"""


import json
import typer
from rich.console import Console
from cmc import __app_name__, __version__

from .models import CmcConfigModel, CmcPackageModel

from .modules.installer import Minecraft
from .modules.initializer import Initializer, CmcConfig, CmcPackage

from typing import Optional

app = typer.Typer()

console = Console()


def _version_callback(value: bool) -> None:

    if value:
        # TODO rework to use pyproject.toml instead of vars
        typer.echo(f"{__app_name__} v{__version__}")

        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
) -> None:

    return


@app.command()
def init(
    project_name: str = typer.Option(
        str("server"),
        "--proj-name",
        "-n",
        prompt="project name",
    ),
) -> None:
    """the init command

    Args:
        project_name (str): the name of your minecraft project (server)
    """

    package = CmcPackage(project_name)
    config = CmcConfig()

    init = Initializer(package, config)

    init.initialize_new_server()

    # create_server(Path.cwd().joinpath(project_name), {}, dynmap={})


@app.command()
def install() -> None:
    """the install command will create a server directory and install your bins in it

    Args:
        project_name (str, optional): _description_. Defaults to typer.Option
        ( str("server"), "--proj-name", "-n", prompt="project name", ).
    """

    package = None
    with open("cmc-package.json", "r") as package_f:
        data = json.load(package_f)
        package = CmcPackageModel(**data)

    config = None
    with open("cmc-config.json", "r") as config_f:
        data = json.load(config_f)
        config = CmcConfigModel(**data)

    # minecraft = Minecraft(Path())
    # minecraft.install()


if __name__ == "__main__":
    main()
