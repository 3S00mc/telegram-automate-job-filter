import asyncio
import sys

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()
    )

from telethon import TelegramClient
from config.settings import API_ID, API_HASH, SESSION_NAME

async def main():
    async with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        async for dialog in client.iter_dialogs():
            if dialog.is_group:
                print(dialog.name, dialog.id)

if __name__ == "__main__":
    asyncio.run(main())
