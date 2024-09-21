import mysql.connector

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


## Manejo de usuario para tp 4
def login_user_ui():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = Database.login(username, password)
    if user:
        print("Login successful!")

    else:
        print("Invalid username or password.")


login_user_ui()
