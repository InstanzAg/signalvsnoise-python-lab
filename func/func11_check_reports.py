from func.func10_ensure_unique_ids import ensure_unique_ids
from func.func08_collect_affected_count_errors import collect_affected_count_errors

def check_reports(reports):
    ensure_unique_ids(reports)
    return collect_affected_count_errors(reports)
    

if __name__ == "__main__":
    reports = [
        {"id": 7, "affected_count": -2},
        {"id": 7, "affected_count": 4},
    ]

    try:
        errors = check_reports(reports)
    except ValueError as error:
        print(f"Check stopped: {error}")
    else:
        print(f"Affected-count errors: {errors}")

    print("Program continues.")


    reports = [
        {"id": 7, "affected_count": 4},
    ]

    try:
        errors = check_reports(reports)
    except ValueError as error:
        print(f"Check stopped: {error}")
    else:
        print(f"Affected-count errors: {errors}")

    print("Program continues.")
    reports = [


        {"id": 7, "affected_count": -2},
    ]

    try:
        errors = check_reports(reports)
    except ValueError as error:
        print(f"Check stopped: {error}")
    else:
        print(f"Affected-count errors: {errors}")

    print("Program continues.")