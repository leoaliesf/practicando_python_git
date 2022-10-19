# existen distintos tipos de datos en python por lo cual es bueno saber con que podriamos encontrarnos 
# integer o por su palabra clave "int" no es mas que todo los numeros enteros ejemplo -1, 12, 123123
# palabra clave "float" son todos los numeros reales ejemplo 2.4, 3.44543, 0.1234
# palabra clave "str" string son todos los datos que ingresas como cadena de texto ejemplo : "hola, python".
# los string deben ingresarse entre comillas a nuestro editor de codigo
#el otro tipo de dato son los boleanos y son los usados para las pruebas logicas, cuando "True" or "False" palabras claves.

print (int (4))
print (int(4.8989))
print ()

print (float(4))
print (float(4.8989))
print()
# observa que el print de float(4) da 4.0 eso es porque python le coloca ese arreglo para diferenciarlo del entero
print ("hola","python")
print()

print ("hola"=="hola")
# entenderas un poco mas los operadores logicos mas adelante, pero de momento hice una comparación 
# de si hola era igual a hola lo cual es hola lo cual es verdadero

print ("2")
print (2)
#como puedes ver estos dan como resultado ambos dos pero uno esta como cadena de texto y otro como integer
#lo puedes comprobar preguntandole a python si esos dos valores son iguales y observar su respuesta.
print()
print ("2"== 2)
#como vemos la respuesta es false por tanto python no los esta viendo como el mismo tipo de dato.