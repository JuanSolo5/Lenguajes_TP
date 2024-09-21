import mysql.connector
import getpass  ## para que no sea visible la pass en consola al escribirla
import sys  ## para poder cerrar la terminal de PY
from lenTP2db import (
    create_user_ui,
    read_users_ui,
    update_user_ui,
    delete_user_ui,
)  ## me traigo las funciones que necesito de " lenTP2db.py "

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
            elif role == "Empleado":
                user_actions()
            else:
                print("Unknown role.")
        else:
            print("Role not found.")
    else:
        print("Invalid username or password.")


## ROL ADMIN
def admin_actions():
    user_management_admin()


def user_management_admin():
    print("\n--- User Administrador ---")
    print("1. Create User")
    print("2. Update User")
    print("3. Delete User")
    print("4. Exit")

    choice = input("Select an option (1-3): ")

    if choice == "1":
        create_user_ui()
    elif choice == "2":
        update_user_ui()
    elif choice == "3":
        delete_user_ui()
    elif choice == "4":
        print("Closing terminal...")
        sys.exit()
    else:
        print("Invalid choice, please try again.")
        user_management_admin()


## ROL EMPLEADO
def user_actions():
    user_management_employee()


def user_management_employee():
    print("\n--- User Employee ---")
    print("1. Read Users")
    print("2. Exit")

    choice = input("Select an option (1-3): ")

    if choice == "1":
        read_users_ui()
    elif choice == "2":
        print("Closing terminal...")
        sys.exit()
    else:
        print("Invalid choice, please try again.")
        user_management_employee()


## Es para que se ejecute solo este codigo, ya que importe las funciones del otro archivo
if __name__ == "__main__":

    login_user_ui()
