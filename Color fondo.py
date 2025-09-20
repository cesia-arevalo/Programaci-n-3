import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Ventana principal ---
main = tk.Tk()
main.title("Controles TTK")
main.geometry("700x400")
main.config(bg="#DCEEF2")  # Fondo azul grisáceo claro

style = ttk.Style(main)
style.theme_use("clam")

# ---- Función para cambiar el fondo ----
def cambiar_fondo():
    color_sel = color_var.get()
    if color_sel == 0:
        main.config(bg="#FF8C69")   # Salmón suave
    elif color_sel == 1:
        main.config(bg="#87CEFA")   # Celeste
    elif color_sel == 2:
        main.config(bg="#2E8B57")   # Verde oscuro

# ---- Frame contenedor ----
container = ttk.Frame(main, padding=20, style="Card.TFrame")
container.place(relx=0.5, rely=0.5, anchor="center")

# ---- Título ----
title = ttk.Label(container, text="Elige un color de fondo",
                  font=("Segoe UI", 16, "bold"))
title.pack(pady=(0, 15))

# ---- Radiobuttons ----
color_var = tk.IntVar(value=-1)

style.configure("Color.TRadiobutton", background="#F7F7F7", foreground="#333", font=("Segoe UI", 12))
style.map("Color.TRadiobutton",
          background=[("active", "#E4E2E2")],
          foreground=[("active", "#000")])

radio_s = ttk.Radiobutton(container, variable=color_var, text="Salmon", value=0, style="Color.TRadiobutton")
radio_c = ttk.Radiobutton(container, variable=color_var, text="SkyBlue", value=1, style="Color.TRadiobutton")
radio_v = ttk.Radiobutton(container, variable=color_var, text="DarkGreen", value=2, style="Color.TRadiobutton")

for rb in (radio_s, radio_c, radio_v):
    rb.pack(anchor="w", pady=4)

# ---- Botones ----
style.configure("Accent.TButton", font=("Segoe UI", 12, "bold"), padding=6)
btn_cambiar = ttk.Button(container, text="Cambiar color", style="Accent.TButton", command=cambiar_fondo)
btn_salir   = ttk.Button(container, text="Salir", style="Accent.TButton", command=main.destroy)

btn_cambiar.pack(pady=(15, 5), fill="x")
btn_salir.pack(fill="x")

main.mainloop()
