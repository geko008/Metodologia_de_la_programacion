cars = ["audi", "bmw", "chevrolet", "corvette", "tesla"]

for car in cars:
    if car == "bmw" or car =="tesla" or car =="audi":
        print(car.upper())
    else:
        print(car)
    

print("\n---condicional---")
# Condicionales: El comdicional es el corazón de un if
# Condicional True

car = "bmw"
print(car=="bmw")

# Condicional false
car_2 = "Audi"
print(car_2=="audi")

car_2 = "Audi"
print(car_2.lower()=="audi") # Salida -> True

# Condicional != para determinar desigualdad
requested_topping = "mushrooms" # - string
if requested_topping != "anchovies": # - True
    print("Hold the anchovies")

# Comparaciones numericas
age = 18 # - int
print(age==18) # -> True

answer = 17
if answer != 42:
    print("Esa no es la repuesta correcta. Intenta otra vez")

age = 19
print(age<21) # -> true
print(age<=21) # -> true
print(age>21) # -> false
print(age>=21) # -> false

# Multiple
age_0 = 22
age_1 = 18

print("Multiples condiciones")
print("Operacion and - pseint (Y)")
print( age_0 >= 21 and age_1 >= 21) # False
print( age_0 >= 21 and age_1 >= 18) # True

print("Operacion or - pseint (O)")
print( age_0 >= 21 or age_1 >= 21) # True
print( age_0 >= 21 or age_1 >= 18) # False

# ¿Como nos preguntamos si un valor esta
# en un lista?

requested_toppings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_topping) #->True
print("pepperoni" in requested_topping) #->False

# A value not in a list
banned_users = ["gabriel", "max", "andrik", "quevedo", "christo"]
user = "pedro"
print(user not in banned_users)

# Variables de tipo BOLEANOS
game_active = True
can_edit = False 


"""
if statement

if condition:
    do something

if condition:
    do something (True)
else:
     do something (False)


"""

# Preguntar la edad del usuario
# Y decirle si tiene la edad 
# suficiente para votar
# input("") -> Str
age = int(input("\n\nEscribe tu edad: "))
print(f"\nTu edad es: {age}")

if int(age)>=18:
    print("Tu tienes la edad para votar")
else:
    print("Lo siento, eres demaciado joven para votar")

