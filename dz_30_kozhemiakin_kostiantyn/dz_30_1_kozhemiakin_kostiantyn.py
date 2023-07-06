import hashlib


class UserAuthentication:
    def __init__(self, table_size=100):
        self.table_size = table_size
        self.hash_table = {}

    def hash_function(self, key):
        return hashlib.md5(key.encode()).hexdigest()

    def add_user(self, login, password):
        hashed_password = self.hash_function(password)
        if login in self.hash_table:
            print(f"{login} already exists.")
        else:
            self.hash_table[login] = hashed_password

    def remove_user(self, login):
        if login in self.hash_table:
            del self.hash_table[login]
        else:
            print(f"{login} does not exist.")

    def register_user(self):
        print("register_user")
        while True:
            login = input("Enter login: ")
            if login in self.hash_table:
                print(f"{login} is already exists.")
                continue
            break
        password = input("Enter password: ")
        self.add_user(login, password)
        print(f"{login} has been registered.")

    def find_user(self, login):
        if login in self.hash_table:
            print(f"{login} found in database.")
        else:
            print(f"{login} not found in database.")

    def authorize_user(self):
        print("authorize_user")
        login = input("Enter login: ")
        password = input("Enter password: ")
        hashed_password = self.hash_function(password)
        stored_password = self.hash_table.get(login)
        if stored_password is None:
            print("Invalid login or password.")
        elif hashed_password == stored_password:
            print("Authorized successfully.")
        else:
            print("Invalid login or password.")

    def print_table(self):
        for login, hashed_password in self.hash_table.items():
            print(f"{login}: {hashed_password}")


user_auth = UserAuthentication()

user_auth.add_user("user1", "password1")
user_auth.add_user("user2", "password2")
user_auth.add_user("user3", "password3")
user_auth.print_table()
user_auth.add_user("user2", "ааааааааа")
user_auth.print_table()
user_auth.remove_user('user2')
user_auth.print_table()
user_auth.find_user("user1")
user_auth.register_user()
user_auth.authorize_user()
user_auth.print_table()
