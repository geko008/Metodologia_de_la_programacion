name = "clase de programacion"
print(name)

# title
print(name.title())

print(name)

"""
    un metodo es una accion que python puede realizar en un fragmento
    de datos o sobre un variable.
    
    el punto . depues de una vaarible seguido de metodo title() dice que se tiene que ejecutar
     el metodo title() de la varible name.

    todos los meetodos van seguidos de parentesis porque en ocasiones necvesita informacion adicional para funcionar, la cual iria dentro
     de los parentesis. en esta ocasion, el metodo .title() no requiere informacion adcional para funcionar
"""

print("metodo upper: ", name.upper())
print("metodo lower: ", name.lower())


# concatenacion de STRINGS
first_name = "mickey"
last_name = "arellano"
full_name = first_name + " " + last_name
print(full_name)
print(full_name.title())

# whitespaces
"""
    un whitespaces se refiere a cualquier caracter que no se imprime, es decir,
    un espacio, tabuladores y finakes de linea. los whitespaces se utlizan comunmente para organizar las salidas de 
    tal manera que sea mas amigable de leer o ver para el usuario.

    ejemplo:
        - tabulador: \t
        - salto de linea: \n
"""
print("\nwihtespace tabulador")
print("python")
print("\tpyhon")
print("\t\tpython")

print("salto de linea")
print("languages: \n\tpython\nc\n\tjavascript")

# eliminacion de espacios en blanco
programming_lenguages = "python"
print(programming_lenguages)
print(programming_lenguages.rstrip())
print(programming_lenguages.lstrip())
print(programming_lenguages.strip())

# syntax error con strings
message = 'una fortaleza de python es su comunidad'
print(message)
message = "una fortaleza de "python" es su comunidad"
print(message)

# f-strings
famous_person = "taylor swift"








#actividad
"""
    varuiable -> elige el nombre de una persona famosa (quien tu quieras).
    varible 2-> elige una cita famosa de esta persona.

    1) realiza la concatenacion utilizando el signo de de suma
    2) realiza la concatenacion utlizando fstrings 
"""

famous_person = "henry calvin"
quote = "python is love"
famous_mesage_ = famous_person+""+quote
print (famous_person+""+quote)
print(famous_mesage)

f_string_message = f"{famous_person} {quote}"
print(f_string_message)
