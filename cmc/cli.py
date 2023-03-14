"""cmc is a tool for quicly spooling up minecraft servers locally or on Google Cloud
Platform

"""


from pathlib import Path
import typer
from rich.console import Console
from cmc import __app_name__, __version__
from .modules.minecraft import Minecraft
from .modules.initializer import Initializer

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
    init = Initializer(project_name)
    init.initialize_new_server()
    # create_server(Path.cwd().joinpath(project_name), {}, dynmap={})


@app.command()
def install(
    project_name: str = typer.Option(
        str("server"),
        "--proj-name",
        "-n",
        prompt="project name",
    ),
) -> None:
    """the install command will create a server directory and install your bins in it

    Args:
        project_name (str, optional): _description_. Defaults to typer.Option
        ( str("server"), "--proj-name", "-n", prompt="project name", ).
    """
    minecraft = Minecraft(Path(project_name))
    minecraft.install()


if __name__ == "__main__":
    main()
