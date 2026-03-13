from core.router import Router
from agents.system_agent import SystemAgent


class CardinalisCore:

    def __init__(self):

        self.router = Router()
        self.system_agent = SystemAgent()

    def handle_text(self, text):

        command = self.router.route(text)

        if command["agent"] == "system":
            self.system_agent.handle(command)

        else:
            print("Cardinalis:", text)