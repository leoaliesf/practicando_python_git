#dado dos conjuntos como en este caso, set1 y set2 queremos un conjunto resultante
# el cual viene dado por todos los elementos de ambos conjuntos (no se repite datos)
# puede ver tambien que hay dos metodos con "union" o " | "
set1 = {1,2,4,5,6,7,8,9}
set2 = {1,2,3,5,7,11}
set3 = set1.union(set2)
print (set3)
print (set1 | set2)
#para hacer una interseccion existen igualmente dos metodos "intersection" y "&", trae todos los elementos 
# que comparten el set1 y set 2, trae solo los elementos que comparten
print()
set4 = set1.intersection(set2)
print (set4)
print (set1 & set2)
# esto viene siendo left join, donde se traen todos los elementos del set1 que no esten
# compartidos con el set 2, "difference" o " - "
print()
set5 = set1.difference(set2)
print (set5)
print (set1 - set2)
# ahora nos queda una ultima opción que seria los elementos que estan en el set1 y en el set2
# que no comparten, se ejecuntan con "symmetric_difference" o "^"
print()
set5 = set1.symmetric_difference(set2)
print (set5)
print (set1 ^ set2)