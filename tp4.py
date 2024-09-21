import mysql.connector
import getpass

config = {
    "user": "root",
    "password": "",
    "host": "localhost",
    "database": "crud_example",
}


class Database:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def connect():
        return mysql.connector.connect(**config)

    @staticmethod
    def create(table, **kwargs):
        conn = Database.connect()
        cursor = conn.cursor()
        columns = ", ".join(kwargs.keys())
        values = tuple(kwargs.values())
        query = f"INSERT INTO {table} ({columns}) VALUES ({', '.join(['%s'] * len(values))})"
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def login(username, password):
        conn = Database.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE name = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

    @staticmethod
    def get_user_role(username):
        conn = Database.connect()
        cursor = conn.cursor()
        query = "SELECT rol FROM users WHERE name = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return result[0]
        else:
            return None


## Manejo de usuario para tp 4
def login_user_ui():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    user = Database.login(username, password)
    user = Database.login(username, password)
    if user:
        print("Login successful!")
        role = Database.get_user_role(username)

        if role:
            print(f"The role of {username} is {role}.")
            if role == "Administrador":
                admin_actions()
            elif role == "Usuario":
                user_actions()
            else:
                print("Unknown role.")
        else:
            print("Role not found.")
    else:
        print("Invalid username or password.")


def admin_actions():
    print("Performing admin actions...")

    print("Admin action 1")
    print("Admin action 2")


def user_actions():
    print("Performing user actions...")

    print("User action 1")
    print("User action 2")


login_user_ui()
