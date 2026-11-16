def validate_affected_count(report):
    if "affected_count" not in report:
        return "missing"
    check_aff_count = report["affected_count"]

    if check_aff_count is None:       # None means no problem
        return None
    elif type(check_aff_count) is int and check_aff_count >= 0:
        return None
    elif type(check_aff_count) is int and check_aff_count < 0:
        return "negative"
    else:
        return "invalid_type"


if __name__ == "__main__":
    print(validate_affected_count({"affected_count":4}))
    print(validate_affected_count({}))
    