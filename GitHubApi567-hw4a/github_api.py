# github_api.py
import requests

def fetch_repo_commit_data(user_id):
    base_url = "https://api.github.com/"
    repos_response = requests.get(base_url +'users/'+ user_id + "/repos")

    if repos_response.status_code != 200:
        return f"Failed to fetch repositories for {user_id}"

    repos = repos_response.json()
    repo_data = []

    for repo in repos:
        repo_name = repo['name']
        commits_response = requests.get(base_url + f"repos/{user_id}/{repo_name}/commits")

        if commits_response.status_code != 200:
            commit_count = "Failed to fetch commit count"
        else:
            commit_count = len(commits_response.json())

        repo_data.append((repo_name, commit_count))

    return repo_data
