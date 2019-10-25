import asyncio


async def get_nums():
    i = 1
    while True:
        print(i)
        i += 1
        await asyncio.sleep(0.5)


async def get_time():
    passed_seconds = 0
    while True:
        if passed_seconds % 5 == 0:
            print(f'{passed_seconds} seconds was passed')
        passed_seconds += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(get_nums())
    task2 = asyncio.create_task((get_time()))

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()

    asyncio.run(main())