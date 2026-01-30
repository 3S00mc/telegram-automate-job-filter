from telethon import events
from filters.matcher import match_message
from config.settings import ALLOWED_GROUPS

matched_messages = []

def register_listeners(client):
    @client.on(events.NewMessage)
    async def handler(event):
        if not event.is_group:
            return

        if event.chat_id not in ALLOWED_GROUPS:
            return

        text = event.raw_text or ""
        score = match_message(text)

        if score:
            matched_messages.append({
                "score": score,
                "text": text,
                "chat": event.chat.title,
                "message_id": event.id
            })
