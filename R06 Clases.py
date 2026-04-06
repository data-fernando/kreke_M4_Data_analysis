class Auto:
    kilometraje=0
    estado="nuevo"

    def __init__(self,marca,modelo,anio,costo=0):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio
        self.costo=costo
        self.kilometraje=0


    def actualizar_kilometraje(self,kilometraje_act):
        if(kilometraje_act>self.kilometraje):
            self.kilometraje=kilometraje_act
        else:
            print("kilometraje menor que el amterior")

    
    def realizar_viaje(self,kil_viaje):
        if(kil_viaje>0):
            self.kilometraje+=kil_viaje
        else:
            print("kilometraje debe ser positivo")

    def estado_auto(self):
        if(self.kilometraje<20000):
            mensaje="como nuevo"
        elif(self.kilometraje>=20000 and self.kilometrajeself>=100000):
            mensaje="ya estoy usado"
        else:
            mensaje="dejame descansar por favor"
        
        return mensaje+": kilometraje"+str(self.kilometraje)
    
    # usar metodo sin instanciar
    @staticmethod
    def imprimir():
        print("soy un metodo estatico")

    ## intancaiar un especifico objeto dentro de la clase
    @classmethod
    def toyotaCarro(cls):
        marca="toyota"
        modelo="pickup"
        anio="2028"
        return cls(marca,modelo,anio)
    
    @staticmethod
    def mismoKilometrake(auto1,auto2):
        if(auto1.kilometraje==auto2.kilometraje):
            return("tienen mismo kilometraje")
        else:
            return("diferente kilometraje")
    
    @classmethod
    def toyotaCarro(cls):
        marca="toyota"
        modelo="pickup"
        anio="2028"
        return cls(marca,modelo,anio)
    
    @classmethod
    def toyotaCarroParam(cls,costo2):
        marca="toyota"
        modelo="pickup"
        anio="2028"
        costo=costo2
        return cls(marca,modelo,anio,costo)
    

vehiculo1=Auto(modelo="formula 1",marca="lamborgini",anio=2015,costo=5000000)
vehiculo2=Auto(modelo="camioneta",marca="ford",anio=2027,costo=50000)
vehiculo3=Auto.toyotaCarroParam(costo2=60000)

vehiculo3.actualizar_kilometraje(50000)

carros=[vehiculo1,vehiculo2,vehiculo3]

for carro in carros:
    print(carro.__dict__)

print("vehiculo 1 y 2: "+str(Auto.mismoKilometrake(vehiculo1,vehiculo2)))
print("vehiculo 1 y 3: "+str(Auto.mismoKilometrake(vehiculo1,vehiculo3)))


    

# vehiculo=Auto(marca="chevrolet",modelo="camioneta",anio=2025)

# print(vehiculo.__dict__)
# print(vehiculo.estado)
# print(vehiculo.anio)
# print(vehiculo.actualizar_kilometraje(200))
# print(vehiculo.realizar_viaje(3000))
# print(vehiculo.estado_auto())
# print(vehiculo.imprimir())
# print("---------")
# caroo_toyota=Auto.toyotaCarro()
# print(caroo_toyota.__dict__)
# print("---------")

# for numero in range(1,11):
#     carroToyota2=Auto.toyotaCarroParam(numero)
#     print(carroToyota2.__dict__)








    
        
    

