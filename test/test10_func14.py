from func.func14_save_reports import save_reports
from func.func13_load_reports import load_reports

save_reports(reports_in="sample_data/reports.json", path_out="sample_data/saved_reports.json")

actual = load_reports(path="sample_data/saved_reports.json")
expected = load_reports(path="sample_data/reports.json")
assert actual == expected