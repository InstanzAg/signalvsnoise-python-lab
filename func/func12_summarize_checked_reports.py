from func.func11_check_reports import check_reports
from func.func03_summerize_open_reports import summarize_open_reports

def summarize_checked_reports(reports, category):
    errors = check_reports(reports)
    if errors:
        raise ValueError(f"Affected-count errors: {errors}")
    return summarize_open_reports(reports, category)
    
if __name__ == "__main__":

    reports1 = [
    {"id": 1, "category": "accessibility", "status": "open", "affected_count": 4},
    {"id": 2, "category": "infrastructure", "status": "open", "affected_count": None},
    {"id": 3, "category": "accessibility", "status": "closed", "affected_count": 12},
    {"id": 4, "category": "accessibility", "status": "open", "affected_count": None},
    {"id": 5, "category": "accessibility", "status": "open", "affected_count": 0},
]
    print(summarize_checked_reports(reports1, "accessibility"))


    reports2 = [
    {"id": 1, "category": "accessibility", "status": "open", "affected_count": 4},
    {"id": 2, "category": "infrastructure", "status": "open", "affected_count": None},
    ]
    
    print(summarize_checked_reports(reports2, "accessibility"))