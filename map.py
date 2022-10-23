
#primer ejemplo de la función map donde te mostrare la diferencia con la manera tadricional
# de como lo harias y versus con se haria con map, queremos una lista resultante que sea el 
#doblel de la primera lista
numbers = [1, 2, 3, 4]
numbers2= []
for i in numbers:
    numbers2.append(i*2)
print(numbers, 'lista de entrada')
print(numbers2, 'lista con for')

numbers3 = list(map(lambda i : i*2, numbers))
print (numbers3, 'lista con map y lambda')
#creamos dos listas para operar con estas dos listas por medio de la función map
list1 =['leo', 'ok', 'polo', 'solo']
list2=[2, 3, 4, 5, 6]
list_result = list(map(lambda x, y : x * y, list1, list2))
print (list_result)
# como se resolveria el mismo problema con for
list_result2 = []
for i in list1:
    list_result2.append(i * list2[list1.index(i)])
print (list_result2)


