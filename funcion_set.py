# set es un conjunto, es similar a los diccionarios o su sintaxis es similar pero no tiene atributos
Set_numeros = {1, 2, 3, 4}
print(Set_numeros)
print(type(Set_numeros))
# aunque se repita un valor dentro del set, este no se va imprimir porque en un conjunto de valores 1 aunque se escriba muchas 
# veces seguira siendo uno por lo cual se identificara
print ()
Set_numeros = {1, 2, 3, 4, 1, 1}
print(Set_numeros)
print(type(Set_numeros))
#set acepta cualquier tipo de datos
print ()
Set_numeros = {1, False, 'hola', 4.98, 1.7}
print(Set_numeros)
# convertir un string en set, devuelve cada letra como caracter dentro del conjunto, tener en cuenta que si una string 
# tiene varias letras repetidas solo tomara una de esas letras
print()
set_string = set('hola como estas')
print (set_string)
# pueder convertir tuplas y listas de la misma manera y se los devolvera como set (no repite datos)
print()
set_lista = set([1,2,3,4,5])
print (set_lista)
#para saber el tamaño de tu conjunto
print()
Set_numeros = {1, 2, 3, 4}
size = len(Set_numeros)
print(size)
# cuando quieres buscar un elemento especifico de u conjunto (el set )
print ()
print (5 in Set_numeros) 
print (3 in Set_numeros)
# para añadir un elemento dentro del conjunto se usa "add"
print()
Set_numeros.add(5)
print(Set_numeros)
# para añadir varios elementos dentro del conjunto se usa "udapte"
print()
Set_numeros.update( {6, 7, 8, 9})
print(Set_numeros)
# para remover un elemento del conjunto, si el elemento a remover no esta dentro
# del conjunto soltara un error
print ()
Set_numeros.remove(5)
print(Set_numeros)
# para limpiar todo el conjunto se hace con "clear", lo cual quedara un conjunto en vacio
print ()
Set_numeros.clear()
print (Set_numeros)