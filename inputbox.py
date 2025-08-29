import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.geometry('600x400')

        # Primer número
        self.label1 = tk.Label(self.ventana1, text="Ingrese un número:")
        self.label1.grid(column=0, row=0)
        self.dato1 = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width=10, textvariable=self.dato1)
        self.entry1.grid(column=0, row=1)

        # Segundo número
        self.label3 = tk.Label(self.ventana1, text="Ingrese otro número:")
        self.label3.grid(column=0, row=4)
        self.dato2 = tk.StringVar()
        self.entry2 = tk.Entry(self.ventana1, width=10, textvariable=self.dato2)
        self.entry2.grid(column=0, row=5)

        self.boton1 = tk.Button(self.ventana1, text="Calcular Cuadrado y Suma", command=self.calcular)
        self.boton1.grid(column=0, row=2)

        self.label2 = tk.Label(self.ventana1, text="resultado")
        self.label2.grid(column=0, row=3)

        self.label4 = tk.Label(self.ventana1, text="suma")
        self.label4.grid(column=0, row=6)

        self.ventana1.mainloop()

    def calcular(self):
        valor1 = int(self.dato1.get())
        valor2 = int(self.dato2.get())

        cuadrado = valor1 * valor1
        suma = valor1 + valor2


        self.label2.configure(text=f"Cuadrado del primer número: {cuadrado}")
        self.label4.configure(text=f"Suma: {suma}")

aplicacion1 = Aplicacion()
