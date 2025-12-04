"""
Generar una lista con los cuadrados usando un ciclo for
y luego usando list comprehension.
"""

# --- Usando ciclo for ---
squares = []
for value in range(0, 11):
    square = value ** 2
    squares.append(square)

print("Cuadrados con ciclo for:")
print(squares)

"""
Una list comprehension combina el ciclo for y
la creación de nuevos elementos en una sola línea
y agrega cada nuevo elemento automáticamente a la lista.
"""

# --- Usando list comprehension ---
squares = [value ** 2 for value in range(0, 11)]
print("\nCuadrados con list comprehension:")
print(squares)

# --- Generar números pares entre el 0 y el 100 ---
evens_range = [value for value in range(0, 101, 2)]
print("\nNúmeros pares con step (range):")
print(evens_range)

# --- Generar números (esta lista estaba incompleta) ---
squares_if = [value ** 2 for value in range(0, 101)]
print("\nCuadrados del 0 al 100:")
print(squares_if)

# --- Filtrar solo pares con condición ---
evens_if = [value for value in range(0, 101) if value % 2 == 0]
print("\nNúmeros pares con condición if:")
print(evens_if)
