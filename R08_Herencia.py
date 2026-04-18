from D02_LAptop import Laptop
import random

class  Laptop_Business(Laptop):

    def __init__(self, marca, procesador,duracion_bateria,almacenamiento, memoria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)

        self.almacenamiento=almacenamiento
        self.duracion_bateria=duracion_bateria

    ##sobreescritura
    def diagnostico(self):
        diagnostoco_Laptop= super().diagnostico()
        diagnostoco_Laptop["conectividad"]=self.verificar_conectividad_red()
        return diagnostoco_Laptop

    def verificar_conectividad_red(self):
        conecion_red={
            "red": random.choice(("wifi","red ethernet","datos","satelital")),
             "acceso_servidor":random.choice((True,False)),
             "latencia":random.choice((200,500,400,100))
        }
        return conecion_red
    
    
        
    


Laptop_BUSINESSiNANCI=Laptop_Business(marca="hp worstation",procesador="7 i ",duracion_bateria="9 HR",almacenamiento="2 TB",memoria="16 gb",costo=800,impuesto=9)
       
print(Laptop_BUSINESSiNANCI.__dict__)
print(Laptop_BUSINESSiNANCI.diagnostico())




    


