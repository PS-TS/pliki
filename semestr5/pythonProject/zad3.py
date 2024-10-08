import asyncio


async def main() -> None:
    await asyncio.gather(pierwsza(), druga())


async def pierwsza() -> None:
    await asyncio.sleep(3)
    print("to")


async def druga() -> None:
    await asyncio.sleep(1)
    print("dziala")


if __name__ == "__main__":
    asyncio.run(main())
