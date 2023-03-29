"""cmc is a tool for quicly spooling up minecraft servers locally or on Google Cloud
Platform

"""


import json
from cmc import typer
from cmc import __app_name__, __version__
from pydantic.error_wrappers import ValidationError
from rich.console import Console

from .models import CmcConfigModel, CmcPackageModel
from .modules.installer import Minecraft, Plugins
from .modules.initializer import Initializer, CmcConfig, CmcPackage

from typing import Optional

app = typer.Typer(no_args_is_help=True)

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


@app.async_command()
async def install(
    api_key: str = typer.Option(
        None,
        "--api-key",
        "-k",
        prompt="enter your curse api key (optional)",
    )
) -> None:
    """Install

    Args:
        api_key (str, optional): Defaults to None.
    """
    # TODO This validation should be done somewhere else
    # and should be more readable for users

    package = None

    try:

        with open("cmc-package.json", "r") as package_f:
            data = json.load(package_f)
            package = CmcPackageModel(**data)

    except ValidationError as err:
        console.print(err)
        return

    config = None

    try:

        with open("cmc-config.json", "r") as config_f:
            data = json.load(config_f)
            config = CmcConfigModel(**data)

    except ValidationError as err:
        console.print(err)
        return

    # End of validation block

    minecraft_installer = Minecraft(package, config)
    plugins_installer = Plugins(package, config)
    minecraft_installer.install()
    plugins_installer.install_from_urls()
    plugins_installer.install_from_curse(api_key)
