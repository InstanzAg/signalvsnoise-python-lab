from func.func11_check_reports import check_reports

actual = check_reports([{"id": 7, "affected_count": -2}])
expected = {7: 'negative'}
assert actual == expected

actual = check_reports([])
expected = {}
assert actual == expected

actual = check_reports([
    {"id": 7, "affected_count": 2},
    {"id": 8, "affected_count": 4},
])
expected = {}
assert actual == expected

try:
    check_reports([
        {"id": 7, "affected_count": -2},
        {"id": 7, "affected_count": 4},
    ])
except ValueError:
    pass
else:
    raise AssertionError("Expected ValueError for duplicate IDs")