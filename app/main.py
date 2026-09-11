from fastapi import FastAPI
from app.services.telegram import send_telegram_message

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