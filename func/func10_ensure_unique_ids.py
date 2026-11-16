from func.func09_find_duplicate_ids import find_duplicate_ids_with_sets

def ensure_unique_ids(reports):
    duplicate_ids = find_duplicate_ids_with_sets(reports)
    if duplicate_ids:
        raise ValueError(f"Duplicate report Ids found: {duplicate_ids}")
    return None

if __name__ == "__main__":
    print(ensure_unique_ids([{"id": 42}, {"id": 8}]))
    print(ensure_unique_ids([{"id": 42}, {"id": 42}]))