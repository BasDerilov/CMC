from rich.console import Console
from rich.theme import Theme

minecraft = Theme(
    {
        "info": "green3",
        "curse": "orange1",
        "warning": "orange_red1",
        "danger": "bold red",
    }
)

console = Console(theme=minecraft)
err_console = Console(stderr=True, theme=minecraft)
