"""
  Vamos a realizar un programa que defina un PIN
  para dar acceso al usuario.

  El usuario tendrá un número máximo de intentos 
  para colocar bien el PIN.

  Si el usuario sobrepasa ese máximo de intentos
  se va a bloquear la cuenta y el acceso.
"""

CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
attempt = 0

while attempt < MAX_ATTEMPTS:

    user_input = input("Ingresa tu PIN: ")

    if user_input == CORRECT_PIN:
        print("Acceso concedido")
        break
    else:
        attempt += 1
        remaining_attempts = MAX_ATTEMPTS - attempt
        
        if remaining_attempts > 0:
            print("PIN no válido")
            print(f"Te quedan {remaining_attempts} intento(s).")
        else:
            print("Cuenta bloqueada")
