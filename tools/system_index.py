import os
import json
from difflib import get_close_matches

CACHE_PATH = "memory/system_index.json"


class SystemIndex:

    def __init__(self):

        self.apps = {}
        self.files = {}
        self.folders = {}

        if os.path.exists(CACHE_PATH):
            self.load_cache()
        else:
            self.build_index()
            self.save_cache()

    def build_index(self):

        self.index_apps()
        self.index_files()

    def index_apps(self):

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

                    self.apps[name.lower()] = name

    def index_files(self):

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
                    full = os.path.join(root, name)

                    self.files[key] = full

                for name in dirs:

                    key = name.lower()
                    full = os.path.join(root, name)

                    self.folders[key] = full

    def save_cache(self):

        data = {
            "apps": self.apps,
            "files": self.files,
            "folders": self.folders
        }

        os.makedirs("memory", exist_ok=True)

        with open(CACHE_PATH, "w") as f:
            json.dump(data, f)

    def load_cache(self):

        with open(CACHE_PATH, "r") as f:
            data = json.load(f)

        self.apps = data["apps"]
        self.files = data["files"]
        self.folders = data["folders"]

    def search_app(self, query):

        query = query.lower()

        if query in self.apps:
            return self.apps[query]

        for key in self.apps:
            if query in key:
                return self.apps[key]

        matches = get_close_matches(query, list(self.apps.keys()), n=1, cutoff=0.5)

        if matches:
            return self.apps[matches[0]]

        return None

    def search_file(self, query):

        matches = get_close_matches(query.lower(), list(self.files.keys()), n=1, cutoff=0.5)

        if matches:
            return self.files[matches[0]]

        return None

    def search_folder(self, query):

        matches = get_close_matches(query.lower(), list(self.folders.keys()), n=1, cutoff=0.5)

        if matches:
            return self.folders[matches[0]]

        return None