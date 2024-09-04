class usuario:
    def __init__(self, nombre, contr, email, direc, tel, estado):
        self.nombre = nombre
        self.contr = contr
        self.email = email
        self.direc = direc
        self.tel = tel
        self.estado = estado

    def __str__(self):
        return f"{self.nombre}, {self.contr}, {self.email}, {self.direc}, {self.tel}, {self.estado}"

## Hola Juancito

listaUsuarios=[]

# consulta la lista de todos los usuarios
def consultarUsuario(listaUser):
    for i in listaUser:
        print(i)

# agrega un usuario a la lista
def agregarUsuario(listaUser):
    nombre = input("Ingrese nombre: ")
    contr = input("Ingrese contraseña: ")
    email = input("Ingrese email: ")
    direc = input("Ingrese dirección: ")
    tel = input("Ingrese teléfono: ")
    estado = input("Ingrese estado: ")
    nuevoUsuario = usuario(nombre, contr, email, direc, tel, estado)
    listaUser.append(nuevoUsuario)
    print(f"Usuario {nuevoUsuario} agregado a la lista.")

# modifica un usuario seleccionado
def modificarUsuario(listaUser):
    i = int(input("Ingrese el número del usuario a modificar: "))
    if i < 0 or i >= len(listaUser):
        print("Índice fuera de rango.")
    else:
        usuario_selec = listaUser[i]
           
        print("Deje el campo vacío si no desea modificar ese atributo.")
        nombre = input(f"Ingrese nuevo nombre ({usuario_selec.nombre}): ") or usuario_selec.nombre
        contr = input(f"Ingrese nueva contraseña ({usuario_selec.contr}): ") or usuario_selec.contr
        email = input(f"Ingrese nuevo email ({usuario_selec.email}): ") or usuario_selec.email
        direc = input(f"Ingrese nueva dirección ({usuario_selec.direc}): ") or usuario_selec.direc
        tel = input(f"Ingrese nuevo teléfono ({usuario_selec.tel}): ") or usuario_selec.tel
        estado = input(f"Ingrese nuevo estado ({usuario_selec.estado}): ") or usuario_selec.estado

        usuario_selec.nombre = nombre
        usuario_selec.contr = contr
        usuario_selec.email = email
        usuario_selec.direc = direc
        usuario_selec.tel = tel
        usuario_selec.estado = estado

        print(f"Usuario {usuario_selec} modificado")

# elimina un usuario 
def eliminarUsuario(listaUser):
    nombreE = input("Ingrese el nombre ")
    contrE = input("ingrese la contraseña ")
    usuario_encontrado = False

    for i in range(len(listaUser)):
        if listaUser[i].nombre == nombreE and listaUser[i].contr == contrE:
            usuario_encontrado = True
            usuario_eliminado = listaUser.pop(i)
            print(f"El usuario {usuario_eliminado} fue eliminado")
    if usuario_encontrado == False:
        print("El usuario no fue encontrado")

# ejecuta las funciones en un menu
def menuUsuarios(listaUser):
    menuActivo = True
    while menuActivo:
        print("MENU:")
        print("1) consultar usuarios")
        print("2) agregar usuario")
        print("3) modificar usuario")
        print("4) eliminar usuario")
        print("5) terminar programa")

        opcion = input("Ingrese una opcion: ")

        match opcion:
            case "1":
                consultarUsuario(listaUser)
            case "2":
                agregarUsuario(listaUser)
            case "3":
                modificarUsuario(listaUser)
            case "4":
                eliminarUsuario(listaUser)
            case "5":
                menuActivo = False

menuUsuarios(listaUsuarios)