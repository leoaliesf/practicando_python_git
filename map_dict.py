
# cuando se trabaja con  dictionarios y map
items = [
    {'product':'camisa', 'price': 100},
     {'product':'pantalones', 'price': 300},
      {'product':'pantalones2', 'price': 200},
]
prices = list(map(lambda item: item['price'], items))
print(prices)
print()

#para añadir una linea en nuestro diccionario de taxes, no se usa lambda porque se necesita mas de dos lineas de comando
'''def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item'''
# se debe usar la función copy si no deseas que se cambie el diccionario original, de la forma que aparece comentada tambien 
# cambia el diccionario original, que quizas no sea lo que desas hacer, de esta forma que esta aqui lo hacemos inmutable
def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item
new_items = list(map(add_taxes, items))
print (new_items)
print (items)
