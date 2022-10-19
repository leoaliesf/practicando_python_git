# las variables son llamadas por cualquier letra o numero y "_", pero implican cierta reglas que debes tener en cuenta
#  no se puede empezar por un numero, puede empezar por letra o "_"  
#  hay diferencia entre mayusculas y minusculas, no es igual tener  My_var que my_var es decir son dos variables totalmente distintas 
# no puede tener espacios dentro de tu variable para separar tu variable si deseas usar "_"
# la siguiente regla a tener en cuenta es que las variables no puedes ser llamadas por las palabras claves reservadas por py revisar : python.txt
my_var = 5
print (my_var)
My_var = 11
print(My_var)
_var = 2
print (_var)
print (my_var + My_var - _var )