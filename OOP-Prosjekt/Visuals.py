from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


#Grafikk delen

class BattleUI:
    def __init__(self):
        self.console = Console()

    def hp_bar(self, pokemon):
        max_hp = 100
        current_hp = max(0, pokemon.hp)

        hp_percentage = current_hp / max_hp

        if hp_percentage > 0.5:
            color = "green"
        elif hp_percentage > 0.2:
            color = "yellow"
        else:
            color = "red"

        bar_length = 25
        filled = round(bar_length * hp_percentage)
        empty = bar_length - filled

        bar = Text()
        bar.append("█" * filled, style=color)
        bar.append("░" * empty, style="grey50")

        return bar
    
    def show_pokemon(self, pokemon, title, color):
        content = Text()

        content.append(
            f"{pokemon.name}\n",
            style="bold white"
        )

        content.append_text(self.hp_bar(pokemon))

        content.append(
            f"\n{pokemon.hp}/100 HP",
            style="white"
        )

        self.console.print(
            Panel(
                content,
                title=title,
                border_style=color
            )
        )

    def show_battle(self, player, enemy, turn):
        self.console.clear()

        self.console.print(
            Panel(
                f"[bold cyan]POKEMON BATTLE[/bold cyan]\n"
                f"Turn {turn}",
                border_style="blue"
            )
        )

        self.show_pokemon(
            enemy,
            "ENEMY POKEMON",
            "red"
        )

        self.console.print(
            "[bold yellow] VS [/bold yellow]"
        )

        self.show_pokemon(
            player,
            "YOUR POKEMON",
            "cyan"
        )

    def show_moves(self, pokemon):
        table = Table(
            title="AVAILABLE MOVES",
            border_style="cyan"
        )

        table.add_column("Index", style="yellow")
        table.add_column("Move", style="cyan")
        table.add_column("Damage", style="red")

        for index, (move, damage) in enumerate(
            pokemon.pokemon_movepool.items()
        ):
            table.add_row(
                str(index),
                move,
                str(damage)
            )

        self.console.print(table)

    def message(self, text, color="white"):
        self.console.print(
            Panel(
                text,
                border_style=color
            )
        )
