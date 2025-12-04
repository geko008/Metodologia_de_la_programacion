"""
Programa para entender el uso de un ciclo while
con un valor centinela.

El usuario puede ingresar valores hasta que escriba
la palabra 'salir'. Ese valor detendrá el ciclo.
"""

# Valor centinela
SENTINEL = "salir"

print("Escribe cualquier cosa. Para terminar escribe 'salir'.")

user_input = input("Ingresa algo: ")

while user_input.lower() != SENTINEL:
    print(f"Escribiste: {user_input}")
    user_input = input("Ingresa algo: ")

print("Programa finalizado. Gracias por usar el sistema.")
