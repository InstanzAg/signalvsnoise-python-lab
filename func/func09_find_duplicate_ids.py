from collections import Counter

def find_duplicate_ids(reports):
    duplicate_ids = set()
    cnt = Counter()
    for report in reports:
        cnt[report["id"]] += 1

    for report_id in cnt:                  # cycles through the ids and their counts given over to counter
        if cnt[report_id] > 1:
            duplicate_ids.add(report_id)
    return duplicate_ids


def find_duplicate_ids_with_sets(reports):
    seen_ids = set()
    duplicate_ids = set()
    
    for report in reports:
        if report["id"] in seen_ids:
            duplicate_ids.add(report["id"])
        seen_ids.add(report["id"])
    return duplicate_ids


reports = [
    {"id": 42},
    {"id": 7},
    {"id": 42},
    {"id": 9},
    {"id": 7},
    {"id": 42},
]

if __name__ == "__main__":
    print(find_duplicate_ids(reports))
    print(find_duplicate_ids_with_sets(reports))