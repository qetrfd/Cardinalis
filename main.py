import os
import webbrowser
import subprocess
import threading
from datetime import datetime

from voice.listen import listen
from voice.tts import speak
from agents.llm_agent import ask_llm
from memory.conversation_memory import add_message
from memory.custom_commands import learn_command, get_command

memory = []


def ai_response(text):

    text = text.lower()

    if "hora" in text:
        return f"Son las {datetime.now().strftime('%H:%M')}"

    if "fecha" in text:
        return datetime.now().strftime("Hoy es %d de %B de %Y")

    if "quien eres" in text or "quién eres" in text:
        return "Soy Cardinalis, tu asistente personal."

    if "recuerda" in text:
        data = text.replace("recuerda", "").strip()
        if data != "":
            memory.append(data)
            return "Lo recordaré."

    if "que recuerdas" in text or "qué recuerdas" in text:
        if len(memory) == 0:
            return "No tengo nada en memoria."
        return "Recuerdo: " + ", ".join(memory)

    return ""


def control_volume(command):

    if "sube volumen" in command:
        os.system("osascript -e 'set volume output volume 80'")
        speak("Subiendo volumen")
        return True

    if "baja volumen" in command:
        os.system("osascript -e 'set volume output volume 30'")
        speak("Bajando volumen")
        return True

    if "silencio" in command:
        os.system("osascript -e 'set volume output muted true'")
        speak("Activando silencio")
        return True

    return False


def open_app_or_file(target):

    try:

        apps = subprocess.check_output(
            ["mdfind", "kMDItemContentTypeTree == 'com.apple.application-bundle'"]
        ).decode().split("\n")

        for app in apps:

            name = os.path.basename(app).replace(".app", "").lower()

            if target in name:
                speak(f"Abriendo {name}")
                os.system(f'open "{app}"')
                return True

        files = subprocess.check_output(
            ["mdfind", target]
        ).decode().split("\n")

        if len(files) > 0 and files[0] != "":
            os.system(f'open "{files[0]}"')
            speak("Abriendo")
            return True

    except:
        pass

    return False


def search_google(query):

    speak(f"Buscando {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")


def execute(command):

    command = command.lower().strip()

    print("Comando recibido:", command)

    learned = get_command(command)

    if learned:
        os.system(learned)
        speak("Ejecutando comando aprendido")
        return

    if "cuando diga" in command and "haz" in command:

        parts = command.split("haz")

        trigger = parts[0].replace("cuando diga", "").strip()
        action = parts[1].strip()

        learn_command(trigger, action)

        speak("He aprendido el comando")

        return

    if command.startswith("abre"):

        target = command.replace("abre", "").strip()

        if open_app_or_file(target):
            return

        speak("No encontré lo que quieres abrir")
        return

    if control_volume(command):
        return

    if command.startswith("busca"):

        query = command.replace("busca", "").strip()

        if query:
            search_google(query)

        return

    response = ai_response(command)

    if response != "":
        speak(response)
        print("Cardinalis:", response)
        return

    try:

        add_message("user", command)

        response = ask_llm(command)

        add_message("assistant", response)

        speak(response)

        print("Cardinalis:", response)

    except:

        speak("No pude procesar la solicitud.")


def voice_loop():

    speak("Modo voz activado")

    while True:

        command = listen()

        if command == "":
            continue

        print("Usuario:", command)

        if "detente voz" in command:
            speak("Desactivando voz")
            break

        execute(command)


def text_loop():

    print("Modo texto activado")

    while True:

        text = input("Tú: ")

        if text == "":
            continue

        if text.lower() == "salir":
            os._exit(0)

        execute(text)


if __name__ == "__main__":

    print("Iniciando Cardinalis...")

    voice_thread = threading.Thread(target=voice_loop)
    text_thread = threading.Thread(target=text_loop)

    voice_thread.start()
    text_thread.start()

    voice_thread.join()
    text_thread.join()