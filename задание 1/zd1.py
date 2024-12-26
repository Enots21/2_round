import asyncio
import sqlite3

from faker import Faker

from main import *

faker = Faker()


async def input_db():
    """
    Input data to database
    """
    if not await db.create_tables():
        await db.create_tables()
    else:
        print("Tables already exist")

    users = [
        (faker.name(), faker.email(),
         faker.random_int(min=18, max=100),
         faker.random_int(min=0, max=1000))
        for _ in range(10)  # Замените N на нужное количество пользователей
    ]

    for user, email, age, balance in users:
        await db.add_input(user, email, age, balance)
        await db.update_db()

    await db.delete_db()

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Выполнение запроса
cursor.execute("SELECT username, age FROM users WHERE age != 60")
results = cursor.fetchall()

# Вывод записей в консоль
for row in results:
    username, age = row
    print(f"Имя: {username} | Возраст: {age}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(input_db())
