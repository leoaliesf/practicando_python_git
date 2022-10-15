# esto es un programa para determinar el perimetro de un cuadrado
print ('Bienvenido a mi programa')
print('este programa es para determinar el perimetro y el area de un cuadrado')
try :
    n = float(input('por favor ingrese el valor del lado del cuadrado : '))
    while True:
        if n < 0:
            print('ingrese un valor valido')
            n = float(input('pruebe con un valor mayor que 0 : '))
            True
    else:
        perimetro = 4*n
        area = n*n
        print('perimetro es igual', "=", perimetro)
        print('area es igual', '=', area)
       
except :
    print("Only numbers are allowed")