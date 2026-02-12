def analyze_failure(log_text):
    if "ModuleNotFoundError" in log_text:
        return "missing_dependency"
    elif "AssertionError" in log_text:
        return "flaky_test"
    elif "TimeoutError" in log_text:
        return "infra_issue"
    else:
        return "unknown"
