


def find_missing_fields(reports, needed_information):
    missing_info_report = {}

    for report in reports:
        missing_info = []
        for info in needed_information:
            if info not in report:
                missing_info.append(info)
        if missing_info:
            missing_info_report[report["id"]] = missing_info
    return missing_info_report

reports = [
    {"id": 1, "category": "accessibility", "status": "open", "affected_count": 4},
    {"id": 2, "category": "infrastructure", "status": "open", "affected_count": None},
    {"id": 3, "category": "accessibility", "status": "open"},
    {"id": 4, "affected_count": 2},
]

needed_information = (
    "category",
    "status",
    "affected_count"
)

if __name__ == "__main__":
    print(find_missing_fields(reports, needed_information))