import mysql.connector

config = {
    "user": "root",
    "password": "",
    "host": "localhost",
    "database": "tp5_bd",
}


class Database:
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
    def update(table, any_id, **kwargs):
        conn = Database.connect()
        cursor = conn.cursor()
        columns = " = %s, ".join(kwargs.keys()) + " = %s"
        values = tuple(kwargs.values())
        query = f"UPDATE {table} SET {columns} WHERE id = %s"
        cursor.execute(query, values + (any_id,))
        conn.commit()
        result = cursor.rowcount > 0
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def delete(table, any_id):
        conn = Database.connect()
        cursor = conn.cursor()
        query = f"DELETE FROM {table} WHERE id = %s"
        cursor.execute(query, (any_id,))
        conn.commit()
        result = cursor.rowcount > 0
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_by_email(email):
        conn = Database.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_store_ids():
        conn = Database.connect()
        cursor = conn.cursor()
        query = "SELECT id FROM stores"
        cursor.execute(query)
        result = [store[0] for store in cursor.fetchall()]
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_stores_id_name():
        conn = Database.connect()
        cursor = conn.cursor()
        query = "SELECT id, name FROM stores"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
