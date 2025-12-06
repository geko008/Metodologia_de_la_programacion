"""
Universidad Politécnica de Victoria
Materia: Metodología de la Programación
Grupo: IM-03
Alumno: Guillen Segura Africa Citlali
Matrícula: 2530275
Proyecto: Fibonacci Series (:
Fecha: 5 de diciembre del 2025
Profesor: Carlos Antonio Tovar García
"""


print("Number of terms:")
n = input()

if not n.isdigit():
    print("Error: invalid input")
    exit()

n = int(n)

if n < 1 or n > 50:
    print("Error: invalid input")
    exit()

print("Fibonacci series:")

a = 0
b = 1

if n == 1:
    print(a)
    exit()

if n == 2:
    print(a, b)
    exit()

print(a, b, end=" ")

count = 2

while count < n:
    c = a + b
    print(c, end=" ")
    a = b
    b = c
    count += 1
