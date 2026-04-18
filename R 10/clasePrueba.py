from Biblioteca import Libro
from Vehiculo import Moto,Auto
from Empleado import EmpleadoParcial,EmpleadoTiempoCmopleto

print("\n Libros")
libro1=Libro(titulo="It",autor="luther king",paginas=200)
libro2=Libro(titulo="harry poter",autor="una mujer",paginas=500)
libro3=Libro(titulo="el secreto",autor="otra persona",paginas=80)

print("metodo mostrar info \n",libro1.mostrar_info(),libro2.mostrar_info(),libro3.mostrar_info())

print("metodo es grande? \n",libro2.mostrar_info(),Libro.es_grande(libro2.paginas))
print("metodo es grande? \n",libro3.mostrar_info(),Libro.es_grande(libro3.paginas))
print("mostrar lista TOTAL ",Libro.total_libros())


print("\n Vehiculos")
auto=Auto(modelo="sedan",anio=2020,marca="toyota",numeroPuertas=4)

moto=Moto(anio="2026",modelo="motocros",marca="toyota",tipo="cadena")

print("auto\n",auto.descripcion())
print("moto\n",moto.descripcion())


print("\n Empleados")

juan=EmpleadoTiempoCmopleto(nombre="Juan",salario_base="1000")
pedro=EmpleadoParcial(nombre="Pedro",salario_base="10000")

print(juan.__dict__,juan.calcular_Salario())
print(pedro.__dict__,pedro.calcular_Salario())
