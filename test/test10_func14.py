from func.func14_save_reports import save_reports
from func.func13_load_reports import load_reports


reports = load_reports(path="sample_data/reports.json")
# print(reports)
reports[0]["affected_count"] = 3
# print(reports)
save_reports(reports=reports, path_out="sample_data/saved_reports.json")

actual = load_reports(path="sample_data/saved_reports.json")
# print(actual)
assert actual == reports