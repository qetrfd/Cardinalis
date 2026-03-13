import subprocess
import re

VOICE = "Rocko"


def normalize_spanish(text):

    replacements = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "ü": "u",
        "ñ": "ny"
    }

    text = text.lower()

    for k, v in replacements.items():
        text = text.replace(k, v)

    text = text.replace("que", "ke")
    text = text.replace("qui", "ki")
    text = text.replace("gue", "ge")
    text = text.replace("gui", "gi")

    text = text.replace("ll", "y")
    text = text.replace("ce", "se")
    text = text.replace("ci", "si")
    text = text.replace("z", "s")
    text = text.replace("v", "b")

    text = text.replace("j", "h")

    return text


def split_sentences(text):

    sentences = re.split(r"[.!?]", text)

    sentences = [s.strip() for s in sentences if s.strip()]

    return sentences


def speak(text):

    try:

        text = normalize_spanish(text)

        sentences = split_sentences(text)

        for s in sentences:

            subprocess.run(
                ["say", "-v", VOICE, "-r", "180", s],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

    except Exception as e:

        print("Error TTS:", e)