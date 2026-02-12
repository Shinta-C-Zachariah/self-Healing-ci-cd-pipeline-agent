from ci_api import get_latest_workflow_run, get_workflow_logs, rerun_workflow
from analyzer import analyze_failure
from fixer import apply_fix
from logger import log_action
import zipfile
import os

MAX_RETRIES = 3


def extract_log_text(zip_file):
    extract_path = "logs"
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    
    log_text = ""
    # Walk through all files recursively
    for root, dirs, files in os.walk(extract_path):
        for fname in files:
            file_path = os.path.join(root, fname)
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    log_text += f.read()
            except Exception as e:
                print(f"Could not read {file_path}: {e}")
    return log_text

def self_heal_pipeline():
    run_info = get_latest_workflow_run()
    run_id = run_info["id"]

    if run_info["conclusion"] == "success":
        log_action("Pipeline succeeded. No action needed.")
        return

    retries = 0
    while retries < MAX_RETRIES:
        log_action(f"Analyzing failure of run {run_id}")
        zip_file = get_workflow_logs(run_id)
        log_text = extract_log_text(zip_file)
        failure_type = analyze_failure(log_text)

        fixed = apply_fix(failure_type, error_message=log_text)

        if not fixed:
            log_action("Cannot auto-fix. Alerting human.")
            break

        log_action("Rerunning pipeline")
        rerun_workflow(run_id)
        retries += 1
        log_action(f"Retry attempt {retries} complete")

if __name__ == "__main__":
    self_heal_pipeline()
