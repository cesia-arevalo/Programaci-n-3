import tkinter as tk
from tkinter import ttk, messagebox
from empleados import Empleados

class FormularioEmpleados:
    def __init__(self):
        self.empleados = Empleados()
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Empleados")
        self.ventana.geometry("600x550")

        self.cuaderno = ttk.Notebook(self.ventana)
        self.crear_pestaña_alta()
        self.crear_pestaña_consulta()
        self.crear_pestaña_baja()
        self.crear_pestaña_modificacion()
        self.cuaderno.pack(expand=1, fill="both")

        self.ventana.mainloop()

    # ---------------- ALTA ----------------
    def crear_pestaña_alta(self):
        self.pestaña1 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pestaña1, text="Alta de empleados")

        etiquetas = ["Nombre", "Apellido Paterno", "Apellido Materno", "Email", "Fecha Contrato (YYYY-MM-DD)", "Notas"]
        self.vars_alta = [tk.StringVar() for _ in etiquetas]

        for i, texto in enumerate(etiquetas):
            ttk.Label(self.pestaña1, text=texto + ":").grid(column=0, row=i, padx=10, pady=8, sticky="e")
            ttk.Entry(self.pestaña1, textvariable=self.vars_alta[i], width=40).grid(column=1, row=i, padx=10, pady=8)

        ttk.Button(self.pestaña1, text="Guardar Empleado", command=self.alta).grid(column=1, row=len(etiquetas), pady=10)

    def alta(self):
        datos = tuple(var.get() for var in self.vars_alta)
        if all(datos):
            self.empleados.alta(datos)
            messagebox.showinfo("Éxito", "Empleado agregado correctamente.")
            for var in self.vars_alta:
                var.set("")
        else:
            messagebox.showwarning("Advertencia", "Debe completar todos los campos.")

    # ---------------- CONSULTA ----------------
    def crear_pestaña_consulta(self):
        self.pestaña2 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pestaña2, text="Consulta por ID")

        ttk.Label(self.pestaña2, text="ID del empleado:").grid(column=0, row=0, padx=10, pady=10)
        self.idconsulta = tk.StringVar()
        ttk.Entry(self.pestaña2, textvariable=self.idconsulta, width=15).grid(column=1, row=0, padx=10, pady=10)

        ttk.Button(self.pestaña2, text="Consultar", command=self.consulta).grid(column=1, row=1, pady=10)
        self.texto_consulta = tk.Text(self.pestaña2, width=60, height=15)
        self.texto_consulta.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

    def consulta(self):
        datos = (self.idconsulta.get(),)
        resultado = self.empleados.consulta(datos)
        self.texto_consulta.delete("1.0", tk.END)
        if resultado:
            for fila in resultado:
                texto = (
                    f"Nombre: {fila[0]}\n"
                    f"Apellido Paterno: {fila[1]}\n"
                    f"Apellido Materno: {fila[2]}\n"
                    f"Email: {fila[3]}\n"
                    f"Fecha Contrato: {fila[4]}\n"
                    f"Notas: {fila[5]}\n"
                )
                self.texto_consulta.insert(tk.END, texto)
        else:
            self.texto_consulta.insert(tk.END, "No se encontró el empleado.")

    # ---------------- BAJA ----------------
    def crear_pestaña_baja(self):
        self.pestaña3 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pestaña3, text="Baja de empleados")

        ttk.Label(self.pestaña3, text="ID del empleado:").grid(column=0, row=0, padx=10, pady=10)
        self.idbaja = tk.StringVar()
        ttk.Entry(self.pestaña3, textvariable=self.idbaja, width=15).grid(column=1, row=0, padx=10, pady=10)

        ttk.Button(self.pestaña3, text="Eliminar", command=self.baja).grid(column=1, row=1, pady=10)

    def baja(self):
        datos = (self.idbaja.get(),)
        if self.idbaja.get():
            self.empleados.baja(datos)
            messagebox.showinfo("Éxito", "Empleado eliminado correctamente.")
            self.idbaja.set("")
        else:
            messagebox.showwarning("Advertencia", "Debe ingresar un ID válido.")

    # ---------------- MODIFICACIÓN ----------------
    def crear_pestaña_modificacion(self):
        self.pestaña4 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pestaña4, text="Modificar empleado")

        etiquetas = ["ID del Empleado", "Nombre", "Apellido Paterno", "Apellido Materno", "Email", "Fecha Contrato (YYYY-MM-DD)", "Notas"]
        self.vars_mod = [tk.StringVar() for _ in etiquetas]

        for i, texto in enumerate(etiquetas):
            ttk.Label(self.pestaña4, text=texto + ":").grid(column=0, row=i, padx=10, pady=8, sticky="e")
            ttk.Entry(self.pestaña4, textvariable=self.vars_mod[i], width=40).grid(column=1, row=i, padx=10, pady=8)

        ttk.Button(self.pestaña4, text="Guardar Cambios", command=self.modificar).grid(column=1, row=len(etiquetas), pady=10)

    def modificar(self):
        datos = tuple(var.get() for var in self.vars_mod[1:]) + (self.vars_mod[0].get(),)
        if all(self.vars_mod):
            self.empleados.modificacion(datos)
            messagebox.showinfo("Éxito", "Empleado modificado correctamente.")
            for var in self.vars_mod:
                var.set("")
        else:
            messagebox.showwarning("Advertencia", "Debe completar todos los campos.")

# --- Punto de entrada ---
if __name__ == "__main__":
    app = FormularioEmpleados()
