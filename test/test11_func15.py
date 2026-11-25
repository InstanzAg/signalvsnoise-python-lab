import json
from func.func15_add_report import add_report, save_reports, load_reports
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    reports = [
        {"id": 1, "category": "accessibility", "status": "open", "affected_count": None},
        {"id": 2, "category": "accessibility", "status": "open", "affected_count": 0}
    ]
    file_path = Path(temp_dir) / "reports.json"
    save_reports(reports, file_path)
    
    report3 = {"id": 3, "category": "accessibility", "status": "open", "affected_count": 4}
    # print(load_reports(file_path))
    add_report(file_path, report3)
    actual = load_reports(file_path)
    # print(load_reports(file_path))
    expected = [reports[0],reports[1],report3]
    assert actual == expected