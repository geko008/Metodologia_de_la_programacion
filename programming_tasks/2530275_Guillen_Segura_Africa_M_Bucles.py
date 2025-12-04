"""
Universidad Politécnica de Victoria
Materia: Metodología de la Programación
Grupo: IM-03
Alumno: Guillen Segura Africa Citlali
Matrícula: 2530275
Proyecto: Manejo de bucles en Python
Fecha: 3 de diciembre del 2025
Profesor: Carlos Antonio Tovar García
"""

#problema 1: Sum of range with for
"""
Description:
This problem involves calculating the sum of all 
integers from 1 up to and including n. 
Additionally, you must calculate the sum of 
only the even numbers within that range using a 
for loop.

Input:
-n: an integer that represents the upper limit of the range.

Output:
-"Sum 1..n:" followed by the total sum.
-"Sum even 1..n:" followed by the sum of even numbers.

Validation:
-Verify that n can be converted to an integer.
-Ensure that n is greater than or equal to 1; otherwise, display an error message.

Test Cases:
1) Input: n = 5
    Output:
    Sum 1..n: 15
    Sum even 1..n: 6
2) Input: n = 10
    Output:
    Sum 1..n: 55
    Sum even 1..n: 30

3) Input: n = -3
    Output:
    Error: n must be greater than or equal to 1.
"""
n = input("Enter a positive integer n: ")
try:
    n = int(n)
    if n < 1:
        print("Error: n must be greater than or equal to 1.")
    else:
        total_sum = 0
        even_sum = 0
        for i in range(1, n + 1):
            total_sum += i
            if i % 2 == 0:
                even_sum += i
        print("Sum 1..n:", total_sum)
        print("Sum even 1..n:", even_sum)
except ValueError:
    print("Error: Please enter a valid integer.")

#problema 2: Multiplication table with for
"""
Description:
Generate and display the multiplication 
table for a base number from 1 up to a 
limit m. For example, if the base is 5 
and m is 4, you should display the 
corresponding multiplications.

Input:
- base: an integer representing the base number of the table.1
- m: an integer indicating the limit of the table.

Output:
-One line per multiplication in the format "base x i = result".

Validation:
-Ensure that both the base and m can be converted to integers.
-Verify that m is greater than or equal to 1; otherwise, display an error message.

Test Cases:
1) Input: base = 3, m = 5
    Output:
    3 x 1 = 3
    3 x 2 = 6
    3 x 3 = 9
    3 x 4 = 12
    3 x 5 = 15
2) Input: base = 7, m = 3
    Output:
    7 x 1 = 7
    7 x 2 = 14
    7 x 3 = 21
3) Input: base = 4, m = 0
    Output:
    Error: m must be greater than or equal to 1.
"""

base = input("Enter the base number for the multiplication table: ")
m = input("Enter the limit m for the multiplication table: ")
try:
    base = int(base)
    m = int(m)
    if m < 1:
        print("Error: m must be greater than or equal to 1.")
    else:
        for i in range(1, m + 1):
            result = base * i
            print(f"{base} x {i} = {result}")
except ValueError:
    print("Error: Please enter valid integers for base and m.")

# Ptoblem 3: Average of numbers with while and sentinel
"""
Description:
This problem requires you to read numbers 
one by one until the user enters a sentinel 
value (for example, -1). Calculate the average 
of the valid numbers entered and the total number 
of numbers read. If the user enters only the 
sentinel value without any valid numbers, 
display an error message.

Inputs:
number: A floating-point number that is read repeatedly.
sentinel_value: A fixed value in the code (for example, -1) that indicates the end of the input.

Outputs:
"Count:" followed by the number of valid inputs.
"Average:" followed by the average of the valid numbers.
If no valid data is entered, display "Error: no data".

Validations:
Each number read should be converted to a floating-point number.
Ignore the sentinel value in calculations.

Test Cases:
1) Input: 5.0, 10.0, 15.0, -1
    Output:
    Count: 3
    Average: 10.0
2) Input: -1
    Output:
    Error: no data
3) Input: 7.5, 2.5, -1
"""
sentinel_value = -1
count = 0   
total_sum = 0.0
while True:
    number = input("Enter a number (or -1 to finish): ")
    try:
        number = float(number)
        if number == sentinel_value:
            break
        total_sum += number
        count += 1
    except ValueError:
        print("Error: Please enter a valid floating-point number.")
