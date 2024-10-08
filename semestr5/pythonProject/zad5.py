import asyncio


async def main(liczba: int) -> None:
    i = 1
    poprzednia = 0
    nastepna = 1
    while i <= liczba:

        tym = poprzednia + nastepna
        poprzednia = nastepna
        nastepna = tym
        print(poprzednia)
        i = i+1
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main(10))
