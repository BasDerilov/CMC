from rich.console import Console
from rich.theme import Theme

theme = Theme(
    {
        "info": "pale_turquoise1",
        "warning": "light_salmon1",
        "danger": "bold red",
    }
)

console = Console(theme=theme)
err_console = Console(stderr=True, theme=theme)
