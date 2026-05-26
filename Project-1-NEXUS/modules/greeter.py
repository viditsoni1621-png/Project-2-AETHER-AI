from datetime import datetime

def get_greeting(name):

    hour = datetime.now().hour

    if hour < 12:
        return f"Good morning, {name}"

    elif hour < 18:
        return f"Good afternoon, {name}"

    else:
        return f"Good evening, {name}"