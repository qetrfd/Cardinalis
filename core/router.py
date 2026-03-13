class Router:

    def route(self, text):

        text = text.lower()

        if "abre" in text or "abrir" in text:
            return {
                "agent": "system",
                "intent": "open",
                "text": text
            }

        if "sube volumen" in text:
            return {
                "agent": "system",
                "intent": "volume_up",
                "text": text
            }

        if "baja volumen" in text:
            return {
                "agent": "system",
                "intent": "volume_down",
                "text": text
            }

        if "silencio" in text:
            return {
                "agent": "system",
                "intent": "mute",
                "text": text
            }

        if "busca" in text:
            return {
                "agent": "system",
                "intent": "search",
                "text": text
            }

        if "youtube" in text or "google" in text or "gmail" in text or "github" in text or "spotify" in text:
            return {
                "agent": "system",
                "intent": "website",
                "text": text
            }

        return {
            "agent": "assistant",
            "intent": "chat",
            "text": text
        }