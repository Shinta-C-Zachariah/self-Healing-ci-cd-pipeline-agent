import requests

GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"
REPO = "username/self_healing_agentic_ai"

def get_latest_workflow_run():
    url = f"https://api.github.com/repos/{REPO}/actions/runs?per_page=1"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    resp = requests.get(url, headers=headers).json()
    run = resp['workflow_runs'][0]
    return {
        "id": run['id'],
        "status": run['status'],
        "conclusion": run.get('conclusion')
    }

def get_workflow_logs(run_id):
    url = f"https://api.github.com/repos/{REPO}/actions/runs/{run_id}/logs"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    resp = requests.get(url, headers=headers)
    zip_file = f"logs_{run_id}.zip"
    with open(zip_file, "wb") as f:
        f.write(resp.content)
    return zip_file

def rerun_workflow(run_id):
    url = f"https://api.github.com/repos/{REPO}/actions/runs/{run_id}/rerun"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    resp = requests.post(url, headers=headers)
    return resp.status_code == 201
