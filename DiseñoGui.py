import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Aplicacion:
    def __init__(self):  # ✅ Constructor corregido
        self.ventana1 = tk.Tk()
        self.ventana1.title("Controles TTK")
        self.ventana1.config(bg="#E4E2E2")
        self.ventana1.geometry("700x400")

        self.valor = 0

        style = ttk.Style(self.ventana1)
        style.theme_use("clam")

        # Label
        style.configure("label1.TLabel", background="#E4E2E2", foreground="#000")
        self.label1 = ttk.Label(master=self.ventana1, text=str(self.valor), style="label1.TLabel")
        self.label1.place(x=308, y=73, width=80, height=40)

        # Botón Aumentar
        style.configure("button1.TButton", background="#E4E2E2", foreground="#000")
        style.map("button1.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])
        self.boton1 = ttk.Button(master=self.ventana1, text="Aumentar",
                                 style="button1.TButton", command=self.incrementar)
        self.boton1.place(x=312, y=152, width=80, height=40)

        # Botón Disminuir
        style.configure("button2.TButton", background="#E4E2E2", foreground="#000")
        style.map("button2.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])
        self.boton2 = ttk.Button(master=self.ventana1, text="Disminuir",
                                 style="button2.TButton", command=self.decrementar)
        self.boton2.place(x=311, y=235, width=80, height=40)

        # Botón Salir
        style.configure("button3.TButton", background="#E4E2E2", foreground="#000")
        style.map("button3.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])
        self.boton3 = ttk.Button(master=self.ventana1, text="Salir",
                                 style="button3.TButton", command=self.ventana1.destroy)
        self.boton3.place(x=311, y=303, width=80, height=40)

        self.ventana1.mainloop()

    def incrementar(self):
        self.valor += 1
        self.label1.config(text=self.valor)

    def decrementar(self):
        self.valor -= 1
        self.label1.config(text=self.valor)


aplicacion1 = Aplicacion()
