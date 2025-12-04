### FUNCIONES
# Las funciones son bloques de código reutilizables que realizan una tarea específica.
# Cuando queremos realizar la tarea, llamamos a la función por su nombre.

"""
Sintaxis para definir una función:

def nombre_funcion():
    acciones de la función
"""

# Ejemplo: vamos a definir una función que salude a Christopher
def greeting_christopher():
    """
    Función que saluda a Christopher imprimiendo su nombre 5 veces.
    """
    for i in range(5):
        print("Christopher")

# Llamando a la función
greeting_christopher()



# EJEMPLO EXTRA: función con parámetro

def greet_person(name):
    """
    Saluda a cualquier persona cuyo nombre se reciba como parámetro.
    """
    print(f"Hola, {name}. ¡Bienvenido!")

greet_person("África")
greet_person("Luis")
greet_person("Christopher")


# Temas relacionados (a futuro):
# - manejo de datos
# - entornos virtuales (.venv)
# - lectura CSV
# - archivos Excel
# - recibir argumentos por consola (args)

