RANKS = [
    (0, "Recruit"),
    (100, "Specialist"),
    (300, "Operative"),
    (700, "Commander"),
    (1500, "NEXUS Elite")
]

XP_TABLE = {
    "task_add": 10,
    "mood_log": 5,
    "focus_complete": 50
}


def get_rank(xp):

    rank = "Recruit"

    for req, title in RANKS:

        if xp >= req:
            rank = title

    return rank


def xp_bar(current, maximum=100):

    filled = int((current / maximum) * 10)

    return (
        "█" * filled
        + "░" * (10 - filled)
    )