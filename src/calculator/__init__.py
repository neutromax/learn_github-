from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# Initialize Rich console
console = Console()


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    return a % b


def floor_div(a, b):
    return a // b


def absolute(a):
    return abs(a)


def main() -> None:
    """Main function to run the calculator."""
    # Display Banner
    banner_text = Text.from_markup(
        "[bold cyan]╔════════════════════════════════════════╗[/bold cyan]\n"
        "[bold cyan]║[/bold cyan]  [bold yellow]🧮 SIMPLE CALCULATOR 🧮[/bold yellow]  [bold cyan]║[/bold cyan]\n"
        "[bold cyan]╚════════════════════════════════════════╝[/bold cyan]"
    )
    console.print(banner_text)
    console.print()

    # Create results table
    table = Table(title="[bold cyan]Calculation Results[/bold cyan]", show_header=True, header_style="bold magenta")
    table.add_column("Operation", style="cyan", width=20)
    table.add_column("Expression", style="green", width=15)
    table.add_column("Result", style="yellow", width=15)

    results = [
        ("Addition", "5 + 3", add(5, 3)),
        ("Subtraction", "10 - 4", subtract(10, 4)),
        ("Multiplication", "4 × 5", multiply(4, 5)),
        ("Division", "10 ÷ 2", divide(10, 2)),
        ("Power", "2 ^ 3", power(2, 3)),
        ("Modulus", "10 % 3", modulus(10, 3)),
        ("Floor Division", "10 // 3", floor_div(10, 3)),
        ("Absolute", "|-5|", absolute(-5)),
    ]

    for operation, expression, result in results:
        table.add_row(operation, expression, str(result))

    console.print(table)
    console.print()

    # Display summary panel
    summary = Panel(
        "[bold green]✓ All calculations completed successfully![/bold green]\n"
        "[dim]Calculator is ready for more operations[/dim]",
        title="[bold blue]Summary[/bold blue]",
        border_style="blue",
        expand=False
    )
    console.print(summary)
