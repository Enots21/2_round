import hashlib
import time
# Всего будет 3 класса: UrTube, Video, User.

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

        # Функция хеширования пароля.
    def hash_password(self, password):  # https://docs.python.org/3/library/hashlib.html
        """Хеширование пароля с использованием алгоритма SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()  # https://www.yourtodo.ru/posts/heshirovanie-v-python/

        # Функция проверки пользователя по имени пользователя.
    def __eq__(self, other):
        """Переопределяем метод сравнения, чтобы проверять пользователя по имени пользователя."""
        return self.nickname == other.nickname

        # Функция строкового представления имени и возраста пользователя.
    def __str__(self):
        return f"{self.nickname}"


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item in self.title

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None


    def log_in(self, nickname, password):
        """Проверяет наличие пользователя с указанным логином и паролем."""
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                # Если такой пользователь существует, то current_user меняется на найденного.
                self.current_user = user
                print(f"Пользователь {nickname} вошёл в систему.")
                return True
        print("Ошибка входа: неверный логин или пароль.")
        return False

    def register(self, nickname, password, age):
        new_users = User(nickname, password, age)
        if new_users in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(new_users)
            self.current_user = new_users




    def log_out(self):
        self.current_user = None
        return None

    def add(self, *args):
        for movie in args:
            if movie not in self.videos:
                self.videos.append(movie)




    def get_videos(self, text: str):
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie


    def watch_video(self, movie: str):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for x in self.videos:
            if x.title == movie:
                if x.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    return

                for i in range(x.duration):
                    print(i, end=' ')
                    x.time_now += 1
                x.time_now = 0
                print('Конец видео')





ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')