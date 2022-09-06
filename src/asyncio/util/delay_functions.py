import asyncio
import datetime


async def delay(period: int) -> int:
    print(f"[{datetime.datetime.utcnow()}] Sleeping for {period} second(s).")
    await asyncio.sleep(period)
    print(f"[{datetime.datetime.utcnow()}] Finished sleeping for {period} second(s).")
    return period
