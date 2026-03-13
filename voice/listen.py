import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()

def listen():
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("🎤 Escuchando...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="es-MX")
        print("Usuario:", text)
        return text.lower()
    except:
        return ""