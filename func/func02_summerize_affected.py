reports = [
    {"id": 1, "affected_count": 4},
    {"id": 2, "affected_count": None},
    {"id": 3, "affected_count": 0},
    {"id": 4, "affected_count": 12},
]

# Rules:
# "known_total": Summe der bekannten Betroffenenzahlen.
# "unknown_reports": Anzahl der Meldungen mit None.
# "zero_reports": Anzahl der Meldungen mit ausdrücklich 0.

def summarize_affected(reports):
    summary = {
        "known_total":0,
        "zero_reports":0,
        "unknown_reports":0
    }
        
    for report in reports:
        if report["affected_count"] is not None and report["affected_count"] > 0:
            summary["known_total"] += report["affected_count"]
        elif report["affected_count"] == 0:
            summary["zero_reports"] += 1
        elif report["affected_count"] is None:
            summary["unknown_reports"] += 1
    return summary

if __name__ == "__main__":
    print(summarize_affected(reports))