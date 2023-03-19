from rich.console import Console
from rich.theme import Theme

theme_init = Theme(
    {
        "info": "dark_sea_green2",
        "warning": "light_salmon1",
        "danger": "bold red",
    }
)

console = Console(theme=theme_init)
err_console = Console(stderr=True, theme=theme_init)
