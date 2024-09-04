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

#menuUsuarios(listaUsuarios)

# login de usuarios
def loginUsuario(listaUser):
    nombreE = input("Ingrese el nombre ")
    contrE = input("ingrese la contraseña ")
    usuario_encontrado = False
    for i in range(len(listaUser)):
        if listaUser[i].nombre == nombreE and listaUser[i].contr == contrE:
            usuario_encontrado = True
            usuarioLogueado = listaUser[i]

    if usuario_encontrado == False:
        print("Datos incorrectos o inexistentes")
    else:
        print("Acceso concedido")

    return usuario_encontrado

# clase de sucursales
class Sucursal:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    def __str__(self):
        return f"Nombre del comercio: {self.nombre}, Dirección: {self.direccion}"
    

# Lista para almacenar las sucursales
listaSucursales = []

# Consulta la lista de todas las sucursales
def consultarSucursal(listaSucursales):
    for i in listaSucursales:
        print(i)

# Agrega una nueva sucursal a la lista
def agregarSucursal(listaSucursales):
    nombre = input("Ingrese el nombre del comercio: ")
    direccion = input("Ingrese la dirección: ")
    nuevaSucursal = Sucursal(nombre, direccion)
    listaSucursales.append(nuevaSucursal)
    print(f"Sucursal {nuevaSucursal} agregada a la lista.")

# Modifica una sucursal existente
def modificarSucursal(listaSucursales):
    i = int(input("Ingrese el número de la sucursal a modificar: "))
    if i < 0 or i >= len(listaSucursales):
        print("Índice fuera de rango.")
    else:
        sucursal_selec = listaSucursales[i]
           
        print("Deje el campo vacío si no desea modificar ese atributo.")
        nombre = input(f"Ingrese nuevo nombre del comercio ({sucursal_selec.nombre}): ") or sucursal_selec.nombre
        direccion = input(f"Ingrese nueva dirección ({sucursal_selec.direccion}): ") or sucursal_selec.direccion

        sucursal_selec.nombre = nombre
        sucursal_selec.direccion = direccion

        print(f"Sucursal {sucursal_selec} modificada")

# elimina una sucursal
def eliminarSucursal(listaSucursales):
    nombreS = input("Ingrese el nombre del comercio: ")
    direccionS = input("Ingrese la dirección: ")
    sucursal_encontrada = False

    for i in range(len(listaSucursales)):
        if listaSucursales[i].nombre == nombreS and listaSucursales[i].direccion == direccionS:
            sucursal_encontrada = True
            sucursal_eliminada = listaSucursales.pop(i)
            print(f"La sucursal {sucursal_eliminada} fue eliminada")

    if not sucursal_encontrada:
        print("La sucursal no fue encontrada")

# Ejecuta las funciones en un menú para las sucursales
def menuSucursales(listaSucursales):
    menuActivo = True
    while menuActivo:
        print("MENU:")
        print("1) Consultar sucursales")
        print("2) Agregar sucursal")
        print("3) Modificar sucursal")
        print("4) Eliminar sucursal")
        print("5) Terminar programa")

        opcion = input("Ingrese una opción: ")

        match opcion:
            case "1":
                consultarSucursal(listaSucursales)
            case "2":
                agregarSucursal(listaSucursales)
            case "3":
                modificarSucursal(listaSucursales)
            case "4":
                eliminarSucursal(listaSucursales)
            case "5":
                menuActivo = False

