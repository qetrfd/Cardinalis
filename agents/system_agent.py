from tools.system_index import SystemIndex
from tools.open_app import open_app
from tools.open_file import open_file
from voice.tts import speak


class SystemAgent:

    def __init__(self):

        print("Indexando sistema...")

        self.index = SystemIndex()

        print(len(self.index.apps), "apps encontradas")
        print(len(self.index.files), "archivos encontrados")
        print(len(self.index.folders), "carpetas encontradas")

    def extract_query(self, text):

        words = text.lower().split()

        if "abre" in words:
            idx = words.index("abre")
            return " ".join(words[idx + 1:])

        return text

    def handle(self, command):

        text = command["text"]

        query = self.extract_query(text)

        if not query:
            speak("No entendí el comando")
            return

        app = self.index.search_app(query)

        if app:
            speak(f"Abriendo {app}")
            open_app(app)
            return

        file = self.index.search_file(query)

        if file:
            speak("Abriendo archivo")
            open_file(file)
            return

        folder = self.index.search_folder(query)

        if folder:
            speak("Abriendo carpeta")
            open_file(folder)
            return

        speak("No encontré eso")