from pyrogram import Client, filters
import os, json
from utils.tracking_utils import load_data, save_data

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

bot = Client("controlbot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@bot.on_message(filters.command("listtracking"))
async def list_tracking(client, message):
    data = load_data()
    if not data:
        await message.reply("❌ No users are being tracked.")
    else:
        msg = "📊 **Tracking List:**\n\n"
        for uid, info in data.items():
            msg += f"• `{info['username']}` - **{info['last_status']}** (Last seen: `{info['last_seen']}`)\n"
        await message.reply(msg)

@bot.on_message(filters.command("cleartracking"))
async def clear_tracking(client, message):
    save_data({})
    await message.reply("✅ All tracking cleared.")

bot.run()
