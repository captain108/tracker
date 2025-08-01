from telethon import TelegramClient, events
import asyncio, json, os
from utils.tracking_utils import load_data, save_data, check_online_status

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = "tracker_userbot"

client = TelegramClient(SESSION, API_ID, API_HASH)

@client.on(events.NewMessage(pattern="/addtracking"))
async def handler(event):
    if event.is_private:
        username = event.raw_text.split(maxsplit=1)[1].strip()
        entity = await client.get_entity(username)
        user_id = str(entity.id)
        data = load_data()
        data[user_id] = {
            "username": entity.username,
            "last_status": "unknown",
            "last_seen": None
        }
        save_data(data)
        await event.reply(f"🔍 Tracking started for `{entity.username}` (ID: {user_id})")

async def monitor_users():
    while True:
        data = load_data()
        for user_id in data:
            status, last_seen = await check_online_status(client, int(user_id))
            data[user_id]["last_status"] = status
            data[user_id]["last_seen"] = last_seen
        save_data(data)
        await asyncio.sleep(30)

async def main():
    await client.start()
    print("✅ UserBot running.")
    await monitor_users()

client.loop.run_until_complete(main())
