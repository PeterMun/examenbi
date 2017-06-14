from tkinter import *
import turtle
import math

def ventana2():
    perimetro = ""
    area = ""
    
    

    ventana2 = Tk()
    ventana2.geometry("640x480")
    ventana2.title("AREAS Y PERIMETROS")
    in1 = StringVar()
    in2 = StringVar()
    in3 = StringVar()
    in4 = StringVar()

    txtn = Entry(ventana2, textvariable = in1).grid(row = 1, column = 3)
    lbln = Label(ventana2, text = "PONGA EL NUMERO DE LADOS DE LA FIGURA: ").grid(row = 1, column = 0)
    ##lblc = Label(ventana2, text = "CUADRADO ").grid(row = 1, column = 0)
    #lblt = Label(ventana2, text = "TRIANGULO: ").grid(row = 1, column = 0)
    #lblrec = Label(ventana2, text = "RECTANGULO ").grid(row = 1, column = 0)
    txtb = Entry(ventana2, textvariable = in2).grid(row = 2, column = 3)
    lblb = Label(ventana2, text = "BASE: ").grid(row = 2, column = 0)
    txtb = Entry(ventana2, textvariable = in3).grid(row = 3, column = 3)
    lblb = Label(ventana2, text = "ALTURA: ").grid(row = 3, column = 0)

    btn1 = Button(ventana2, padx = 15, bd = 5, text = "calcular",
              fg = "black", command = calcular).place(x = 200, y = 100)


                                                      
    ventana2.mainloop()   

 


def ventana3():
    ventana3 = Tk()
    ventana3.geometry("640x480")
    ventana3.title("ANIMACION")

    



    



    
##CREANDO LA VENTANA
ventana = Tk()
ventana.geometry("640x480")
ventana.title("MENU")

##CREANDO LOS BOTONES
labelmenu = Label(ventana, text = "ELIJA CUALQUIER OPCION").grid(row = 1, column = 2)
btn1 = Button(ventana, padx = 20, bd = 5, text = "1",
              fg = "black", command = ventana2).grid(row = 2, column = 0)
btn2 = Button(ventana, padx = 20, bd = 5, text = "2",
              fg = "black", command = ventana3).grid(row = 2, column = 1)








ventana.mainloop()
