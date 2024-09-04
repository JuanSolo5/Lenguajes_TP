class usuario:
    def __init__(self, nombre, contr, email, dir, tel, estado):
        self.nombre = nombre
        self.contr = contr
        self.email = email
        self.dir = dir
        self.tel = tel
        self.estado = estado

## Hola Juancito

listaUser=[]



def menuUsuarios(listaUser):
    menuActivo = True
    while menuActivo:
        print("MENU:")
        print("1) consultar usuarios")
        print("2) agregar usuario")
        print("3) modificar usuario")
        print("4) eliminar usuario")

        opcion = input("Ingrese una opcion: ")

        match opcion:
            case "1":
                consultarUsuarios(listaUser)
            case "2":
                agregarUsuario(listaUser)
            case "3":
                modificarUsuario(listaUser)
            case "4":
                eliminarUsuario(listaUser)
