from func.func06_find_missing_fields import find_missing_fields

reports01 = [
    {"id": 1, "category": "accessibility", "status": "open", "affected_count": 4},
    {"id": 2, "category": "infrastructure", "status": "open", "affected_count": None},
    {"id": 3, "category": "accessibility", "status": "open"},
    {"id": 4, "affected_count": 2},
]

reports02 = [
    {"id": 1, "category": "accessibility", "status": "open", "affected_count": 4},
    {"id": 2, "category": "infrastructure", "status": "open", "affected_count": None},
    {"id": 42, "category": None, "status": "open"},
    {"id": 7, "affected_count": 2},
]

needed_information01 = (
    "category",
    "status",
    "affected_count"
)

needed_information02 = ()

actual = find_missing_fields(reports01, needed_information01)
expected = {3: ['affected_count'], 4: ['category', 'status']}
assert actual == expected

actual = find_missing_fields(reports01[::-1], needed_information01)
expected = {3: ['affected_count'], 4: ['category', 'status']}
assert actual == expected

actual = find_missing_fields(reports02[::-1], needed_information01)
expected = {42: ['affected_count'], 7: ['category', 'status']}
assert actual == expected

actual = find_missing_fields([], needed_information01)
expected = {}
assert actual == expected

actual = find_missing_fields(reports01, needed_information02)
expected = {}
assert actual == expected