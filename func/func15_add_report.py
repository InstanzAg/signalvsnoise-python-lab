import json
from func.func14_save_reports import load_reports ,save_reports

def add_report(path, new_report):
    reports = load_reports(path)
    reports.append(new_report)
    save_reports(reports, path)
    # with open(path , mode="r+", encoding="utf-8") as file:
        # json.dump(new_report, file)
        

if __name__ == "__main__":
    add_report("sample_data/reports.json", {"id": 3, "category": "accessibility", "status": "open", "affected_count": 3})