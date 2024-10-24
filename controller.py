import random
import string
from model import Database


class Login:
    @staticmethod
    def login_user(email, password):
        user = Database.read_by_email(email)

        if not user:
            return {"success": False, "error": "Invalid email"}

        if user[7] == "Bloqueado":
            return {"success": False, "error": "Blocked Account"}

        if user[3] == password:
            return {"success": True, "role": user[4], "user_data": user}
        else:
            return {"success": False, "error": "Invalid password"}


class UserCrud:
    @staticmethod
    def generate_password():
        password_chars = [  # para que tenga al menos una letra y un digito
            random.choice(string.ascii_letters),
            random.choice(string.digits)
        ]

        characters = string.ascii_letters + string.digits
        password_chars += random.choices(characters, k=6)  # agregamos otros 6 caracteres random
        random.shuffle(password_chars)
        password = ''.join(password_chars)
        return password

    @staticmethod
    def create_user(name, email, role, telephone, address, store_id):
        password = UserCrud.generate_password()
        status = "Activo"

        existing_user = Database.read_by_email(email)
        if existing_user:
            raise ValueError(f"User with email {email} already exists.")

        Database.create(
            "users",
            name=name,
            email=email,
            password=password,
            rol=role,
            telephone=telephone,
            address=address,
            status=status,
            store_id=store_id
        )

    @staticmethod
    def read_users():
        users = Database.read("users")
        return users

    @staticmethod
    def update_user(user_id, name, email, password, role, telephone, address, status, store_id):

        users = Database.read("users")
        for user in users:
            if user[2] == email and user[0] != user_id:
                raise ValueError(f"User with email {email} already exists.")

        Database.update(
            "users",
            user_id,
            name=name,
            email=email,
            password=password,
            rol=role,
            telephone=telephone,
            address=address,
            status=status,
            store_id=store_id
            )


class StoreCrud:
    @staticmethod
    def create_store(name, address):
        Database.create("stores", name=name, address=address)

    @staticmethod
    def read_stores():
        stores = Database.read("stores")
        return stores

    @staticmethod
    def update_store(store_id, name, address):
        Database.update("stores", store_id, name=name, address=address)
