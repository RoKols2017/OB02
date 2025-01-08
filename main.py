class User:
    def __init__(self, user_id, name):
        self._id = user_id
        self._name = name
        self._access_level = 'user'

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def access_level(self):
        return self._access_level

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', access_level='{self.access_level}')"


class Admin(User):
    def __init__(self, admin_id, name):
        super().__init__(admin_id, name)
        self._access_level = 'admin'
        self.users = []

    def add_user(self, new_user):
        if isinstance(new_user, User):
            self.users.append(new_user)
        else:
            raise TypeError("new_user must be an instance of the User class")

    def remove_user(self, user_to_remove):
        try:
            self.users.remove(user_to_remove)
        except ValueError as e:
            print(f"User not found in the list: {e}")

# Создание обычного пользователя
john = User(1, "John Doe")
print(john)  # Output: User(id=1, name='John Doe', access_level='user')

# Создание администратора
alice = Admin(2, "Alice Smith")
print(alice)  # Output: User(id=2, name='Alice Smith', access_level='admin')

# Добавляем Джона в список пользователей Алисы
alice.add_user(john)
print(alice.users)  # Output: [User(id=1, name='John Doe', access_level='user')]

# Пытаемся добавить объект, который не является пользователем
try:
    alice.add_user("Not a user object")
except TypeError as e:
    print(e)  # Output: new_user must be an instance of the User class

# Удаляем Джона из списка пользователей Алисы
alice.remove_user(john)
print(alice.users)  # Output: []