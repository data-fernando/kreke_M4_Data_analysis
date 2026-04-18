from D02_LAptop import Laptop

class LaptopGamming(Laptop):
    # pass
    #tarjetagrafica debe tener valores o antes de los parametros con valores
    def __init__(self, marca, procesador, memoria,tarjetaGrafica:str, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.tarjetaGraficaa=tarjetaGrafica

    def diagnostico(self):
        resultado= super().diagnostico()
        resultado["fps_juegos"]=self.diagnosticoJuegos()
        return resultado

    def diagnosticoJuegos(self):
        juegos=["fornite","GTA 6","LOL"]
        FPS={}

        for juego in juegos:
            base_fps=30
            if "ryze 2400" in self.tarjetaGraficaa:
                fps_final=base_fps*3
            elif "GTx" in self.tarjetaGraficaa:
                fps_final=base_fps*2
            else:
                fps_final=base_fps
            
            FPS[juego]=fps_final

        return FPS
    pass

    def realizar_informeuso(self):
        informe_polimorfismo=super().realizar_informeuso()
        informe_polimorfismo.update(
            {
            "tipo":"gaming",
            "uso recomentado":"juegos",
            "horas uso":4,
            "diagnostico":self.diagnostico()
        }
        )

        return informe_polimorfismo







laptop_juanGaming=LaptopGamming(costo=900,marca="lenovo",impuesto=10,procesador="i13",memoria="16 GB",tarjetaGrafica="ryze 2400")



print("Herencia")
print(laptop_juanGaming.__dict__)
print(laptop_juanGaming.diagnostico())
print("polimorfismo")
print(laptop_juanGaming.realizar_informeuso())

