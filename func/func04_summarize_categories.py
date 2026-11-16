from func.func03_summerize_open_reports import summarize_open_reports

def summarize_categories(reports, categories):
    summary_categories = {}
    for category in categories:
        summary_categories[category] = summarize_open_reports(reports, category)
    return summary_categories
    


if __name__ == "__main__":
    from sample_data.sample_data01 import reports
    
    print(summarize_categories(
        reports,
        ["accessibility", "infrastructure", "education"],
    ))