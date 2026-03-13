import os


class AppIndexer:

    def __init__(self):

        self.apps = {}

        self.scan_apps()

    def scan_apps(self):

        paths = [
            "/Applications",
            "/System/Applications"
        ]

        for path in paths:

            if not os.path.exists(path):
                continue

            for app in os.listdir(path):

                if app.endswith(".app"):

                    name = app.replace(".app", "")

                    key = name.lower()

                    self.apps[key] = name

    def find(self, query):

        query = query.lower()

        for key in self.apps:

            if query in key:
                return self.apps[key]

        return None