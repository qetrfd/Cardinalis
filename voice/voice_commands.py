import os
import webbrowser
from voice.tts import speak

def execute(command):

    if "abre chrome" in command:
        speak("Abriendo Google Chrome")
        os.system("open -a 'Google Chrome'")

    elif "abre youtube" in command:
        speak("Abriendo YouTube")
        webbrowser.open("https://youtube.com")

    elif "abre spotify" in command:
        speak("Abriendo Spotify")
        os.system("open -a Spotify")

    elif "hola" in command:
        speak("Hola. Soy Cardinalis. ¿En qué puedo ayudarte?")

    elif "cómo estás" in command:
        speak("Funcionando perfectamente.")

    elif "gracias" in command:
        speak("Para servirte.")

    else:
        speak("No entendí el comando.")