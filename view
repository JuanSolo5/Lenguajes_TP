from model2 import Database
from controller2 import Login, UserCrud, StoreCrud
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class LoginUI:
    @staticmethod
    def login_user_ui():
        window = tk.Tk()
        window.title("Login")
        height = 200
        width = 290
        x = (window.winfo_screenwidth()//2) - (width//2)
        y = (window.winfo_screenheight()//2) - (height//2)
        window.geometry('{}x{}+{}+{}'. format(width, height, x, y))
        window.resizable(width=False, height=False)

        email_label = tk.Label(window, text="Email")
        email_label.grid(row=0, column=0, padx=10, pady=10)
        email_entry = tk.Entry(window, width=30)
        email_entry.grid(row=0, column=1, padx=10, pady=10)

        password_label = tk.Label(window, text="Password")
        password_label.grid(row=1, column=0, padx=10, pady=10)
        password_entry = tk.Entry(window, show="*", width=30)
        password_entry.grid(row=1, column=1, padx=10, pady=10)

        def attempt_login():
            email = email_entry.get()
            password = password_entry.get()

            result = Login.login_user(email, password)

            if not result["success"]:
                messagebox.showerror("Error", result["error"])
            else:
                messagebox.showinfo("Success", "Login successful")
                window.destroy()

                if result["role"] == "Administrador":
                    MenuUI.main_menu_ui()
                elif result["role"] == "Empleado":
                    MenuUI.employee_management_ui(result["user_data"])

        login_button = tk.Button(window, text="Login", width=16, command=attempt_login)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

        exit_button = tk.Button(window, text="Exit", width=16, command=window.destroy)
        exit_button.grid(row=3, column=0, columnspan=2, pady=10)

        window.mainloop()


class MenuUI:
    @staticmethod
    def main_menu_ui():
        window = tk.Tk()
        window.title("Administrator Main Menu")
        height = 300
        width = 300
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        window.resizable(width=False, height=False)

        def to_user_management():
            window.destroy()
            MenuUI.user_management_ui()

        def to_store_management():
            window.destroy()
            MenuUI.store_management_ui()

        user_button = tk.Button(window, text="User Management", width=16, command=to_user_management)
        user_button.pack(pady=10)

        store_button = tk.Button(window, text="Store Management", width=16, command=to_store_management)
        store_button.pack(pady=10)

        exit_button = tk.Button(window, text="Exit", width=16, command=window.destroy)
        exit_button.pack(pady=10)

        window.mainloop()

    @staticmethod
    def user_management_ui():
        window = tk.Tk()
        window.title("User Management")
        height = 300
        width = 300
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        window.resizable(width=False, height=False)

        def to_create_user():
            window.destroy()
            UserCrudUI.create_user_ui()

        def to_read_users():
            window.destroy()
            UserCrudUI.show_users()

        def to_update_user():
            window.destroy()
            UserCrudUI.user_selection_ui()

        def to_delete_user():
            window.destroy()
            UserCrudUI.delete_user_ui()

        def back_to_main():
            window.destroy()
            MenuUI.main_menu_ui()

        create_user_button = tk.Button(window, text="Create User", width=16, command=to_create_user)
        create_user_button.pack(pady=10)

        read_users_button = tk.Button(window, text="Read Users", width=16, command=to_read_users)
        read_users_button.pack(pady=10)

        update_user_button = tk.Button(window, text="Update User", width=16, command=to_update_user)
        update_user_button.pack(pady=10)

        delete_user_button = tk.Button(window, text="Delete User", width=16, command=to_delete_user)
        delete_user_button.pack(pady=10)

        back_button = tk.Button(window, text="Main Menu", width=16, command=back_to_main)
        back_button.pack(pady=10)

        window.mainloop()

    @staticmethod
    def employee_management_ui(user):
        window = tk.Tk()
        window.title("User Management")
        height = 150
        width = 300
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        window.resizable(width=False, height=False)

        def to_read_user():
            window.destroy()
            UserCrudUI.read_single_user_ui(user)

        def to_update_password():
            window.destroy()
            UserCrudUI.update_password_ui(user[0])

        read_user_button = tk.Button(window, text="My Info", width=16, command=to_read_user)
        read_user_button.pack(pady=10)

        update_password_button = tk.Button(window, text="Change Password", width=16, command=to_update_password)
        update_password_button.pack(pady=10)

        exit_button = tk.Button(window, text="Exit", width=16, command=window.destroy)
        exit_button.pack(pady=10)

    @staticmethod
    def store_management_ui():
        window = tk.Tk()
        window.title("Store Management")
        height = 300
        width = 300
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        window.resizable(width=False, height=False)

        def to_create_store():
            window.destroy()
            StoreCrudUI.create_store_ui()

        def to_read_stores():
            window.destroy()
            StoreCrudUI.show_stores()

        def to_update_store():
            window.destroy()
            StoreCrudUI.store_selection_ui()

        def to_delete_store():
            window.destroy()
            StoreCrudUI.delete_store_ui()

        def back_to_main():
            window.destroy()
            MenuUI.main_menu_ui()

        create_store_button = tk.Button(window, text="Create Store", width=16, command=to_create_store)
        create_store_button.pack(pady=10)

        read_stores_button = tk.Button(window, text="Read Stores", width=16, command=to_read_stores)
        read_stores_button.pack(pady=10)

        update_store_button = tk.Button(window, text="Update Store", width=16, command=to_update_store)
        update_store_button.pack(pady=10)

        delete_store_button = tk.Button(window, text="Delete Store", width=16, command=to_delete_store)
        delete_store_button.pack(pady=10)

        back_button = tk.Button(window, text="Main Menu", width=16, command=back_to_main)
        back_button.pack(pady=10)

        window.mainloop()


class UserCrudUI:
    @staticmethod
    def create_user_ui():
        window = tk.Tk()
        window.title("Create User")
        height = 400
        width = 300
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        window.resizable(width=False, height=False)

        name_label = tk.Label(window, text="Name")
        name_label.grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(window, width=30)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        email_label = tk.Label(window, text="Email")
        email_label.grid(row=1, column=0, padx=10, pady=10)
        email_entry = tk.Entry(window, width=30)
        email_entry.grid(row=1, column=1, padx=10, pady=10)

        role_label = tk.Label(window, text="Role")
        role_label.grid(row=2, column=0, padx=10, pady=10)

        role_options = ["Administrador", "Empleado"]
        role_var = tk.StringVar(window)
        role_var.set(role_options[0])

        role_combobox = ttk.Combobox(window, values=role_options, width=27)
        role_combobox.set(role_options[0])
        role_combobox.grid(row=2, column=1, padx=10, pady=10)

        telephone_label = tk.Label(window, text="Telephone")
        telephone_label.grid(row=3, column=0, padx=10, pady=10)
        telephone_entry = tk.Entry(window, width=30)
        telephone_entry.grid(row=3, column=1, padx=10, pady=10)

        address_label = tk.Label(window, text="Address")
        address_label.grid(row=4, column=0, padx=10, pady=10)
        address_entry = tk.Entry(window, width=30)
        address_entry.grid(row=4, column=1, padx=10, pady=10)

        stores = Database.get_stores_id_name()
        store_options = [f"[{id}] {name}" for id, name in stores]

        store_label = tk.Label(window, text="Store")
        store_label.grid(row=5, column=0, padx=10, pady=10)

        store_var = tk.StringVar(window)
        store_var.set(store_options[0])

        store_combobox = ttk.Combobox(window, values=store_options, textvariable=store_var, width=27)
        store_combobox.grid(row=5, column=1, padx=10, pady=10)

        def get_selected_store_id():
            selected_store = store_var.get()
            selected_store_id = selected_store.split('[')[-1].strip(']')[0]
            return selected_store_id

        # store_label = tk.Label(window, text="Store ID")
        # store_label.grid(row=5, column=0, padx=10, pady=10)

        # store_ids = Database.get_all_store_ids()
        # store_var = tk.StringVar(window)
        # store_var.set(store_ids[0])

        # store_combobox = ttk.Combobox(window, values=store_ids, width=27)
        # store_combobox.set(store_ids[0])
        # store_combobox.grid(row=5, column=1, padx=10, pady=10)

        def try_user_creation():
            try:
                name = name_entry.get()
                email = email_entry.get()
                role = role_combobox.get()
                telephone = telephone_entry.get()
                address = address_entry.get()
                # store_id = store_combobox.get()
                store_id = get_selected_store_id()

                UserCrud.create_user(name, email, role, telephone, address, store_id)

                messagebox.showinfo("Success", "User created successfully")
                window.destroy()
                MenuUI.user_management_ui()
            except ValueError as ve:
                messagebox.showerror("Error", str(ve))

        create_button = tk.Button(window, text="Create", width=16, command=try_user_creation)
        create_button.place(relx=0.5, rely=0.80, anchor="center")

        def back_to_users():
            window.destroy()
            MenuUI.user_management_ui()

        back_button = tk.Button(window, text="Back", width=16, command=back_to_users)
        back_button.place(relx=0.5, rely=0.90, anchor="center")

        window.mainloop()

    @staticmethod
    def show_users():
        users = UserCrud.read_users()
        UserCrudUI.read_users_ui(users)

    @staticmethod
    def read_users_ui(users):
        window = tk.Tk()
        window.title("User Data")
        height = 500
        width = 1200
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        user_frame = tk.Frame(window)
        user_frame.pack(padx=10, pady=10, fill="both", expand=True)

        columns = ("ID", "Name", "Email", "Password", "Role", "Telephone", "Address", "Status", "Store ID")
        tree = ttk.Treeview(user_frame, columns=columns, show="headings", height=15)

        tree.heading("ID", text="ID")
        tree.column("ID", width=50, anchor="center")

        tree.heading("Name", text="Name")
        tree.column("Name", width=100, anchor="center")

        tree.heading("Email", text="Email")
        tree.column("Email", width=150, anchor="center")

        tree.heading("Password", text="Password")
        tree.column("Password", width=120, anchor="center")

        tree.heading("Role", text="Role")
        tree.column("Role", width=100, anchor="center")

        tree.heading("Telephone", text="Telephone")
        tree.column("Telephone", width=100, anchor="center")

        tree.heading("Address", text="Address")
        tree.column("Address", width=120, anchor="center")

        tree.heading("Status", text="Status")
        tree.column("Status", width=100, anchor="center")

        tree.heading("Store ID", text="Store ID")
        tree.column("Store ID", width=50, anchor="center")

        for user in users:
            tree.insert("", "end", values=user)

        scrollbar = ttk.Scrollbar(user_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def back_to_users():
            window.destroy()
            MenuUI.user_management_ui()

        back_button = tk.Button(window, text="Back", width=16, command=back_to_users)
        back_button.pack(pady=20)

        window.mainloop()

    @staticmethod
    def read_single_user_ui(user):
        id, name, email, password, role, telephone, address, status, store_id = user

        store = Database.read_by_id("stores", store_id)
        store_name = store[1]

        window = tk.Tk()
        window.title("User Details")
        height = 300
        width = 700
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        user_frame = tk.Frame(window, width=600)
        user_frame.pack(padx=10, pady=10, fill="both", expand=True)

        columns = ("Name", "Email", "Telephone", "Address", "Store Name")
        tree = ttk.Treeview(user_frame, columns=columns, show="headings", height=1)

        tree.heading("Name", text="Name")
        tree.column("Name", width=100, anchor="center")

        tree.heading("Email", text="Email")
        tree.column("Email", width=150, anchor="center")

        tree.heading("Telephone", text="Telephone")
        tree.column("Telephone", width=100, anchor="center")

        tree.heading("Address", text="Address")
        tree.column("Address", width=120, anchor="center")

        tree.heading("Store Name", text="Store Name")
        tree.column("Store Name", width=100, anchor="center")

        tree.insert("", "end", values=(name, email, telephone, address, store_name))

        tree.pack(fill="both", expand=True)

        def back_to_users():
            window.destroy()
            MenuUI.employee_management_ui(user)

        back_button = tk.Button(window, text="Back", width=16, command=back_to_users)
        back_button.pack(pady=20)

        window.mainloop()

    @staticmethod
    def update_password_ui(user_id):
        window = tk.Tk()
        window.title("User Data")
        height = 280
        width = 300
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        window.resizable(width=False, height=False)

        user = Database.read_by_id("users", user_id)
        current_password = user[3]

        current_password_label = tk.Label(window, text="Current Password:")
        current_password_label.pack(pady=5)

        current_password_entry = tk.Entry(window)
        current_password_entry.insert(0, current_password)
        current_password_entry.pack(pady=5)

        new_password_label = tk.Label(window, text="New Password:")
        new_password_label.pack(pady=5)

        new_password_entry = tk.Entry(window, show='*')
        new_password_entry.pack(pady=5)

        def try_update_password():
            new_password = new_password_entry.get()
            if not new_password:
                messagebox.showerror("Error", "New password cannot be empty.")
                return

            result = Database.update("users", user_id, password=new_password)
            if result:
                messagebox.showinfo("Success", "Password updated successfully.")
                window.destroy()
                MenuUI.employee_management_ui(user)
            else:
                messagebox.showerror("Error", "Failed to update password.")

        update_button = tk.Button(window, text="Update", width=16, command=try_update_password)
        update_button.place(relx=0.5, rely=0.72, anchor="center")

        def back_to_employee():
            window.destroy()
            MenuUI.employee_management_ui(user)

        back_button = tk.Button(window, text="Back", width=16, command=back_to_employee)
        back_button.place(relx=0.5, rely=0.88, anchor="center")

        window.mainloop()

    @staticmethod
    def user_selection_ui():
        window = tk.Tk()
        window.title("Select User to Update")
        height = 500
        width = 1200
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        user_frame = tk.Frame(window)
        user_frame.pack(padx=10, pady=10, fill="both", expand=True)

        columns = ("ID", "Name", "Email", "Password", "Role", "Telephone", "Address", "Status", "Store ID")
        tree = ttk.Treeview(user_frame, columns=columns, show="headings", height=15)

        tree.heading("ID", text="ID")
        tree.column("ID", width=50, anchor="center")

        tree.heading("Name", text="Name")
        tree.column("Name", width=100, anchor="center")

        tree.heading("Email", text="Email")
        tree.column("Email", width=150, anchor="center")

        tree.heading("Password", text="Password")
        tree.column("Password", width=120, anchor="center")

        tree.heading("Role", text="Role")
        tree.column("Role", width=100, anchor="center")

        tree.heading("Telephone", text="Telephone")
        tree.column("Telephone", width=100, anchor="center")

        tree.heading("Address", text="Address")
        tree.column("Address", width=120, anchor="center")

        tree.heading("Status", text="Status")
        tree.column("Status", width=100, anchor="center")

        tree.heading("Store ID", text="Store ID")
        tree.column("Store ID", width=50, anchor="center")

        users = Database.read("users")
        for user in users:
            tree.insert("", "end", values=user)

        tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(user_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        def select_user():
            selected_item = tree.selection()
            if selected_item:
                user_data = tree.item(selected_item[0])['values']
                if user_data:
                    window.destroy()
                    UserCrudUI.update_user_ui(user_data)

        select_button = tk.Button(window, text="Select", width=16, command=select_user)
        select_button.pack(pady=20)

        def back_to_users():
            window.destroy()
            MenuUI.user_management_ui()

        back_button = tk.Button(window, text="Back", width=16, command=back_to_users)
        back_button.pack(pady=10)

        window.mainloop()

    @staticmethod
    def update_user_ui(user):
        window = tk.Tk()
        window.title("Update User")
        height = 500
        width = 300
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        window.resizable(width=False, height=False)

        id, name, email, password, role, telephone, address, status, store_id = user

        name_label = tk.Label(window, text="Name")
        name_label.grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(window, width=30)
        name_entry.insert(0, name)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        email_label = tk.Label(window, text="Email")
        email_label.grid(row=1, column=0, padx=10, pady=10)
        email_entry = tk.Entry(window, width=30)
        email_entry.insert(0, email)
        email_entry.grid(row=1, column=1, padx=10, pady=10)

        password_label = tk.Label(window, text="Password")
        password_label.grid(row=2, column=0, padx=10, pady=10)
        password_entry = tk.Entry(window, width=30)
        password_entry.insert(0, password)
        password_entry.grid(row=2, column=1, padx=10, pady=10)

        role_label = tk.Label(window, text="Role")
        role_label.grid(row=3, column=0, padx=10, pady=10)

        role_options = ["Administrador", "Empleado"]
        role_var = tk.StringVar(window)
        role_var.set(role)
        role_combobox = ttk.Combobox(window, values=role_options, width=27)
        role_combobox.set(role)
        role_combobox.grid(row=3, column=1, padx=10, pady=10)

        telephone_label = tk.Label(window, text="Telephone")
        telephone_label.grid(row=4, column=0, padx=10, pady=10)
        telephone_entry = tk.Entry(window, width=30)
        telephone_entry.insert(0, telephone)
        telephone_entry.grid(row=4, column=1, padx=10, pady=10)

        address_label = tk.Label(window, text="Address")
        address_label.grid(row=5, column=0, padx=10, pady=10)
        address_entry = tk.Entry(window, width=30)
        address_entry.insert(0, address)
        address_entry.grid(row=5, column=1, padx=10, pady=10)

        status_label = tk.Label(window, text="Status")
        status_label.grid(row=6, column=0, padx=10, pady=10)

        status_options = ["Activo", "Bloqueado"]
        status_var = tk.StringVar(window)
        status_var.set(status)
        status_combobox = ttk.Combobox(window, values=status_options, width=27)
        status_combobox.set(status)
        status_combobox.grid(row=6, column=1, padx=10, pady=10)

        stores = Database.get_stores_id_name()
        store_options = [f"[{id}] {name}" for id, name in stores]

        store_label = tk.Label(window, text="Store")
        store_label.grid(row=7, column=0, padx=10, pady=10)

        store_var = tk.StringVar(window)
        current_store = ""
        for store in stores:
            if store[0] == store_id:
                current_store = f"[{store[0]}] {store[1]}"
        store_var.set(current_store)

        store_combobox = ttk.Combobox(window, values=store_options, textvariable=store_var, width=27)
        store_combobox.grid(row=7, column=1, padx=10, pady=10)

        def get_selected_store_id():
            selected_store = store_var.get()
            selected_store_id = selected_store.split('[')[-1].strip(']')[0]
            return selected_store_id

        # store_id_label = tk.Label(window, text="Store ID")
        # store_id_label.grid(row=7, column=0, padx=10, pady=10)

        # store_id_options = Database.get_all_store_ids()
        # store_id_var = tk.StringVar(window)
        # store_id_var.set(store_id)
        # store_id_combobox = ttk.Combobox(window, values=store_id_options, width=27)
        # store_id_combobox.set(store_id)
        # store_id_combobox.grid(row=7, column=1, padx=10, pady=10)

        def try_user_update():
            try:
                updated_name = name_entry.get()
                updated_email = email_entry.get()
                updated_password = password_entry.get()
                updated_role = role_combobox.get()
                updated_telephone = telephone_entry.get()
                updated_address = address_entry.get()
                updated_status = status_combobox.get()
                # updated_store_id = store_id_combobox.get()
                updated_store_id = get_selected_store_id()

                UserCrud.update_user(
                    id,
                    updated_name,
                    updated_email,
                    updated_password,
                    updated_role,
                    updated_telephone,
                    updated_address,
                    updated_status,
                    updated_store_id
                )

                messagebox.showinfo("Success", "User updated successfully")
                window.destroy()
                MenuUI.user_management_ui()

            except ValueError as ve:
                messagebox.showerror("Error", str(ve))
            except Exception as e:
                messagebox.showerror("Error", f"Unexpected error: {e}")

        update_button = tk.Button(window, text="Update", width=16, command=try_user_update)
        update_button.place(relx=0.5, rely=0.84, anchor="center")

        def back_to_users():
            window.destroy()
            MenuUI.user_management_ui()

        back_button = tk.Button(window, text="Back", width=16, command=back_to_users)
        back_button.place(relx=0.5, rely=0.93, anchor="center")

        window.mainloop()

    @staticmethod
    def delete_user_ui():
        window = tk.Tk()
        window.title("Delete User")
        height = 500
        width = 1200
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        user_frame = tk.Frame(window)
        user_frame.pack(padx=10, pady=10, fill="both", expand=True)

        columns = ("ID", "Name", "Email", "Password", "Role", "Telephone", "Address", "Status", "Store ID")
        tree = ttk.Treeview(user_frame, columns=columns, show="headings", height=15)

        tree.heading("ID", text="ID")
        tree.column("ID", width=50, anchor="center")

        tree.heading("Name", text="Name")
        tree.column("Name", width=100, anchor="center")

        tree.heading("Email", text="Email")
        tree.column("Email", width=150, anchor="center")

        tree.heading("Password", text="Password")
        tree.column("Password", width=120, anchor="center")

        tree.heading("Role", text="Role")
        tree.column("Role", width=100, anchor="center")

        tree.heading("Telephone", text="Telephone")
        tree.column("Telephone", width=100, anchor="center")

        tree.heading("Address", text="Address")
        tree.column("Address", width=120, anchor="center")

        tree.heading("Status", text="Status")
        tree.column("Status", width=100, anchor="center")

        tree.heading("Store ID", text="Store ID")
        tree.column("Store ID", width=50, anchor="center")

        users = Database.read("users")
        for user in users:
            tree.insert("", "end", values=user)

        tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(user_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        def try_user_delete():
            selected_item = tree.selection()
            if selected_item:
                user_data = tree.item(selected_item[0])['values']
                user_id = user_data[0]

                confirmation = messagebox.askyesno("Confirm Delete",
                                                   f"Are you sure you want to delete user ID {user_id}?")
                if confirmation:
                    result = Database.delete("users", user_id)
                    if result:
                        messagebox.showinfo("Success", "User deleted successfully.")
                        window.destroy()
                        MenuUI.user_management_ui()
                    else:
                        messagebox.showerror("Error", "User deletion failed.")
            else:
                messagebox.showerror("Error", "No user selected.")

        delete_button = tk.Button(window, text="Delete", width=16, command=try_user_delete)
        delete_button.pack(pady=20)

        def back_to_users():
            window.destroy()
            MenuUI.user_management_ui()

        back_button = tk.Button(window, text="Back", width=16, command=back_to_users)
        back_button.pack(pady=10)

        window.mainloop()


class StoreCrudUI:
    @staticmethod
    def create_store_ui():
        window = tk.Tk()
        window.title("Create Store")
        height = 200
        width = 300
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        window.resizable(width=False, height=False)

        name_label = tk.Label(window, text="Name")
        name_label.grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(window, width=30)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        address_label = tk.Label(window, text="Address")
        address_label.grid(row=4, column=0, padx=10, pady=10)
        address_entry = tk.Entry(window, width=30)
        address_entry.grid(row=4, column=1, padx=10, pady=10)

        def try_store_creation():
            try:
                name = name_entry.get()
                address = address_entry.get()

                StoreCrud.create_store(name, address)

                messagebox.showinfo("Success", "Store created successfully")
                window.destroy()
                MenuUI.store_management_ui()
            except ValueError as ve:
                messagebox.showerror("Error", str(ve))

        create_button = tk.Button(window, text="Create", width=16, command=try_store_creation)
        create_button.place(relx=0.5, rely=0.66, anchor="center")

        def back_to_stores():
            window.destroy()
            MenuUI.store_management_ui()

        back_button = tk.Button(window, text="Back", width=16, command=back_to_stores)
        back_button.place(relx=0.5, rely=0.86, anchor="center")

        window.mainloop()

    @staticmethod
    def show_stores():
        stores = StoreCrud.read_stores()
        StoreCrudUI.read_stores_ui(stores)

    @staticmethod
    def read_stores_ui(stores):
        window = tk.Tk()
        window.title("Store Data")
        height = 500
        width = 1000
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        store_frame = tk.Frame(window)
        store_frame.pack(padx=10, pady=10, fill="both", expand=True)

        columns = ("ID", "Name", "Address")
        tree = ttk.Treeview(store_frame, columns=columns, show="headings", height=15)

        tree.heading("ID", text="ID")
        tree.column("ID", width=50, anchor="center")

        tree.heading("Name", text="Name")
        tree.column("Name", width=100, anchor="center")

        tree.heading("Address", text="Address")
        tree.column("Address", width=120, anchor="center")

        for store in stores:
            id, name, address = store
            tree.insert("", "end", values=(id, name, address))

        tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(store_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        def back_to_stores():
            window.destroy()
            MenuUI.store_management_ui()

        back_button = tk.Button(window, text="Back", width=16, command=back_to_stores)
        back_button.pack(pady=20)

        window.mainloop()

    @staticmethod
    def store_selection_ui():
        window = tk.Tk()
        window.title("Update Store")
        height = 500
        width = 1000
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        store_frame = tk.Frame(window)
        store_frame.pack(padx=10, pady=10, fill="both", expand=True)

        columns = ("ID", "Name", "Address")
        tree = ttk.Treeview(store_frame, columns=columns, show="headings", height=15)

        tree.heading("ID", text="ID")
        tree.column("ID", width=50, anchor="center")

        tree.heading("Name", text="Name")
        tree.column("Name", width=100, anchor="center")

        tree.heading("Address", text="Address")
        tree.column("Address", width=120, anchor="center")

        stores = Database.read("stores")
        for store in stores:
            id, name, address = store
            tree.insert("", "end", values=(id, name, address))

        tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(store_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        def select_store():
            selected_item = tree.selection()
            if selected_item:
                store_data = tree.item(selected_item[0])['values']
                if store_data:
                    window.destroy()
                    StoreCrudUI.update_store_ui(store_data)

        select_button = tk.Button(window, text="Select", width=16, command=select_store)
        select_button.pack(pady=20)

        def back_to_stores():
            window.destroy()
            MenuUI.store_management_ui()

        back_button = tk.Button(window, text="Back", width=16, command=back_to_stores)
        back_button.pack(pady=10)

        window.mainloop()

    @staticmethod
    def update_store_ui(store):
        window = tk.Tk()
        window.title("Update Store")
        height = 200
        width = 300
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        window.resizable(width=False, height=False)

        id, name, address = store

        name_label = tk.Label(window, text="Name")
        name_label.grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(window, width=30)
        name_entry.insert(0, name)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        address_label = tk.Label(window, text="Address")
        address_label.grid(row=5, column=0, padx=10, pady=10)
        address_entry = tk.Entry(window, width=30)
        address_entry.insert(0, address)
        address_entry.grid(row=5, column=1, padx=10, pady=10)

        def try_store_update():
            try:
                updated_name = name_entry.get()
                updated_address = address_entry.get()

                StoreCrud.update_store(id, updated_name, updated_address)

                messagebox.showinfo("Success", "Store updated successfully")
                window.destroy()
                MenuUI.store_management_ui()

            except ValueError as ve:
                messagebox.showerror("Error", str(ve))
            except Exception as e:
                messagebox.showerror("Error", f"Unexpected error: {e}")

        update_button = tk.Button(window, text="Update", width=16, command=try_store_update)
        update_button.place(relx=0.5, rely=0.66, anchor="center")

        def back_to_stores():
            window.destroy()
            MenuUI.store_management_ui()

        back_button = tk.Button(window, text="Back", width=16, command=back_to_stores)
        back_button.place(relx=0.5, rely=0.85, anchor="center")

        window.mainloop()

    @staticmethod
    def delete_store_ui():
        window = tk.Tk()
        window.title("Delete Store")
        height = 500
        width = 1000
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        store_frame = tk.Frame(window)
        store_frame.pack(padx=10, pady=10, fill="both", expand=True)

        columns = ("ID", "Name", "Address")
        tree = ttk.Treeview(store_frame, columns=columns, show="headings", height=15)

        tree.heading("ID", text="ID")
        tree.column("ID", width=50, anchor="center")

        tree.heading("Name", text="Name")
        tree.column("Name", width=100, anchor="center")

        tree.heading("Address", text="Address")
        tree.column("Address", width=120, anchor="center")

        stores = Database.read("stores")
        for store in stores:
            id, name, address = store
            tree.insert("", "end", values=(id, name, address))

        tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(store_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        def try_store_delete():
            selected_item = tree.selection()
            if selected_item:
                store_data = tree.item(selected_item[0])['values']
                store_id = store_data[0]

                confirmation = messagebox.askyesno("Confirm Delete",
                                                   f"Are you sure you want to delete store ID {store_id}?")
                if confirmation:
                    result = Database.delete("stores", store_id)
                    if result:
                        messagebox.showinfo("Success", "Store deleted successfully.")
                        window.destroy()
                        MenuUI.store_management_ui()
                    else:
                        messagebox.showerror("Error", "Store deletion failed.")
            else:
                messagebox.showerror("Error", "No user selected.")

        delete_button = tk.Button(window, text="Delete", width=16, command=try_store_delete)
        delete_button.pack(pady=10)

        def back_to_stores():
            window.destroy()
            MenuUI.store_management_ui()

        back_button = tk.Button(window, text="Back", width=16, command=back_to_stores)
        back_button.pack(pady=10)

        window.mainloop()


LoginUI.login_user_ui()
