from func.func12_summarize_checked_reports import summarize_checked_reports

reports1 = [
    {"id": 1, "category": "accessibility", "status": "open", "affected_count": 4},
    {"id": 2, "category": "infrastructure", "status": "open", "affected_count": None},
    {"id": 3, "category": "accessibility", "status": "closed", "affected_count": 12},
    {"id": 4, "category": "accessibility", "status": "open", "affected_count": None},
    {"id": 5, "category": "accessibility", "status": "open", "affected_count": 0},
]

actual = summarize_checked_reports(reports1, "accessibility")
expected = {"known_total": 4, "unknown_reports": 1, "zero_reports": 1}
assert actual == expected


actual = summarize_checked_reports([], "accessibility")
expected = {"known_total": 0, "unknown_reports": 0, "zero_reports": 0}
assert actual == expected


reports2 = [
    {"id": 1, "category": "accessibility", "status": "open", "affected_count": 4},
    {"id": 1, "category": "infrastructure", "status": "open", "affected_count": None}
]

try:
    error = summarize_checked_reports(reports2, "accessibility")
except ValueError as error:
    print(f"Check stopped: {error}")
else:
    print("The program continues.")


reports3 = [
    {"id": 1, "category": "accessibility", "status": "open", "affected_count": 4},
    {"id": 2, "category": "infrastructure", "status": "open", "affected_count": -3},
    {"id": 3, "category": "accessibility", "status": "closed", "affected_count": 12},
    {"id": 4, "category": "accessibility", "status": "open", "affected_count": None},
    {"id": 5, "category": "accessibility", "status": "open", "affected_count": 0},
]
try:
    error = summarize_checked_reports(reports3, "accessibility")
except ValueError as error:
    print(f"Check stopped: {error}")
else:
    print("The program continues.")


