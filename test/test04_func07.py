from func.func07_validate_affected_count import validate_affected_count

actual = validate_affected_count({})
expected = "missing"
assert actual == expected

actual = validate_affected_count({"affected_count": None})
expected = None
assert actual == expected

actual = validate_affected_count({"affected_count": 0})
expected = None
assert actual == expected

actual = validate_affected_count({"affected_count": 4})
expected = None
assert actual == expected

actual = validate_affected_count({"affected_count": -2})
expected = "negative"
assert actual == expected

actual = validate_affected_count({"affected_count": "4"})
expected = "invalid_type"
assert actual == expected

actual = validate_affected_count({"affected_count": 4.0})
expected = "invalid_type"
assert actual == expected

actual = validate_affected_count({"affected_count": True})
expected = "invalid_type"
assert actual == expected

actual = validate_affected_count({"id": 1})
expected = "missing"
assert actual == expected

actual = validate_affected_count({"id": 1, "affected_count": -2})
expected = "negative"
assert actual == expected

actual = validate_affected_count({"category": "accessibility", "affected_count": 4})
expected = None
assert actual == expected



