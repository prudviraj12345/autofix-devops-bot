from fastapi import FastAPI

from app.services.telegram import send_telegram_message
from app.services.github import (
    test_github_connection,
    get_dev_branch,
    get_dev_files
)


app = FastAPI(title="Autonomous Auto-Fixing DevOps Bot")


@app.get("/")
def root():
    return {
        "message": "AutoFix DevOps Bot is running"
    }


@app.get("/test-telegram")
async def test_telegram():
    chat_id = 6419973623

    await send_telegram_message(
        chat_id,
        "🤖 AutoFix DevOps Bot is connected successfully!"
    )

    return {
        "status": "Telegram message sent successfully"
    }


@app.get("/test-github-connection")
def github_connection():
    return test_github_connection()


@app.get("/test-github")
def github_branch():
    branch = get_dev_branch()

    return {
        "repository": branch.repository.full_name,
        "branch": branch.name,
        "latest_commit": branch.commit.sha
    }


@app.get("/dev-files")
def dev_files():
    return get_dev_files()