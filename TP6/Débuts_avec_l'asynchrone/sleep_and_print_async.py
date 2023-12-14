import asyncio

async def p1():
    for i in range(1, 11):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    await p1()
    await p1()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
