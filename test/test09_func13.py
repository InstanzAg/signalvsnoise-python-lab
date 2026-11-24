from func.func13_load_reports import load_reports
from func.func12_summarize_checked_reports import summarize_checked_reports

reports = load_reports("sample_data/reports.json")
assert reports[0]["affected_count"] is None
assert reports[1]["affected_count"] == 0


actual = summarize_checked_reports(reports, "accessibility")
expected = {"known_total":0,"zero_reports":1,"unknown_reports":1}
assert actual == expected