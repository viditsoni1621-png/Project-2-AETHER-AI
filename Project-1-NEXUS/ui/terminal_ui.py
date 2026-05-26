import time

from rich.console import Console

console = Console()


def slow_print(text):

    for char in text:

        print(char, end="", flush=True)

        time.sleep(0.01)

    print()


def divider():

    console.print(
        "─" * 60,
        style="bright_black"
    )