import random
import time


def matrix_mode():

    for _ in range(20):

        print(
            "".join(
                random.choice("01")
                for _ in range(50)
            )
        )

        time.sleep(0.05)

    return "Reality stabilized."


def self_destruct():

    for i in range(5, 0, -1):

        print(i)

        time.sleep(1)

    return "Just kidding. NEXUS cannot be destroyed."