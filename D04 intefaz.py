from D03_Herencia import LaptopGamming
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import random


class AppLaptop:

    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.imagenes=[r"img/pcgamer2.png", r"img/pcgamer1.png"]
        root.title("Ingresar datos")
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

        # Memoria
        ttk.Label(self.root, text="Memoria (GB)").grid(row=2, column=0)
        self.memoria = tk.IntVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=2, column=1)

        # Tarjeta Grafica
        ttk.Label(self.root, text="Tarjeta Gráfica").grid(row=3, column=0)
        self.tarjetaGrafica = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.tarjetaGrafica).grid(row=3, column=1)

        # Botón para crear objeto
        ttk.Button(self.root, text="Crear Laptop", command=self.crear_laptop).grid(row=4, column=0, columnspan=2)

        self.mostrar_laptop=tk.Text(self.root,height=15,width=40)
        self.mostrar_laptop.grid(row=5,column=0,columnspan=2)

        self.canva=tk.Canvas(self.root,width=200,height=200)
        self.canva.grid(row=5,column=3)

    def crear_laptop(self):
        laptop = LaptopGamming(
            marca=self.marca.get(),
            procesador=self.procesador.get(),
            memoria=self.memoria.get(),
            tarjetaGrafica=self.tarjetaGrafica.get()
        )
        self.laptops.append(laptop)
        print("Laptop creada UI\n:", laptop.__dict__)
        self.mostrar_laptop.insert(tk.END,f"{laptop.__dict__}")
        # imagenes
        self.crear_imagenesAleatorias()

    def crear_imagenesAleatorias(self):
        imagen_path=random.choice(self.imagenes)
        imagen=Image.open(imagen_path)
        imagen=imagen.resize((200,200),Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(imagen)

        self.canva.create_image(0, 0, anchor=tk.NW, image=self.photo)

        pass



root = tk.Tk()
app = AppLaptop(root)
root.mainloop()
