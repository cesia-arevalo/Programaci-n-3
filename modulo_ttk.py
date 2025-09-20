import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.valor = 1
        self.ventana1 = tk.Tk()
        self.ventana1.title('Controles con ttk')

        self.label1 = ttk.Label(self.ventana1, text=self.valor)
        self.label1.grid(column=0, row=0)
        self.label1.configure(foreground="red")

        self.boton1 = ttk.Button(self.ventana1, text="Aumentar", command=self.aumenta)
        self.boton1.grid(column=0, row=1)

        self.boton2 = ttk.Button(self.ventana1, text="Disminuir", command=self.disminuir)
        self.boton2.grid(column=0, row=2)

        self.ventana1.mainloop()

    def aumenta(self):
        self.valor += 1
        self.label1.config(text=self.valor)

    def disminuir(self):
        self.valor -= 1
        self.label1.config(text=self.valor)

Ejecutar = Aplicacion()
