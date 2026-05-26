def log_mood(memory, mood):

    memory["moods"].append(mood)

    if len(memory["moods"]) > 5:
        memory["moods"].pop(0)

    return f"Mood logged: {mood}"