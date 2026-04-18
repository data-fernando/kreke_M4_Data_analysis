from abc import abstractmethod
class Empleado:

    def __init__(self,nombre:str,salario_base:float):

        self.nombre=nombre,
        self.salario_base=salario_base

    @abstractmethod
    def calcular_Salario(self):
        pass


class EmpleadoTiempoCmopleto(Empleado):

    def __init__(self, nombre, salario_base):
        super().__init__(nombre, salario_base)


    def calcular_Salario(self):
        return float(self.salario_base)*1.2


    

class EmpleadoParcial(Empleado):

    def __init__(self, nombre, salario_base):
        super().__init__(nombre, salario_base)

    def calcular_Salario(self):
        return float(self.salario_base)*1.1

        