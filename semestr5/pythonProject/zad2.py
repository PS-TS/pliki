import asyncio


async def main() -> None:
    await asyncio.sleep(1)
    print("Hello")
    await asyncio.sleep(1)
    print("World")


if __name__ == "__main__":
    asyncio.run(main())
