datos = []

cantidad = int(input("Cuantos datos desea ingresar: "))

for i in range(cantidad):
    valor = input("Ingrese el dato: ")

    if valor.isdigit():
        datos.append(int(valor))
    else:
        try:
            numero = float(valor)
            datos.append(numero)
        except ValueError:
            datos.append(valor)

print(f"Su lista es: {datos}")
