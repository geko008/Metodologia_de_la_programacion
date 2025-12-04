"""
Slicing a list
"""
players = ["charles", "martina", "michael", "florence", "eli"]
print("Lista Original: ", players)

print("Slice de lista original", players[0:3])
print("Slice de lista original", players[1:4])
print("Slice de lista original", players[:4])
print("Slice de lista original", players[2.])
print("Slice de lista original", players[-3:])
print("Slice de lista original", players[-3:-1])

"""
    Slicing en un for
"""

players = ["charles", "martina", "michael", "florence", "eli"]
print("Aqui se precentan los primeros 3 jugadores del equipo")
for player in players[0:3]:
    print(player.title())

"""
    Copiando una lista
"""
my_foods = ["pizza", "tacos", "flautas", "gorditas"]
# my_foods_copy = my_foods # Error: esta no es la manera de copiar una lista
my_foods_1 = my_foods[:]
my_foods_2 = my_foods.copy()
my_foods_3 = list(my_foods)
