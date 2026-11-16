from func.func07_validate_affected_count import validate_affected_count


def collect_affected_count_errors(reports):
    faulty_reports = {}
    
    for report in reports:    
        potential_fault = validate_affected_count(report)
        if potential_fault is not None:
            faulty_reports[report["id"]] = potential_fault
    
    return faulty_reports

if __name__ == "__main__":
    print(collect_affected_count_errors([]))