import json, os
from datetime import datetime

DATA_PATH = "tracked.json"

def load_data():
    if not os.path.exists(DATA_PATH):
        return {}
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=4)

async def check_online_status(client, user_id):
    try:
        user = await client.get_entity(user_id)
        if user.status is None:
            return "offline", "Unknown"
        if hasattr(user.status, "was_online"):
            return "offline", str(user.status.was_online)
        if hasattr(user.status, "expires"):
            return "online", str(user.status.expires)
        return "online", str(datetime.now())
    except Exception:
        return "unknown", "error"
