

def find_incomplete_reports(reports):
    missing_information_id = []
    for report in reports:
        for key in needed_information:
            if key not in report:
                missing_information_id.append(report["id"])
                break
    return missing_information_id


reports = [
    {"id": 1, "category": "accessibility", "status": "open", "affected_count": 4},
    {"id": 2, "category": "infrastructure", "status": "open", "affected_count": None},
    {"id": 3, "category": "accessibility", "status": "open"},
    {"id": 4, "affected_count": 2},
]

needed_information = [
    "category",
    "status",
    "affected_count"
]

if __name__ == "__main__":
    print(find_incomplete_reports(reports))