# un ejemplo sencillo donde puedes ver la diferencia entre map y filter donde map devuelve la 
# respuesta en tru false y filter los valores dentro de la lista
num = [1,2,3,4,5,6]
new_num = list (map(lambda x: x % 2 == 0, num))
print(new_num)
print (num)
print ()
num = [1,2,3,4,5,6]
new_num = list (filter(lambda x: x % 2 == 0, num))
print(new_num)
print (num)
print()

#filter no modifica la lista original, aqui estamos creando una nueva lista donde buscamos, que solo muestre los equipos que han ganado
# y podemos notar que no modifica la lista original pero si me crea una nueva
matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

print(matches)
print()

new_list= list(filter(lambda item: item['home_team_result'] == 'Win' , matches))
print (new_list)

print()
print(matches)
