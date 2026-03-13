import os


class FileIndexer:

    def __init__(self):

        self.files = {}

        self.scan()

    def scan(self):

        paths = [
            os.path.expanduser("~/Desktop"),
            os.path.expanduser("~/Documents"),
            os.path.expanduser("~/Downloads")
        ]

        for path in paths:

            if not os.path.exists(path):
                continue

            for root, dirs, files in os.walk(path):

                for name in files:

                    key = name.lower()

                    full_path = os.path.join(root, name)

                    self.files[key] = full_path

    def find(self, query):

        query = query.lower()

        for key in self.files:

            if query in key:
                return self.files[key]

        return None