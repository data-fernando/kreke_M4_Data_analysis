from D02_LAptop import Laptop
from R08_Herencia import Laptop_Business
import tkinter as tk
from tkinter import ttk
import random
from PIL import Image,ImageTk


class AppLaptopBusiness:

    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.imagenes=[r"img/imageReto2.png",r"img/imageReto.png"]
        root.title("Ingresar datos Laptop Business")
        self.setup_ui()

    def setup_ui(self):
        # Marca
        ttk.Label(self.root, text="Marca").grid(row=0, column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0, column=1)

        # Procesador
        ttk.Label(self.root, text="Procesador").grid(row=1, column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1, column=1)

        # Duración batería
        ttk.Label(self.root, text="Duración batería (hrs)").grid(row=2, column=0)
        self.duracion_bateria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.duracion_bateria).grid(row=2, column=1)

        # Almacenamiento
        ttk.Label(self.root, text="Almacenamiento (GB/TB)").grid(row=3, column=0)
        self.almacenamiento = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.almacenamiento).grid(row=3, column=1)

        # Memoria
        ttk.Label(self.root, text="Memoria (GB)").grid(row=4, column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=4, column=1)

        # Costo
        ttk.Label(self.root, text="Costo").grid(row=5, column=0)
        self.costo = tk.IntVar(value=500)
        ttk.Entry(self.root, textvariable=self.costo).grid(row=5, column=1)

        # Impuesto
        ttk.Label(self.root, text="Impuesto").grid(row=6, column=0)
        self.impuesto = tk.IntVar(value=10)
        ttk.Entry(self.root, textvariable=self.impuesto).grid(row=6, column=1)

        # Botón para crear objeto
        ttk.Button(self.root, text="Crear Laptop Business", command=self.crear_laptop).grid(row=7, column=0, columnspan=2)

        # Área de texto para mostrar datos
        self.mostrar_laptop = tk.Text(self.root, height=15, width=50)
        self.mostrar_laptop.grid(row=8, column=0, columnspan=2)

        self.canva=tk.Canvas(self.root,width=200,height=200)
        self.canva.grid(row=8,column=3)

    def crear_laptop(self):
        laptop = Laptop_Business(
            marca=self.marca.get(),
            procesador=self.procesador.get(),
            duracion_bateria=self.duracion_bateria.get(),
            almacenamiento=self.almacenamiento.get(),
            memoria=self.memoria.get(),
            costo=self.costo.get(),
            impuesto=self.impuesto.get()
        )
        self.laptops.append(laptop)
        print("Laptop Business creada:\n", laptop.__dict__)
        self.mostrar_laptop.insert(tk.END, f"{laptop.__dict__}\n")
        self.mostrar_laptop.insert(tk.END, f"Diagnóstico: {laptop.diagnostico()}\n\n")

        self.crear_imagenesAleatorias()
        

    def crear_imagenesAleatorias(self):
        imagen_path=random.choice(self.imagenes)
        imagen=Image.open(imagen_path)
        imagen=imagen.resize((200,200),Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(imagen)

        self.canva.create_image(0, 0, anchor=tk.NW, image=self.photo)

    pass


root = tk.Tk()
app = AppLaptopBusiness(root)
root.mainloop()
