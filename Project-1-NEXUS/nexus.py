import json
from datetime import datetime

from rich.console import Console

from ui.ascii_art import nexus_logo
from ui.terminal_ui import slow_print, divider

from modules.greeter import get_greeting
from modules.task_manager import add_task, show_tasks
from modules.mood_tracker import log_mood
from modules.motivator import get_quote
from modules.easter_eggs import (
    self_destruct,
    matrix_mode
)
from modules.xp_system import (
    XP_TABLE,
    get_rank,
    xp_bar
)
from modules.focus_mode import start_focus


console = Console()


# LOAD MEMORY
with open("data/operator.json", "r") as file:

    memory = json.load(file)


# BOOT SCREEN
console.print(
    nexus_logo(),
    style="cyan"
)

slow_print(
    "Initializing NEXUS Personal OS..."
)

slow_print(
    "Loading operator profile..."
)

slow_print(
    "System online."
)

name = memory["name"]

console.print(
    get_greeting(name),
    style="green"
)


# SAVE MEMORY
def save_memory():

    with open(
        "data/operator.json",
        "w"
    ) as file:

        json.dump(
            memory,
            file,
            indent=4
        )


# MAIN LOOP
while True:

    divider()

    user = input(
        "[OPERATOR] > "
    ).lower().strip()

    # EMPTY INPUT
    if user == "":

        console.print(
            "NEXUS is listening, Operator.",
            style="yellow"
        )

    # HELP
    elif user == "help":

        print("""

AVAILABLE COMMANDS
──────────────────

help
motivate
brief today
show tasks
exit

TASK COMMANDS
──────────────────

task add [task]

MOOD COMMANDS
──────────────────

mood log [mood]

FOCUS COMMANDS
──────────────────

focus start [minutes]

SECRET COMMANDS
──────────────────

matrix
self destruct

""")

    # TASK ADD
    elif user.startswith(
        "task add"
    ):

        task = user.replace(
            "task add",
            ""
        ).strip()

        if task == "":

            console.print(
                "Expected: task add [task]",
                style="red"
            )

        else:

            result = add_task(
                memory,
                task
            )

            memory["xp"] += XP_TABLE[
                "task_add"
            ]

            memory["level"] = get_rank(
                memory["xp"]
            )

            console.print(
                result,
                style="green"
            )

            console.print(
                f"+{XP_TABLE['task_add']} XP",
                style="yellow"
            )

    # SHOW TASKS
    elif user == "show tasks":

        console.print(
            show_tasks(memory),
            style="cyan"
        )

    # MOOD LOG
    elif user.startswith(
        "mood log"
    ):

        mood = user.replace(
            "mood log",
            ""
        ).strip()

        if mood == "":

            console.print(
                "Expected: mood log [mood]",
                style="red"
            )

        else:

            result = log_mood(
                memory,
                mood
            )

            memory["xp"] += XP_TABLE[
                "mood_log"
            ]

            memory["level"] = get_rank(
                memory["xp"]
            )

            console.print(
                result,
                style="magenta"
            )

    # MOTIVATION
    elif user == "motivate":

        console.print(
            get_quote(),
            style="yellow"
        )

    # DAILY BRIEF
    elif user == "brief today":

        now = datetime.now().strftime(
            "%d %B %Y | %H:%M"
        )

        console.print(
            f"DATE: {now}",
            style="cyan"
        )

        console.print(
            f"XP: {memory['xp']}",
            style="green"
        )

        console.print(
            f"RANK: {memory['level']}",
            style="yellow"
        )

        console.print(
            f"XP BAR: {xp_bar(memory['xp'] % 100)}",
            style="magenta"
        )

        console.print(
            get_quote(),
            style="cyan"
        )

    # FOCUS MODE
    elif user.startswith(
        "focus start"
    ):

        try:

            minutes = int(
                user.replace(
                    "focus start",
                    ""
                ).strip()
            )

            start_focus(minutes)

            memory["xp"] += XP_TABLE[
                "focus_complete"
            ]

            memory["level"] = get_rank(
                memory["xp"]
            )

        except:

            console.print(
                "Expected: focus start [minutes]",
                style="red"
            )

    # MATRIX MODE
    elif user == "matrix":

        console.print(
            matrix_mode(),
            style="green"
        )

    # SELF DESTRUCT
    elif user == "self destruct":

        console.print(
            self_destruct(),
            style="red"
        )

    # EXIT
    elif user == "exit":

        save_memory()

        console.print(
            "Shutting down NEXUS...",
            style="red"
        )

        break

    # UNKNOWN COMMAND
    else:

        console.print(
            "Unknown command.",
            style="red"
        )

        console.print(
            "Type 'help' to view commands.",
            style="yellow"
        )

    # SAVE MEMORY
    save_memory()