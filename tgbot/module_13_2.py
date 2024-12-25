import asyncio  # Библиотека синхронизации
import logging  # Библиотека логирования

from aiogram import Bot, Dispatcher, types, Router, F  # Библиотека
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

import config  # настройка конфигурации подключение Токена
from statess import UserState

loop = asyncio.get_event_loop()  # синхронизация
bot = Bot(token=config.TOKEN, loop=loop)  # бот
storage = MemoryStorage()  # синхронизация
dp = Dispatcher(storage=storage)  # Диспетчер

logging.basicConfig(level=logging.INFO)  # логирование

router = Router()  # Создание роутера


@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@router.message(F.text == 'Calories')
async def set_age(message: types.Message, state: FSMContext):
    await message.answer('Введите свой возраст:')
    await state.set_state(UserState.age)


@router.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await state.set_state(UserState.growth)


@router.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)


@router.message(UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    await message.answer('Какой у вас пол М.Ж')
    await state.set_state(UserState.floor)


@router.message(UserState.floor)
async def send_floor(message: types.Message, state: FSMContext):
    await state.update_data(floor=message.text)
    date = await state.get_data()
    age = date['age']
    growth = date['growth']
    weight = date['weight']
    floor = date['floor']
    floos = floor.lower()
    if floos == 'м':
        calor = 10 * int(weight) + 6.25 * int(growth) - 5 * int(age) + 5
    else:
        calor = 10 * int(weight) + 6.25 * int(growth) - 5 * int(age) - 161
    await message.answer(f'Ваша норма калорий в день {calor}')
    await state.clear()


async def main():  # Запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    # asyncio.run(main())
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.create_task(main())
        loop.run_forever()
        print("ok")
    except KeyboardInterrupt:
        print("404")
