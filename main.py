class User:
    def __init__(self, user_id, name):
        # Уникальный идентификатор пользователя
        self._user_id = user_id
        # Имя пользователя
        self._name = name
        # Уровень доступа (по умолчанию "user")
        self._access_level='user'

    # Получить ID пользователя
    def get_user_id(self):
        return self._user_id

    # Получить имя пользователя
    def get_name(self):
        return self._name

    # Установить новое имя пользователя
    def set_name(self, name):
        self._name = name

    # Получить уровень доступа пользователя
    def get_access_level(self):
        return self._access_level

class Admin(User):
    def __init__(self, user_id, name):
        # Инициализация базового класса User с уровнем доступа "admin"
        super().__init__(user_id, name)
        # Дополнительный уровень доступа для администратора
        self._admin_access_level='admin'

    # Получить уровень доступа администратора
    def get_admin_access_level(self):
        return self._admin_access_level

    # Добавить пользователя в систему
    def add_user(self, user_list, user):
        users_list.append(user)
        print(f"Пользователь {user.get_name()} успешно добавлен.")

    # Удалить пользователя из системы по ID
    def remove_user(self, users_list, user):
        users_list.remove(user)
        print(f"Пользователь {user.get_name()} успешно удален.")

# Вывести список всех пользователей в системе
def list_users(users_list):
    if not users_list:
        print("В системе нет пользователей.")
    else:
        print("Список пользователей в системе:")
        for user in users_list:
            print(f"Пользователь {user.get_name()}")

# Пример использования
if __name__ == "__main__":
    # Список всех пользователей в системе
    users_list = []

    # Вывод списка пользователей
    list_users(users_list)

    # Создание пользователей
    user1 = User(1, "Алексей")
    user2 = User(2, "Мария")

    # Создание администратора
    admin1 = Admin(0, "Иван")

    # Добавление пользователей в список админа1
    admin1.add_user(users_list, user1)
    admin1.add_user(users_list, user2)

    # Вывод списка пользователей
    list_users(users_list)

    # Удаление пользователя
    admin1.remove_user(users_list, user1)

    # Вывод списка пользователей после удаления
    list_users(users_list)
