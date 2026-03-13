import json
import os

FILE = "memory/custom_commands.json"

def load_commands():

    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r") as f:
        return json.load(f)

def save_commands(data):

    with open(FILE, "w") as f:
        json.dump(data, f)

def learn_command(trigger, action):

    commands = load_commands()

    commands[trigger] = action

    save_commands(commands)

def get_command(text):

    commands = load_commands()

    for trigger in commands:

        if trigger in text:
            return commands[trigger]

    return None