if count == 0:
    print("Error: no data")
else:
    average = total_sum / count
    print("Count:", count)
    print("Average:", average)

#problema 4: Factorial with while
"""
Description:
Implement a simple password attempt system 
where you define a valid password in the code 
(for example, "admin123"). The user has a maximum 
number of attempts to enter the password. If they 
enter it correctly within the limit, display a success 
message; if they run out of attempts, display a locked 
message.

Inputs:
user_password: a string read on each attempt.

Outputs:
"Login success" if the password is correct.
"Account locked" if attempts are exhausted.

Validations:
Ensure that MAX_ATTEMPTS is greater than 0 (defined as a constant in the code, for example, 3).
Keep an accurate count of attempts.

Test Cases:
1) Input: "admin123" (on first attempt)
    Output:
    Login success
2) Input: "wrongpass", "admin123" (on second attempt)
    Output:
    Login success
3) Input: "wrong1", "wrong2", "wrong3" (all incorrect)
    Output:
    Account locked
"""
VALID_PASSWORD = "admin123"
MAX_ATTEMPTS = 3
if MAX_ATTEMPTS <= 0:
    print("Error: MAX_ATTEMPTS must be greater than 0.")
else:
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        user_password = input("Enter password: ")
        if user_password == VALID_PASSWORD:
            print("Login success")
            break
        attempts += 1
    else:
        print("Account locked")

# Problema 5: Simple menu with while
"""
Description:
Implement a text menu that loops until 
the user selects the exit option. The 
menu should offer several options, such 
as displaying a greeting, showing the 
current value of a counter, and incrementing 
the counter. The program should execute the 
action corresponding to each option and then 
repeat the menu until the exit option is selected.

Inputs:
option: An option selected by the user (can be an integer or string).

Outputs:
Messages based on the selected option, such as "Hello!" 
for a greeting or "Counter:" followed by the counter value.
A farewell message upon exiting and an error message for invalid options.

Validations:
Normalize option (for example, convert it to an integer with error handling).
Ensure that only options 0, 1, 2, and 3 are accepted as valid.

Test Cases:
1) Input: 1, 2, 3, 0
    Output:
    Hello!
    Counter: 0
    Counter incremented.
    Exiting program. Goodbye!
2) Input: 2, 2, 0
    Output:
    Counter: 0
    Counter: 0
    Exiting program. Goodbye!
3) Input: 5, 1, 0
    Output:
    Invalid option. Please try again.
    Hello!
    Exiting program. Goodbye!
"""
counter = 0
while True:
    print("\nMenu:")
    print("1. Greet")
    print("2. Show counter")
    print("3. Increment counter")
    print("0. Exit")
    option = input("Select an option: ")
    try:
        option = int(option)
        if option == 1:
            print("Hello!")
        elif option == 2:
            print("Counter:", counter)
        elif option == 3:
            counter += 1
            print("Counter incremented.")
        elif option == 0:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Invalid option. Please try again.")

#Problema 6: Pattern printing with nested loops
"""
Description:
Uses nested for loops to print a pattern of 
asterisks in the shape of a right triangle. 
For example, if n = 4, the program should print 
a triangle of asterisks with 4 rows. Optionally, 
you can implement a reversed pattern.

Inputs:
n: An integer representing the number of rows in the pattern.

Outputs:
Asterisk pattern, line by line.
(Optional) Reversed pattern if you choose to implement it.

Validations:
Verifies that n can be converted to an integer.
Ensures that n is greater than or equal to 1; otherwise, displays an error message.

Test Cases:
1) Input: n = 4
    Output:
    *
    **
    ***
    ****

2) Input: n = 5
    Output:
    *
    **
    ***
    ****
    *****

3) Input: n = 0
    Output:
    Error: n must be greater than or equal to 1.
"""

n = input("Enter the number of rows for the pattern: ")
try:
    n = int(n)
    if n < 1:
        print("Error: n must be greater than or equal to 1.")
    else:
        for i in range(1, n + 1):
            print('*' * i) 
        # Optional reversed pattern
        print("\nReversed pattern:")
        for i in range(n, 0, -1):
            print('*' * i)
except ValueError:
    print("Error: Please enter a valid integer.")

"""
Conclusion:
This project successfully demonstrates the 
use of loops in Pythonto solve various problems, 
including summation, multiplication tables,average 
calculation, password attempts, menu handling, 
and pattern printing.
"""
