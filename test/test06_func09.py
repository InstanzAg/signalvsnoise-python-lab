from func.func09_find_duplicate_ids import find_duplicate_ids, find_duplicate_ids_with_sets


reports = [
    {"id": 42},
    {"id": 7},
    {"id": 42},
    {"id": 9},
    {"id": 7},
    {"id": 42},
]


actual = find_duplicate_ids(reports)
expected = {42, 7}
assert actual == expected

actual = find_duplicate_ids([{"id":42}, {"id":7}])
expected = set()
assert actual == expected

actual = find_duplicate_ids([])
expected = set()
assert actual == expected

actual = find_duplicate_ids_with_sets(reports)
expected = {42, 7}
assert actual == expected

actual = find_duplicate_ids_with_sets([{"id":42}, {"id":7}])
expected = set()
assert actual == expected

actual = find_duplicate_ids_with_sets([])
expected = set()
assert actual == expected