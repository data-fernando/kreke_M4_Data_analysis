lista=[1,2,3,4]
lista2=[4,1,2]
lista.append(3)
lista.insert(2,69)
lista.extend(lista2)
print(lista)

##Ceniene elemento "4" en la lista :true or false
print( 4 in lista)
##buscar
print("indice de la lista con elemento '69' es :",lista.index(69))
# contar
print("contar: ",lista.count(4))


# pop eliminar ultimo elemnento
lista.pop()
print(lista)
lista.remove(69)
print(lista)



# lista.clear()
# print(lista)

lista.sort()
print(lista)

lista.reverse()
print(lista)

lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
