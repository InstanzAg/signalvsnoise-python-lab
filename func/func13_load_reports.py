import json

def load_reports(path):
    with open(path, encoding="utf-8") as file:
        return json.load(file)