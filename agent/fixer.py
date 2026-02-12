import os
from logger import log_action
from ai_reasoner import ai_suggest_fix

def apply_fix(failure_type, error_message=None):
    if failure_type == "missing_dependency":
        log_action("Installing missing dependencies")
        os.system("pip install -r requirements.txt")
        return True
    elif failure_type == "flaky_test":
        log_action("Retrying flaky tests")
        os.system("pytest tests/ --maxfail=1 --reruns 2")
        return True
    elif failure_type == "infra_issue":
        log_action("Restarting environment or agent")
        return True
    elif failure_type == "unknown" and error_message:
        suggestion = ai_suggest_fix(error_message)
        if suggestion:
            log_action(f"Executing AI suggested fix: {suggestion}")
            os.system(suggestion)
            return True
    log_action("Cannot fix the error automatically. Human intervention required.")
    return False
