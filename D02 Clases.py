class PastelCumple:
    sabor="chocolate"
    tamanio=4
    forma="cuadrados"

pastelJuan=PastelCumple()

pastelMaria=PastelCumple()

print(pastelJuan.tamanio)


class Laptop:
    def __init__(self,marca,procesador,memoria, costo=500,impuesto=10):
        self.marca=marca
        self.procesador=procesador
        self.memoria=memoria
        self.costo=costo
        self.impuesto=impuesto

    ##self no se pasa como parametro
    def valor_final(self,descuento):
        return (self.costo*descuento)/100


laptop_pepito=Laptop("lenovo","i7",32)

print(laptop_pepito.__dict__)
print(laptop_pepito.valor_final(15))
        