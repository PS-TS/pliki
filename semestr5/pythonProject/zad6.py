import asyncio
import random


async def main() -> None:
    wynik = await asyncio.gather(fetch(3), fetch(1), fetch(4), fetch(1))
    print(wynik)

async def fetch(delay: int) -> int:
    await asyncio.sleep(delay)
    return random.randint(1, 6)


if __name__ == "__main__":
    asyncio.run(main())
