# creando una lista de  manera simplificada 
lista = [element for element in range (1,11)]
print (lista)
# creando una lista pero modificandole para que sea el triple del rango que hice
print ()
lista = [element * 3 for element in range (1,11)]
print (lista)
#si quisieramos añadir una condicion de que solo tome los valores del rango
# que sean divisibles entre 2
print ()
lista = [element * 3  for element in range (1,11) if element % 2 == 0]
print (lista)
#input list
n = int(input('numero de elementos de la lista:'))
lista =[]
for i in range(n):
    m= int(input('ingresa el elemento:'))
    lista.append(m)
print()
print(lista)
