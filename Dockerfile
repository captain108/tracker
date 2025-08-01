FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV API_ID=your_api_id
ENV API_HASH=your_api_hash
ENV BOT_TOKEN=your_bot_token

CMD ["sh", "-c", "python userbot.py & python controlbot.py & python dashboard/app.py"]
