# Africa Citlali Guillen Segura/2530275
# Password attempts with while (problema1)
# implementa un sistema sencillo de contraseña


-user_password = "admin123"
MAX_ATTEMPTS = 3 

while MAX_ATTEMPTS > 0:
    password = input("set your password: ")
    if password == user_password:
        print("login success")
        break
    else:
        MAX_ATTEMPTS -=1 
        print(f". Te quedan {MAX_ATTEMPTS} intento(s).")


if MAX_ATTEMPTS == 0:
    print("account locked")
    

# factorial fuction(iterative or recursive)(problema2)
# define una fincion factorial 
- n (int)
-"factorial:" <factorial_value>

-n entero 
-n >= 0
n <= 20









# pregunta de rescate 1

while True:
    num = input("Ingresa un número: ")

    if num.isdigit() and int(num) > 0:
        num = int(num)
        break
    else:
        print("Entrada inválida.\n")
a, b = 0, 1

print(f"\nSerie hasta {num}:\n")

for _ in range(num):
    if a > num:
        break  

    print(a)
    a, b = b, a + b

   

