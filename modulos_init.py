#son modulos incorporados en python que podrias encontrar normalmente y debes conocer
#re.findall encuentra los valores que buscas en el texo
import re
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'
result = re.findall('[0-9]+', text)
print(result)
print()
#para trabajar con el tiempo en python esta este modulo, time.time solo entendible para la maquina 
#time.localtime + time.asctime agrega el tiempo en una medida entendible para la persona
import time
timestamp = time.time()
print(timestamp)
print()
local = time.localtime()
result = time.asctime(local)
print(result)
print()
#collections.counter devuelve el numero de repeticiones que ocurren en una lista
import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)