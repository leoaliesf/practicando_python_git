# usando variables para guardar informacion y realizar operaciones con estas.
hello = 'vas apreder sobre como usar variables'
print (hello)
print ()
#esta es la primera variable (hello) le asigne un string o cadena de texto, asi cuando invoque esta variable imprime su msj.
my_var = 5
my_string= "2"
print (my_var*my_string)
# que resultado esperabas mira que la respues es "22222" esto se debe a que my_string esta guardado como una 
# cadena de texto por tanto no puede realizar operaciones matematicas igual que como con numeros 
# para el caso de las string se repite 5 veces que es el numero de my_var
print()
my_var =3
my_var2= 4
print (my_var+ my_var2)
#como veras en esta ocacion le asignamos un nuevo valor a la variable my_var este valor cambia al pasado, puede
# cambiar el valor de la variable cuantas veces necesites 
print()
my_var = my_var2 /2
print (my_var)
print (my_var2)
#observa que he usado la variable my_var2 y la dividi entre 2 para darle un nuevo valor a mi variable 
# el valor de tus variables sera aceptado por otras variables con el dato asignado
print ()
num1 = 1
num2 = 2
num3 = 3
num4 = num1 + num2 * num3
print (num4)
#las operaciones matematicas en python siguen un orden jerarquico, ten en cuenta que la multiplicación siempre sera primero
# que la suma, ademas mira que se creo una variable a partir de otras variables y esta toma el valor de la operación que le asignamos
print ()
print(my_string+hello)