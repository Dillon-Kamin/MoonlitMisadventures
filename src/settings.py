# src/settings.py

import json
import os

class Settings:
    def __init__(self, config_dir=None):
        base_dir = os.path.dirname(__file__)
        self.config_dir = config_dir or os.path.join(base_dir, "..", "config")
        self.settings = {}
        self.settings["video"] = self._load("video.json")

    def _load(self, filename):
        path = os.path.join(self.config_dir, filename)
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"ERROR::settings.py::Missing required config file: {filename}")
        except json.JSONDecodeError as e:
            raise ValueError(f"ERROR::settings.py::Invalid JSON in {filename}: {e}")

    def _load_optional(self, filename):
        path = os.path.join(self.config_dir, filename)
        if not os.path.exists(path):
            return {}
        with open(path, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError as e:
                print(f"ERROR::settings.py::Warning: Skipping invalid JSON in {filename}: {e}")
                return {}
