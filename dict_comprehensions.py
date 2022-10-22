# crear un directorio donde  el artributo sea el doble de la llave
dict1 = {i : i*2 for i in range (1, 6)}
print (dict1)
#para este caso en particular haremos una lista con paises, a los cuales le añadimos 
# un valor random importando el modulo para que de un numero aleatorio del atributo
print ()
import random
contries = ['colombia', 'francia', 'brasil', 'españa', 'haiti']
dict2 = {contry: random.randint(20, 100) for contry in contries}
print (dict2)
# con el resultado de dict2 ahora coloquemos una condición , sabiendo que este puede varias
# pues los de población (values o atributos) los estamos generando de manera aleatoria
print ()
result = {contry : popula for (contry, popula) in dict2.items() if popula >= 45}
print (result)
# como juntar dos listas usando zip, los valores que no tengan par, quedan 
# por fuera del diccionario
print ()
names = ['nico', 'zule', 'santi','oko']
ages = [12, 56, 98]
print (dict(zip(names, ages)))
# se crea un string donde se sacan las llaves que vienen siendo las vocales que aparecen
# en ella se coloca el condicional para probar que esten dentro e imprime las que si se 
#encuentran colocandole como values esa misma vocal pero en mayuscula
print ()
text = ' hola estoy comiendo'
unique = {caracter: caracter.upper() for caracter in text if caracter in 'aeiou'}
print (unique)
