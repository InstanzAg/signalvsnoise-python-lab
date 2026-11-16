from sample_data.sample_data01 import reports
from func.func04_summarize_categories import summarize_categories

actual = summarize_categories(reports, [])
expected = {}
assert actual == expected

actual = summarize_categories(reports, ["accessibility"])
expected = {'accessibility': {'known_total': 4, 'zero_reports': 1, 'unknown_reports': 1}}
assert actual == expected

actual = summarize_categories([], ["accessibility"])
expected = {'accessibility': {'known_total': 0, 'zero_reports': 0, 'unknown_reports': 0}}
assert actual == expected

actual = summarize_categories(reports, ["education"])
expected = {"education" : {'known_total': 0, 'zero_reports': 0, 'unknown_reports': 0}}
assert actual == expected

print("All checks passed.")