import tkinter as tk
from tkinter import messagebox

def calcular_promedio():
    try:
        lab1 = float(entry_lab1.get())
        lab2 = float(entry_lab2.get())
        parcial = float(entry_parcial.get())

        # Validar que las notas sean entre 0 y 10
        if not (0 <= lab1 <= 10 and 0 <= lab2 <= 10 and 0 <= parcial <= 10):
            messagebox.showerror("Error", "Las notas deben estar entre 0 y 10")
            return

        # Cálculo del promedio
        promedio = (lab1 * 0.30) + (lab2 * 0.30) + (parcial * 0.40)

        messagebox.showinfo("Resultado", f"Tu promedio es: {promedio:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Promedio Cómputo 1")
ventana.geometry("300x250")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Nota Lab 1 (30%):").pack(pady=5)
entry_lab1 = tk.Entry(ventana)
entry_lab1.pack()

tk.Label(ventana, text="Nota Lab 2 (30%):").pack(pady=5)
entry_lab2 = tk.Entry(ventana)
entry_lab2.pack()

tk.Label(ventana, text="Nota Parcial (40%):").pack(pady=5)
entry_parcial = tk.Entry(ventana)
entry_parcial.pack()

# Botón para calcular
btn_calcular = tk.Button(ventana, text="Calcular Promedio", command=calcular_promedio)
btn_calcular.pack(pady=15)

ventana.mainloop()