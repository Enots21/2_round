import aiosqlite



class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    async def connect(self):  # connect to database
        self.conn = await aiosqlite.connect(self.db_name)

    async def disconnect(self):  # disconnect from database
        if self.conn:
            await self.conn.close()

    async def execute_query(self, query, *args):  # Запрос базы данных
        if self.conn is None:
            await self.connect()
        async with self.conn.cursor() as cursor:
            await cursor.execute(query, *args)
            result = await cursor.fetchall()
        await self.conn.commit()

        return result

    async def create_tables(self) -> None:  # Создание таблицы
        if self.conn is None:
            await self.connect()

        await self.execute_query('''
                   CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY,
                   username TEXT NULL,
                   email TEXT NULL,
                   age TEXT NULL,
                   balance TEXT NULL
               )
               ''')

    async def add_input(self, username, email, age, balance):
        await self.execute_query('''
            INSERT INTO users (username, email, age, balance)
            VALUES (?, ?, ?, ?)
        ''', (username, email, age, balance))  # Оберните параметры в кортеж

    async def update_db(self):
        await self.execute_query('''
        UPDATE users
        SET balance = 500
        WHERE id IN (
            SELECT id
            FROM (
                SELECT id, ROW_NUMBER() OVER (ORDER BY id) as rownum
                FROM users
            )
            WHERE rownum % 2 = 1
        )
    ''')  # Обратите внимание на запятую, чтобы создать кортеж

    async def delete_db(self):
        await self.execute_query('''
        DELETE FROM users
        WHERE id IN (
            SELECT id
            FROM (
                SELECT id, ROW_NUMBER() OVER (ORDER BY id) as rownum
                FROM users
            )
            WHERE rownum % 3 = 1
        )
    ''')

    async def all_users(self):
        await self.execute_query('''
        SELECT username, age FROM users
        ''')


db = DataBase('not_telegram.db')  # подключение БД
