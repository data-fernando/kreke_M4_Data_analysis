alto=input("ingrese Alto")
lado=input("ingrese Lado")

def area_Rec(alto,lado):
    altoo=float(alto)
    ladoo=float(lado)
    return ladoo*altoo

def perimetro(alto,lado):
    altoo=float(alto)
    ladoo=float(lado)
    return (altoo+ladoo)*2

def area_triangulo(alto,lado):
    altoo=float(alto)
    ladoo=float(lado)
    return (ladoo*altoo)/2




print("El área del rectángulo: ",area_Rec(alto,lado))
print("El perímetro del rectángulo: ",perimetro(alto,lado))
print("Superficie del rectángulo: ",area_triangulo(alto,lado))
