from func.func05_find_incomplete_reports import find_incomplete_reports, reports

actual = find_incomplete_reports(reports)
expected = [3,4]
assert actual == expected

actual = find_incomplete_reports([])
expected = []
assert actual == expected