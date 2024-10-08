import asyncio


async def main() -> None:
    i = 1
    while i <= 5:
        print(i)
        await asyncio.sleep(1)
        i = i+1


if __name__ == "__main__":
    asyncio.run(main())
