class Vehiculo:

    def __init__(self,marca:str,modelo:str,anio:int):

        self.marca=marca
        self.modelo=modelo
        self.anio=anio

        pass

    def descripcion(self):
        muestra={
            "marca":self.marca,
            "modelo":self.modelo,
            "anio":self.anio
        }   
        return muestra
    

class Auto(Vehiculo):

    def __init__(self, marca, modelo, anio,numeroPuertas:int):
        super().__init__(marca, modelo, anio)
        self.numeroPuertas=numeroPuertas

    def descripcion(self):
        descripcionAuto=super().descripcion()
        descripcionAuto["numP"]=self.numeroPuertas
        return descripcionAuto




class Moto(Vehiculo):

    def __init__(self, marca, modelo, anio,tipo:str):
        super().__init__(marca, modelo, anio)
        self.tipo=tipo

    def descripcion(self):
        descripcionMoto=super().descripcion()
        descripcionMoto["tipo"]=self.tipo
        return descripcionMoto



