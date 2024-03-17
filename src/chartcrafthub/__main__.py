from rich.console import Console
from rich.table import Table
from rich.text import Text

from chartcrafthub.core import fundamentals

if __name__ == "__main__":
    table = Table.grid(padding=1, pad_edge=True)
    chart_craft_hub_logo = r"""
     _____ _                _     _____            __ _     _   _       _     
    /  __ \ |              | |   /  __ \          / _| |   | | | |     | |    
    | /  \/ |__   __ _ _ __| |_  | /  \/_ __ __ _| |_| |_  | |_| |_   _| |__  
    | |   | '_ \ / _` | '__| __| | |   | '__/ _` |  _| __| |  _  | | | | '_ \ 
    | \__/\ | | | (_| | |  | |_  | \__/\ | | (_| | | | |_  | | | | |_| | |_) |
     \____/_| |_|\__,_|_|   \__|  \____/_|  \__,_|_|  \__| \_| |_/\__,_|_.__/
    """
    table.add_row(f"[cyan]{chart_craft_hub_logo}")

    intro = Text.from_markup(
        """Thanks for attending [italic]"Code, debug, reuse this chart"[/] workshop!

In this workshop, you'll learn how to:

✓ Craft visually compelling figures that enhance your document's overall appearance.
✓ Develop modular plotting functions utilizing matplotlib.
✓ Utilize Rich and debugging and method exploration.
✓ Organize your code for enhanced usability.
✓ Package your code for seamless portability.

To begin, visit the documentation home page: [u Blue]https://kislovskiy.github.io/ChartCraftHub/][/]

- Artem
"""
    )

    table.add_row(intro)

    console = Console()
    console.print(table, justify="center")
    console.print(f"[italic]{fundamentals()}[/]", justify="center")
