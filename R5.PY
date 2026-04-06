pacientes=[]
EDADES=[]


num=int(input("ingrese el numero de datos"))

for i in range(num):
    valorNombre = input(f"Ingrese el nombre dato: {i+1}\n")
    valorNac = input(f"edad de nacimiento dato: {i+1}\n")

    if int(valorNac)<=2026:
        pacientes.append(valorNombre)
        EDADES.append(2026 -int(valorNac))
    else:
        print("edad de nacimiento no puede ser mayor a 2026")

print(f'pacientes',pacientes)
print(f'edades',EDADES)

print(f'mayor ',max(EDADES),pacientes[EDADES.index(max(EDADES))])
print(f'menor ',min(EDADES),pacientes[EDADES.index(min(EDADES))])







