import asyncio
import sys
from datetime import datetime, timedelta

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()
    )

from telegram.client import get_client
from telegram.listeners import register_listeners, matched_messages
from config.settings import SUMMARY_HOUR


async def daily_summary(client):
    while True:
        now = datetime.now()
        target = now.replace(hour=SUMMARY_HOUR, minute=0, second=0, microsecond=0)

        if now >= target:
            target += timedelta(days=1)

        await asyncio.sleep((target - now).seconds)

        if not matched_messages:
            await client.send_message("me", "📭 Nenhuma vaga Java Júnior hoje.")
            continue

        msg = "📌 Resumo diário – Vagas Java Júnior\n\n"

        for m in matched_messages:
            msg += (
                f"🔥 Score {m['score']} | {m['chat']}\n"
                f"{m['text'][:300]}...\n\n"
            )

        await client.send_message("me", msg)
        matched_messages.clear()


async def main():
    client = get_client()
    register_listeners(client)

    async with client:
        await daily_summary(client)


if __name__ == "__main__":
    asyncio.run(main())
