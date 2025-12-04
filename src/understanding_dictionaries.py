# understanding_dictionaries.py

# Un diccionario almacena pares clave: valor
# Es una forma de organizar información de manera estructurada.

alien_0 = {"color": "yellow"}
print(alien_0["color"])  # -> yellow



# Agregar más información

alien_0["points"] = 10
alien_0["speed"] = "medium"

print("\nDiccionario completo:")
print(alien_0)



# Acceder a valores

print("\nColor del alien:", alien_0["color"])
print("Puntos que vale:", alien_0["points"])



# Modificar valores

alien_0["color"] = "green"
alien_0["speed"] = "fast"

print("\nAlien después de modificar valores:")
print(alien_0)



# Eliminar una clave

del alien_0["points"]

print("\nLuego de eliminar 'points':")
print(alien_0)



# Usar get() para evitar errores

print("\nUsando get():")
print(alien_0.get("color"))     # existe
print(alien_0.get("points"))    # no existe -> devuelve None
print(alien_0.get("points", "No tiene puntos"))  # mensaje personalizado



# Recorrer un diccionario


otro_alien = {
    "color": "purple",
    "speed": "slow",
    "health": 50
}

print("\nRecorriendo keys:")
for key in otro_alien.keys():
    print(key)

print("\nRecorriendo values:")
for value in otro_alien.values():
    print(value)

print("\nRecorriendo items (clave y valor):")
for key, value in otro_alien.items():
    print(f"{key}: {value}")



# Lista de diccionarios

aliens = [
    {"color": "green", "speed": "fast"},
    {"color": "yellow", "speed": "medium"},
    {"color": "red", "speed": "slow"}
]

print("\nLista de aliens:")
for alien in aliens:
    print(alien)



# Modificando diccionarios dentro de una lista

print("\nModificando todos los aliens a 'blue':")
for alien in aliens:
    alien["color"] = "blue"

print(aliens)
