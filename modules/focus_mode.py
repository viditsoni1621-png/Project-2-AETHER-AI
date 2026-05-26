import time


def start_focus(minutes):

    seconds = minutes * 60

    print(f"\nFocus session started for {minutes} minutes.")
    print("Zero distractions. Stay locked in.\n")

    while seconds > 0:

        mins = seconds // 60
        secs = seconds % 60

        timer = f"{mins:02d}:{secs:02d}"

        print(timer, end="\r")

        time.sleep(1)

        seconds -= 1

    print("\nFocus session complete.")
    print("+50 XP earned.")