# comparación de una función lambda y una funcion por "def", obteniendo el mismo resultado
# se añade a una variable la funcion lambda y luego de los dos puntos se coloca todo lo necesario
# para cumplir tu funcion
def incremento(x):
    return x + 1

incremento2 = lambda x : x + 1
print (incremento2(10))
print (incremento(10))
print ()
# una función lambda para escribir tu nombre dentro de la frase
full_name = lambda name , last_name: f'Full name is {name.title()}{last_name.title()}'

print (full_name('leo', ' alies'))
print()
#una función lambda que toma valor predeterminados las condiciones ambientes para la 
# función de gases ideales, donde se quiere hallar el numero de moles, se puede o no
# agregar valores a los parametros según conveniencia 
n_moles = lambda p=1, v=25, t=298.3, r=0.082: (p*v)/(t*r) 
print (n_moles(), 'sin valores añadidos')
print ('ejemplos cambiando los valores de los parametros')
print (n_moles(p=3, t=239.9))
print (n_moles(v=10))
print (n_moles(t=298.3, p=12, v=90))
print (n_moles(t=12))
