#reduce, sirve para hacer operaciones dentro de la lista y obtener un valor como respuesta, es este primer ejemplo
#queremos obtener el numero mayor de una lista de valores
import functools 
num = [8, 1, 2, 3, 4]
def mayor(counter, item):
    if counter <= item :
        return item
    else :
        return counter
result = functools.reduce(mayor, num) 
print (result)
print()
#segundo ejemplo para obtenr el acumulado de la suma de valores internos de la lista
num2 = [1, 2, 3, 4]
resut2= functools.reduce(lambda counter, item: counter + item , num2)
print (resut2)