from func.func01_filter_open_reports import filter_open_reports
from func.func02_summerize_affected import summarize_affected

reports = [
    {"id": 1, "category": "accessibility", "status": "open", "affected_count": 4},
    {"id": 2, "category": "infrastructure", "status": "open", "affected_count": None},
    {"id": 3, "category": "accessibility", "status": "closed", "affected_count": 12},
    {"id": 4, "category": "accessibility", "status": "open", "affected_count": None},
    {"id": 5, "category": "accessibility", "status": "open", "affected_count": 0},
]

def summarize_open_reports(reports, category):
    selected_reports = filter_open_reports(reports, category)
    summary = summarize_affected(selected_reports)
    return summary

if __name__ == '__main__':
    print(summarize_open_reports(reports, "accessibility"))

