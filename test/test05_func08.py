from func.func08_collect_affected_count_errors import collect_affected_count_errors


reports = [
    {"id": 42, "affected_count": 4},
    {"id": 7, "affected_count": -2},
    {"id": 15},
    {"id": 3, "affected_count": None},
    {"id": 9, "affected_count": True},
    {"id": 9, "affected_count": -5},
    {"id": 9, "affected_count": None},
]

actual = collect_affected_count_errors([])
expected = {}
assert actual == expected

actual = collect_affected_count_errors(reports)
expected = {
    7 : 'negative',
    15 : 'missing',
    9 : 'negative'
}
assert actual == expected

# actual = 
# expected = 
# assert actual == expected

# actual = 
# expected = 
# assert actual == expected

# actual = 
# expected = 
# assert actual == expected

# actual = 
# expected = 
# assert actual == expected

