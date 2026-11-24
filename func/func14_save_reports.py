import json
from func.func13_load_reports import load_reports


def save_reports(reports, path_out):
    with open(path_out, mode="w", encoding="utf-8") as file:
        json.dump(reports, file)

if __name__ == "__main__":
    save_reports("sample_data/reports.json", "sample_data/saved_reports.json")