# Teabajando con listas

"""
Recorer una lista sin importar el tamaño
 de la cantidad de elementos que tenga la lista
"""
magicians = ["ron", "harry", "hermione"]

print(magicians[0], magicians[1])

for magician in magicians:
    print(magician)
    print(magician.upper())
    print(f"{magician.title()}, ese fue un gran hechizo.")
    print(f"{magician.lower()}, no pudemos esperar a ver tu próximo truco.")

print("\nGracias a todos por participar en el espectáculo de hoy.")

"""
Identacion:

python utiliza la indentacion para determinar a que bloque de codigo pertenece una linea
que esta conectada a otra linea del codigo anterior.

basicamente se utilizan 4 espacios para indicar que una linea pertenece a un bloque de codigo
"""

# No olvidemos identar
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)
    print(f"i can't wait to see your next trick, {magician.title()}.")

"""
# Identacion incorrecta
message = "Hello!"
    print(message)
