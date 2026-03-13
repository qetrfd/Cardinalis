import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, "conversation.json")


def load_memory():

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)


def save_memory(memory):

    os.makedirs(os.path.dirname(FILE), exist_ok=True)

    with open(FILE, "w") as f:
        json.dump(memory, f)


def add_message(role, content):

    memory = load_memory()

    memory.append({
        "role": role,
        "content": content
    })

    memory = memory[-20:]

    save_memory(memory)


def get_memory():

    return load_memory()