
import requests
import base64


class GitHubService:

    def __init__(self):
        self.base_url = "https://api.github.com"

    # Get repository details
    def get_repository(self, owner, repo):

        url = f"{self.base_url}/repos/{owner}/{repo}"

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        return response.json()

    # Get repository files and folders
    def get_repository_files(self, owner, repo):

        url = f"{self.base_url}/repos/{owner}/{repo}/contents"

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        return response.json()

    # Get source code of a specific file
    def get_file_content(self, owner, repo, path):

        url = f"{self.base_url}/repos/{owner}/{repo}/contents/{path}"

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        file_data = response.json()

        if file_data.get("type") != "file":
            raise ValueError("The requested path is not a file.")

        if file_data.get("encoding") != "base64":
            raise ValueError("Unsupported file content encoding.")

        encoded_content = file_data["content"]

        decoded_content = base64.b64decode(
            encoded_content
        ).decode("utf-8", errors="replace")

        return decoded_content
