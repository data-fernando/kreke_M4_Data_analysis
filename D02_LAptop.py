import random 

class Laptop:
    tipo="tecnologia"

    def __init__(self,marca,procesador,memoria, costo=500,impuesto=10):
        self.marca=marca
        self.procesador=procesador
        self.memoria=memoria
        self.costo=costo
        self.impuesto=impuesto

    ##self no se pasa como parametro
    def valor_final(self,descuento):
        return (self.costo*descuento)/100
    
    @staticmethod
    def metodoestatico():
        print("soy un metodo estatico")


    ##depende orde de los parametros del constructor
    @classmethod
    def metodoClaseInstancia_especifica(cls):
        tipo="clase tecnologia especial"
        marca="mac"
        procesador="i9"
        memoria="8 GB Ram"
        costo="900"
        impuesto="10"

        return cls(marca,procesador,memoria)
    
    def diagnostico(self):
        resultado={
            "marca": self.marca,
            "procesador": self.procesador,
            "memoria Espacio": "ok" if self.memoria<"8 GB Ram" else "aumentar memoria Ram",
            "bateria":"ok" if random.choice([True,False]) else "cambiar de bateria"
        }
        return resultado
    
    ##para el polimorfismos
    def realizar_informeuso(self):
        informe={
            "tipo":"generica",
            "uso recomentado":"teareas cotidianas",
            "horas uso":5,
            "diagnodtico":self.diagnostico()
        }
        return informe

        




laptop_pepito=Laptop("lenovo","i7",32)

print(laptop_pepito.__dict__)
print(laptop_pepito.valor_final(15))
print()
print(Laptop.metodoClaseInstancia_especifica().__dict__)