pais=input("Selecione 1 para Ecuador, 2 para Colombia, y 3 para Peru\n")
zona=input("Selecione 1 para urbana , 2 para rural, y 3 para perimetral\n")
velocidad=input(" Selecione su velocidad\n")


mensaje=""
mensaje2=""
selecion=float(pais)
zonaa=int(zona)
velocidadd=int(velocidad)

if(selecion==1):
    mensaje+="Ecuador"

    if(velocidadd>10 or velocidadd<=51 and zonaa==1):
        mensaje+="\n urbana  mínimo 10 Km/h, Máximo 50 Km/h"
    elif(velocidadd>51 or velocidadd<=71 and zonaa==2):
        mensaje+="\n urbana  mínimo 51 Km/h, Máximo 70 Km/h"
    elif(velocidadd>71 or velocidadd>=90 and zonaa==3):
        mensaje+="\n urbana  mínimo 70 Km/h, Máximo 90 Km/h"
    else:
        mensaje+="\n fuera de rango de su zona"

elif(selecion==2):
    mensaje+="Colombia"
    if(velocidadd>10 or velocidadd<=31 and zonaa==1):
        mensaje+="\n urbana  mínimo 10 Km/h, Máximo 50 Km/h"
    elif(velocidadd>31 or velocidadd<=81 and zonaa==2):
        mensaje+="\n urbana  mínimo 51 Km/h, Máximo 70 Km/h"
    elif(velocidadd>81 or velocidadd>=100 and zonaa==3):
        mensaje+="\n urbana  mínimo 70 Km/h, Máximo 90 Km/h"
    else:
        mensaje+="\n fuera de rango de su zona"

elif(selecion==3):
    mensaje+="Colombia"
    if(velocidadd>10 or velocidadd<=31 and zonaa==1):
        mensaje+="\n urbana  mínimo 10 Km/h, Máximo 50 Km/h"
    elif(velocidadd>31 or velocidadd<=81 and zonaa==2):
        mensaje+="\n urbana  mínimo 51 Km/h, Máximo 70 Km/h"
    elif(velocidadd>81 or velocidadd>=100 and zonaa==3):
        mensaje+="\n urbana  mínimo 70 Km/h, Máximo 90 Km/h"
    else:
        mensaje+="\n fuera de rango de su zona"
else:
    mensaje+="algo hizo mal en sus entradas"

print(mensaje, "su velocidad fue: ",velocidadd)



