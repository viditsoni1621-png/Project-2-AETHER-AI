import json
import random

with open("data/quotes.json", "r") as file:

    quotes = json.load(file)


def get_quote():

    return random.choice(quotes)