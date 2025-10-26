import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import mascotas

class FormularioMascotas:
    def __init__(self):
        self.mascota1 = mascotas.Mascotas()
        self.ventana1 = tk.Tk()
        self.ventana1.title("Registro de Mascotas")
        self.cuaderno1 = ttk.Notebook(self.ventana1)

        self.carga_mascotas()
        self.consulta_por_id()
        self.borrado()
        self.modificar()

        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def carga_mascotas(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Insertar")
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Mascota")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        ttk.Label(self.labelframe1, text="Name:").grid(column=0, row=0, padx=4, pady=4)
        self.name_carga = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.name_carga).grid(column=1, row=0, padx=4, pady=4)

        ttk.Label(self.labelframe1, text="Species:").grid(column=0, row=1, padx=4, pady=4)
        self.species_carga = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.species_carga).grid(column=1, row=1, padx=4, pady=4)

        ttk.Label(self.labelframe1, text="Sex:").grid(column=0, row=2, padx=4, pady=4)
        self.sex_carga = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.sex_carga).grid(column=1, row=2, padx=4, pady=4)

        ttk.Label(self.labelframe1, text="Birth:").grid(column=0, row=3, padx=4, pady=4)
        self.birth_carga = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.birth_carga).grid(column=1, row=3, padx=4, pady=4)

        ttk.Button(self.labelframe1, text="Guardar", command=self.agregar).grid(column=1, row=4, padx=4, pady=4)

    def agregar(self):
        datos = (self.name_carga.get(), self.species_carga.get(),
                 self.sex_carga.get(), self.birth_carga.get())
        self.mascota1.alta(datos)
        mb.showinfo("Información", "Mascota registrada correctamente")
        self.name_carga.set("")
        self.species_carga.set("")
        self.sex_carga.set("")
        self.birth_carga.set("")

    def consulta_por_id(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por PetID")
        self.labelframe2 = ttk.LabelFrame(self.pagina2, text="Mascota")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        ttk.Label(self.labelframe2, text="PetID:").grid(column=0, row=0, padx=4, pady=4)
        self.petid_consulta = tk.StringVar()
        ttk.Entry(self.labelframe2, textvariable=self.petid_consulta).grid(column=1, row=0, padx=4, pady=4)

        ttk.Label(self.labelframe2, text="Name:").grid(column=0, row=1, padx=4, pady=4)
        self.name_consulta = tk.StringVar()
        ttk.Entry(self.labelframe2, textvariable=self.name_consulta, state="readonly").grid(column=1, row=1, padx=4, pady=4)

        ttk.Label(self.labelframe2, text="Species:").grid(column=0, row=2, padx=4, pady=4)
        self.species_consulta = tk.StringVar()
        ttk.Entry(self.labelframe2, textvariable=self.species_consulta, state="readonly").grid(column=1, row=2, padx=4, pady=4)

        ttk.Label(self.labelframe2, text="Sex:").grid(column=0, row=3, padx=4, pady=4)
        self.sex_consulta = tk.StringVar()
        ttk.Entry(self.labelframe2, textvariable=self.sex_consulta, state="readonly").grid(column=1, row=3, padx=4, pady=4)

        ttk.Label(self.labelframe2, text="Birth:").grid(column=0, row=4, padx=4, pady=4)
        self.birth_consulta = tk.StringVar()
        ttk.Entry(self.labelframe2, textvariable=self.birth_consulta, state="readonly").grid(column=1, row=4, padx=4, pady=4)

        ttk.Button(self.labelframe2, text="Consultar", command=self.consultar).grid(column=1, row=5, padx=4, pady=4)

    def consultar(self):
        datos = (self.petid_consulta.get(), )
        respuesta = self.mascota1.consulta(datos)
        if len(respuesta) > 0:
            self.name_consulta.set(respuesta[0][0])
            self.species_consulta.set(respuesta[0][1])
            self.sex_consulta.set(respuesta[0][2])
            self.birth_consulta.set(respuesta[0][3])
        else:
            self.name_consulta.set('')
            self.species_consulta.set('')
            self.sex_consulta.set('')
            self.birth_consulta.set('')
            mb.showinfo("Información", "No existe una mascota con dicho PetID")

    def borrado(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Borrar")
        self.labelframe3 = ttk.LabelFrame(self.pagina3, text="Mascota")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)

        ttk.Label(self.labelframe3, text="PetID:").grid(column=0, row=0, padx=4, pady=4)
        self.petid_borra = tk.StringVar()
        ttk.Entry(self.labelframe3, textvariable=self.petid_borra).grid(column=1, row=0, padx=4, pady=4)

        ttk.Button(self.labelframe3, text="Borrar", command=self.borrar).grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos = (self.petid_borra.get(), )
        cantidad = self.mascota1.baja(datos)
        if cantidad == 1:
            mb.showinfo("Información", "Se borró la mascota")
        else:
            mb.showinfo("Información", "No existe una mascota con dicho PetID")

    # ================= Modificar =================
    def modificar(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Modificar")
        self.labelframe4 = ttk.LabelFrame(self.pagina4, text="Mascota")
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)

        ttk.Label(self.labelframe4, text="PetID:").grid(column=0, row=0, padx=4, pady=4)
        self.petid_mod = tk.StringVar()
        ttk.Entry(self.labelframe4, textvariable=self.petid_mod).grid(column=1, row=0, padx=4, pady=4)

        ttk.Label(self.labelframe4, text="Name:").grid(column=0, row=1, padx=4, pady=4)
        self.name_mod = tk.StringVar()
        ttk.Entry(self.labelframe4, textvariable=self.name_mod).grid(column=1, row=1, padx=4, pady=4)

        ttk.Label(self.labelframe4, text="Species:").grid(column=0, row=2, padx=4, pady=4)
        self.species_mod = tk.StringVar()
        ttk.Entry(self.labelframe4, textvariable=self.species_mod).grid(column=1, row=2, padx=4, pady=4)

        ttk.Label(self.labelframe4, text="Sex:").grid(column=0, row=3, padx=4, pady=4)
        self.sex_mod = tk.StringVar()
        ttk.Entry(self.labelframe4, textvariable=self.sex_mod).grid(column=1, row=3, padx=4, pady=4)

        ttk.Label(self.labelframe4, text="Birth:").grid(column=0, row=4, padx=4, pady=4)
        self.birth_mod = tk.StringVar()
        ttk.Entry(self.labelframe4, textvariable=self.birth_mod).grid(column=1, row=4, padx=4, pady=4)

        ttk.Button(self.labelframe4, text="Modificar", command=self.modifica).grid(column=1, row=5, padx=4, pady=4)

    def modifica(self):
        datos = (self.name_mod.get(), self.species_mod.get(),
                 self.sex_mod.get(), self.birth_mod.get(), self.petid_mod.get())
        cantidad = self.mascota1.modificacion(datos)
        if cantidad == 1:
            mb.showinfo("Información", "Se modificó la mascota")
        else:
            mb.showinfo("Información", "No existe una mascota con dicho PetID")

FormularioMascotas()