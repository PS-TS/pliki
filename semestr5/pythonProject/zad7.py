import asyncio


async def main() -> None:
    await asyncio.gather(kucharz1(),kucharz2(),kucharz3())


async def kucharz1() -> None:
    kucharz = "Kucharz 1 "
    await krojenie(kucharz)
    await gotowanie(kucharz)
    await pieczenie(kucharz)

async def kucharz2() -> None:
    kucharz = "Kucharz 2 "
    await krojenie(kucharz)
    await pieczenie(kucharz)
    await smazenie(kucharz)

async def kucharz3() -> None:
    kucharz = "Kucharz 3 "
    await smazenie(kucharz)
    await gotowanie(kucharz)
    await krojenie(kucharz)

async def krojenie(kucharz) -> None:
    await asyncio.sleep(5)
    print(kucharz + "sieka ")

async def gotowanie(kucharz) -> None:
    await asyncio.sleep(6)
    print(kucharz + "gotuje ")

async def smazenie(kucharz) -> None:
    await asyncio.sleep(4)
    print(kucharz + "smaży ")

async def pieczenie(kucharz) -> None:
    await asyncio.sleep(1)
    print(kucharz + "piecze ")

if __name__ == "__main__":
    asyncio.run(main())