import asyncio
import time


async def get_temp():
    print('Первое показание')
    await asyncio.sleep(3)
    print('21 градус')


async def get_pres():
    print('Второе показание')
    await asyncio.sleep(5)
    print('121 кпа')


async def main():
    print('Запуск программы')
    task1 = asyncio.create_task(get_temp())  # Первое показание#
    task2 = asyncio.create_task(get_pres())  # Второе показание
    await task1
    await task2
    print('Завершение программы')


start = time.time()
asyncio.run(main())  # Запуск программы
finish = time.time()

print(f'Время выполнения программы: {round(finish - start, 2)}')
