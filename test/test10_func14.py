from func.func14_save_reports import load_reports ,save_reports
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    input_path =  Path("sample_data") / "reports.json"
    output_path = Path(temp_dir) / "saved_reports.json"
    reports = load_reports(path=input_path)
    # print(reports)
    reports[0]["affected_count"] = 3
    # print(reports)
    save_reports(reports=reports, path_out=output_path)

    actual = load_reports(path=output_path)
    # print(actual)
    assert actual == reports
