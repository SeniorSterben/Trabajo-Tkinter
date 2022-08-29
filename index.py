from tkinter import ttk
from tkinter import *

import sqlite3 #Llamar libreria SQL

class Product:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Mi primer Aplicación')
        
  # Creando un contenedor o frame 
        frame = LabelFrame(self.wind, text = 'Registrar un nuevo producto')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)


        # Nombre Input
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        # Precio Input
        Label(frame, text = 'Precio: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

if __name__=='__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()    