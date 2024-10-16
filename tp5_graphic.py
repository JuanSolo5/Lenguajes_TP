import tkinter

window = tkinter.Tk()
window.geometry("500x500")

etiqueta1 = tkinter.Label(window, text= "Hola Mundo")
etiqueta1.pack(side= tkinter.BOTTOM)

def saludo():
    print("hola mundo")

def siuu():
    print("siuuuuuuu")

def holanombre(nombre):
    print("tu nombre es "+ nombre)

boton1 = tkinter.Button(window, text = "apretame", command= lambda: holanombre("juan"))
boton1.pack()
boton2 = tkinter.Button(window, text = "chinchulin", command = siuu)
boton2.pack()
window.mainloop()