# Lists

"""
   Las listas son elementos mutables,
   es decir, que pueden cambiar su contenido

   Las listas nos permiten almasenar información
   en un luga, la cantidad de informacion
   que tengas: ya sean pocos elementos o millones
   de elementos.

   Se recomienda nombrar una variable de tipo lista
   en plural. 

   En python los corchetes ( [ ] ) definen una lista,
   sus elementos van separados por comas.
   Ejemplo:
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'giant']
print(bicycles)

print(bicycles[0].title())

# Los indices comienzan en 0 y terminan en n-1, donde n es la cantidad de elementos.

print(bicycles[4].title())

# Acceder al ultimo elemento de una lista.
print(bicycles[-1].title()) # Acceder al ultimo elemento.
print(bicycles[-2].title()) # Acceder al penultimo elemento.
print(bicycles[-5].title()) # Acceder al primer elemento.

# Utilizando valores de la lista
message = "Mi bicicleta favorita es la " + bicycles[4].upper() + "."
print(message)

message_f = f"Mi bicicleta favorita es la {bicycles[4].title()}."
print(message_f)

# Agregar elementos a una lista
print("\n")
print("Agregar elementos a una lista:")
print(bicycles)

print("Agregar un elemento al final de la lista:")
bicycles.append('ducatti')
print(bicycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducatti')
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki', 'ducatti']

print("\n--- Agregar elementos a una lista método insert() ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducatti')
print(motorcycles) #Salida: ['ducatti', 'honda', 'yamaha', 'suzuki']

"""
Eliminar elementos de una lista (del)

"""
print("\n--- Eliminar elementos de una lista (del) ---")
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles) #Salida: ['yamaha', 'suzuki']

"""
Eliminar elementos de una lista (pop)
"""
print("\n--- Eliminar elementos de una lista (pop) ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles) #Salida: ['honda', 'yamaha']
print(f'La motocicleta que borraste fue {popped_motorcycle.title()}.')

"""
Eliminar un elemento de una lista por valor (pop)

"""
print("\n--- Eliminar un elemento de una lista por valor (pop) ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop(1)
print(motorcycles) #Salida: ['honda', 'yamaha']
print(f'La motocicleta que borraste fue {popped_motorcycle.title()}.')

"""
Eliminar un elemento de una lista por valor (remove)

"""
print("\n--- Eliminar un elemento de una lista por valor (remove) ---")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducatti']
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki', 'ducatti']
motorcycles.remove('ducatti')
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki']
print("\n")

"""
organizar una lista permanente con sort()
"""
print("\n--- organizar una lista permanente con sort() ---")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) #Salida: ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() 
print(cars) #Salida: ['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse=True)
print(cars) #Salida: ['toyota', 'subaru', 'bmw', 'audi']      

"""
Ejemplo:

"""
students = ["Jesus", "joshue", "andrik", "jen", "mike", "africa"]
print(students)
desired_student = input("¿Cuál es el estudiante que deseas eliminar?: ")
stiudents.remove(desired_student.script().lower())
print(students)
print("Tu has eliminado", desired_student)
students.reverse()
print(students) 

print(len(students))


cars = ["kia", "ford", "tesla", "volvo", "chevrolet"]
print(cars)
print(sorted(cars))
sorted_cars = sorted(cars)
print("Lista original:", cars)