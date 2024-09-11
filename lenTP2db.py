import mysql.connector

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'crud_example',
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
        columns = ', '.join(kwargs.keys())
        values = tuple(kwargs.values())
        query = f"INSERT INTO {table} ({columns}) VALUES ({', '.join(['%s'] * len(values))})"
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def read(table):
        conn = Database.connect()
        cursor = conn.cursor()
        query = f"SELECT * FROM {table}"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_by_id(table, any_id):
        conn = Database.connect()
        cursor = conn.cursor()
        query = f"SELECT * FROM {table} WHERE id = %s"
        cursor.execute(query, (any_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_by_name(table, name):
        conn = Database.connect()
        cursor = conn.cursor()
        query = f"SELECT * FROM {table} WHERE name = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def update(table, any_id, **kwargs):
        conn = Database.connect()
        cursor = conn.cursor()
        columns = ' = %s, '.join(kwargs.keys()) + ' = %s'
        values = tuple(kwargs.values())
        query = f"UPDATE {table} SET {columns} WHERE id = %s"
        cursor.execute(query, values + (any_id,))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete(table, any_id):
        conn = Database.connect()
        cursor = conn.cursor()
        query = f"DELETE FROM {table} WHERE id = %s"
        cursor.execute(query, (any_id,))
        conn.commit()
        cursor.close()
        conn.close()


def main_menu():
    print("\n--- Main Menu ---")
    print("1. User Management")
    print("2. Store Management")
    print("3. Exit")
    choice = input("Select an option (1-3): ")

    if choice == '1':
        user_management()
    elif choice == '2':
        store_management()
    elif choice == '3':
        print("Exiting program...")
    else:
        print("Invalid choice, please try again.")
        main_menu()


def user_management():
    print("\n--- User Management ---")
    print("1. Create User")
    print("2. Read Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Login")
    print("6. Back to Main Menu")
    choice = input("Select an option (1-6): ")

    if choice == '1':
        create_user_ui()
    elif choice == '2':
        read_users_ui()
    elif choice == '3':
        update_user_ui()
    elif choice == '4':
        delete_user_ui()
    elif choice == '5':
        login_user_ui()
    elif choice == '6':
        main_menu()
    else:
        print("Invalid choice, please try again.")
        user_management()


def store_management():
    print("\n--- Store Management ---")
    print("1. Create Store")
    print("2. Read Stores")
    print("3. Update Store")
    print("4. Delete Store")
    print("5. Back to Main Menu")
    choice = input("Select an option (1-5): ")

    if choice == '1':
        create_store_ui()
    elif choice == '2':
        read_stores_ui()
    elif choice == '3':
        update_store_ui()
    elif choice == '4':
        delete_store_ui()
    elif choice == '5':
        main_menu()
    else:
        print("Invalid choice, please try again.")
        store_management()


def create_user_ui():
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    telephone = input("Enter telephone: ")
    address = input("Enter address: ")
    status = input("Enter status: ")
    store_id = input("Enter store: ")

    Database.create(
        'users',
        name=name,
        email=email,
        password=password,
        telephone=telephone,
        address=address,
        status=status,
        store_id=store_id
    )
    print("User created successfully.")
    user_management()


def read_users_ui():
    users = Database.read('users')
    for user in users:
        print(user)
    user_management()


def update_user_ui():
    user_id = input("Enter user ID to update: ")

    user = Database.read_by_id('users', user_id)
    if not user:
        print("User not found.")
        user_management()
        return

    (current_name, current_email, current_password, current_telephone, current_address,
     current_status, current_store_id) = user[1:]

    name = input(f"Enter new name (or press Enter to keep current: {current_name}): ") or current_name
    email = input(f"Enter new email (or press Enter to keep current: {current_email}): ") or current_email
    password = input(f"Enter new password (or press Enter to keep current): ") or current_password
    telephone = input(
        f"Enter new telephone (or press Enter to keep current: {current_telephone}): ") or current_telephone
    address = input(f"Enter new address (or press Enter to keep current: {current_address}): ") or current_address
    status = input(f"Enter new status (or press Enter to keep current: {current_status}): ") or current_status
    store_id = input(f"Enter new store (or press Enter to keep current: {current_store_id}): ") or current_store_id

    Database.update('users',
                    user_id,
                    name=name,
                    email=email,
                    password=password,
                    telephone=telephone,
                    address=address,
                    status=status,
                    store_id=store_id
                    )
    print("User updated successfully.")
    user_management()


def delete_user_ui():
    user_id = input("Enter user ID to delete: ")
    Database.delete('users', user_id)
    print("User deleted successfully.")
    user_management()


def create_store_ui():
    name = input("Enter store name: ")
    address = input("Enter store address: ")

    Database.create(
        'stores',
        name=name,
        address=address
    )
    print("Store created successfully.")
    store_management()


def read_stores_ui():
    stores = Database.read('stores')
    for store in stores:
        print(store)
    store_management()


def update_store_ui():
    store_id = input("Enter store ID to update: ")

    store = Database.read_by_id('stores', store_id)
    if not store:
        print("Store not found.")
        store_management()
        return

    current_name = store[1]
    current_address = store[2]

    name = input(f"Enter new name (or press Enter to keep current: {current_name}): ") or current_name
    address = input(f"Enter new address (or press Enter to keep current: {current_address}): ") or current_address

    Database.update('stores',
                    store_id,
                    name=name,
                    address=address
                    )
    print("Store updated successfully.")
    store_management()


def delete_store_ui():
    store_id = input("Enter store ID to delete: ")
    Database.delete('stores', store_id)
    print("Store deleted successfully.")
    store_management()


def login_user_ui():
    username = input("Enter username: ")
    user = Database.read_by_name('users', username)
    if user is None:
        print("Username not found.")
        return
    password = input("Enter password: ")
    if user[3] == password:
        print("Login successful.")
    else:
        print("Invalid password.")
    user_management()


main_menu()
