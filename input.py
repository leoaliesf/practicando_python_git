# "input" es la palabra clave de python para pedir que ingreses valores, ese valor se le asigna a una variable
# que tu hayas nombrado

my_var = input('ingrese un valor cualquier :')
print (my_var*2)  
# veras que el resultado es lo que ingresaste repetido, es decir si ingresas 2 tu salida sera "22" esto se debe 
# a que "input" siempre asumira la entrada como una cadena de texto debemos decirle que tipo de dato es si queremos
#cambiar esto
print ()
my_var = int(input('ingrese un valor cualquier :'))
print (my_var*2)  
# si ves la respuesta para este caso si ingresas el mismo 2 sera 4, ya que hemos usado la palabra clave "int()" y dentro de ella
#esta el input por tanto le decimos a python que el valor ingresado sera un entero y que lo guarde de esta manera.
# podras notar que si ingresas un numero racional como 3.8 no podras pues este no es un tipo entero para ello esta la
#siguiente solución
print ()
my_var = float(input('ingresa cualquier valor'))
print (my_var*2)
# para esta ocasión cualquier numero que ingreses sera aceptado incluso si es 3.8 






