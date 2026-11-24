

# nur offene Meldungen der übergebenen category auswählen;
# die vollständigen ausgewählten Dictionaries in einer Liste zurückgeben;
# die ursprüngliche Liste unverändert lassen;
# bei keinem Treffer eine leere Liste zurückgeben.


def filter_open_reports(reports, category):
    wanted_reports = []
    for report in reports:
        if category == report["category"] and report["status"] == "open":
            wanted_reports.append(report)
    return wanted_reports



if __name__ == "__main__":
    reports = [
        {
            "id": 1,
            "titel": "Bordstein nicht abgesenkt",
            "category": "Barrierefreiheit",
            "betroffene": 4,
            "status": "open",
        },
        {
            "id": 2,
            "titel": "Beleuchtung ausgefallen",
            "category": "Infrastruktur",
            "betroffene": None,
            "status": "open",
        },
        {
            "id": 3,
            "titel": "Aufzug außer Betrieb",
            "category": "Barrierefreiheit",
            "betroffene": 12,
            "status": "closed",
        },
        {
            "id": 4,
            "titel": "Zugang zum Beratungsraum versperrt",
            "category": "Barrierefreiheit",
            "betroffene": None,
            "status": "open",
        },
    ]
    print(filter_open_reports(reports, "Barrierefreiheit"))