# Esta version hace todos los requerimientos pero no usa clases lo cual no esta muy bueno.

import mysql.connector

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'crud_example',
}


def connect_db():
    return mysql.connector.connect(**config)


def create_user(name, email, password, telephone, address, status):
    conn = connect_db()
    cursor = conn.cursor()
    query = """
    INSERT INTO users (name, email, password, telephone, address, status)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (name, email, password, telephone, address, status))
    conn.commit()
    cursor.close()
    conn.close()
    print("Usuario creado exitosamente")


def read_users():
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users


def read_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


def read_user_by_username(username):
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = %s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


def update_user(user_id, name, email, password, telephone, address, status, store_id):
    conn = connect_db()
    cursor = conn.cursor()
    query = """
    UPDATE users 
    SET name = %s, email = %s, password = %s, telephone = %s, address = %s, status = %s, store_id = %s 
    WHERE id = %s
    """
    cursor.execute(query, (name, email, password, telephone, address, status, store_id, user_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Usuario actualizado exitosamente")


def delete_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Usuario eliminado exitosamente")


def create_store(name, address):
    conn = connect_db()
    cursor = conn.cursor()
    query = """
    INSERT INTO stores (name, address)
    VALUES (%s, %s)
    """
    cursor.execute(query, (name, address))
    conn.commit()
    cursor.close()
    conn.close()
    print("Sucursal creada exitosamente")


def read_stores():
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM stores"
    cursor.execute(query)
    stores = cursor.fetchall()
    cursor.close()
    conn.close()
    return stores


def read_store(store_id):
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM stores WHERE id = %s"
    cursor.execute(query, (store_id,))
    store = cursor.fetchone()
    cursor.close()
    conn.close()
    return store


def update_store(store_id, name, address):
    conn = connect_db()
    cursor = conn.cursor()
    query = """
    UPDATE stores 
    SET name = %s, address = %s
    WHERE id = %s
    """
    cursor.execute(query, (name, address, store_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Sucursal actualizada exitosamente")


def delete_store(store_id):
    conn = connect_db()
    cursor = conn.cursor()
    query = "DELETE FROM stores WHERE id = %s"
    cursor.execute(query, (store_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Sucursal eliminada exitosamente")


def user_console_interface():
    print("\n1. Crear Usuario")
    print("2. Leer Usuarios")
    print("3. Actualizar Usuario")
    print("4. Borrar Usuario")
    print("5. Crear Sucursal")
    print("6. Leer Sucursales")
    print("7. Actualizar Sucursal")
    print("8. Borrar Sucursal")
    print("9. Salir")

    choice = input("\nSeleccione una opcion (1-9): ")

    while choice != 9:
        if choice == '1':
            name = input("Ingrese nombre: ")
            email = input("Ingrese email: ")
            password = input("Ingrese password: ")
            telephone = input("Ingrese telefono: ")
            address = input("Ingrese direccion: ")
            status = input("Ingrese estado: ")

            create_user(name, email, password, telephone, address, status)

            print("\n1. Crear Usuario")
            print("2. Leer Usuarios")
            print("3. Actualizar Usuario")
            print("4. Borrar Usuario")
            print("5. Crear Sucursal")
            print("6. Leer Sucursales")
            print("7. Actualizar Sucursal")
            print("8. Borrar Sucursal")
            print("9. Salir")

            choice = input("\nSeleccione una opcion (1-9): ")

        elif choice == '2':
            users = read_users()
            for user in users:
                print(user)

            print("\n1. Crear Usuario")
            print("2. Leer Usuarios")
            print("3. Actualizar Usuario")
            print("4. Borrar Usuario")
            print("5. Crear Sucursal")
            print("6. Leer Sucursales")
            print("7. Actualizar Sucursal")
            print("8. Borrar Sucursal")
            print("9. Salir")

            choice = input("\nSeleccione una opcion (1-9): ")

        elif choice == '3':
            user_id = input("Ingrese ID del usuario a actualizar: ")
            user = read_user(user_id)
            if user:
                print(f"Nombre actual: {user[1]}")
                name = input("Ingrese nombre nuevo (dejar en blanco para conservar el actual): ")
                if name == "":
                    name = user[1]

                print(f"Email actual: {user[2]}")
                email = input("Ingrese email nuevo (dejar en blanco para conservar el actual): ")
                if email == "":
                    email = user[2]

                print(f"Password actual: {user[3]}")
                password = input("Ingrese password nuevo (dejar en blanco para conservar el actual): ")
                if password == "":
                    password = user[3]

                print(f"Telefono actual: {user[4]}")
                telephone = input("Ingrese telefono nuevo (dejar en blanco para conservar el actual): ")
                if telephone == "":
                    telephone = user[4]

                print(f"Direccion actual: {user[5]}")
                address = input("Ingrese direccion nueva (dejar en blanco para conservar el actual): ")
                if address == "":
                    address = user[5]

                print(f"Estado actual: {user[6]}")
                status = input("Ingrese estado nuevo (dejar en blanco para conservar el actual): ")
                if status == "":
                    status = user[6]

                print(f"Sucursal actual: {user[7]}")
                store_id = input("Ingrese sucursal nueva (dejar en blanco para conservar el actual): ")
                if store_id == "":
                    store_id = user[6]

                update_user(user_id, name, email, password, telephone, address, status, store_id)
            else:
                print(f"Usuario con ID {user_id} no encontrado.")

            print("\n1. Crear Usuario")
            print("2. Leer Usuarios")
            print("3. Actualizar Usuario")
            print("4. Borrar Usuario")
            print("5. Crear Sucursal")
            print("6. Leer Sucursales")
            print("7. Actualizar Sucursal")
            print("8. Borrar Sucursal")
            print("9. Salir")

            choice = input("\nSeleccione una opcion (1-9): ")

        elif choice == '4':
            user_id = input("Ingrese el ID del usuario a borrar: ")
            delete_user(user_id)

            print("\n1. Crear Usuario")
            print("2. Leer Usuarios")
            print("3. Actualizar Usuario")
            print("4. Borrar Usuario")
            print("5. Crear Sucursal")
            print("6. Leer Sucursales")
            print("7. Actualizar Sucursal")
            print("8. Borrar Sucursal")
            print("9. Salir")

            choice = input("\nSeleccione una opcion (1-9): ")

        if choice == '5':
            name = input("Ingrese nombre: ")
            address = input("Ingrese direccion: ")

            create_store(name, address)

            print("\n1. Crear Usuario")
            print("2. Leer Usuarios")
            print("3. Actualizar Usuario")
            print("4. Borrar Usuario")
            print("5. Crear Sucursal")
            print("6. Leer Sucursales")
            print("7. Actualizar Sucursal")
            print("8. Borrar Sucursal")
            print("9. Salir")

            choice = input("\nSeleccione una opcion (1-9): ")

        elif choice == '6':
            stores = read_stores()
            for store in stores:
                print(store)

            print("\n1. Crear Usuario")
            print("2. Leer Usuarios")
            print("3. Actualizar Usuario")
            print("4. Borrar Usuario")
            print("5. Crear Sucursal")
            print("6. Leer Sucursales")
            print("7. Actualizar Sucursal")
            print("8. Borrar Sucursal")
            print("9. Salir")

            choice = input("\nSeleccione una opcion (1-9): ")

        elif choice == '7':
            store_id = input("Ingrese ID de la sucursal a actualizar: ")
            store = read_store(store_id)
            if store:
                print(f"Nombre actual: {store[1]}")
                name = input("Ingrese nombre nuevo (dejar en blanco para conservar el actual): ")
                if name == "":
                    name = store[1]

                print(f"Direccion actual: {store[2]}")
                address = input("Ingrese direccion nueva (dejar en blanco para conservar el actual): ")
                if address == "":
                    address = store[2]

                update_store(store_id, name, address)
            else:
                print(f"Sucursal con ID {store_id} no encontrada.")

            print("\n1. Crear Usuario")
            print("2. Leer Usuarios")
            print("3. Actualizar Usuario")
            print("4. Borrar Usuario")
            print("5. Crear Sucursal")
            print("6. Leer Sucursales")
            print("7. Actualizar Sucursal")
            print("8. Borrar Sucursal")
            print("9. Salir")

            choice = input("\nSeleccione una opcion (1-9): ")

        elif choice == '8':
            store_id = input("Ingrese el ID de la sucursal a borrar: ")
            delete_store(store_id)

            print("\n1. Crear Usuario")
            print("2. Leer Usuarios")
            print("3. Actualizar Usuario")
            print("4. Borrar Usuario")
            print("5. Crear Sucursal")
            print("6. Leer Sucursales")
            print("7. Actualizar Sucursal")
            print("8. Borrar Sucursal")
            print("9. Salir")

            choice = input("\nSeleccione una opcion (1-9): ")

        elif choice == '9':
            print("\nSaliendo del programa...")

            return

        else:
            print("\nSeleccione una opcion valida.")

            print("\n1. Crear Usuario")
            print("2. Leer Usuarios")
            print("3. Actualizar Usuario")
            print("4. Borrar Usuario")
            print("5. Crear Sucursal")
            print("6. Leer Sucursales")
            print("7. Actualizar Sucursal")
            print("8. Borrar Sucursal")
            print("9. Salir")

            choice = input("\nSeleccione una opcion (1-9): ")


def login_user():
    username = input("Ingrese nombre: ")

    user = read_user_by_username(username)
    if user is None:
        print("Nombre no encontrado.")
        return

    password = input("Ingrese password: ")

    if user[3] == password:
        print("Login exitoso.")
    else:
        print("Password invalido.")


user_console_interface()

# login_user()
