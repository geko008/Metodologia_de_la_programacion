"""
# Numbers 
Enteros: los podemos sumar (+), restar (-), 
multiplicar (*) y dividir (/)
Les podemos aplicar potencias (**, **3, **2, ...),
y también el módulo (%)
"""

number_1 = 35
number_2 = 35

suma = number_1 + number_2
resta = number_1 - number_2
multiplicacion = number_1 * number_2
division = number_1 / number_2
potencia = number_1 ** 2
modulo = number_1 % number_2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Potencia:", potencia)
print("Módulo:", modulo)

"""
Jerarquía de operaciones

 2 + 3 * 4 = 14
 (2 + 3) * 4 = 20
"""

"""
Floats:
Python considera 'float' a cualquier número con punto decimal.

Podemos sumar (+), restar (-), 
multiplicar (*), dividir (/)
y aplicar potencias (**)
"""

print(0.1 + 0.1)
print(0.2 - 0.2)
print(2 * 0.2)

# Imprimir la edad de alguien 
age = 33

# Esto genera un error:
# message = "Fulanito tiene " + age + " años."
# TypeError: no se puede concatenar string con entero

# Forma correcta:
message = "Fulanito tiene " + str(age) + " años."
print(message)

# Otra forma más moderna:
message = f"Fulanito tiene {age} años."
print(message)
