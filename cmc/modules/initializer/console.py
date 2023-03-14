from rich.console import Console
from rich.theme import Theme

theme_init = Theme(
    {
        "info": "pale_turquoise1",
        "warning": "orange_red1",
        "danger": "bold red",
    }
)

console = Console(theme=theme_init)
err_console = Console(stderr=True, theme=theme_init)
