import asyncio
from util.delay_functions import delay


async def hello_world() -> str:
    await delay(1)
    return "Hello World!"


async def main() -> None:
    message = await hello_world()
    print(message)


asyncio.run(main())
