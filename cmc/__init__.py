"""Top-level package for cmc."""

from functools import wraps
from asyncio import run
import typer

__app_name__ = "cmc"
__version__ = "0.9.0"


# IMPORTANT! This implementation is a workaround to make typer asynchronous.
# The async_command decorator is custom and should be removed when
# hopefully someday the smart assets at the typer project decide
# to listen to the guy who came up with this smart solution
# https://github.com/tiangolo/typer/issues/88
# if you are reading this check if this has been merged
# https://github.com/tiangolo/typer/pull/332


def async_command(app, *args, **kwargs):
    def decorator(async_func):
        @wraps(async_func)
        def sync_func(*_args, **_kwargs):
            return run(async_func(*_args, **_kwargs))

        app.command(*args, **kwargs)(sync_func)

        return async_func

    return decorator


typer.Typer.async_command = async_command
