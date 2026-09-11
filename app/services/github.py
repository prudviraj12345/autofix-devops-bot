import os

from dotenv import load_dotenv
from github import Github


load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

github = Github(GITHUB_TOKEN)

REPO_NAME = "prudviraj12345/autofix-devops-bot"
DEV_BRANCH = "Dev"


def get_repository():
    return github.get_repo(REPO_NAME)


def test_github_connection():
    if not GITHUB_TOKEN:
        return {
            "status": "error",
            "message": "GITHUB_TOKEN not found in .env"
        }

    user = github.get_user()

    return {
        "github_username": user.login,
        "message": "GitHub connection successful"
    }


def get_dev_branch():
    repo = get_repository()

    return repo.get_branch(DEV_BRANCH)


def get_dev_files():
    repo = get_repository()

    contents = repo.get_contents(
        "",
        ref=DEV_BRANCH
    )

    files = []

    for item in contents:
        if item.type == "file":
            files.append(item.path)

    return {
        "branch": DEV_BRANCH,
        "files": files
    }