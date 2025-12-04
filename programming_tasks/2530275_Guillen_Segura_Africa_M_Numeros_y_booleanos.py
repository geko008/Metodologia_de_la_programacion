"""
Universidad politécnica de Victoria
Materia: Metodología de la Programación
Grupo: IM-03
Alumno: Guillen Segura Africa Citlali 
Matrícula: 2530275
Proyecto: Manejo de números y booleanos en Python
Fecha: 3 de diciembre del 2025
Profesor: Carlos Antonio Tovar García
"""
# Problem 1: : Temperature Converter and Range Flag

"""
Descripción:
This program converts a given temperature in degrees Celsius 
to Fahrenheit and Kelvin. It also determines if the temperature 
is high (30°C or higher) and returns a Boolean value.

Inputs:
- temperature: float (in degrees Celsius)

Outputs:
- temperature_fahrenheit: float (converted to Fahrenheit)
- temperature_kelvin: float (converted to Kelvin)
- is_high: bool (true if temperature >= 30°C, false otherwise)
- range_flag: str (indicating if the temperature is high or low)

Validations:
- The input must be a valid number.
- The input must be a number between -273.15 and 1000.
- The output must be formatted to two decimal places.
- The range flag must be "High" or "Low".

Test cases:
1) Normal: 25.0 -> 77.00°F, 298.15K, False, Low
2) Border: 30.0 -> 86.00°F, 303.15K, True, High
3) Error: -300.0 -> Error: Invalid temperature
"""
temperature = input("Enter temperature in Celsius: ")
try:
    temperature = float(temperature)
    if temperature < -273.15 or temperature > 1000:
        raise ValueError("Invalid temperature")
    
    temperature_fahrenheit = (temperature * 9/5) + 32
    temperature_kelvin = temperature + 273.15
    is_high = temperature >= 30
    range_flag = "High" if is_high else "Low"
    
    print(f"Temperature in Fahrenheit: {temperature_fahrenheit:.2f}°F")
    print(f"Temperature in Kelvin: {temperature_kelvin:.2f}K")
    print(f"Is high temperature: {is_high}")
    print(f"Range flag: {range_flag}")
except ValueError as e:
    print(f"Error: {e}")

# Problem 2: Work Hours and Overtime Payment
""""
Descripción:
This program calculates an employee's total weekly pay. 
The first 40 hours are paid at the regular rate, and 
overtime is paid at 150%. It also indicates whether the 
employee worked overtime.

Inputs:
- hours_worked: float (total hours worked in a week)
- hourly_rate: float (regular hourly wage)

Outputs:
- total_pay: float (total weekly pay)
- worked_overtime: bool (true if hours_worked > 40, false otherwise)
- overtime_hours: float (number of overtime hours worked)
- overtime_pay: float (total pay for overtime hours)

Validations:
- The hours worked must be a non-negative number.
- The hourly rate must be a non-negative number.

Test cases:
1) Normal: 45, 20.0 -> Total pay: $950.00
2) Border: 40, 15.0 -> Total pay: $600.00
3) Error: -5, 20.0 -> Error: Invalid input
"""

hours_worked = input("Enter hours worked in a week: ")
hourly_rate = input("Enter hourly rate: ")
try:
    hours_worked = float(hours_worked)
    hourly_rate = float(hourly_rate)

    if hours_worked < 0 or hourly_rate < 0:
        raise ValueError("Invalid input")

    if hours_worked <= 40:
        total_pay = hours_worked * hourly_rate
        worked_overtime = False
        overtime_hours = 0
        overtime_pay = 0
    else:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = (40 * hourly_rate) + overtime_pay
        worked_overtime = True

    print(f"Total pay: ${total_pay:.2f}")
    print(f"Worked overtime: {worked_overtime}")
    print(f"Overtime hours: {overtime_hours}")
    print(f"Overtime pay: ${overtime_pay:.2f}")
except ValueError as e:
    print(f"Error: {e}")

# Problem 3: Discount Eligibility with Booleans
"""
Descripción:
This program determines if a customer is eligible for 
a discount based on their student or senior status, 
or if their total purchase is equal to or greater 
than 1000. It also calculates the total to pay with 
a 10% discount if eligible.

Inputs:
- is_student: bool (true if the customer is a student)
- is_senior: bool (true if the customer is a senior)
- total_purchase: float (total purchase amount)

Outputs:
- eligible_for_discount: bool (true if eligible for discount)
- total_to_pay: float (total after discount if eligible)

Validations:
- The total purchase must be a non-negative number.

Test cases:
1) Normal: True, False, 1200.0 -> Eligible for discount: True
2) Border: False, True, 1000.0 -> Eligible for discount: True
3) Error: False, False, -100.0 -> Error: Invalid total purchase

"""

total_payment = input("Enter total purchase amount: ")
is_student = input("Are you a student? (yes/no): ").strip().lower()
is_senior = input("Are you a senior? (yes/no): ").strip().lower()
try:
    total_purchase = float(total_payment)
    if total_purchase < 0:
        raise ValueError("Invalid total purchase")

    is_student = is_student == 'yes'
    is_senior = is_senior == 'yes'

    eligible_for_discount = is_student or is_senior or total_purchase >= 1000
    if eligible_for_discount:
        total_to_pay = total_purchase * 0.9
    else:
        total_to_pay = total_purchase

    print(f"Eligible for discount: {eligible_for_discount}")
    print(f"Total to pay: ${total_to_pay:.2f}")
except ValueError as e:
    print(f"Error: {e}")

# Problem 4: Basic Statistics of Three Integers 
"""
Descripción:
This program reads three integers and calculates 
the sum, average, maximum value, minimum value, 
and determines if all the numbers are even.

Inputs:
- num1: int
- num2: int
- num3: int

Outputs:
- sum: int
- average: float
- max_value: int
- min_value: int
- all_even: bool

Validations:
- The inputs must be valid integers.

Test cases:
1) Normal: 4, 8, 12 -> Sum: 24, Average: 8.00, Max: 12, Min: 4, All even: True
2) Border: 1, 2, 3 -> Sum: 6, Average: 2.00, Max: 3, Min: 1, All even: False
3) Error: 4, "a", 6 -> Error: Invalid input
"""
try:
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))
    num3 = int(input("Enter third integer: "))

    total_sum = num1 + num2 + num3
    average = total_sum / 3
    max_value = max(num1, num2, num3)
    min_value = min(num1, num2, num3)
    all_even = (num1 % 2 == 0) and (num2 % 2 == 0) and (num3 % 2 == 0)

    print(f"Sum: {total_sum}")
    print(f"Average: {average:.2f}")
    print(f"Max value: {max_value}")
    print(f"Min value: {min_value}")
    print(f"All even: {all_even}")
except ValueError:
    print("Error: Invalid input.")
    
# Problem 5: Loan Eligibility (Income and Debt Ratio)
"""
Descripción:
This program determines if a person is eligible for a 
loan based on their monthly income, monthly debt, and 
credit score. It calculates the debt-to-income ratio.

Inputs:
- monthly_income: float
- monthly_debt: float
- credit_score: int

Outputs:
- eligible_for_loan: bool
- debt_to_income_ratio: float
- reason: str (if not eligible)

Validations:
- Monthly income and debt must be non-negative.
- Credit score must be between 300 and 850.

Test cases:
1) Normal: 5000.0, 1500.0, 700 -> Eligible for loan: True
2) Border: 4000.0, 2000.0, 600 -> Eligible for loan: False
3) Error: -3000.0, 1000.0, 750 -> Error: Invalid input
"""

try:
    monthly_income = float(input("Enter monthly income: "))
    monthly_debt = float(input("Enter monthly debt: "))
    credit_score = int(input("Enter credit score: "))

    if monthly_income < 0 or monthly_debt < 0 or not (300 <= credit_score <= 850):
        raise ValueError("Invalid input")

    debt_to_income_ratio = monthly_debt / monthly_income if monthly_income > 0 else 0
    eligible_for_loan = debt_to_income_ratio < 0.4 and credit_score >= 650

    if eligible_for_loan:
        reason = ""
    else:
        reason = "High debt-to-income ratio" if debt_to_income_ratio >= 0.4 else "Low credit score"

    print(f"Eligible for loan: {eligible_for_loan}")
    print(f"Debt-to-income ratio: {debt_to_income_ratio:.2f}")
    if reason:
        print(f"Reason: {reason}")
except ValueError as e:
    print(f"Error: {e}")

# Problem 6: Body Mass Index (BMI) and Category Flag
"""
Descripción:
This program calculates a person's body 
mass index (BMI) and determines if they are 
underweight, at a normal weight, or overweight.

Inputs:
- weight: float (in kilograms)
- height: float (in meters)
Outputs:
- bmi: float
- category: str (Underweight, Normal weight, Overweight)
Validations:
- Weight and height must be positive numbers.
Test cases:
1) Normal: 70.0, 1.75 -> BMI: 22.86, Category: Normal weight
2) Border: 50.0, 1.60 -> BMI: 19.53, Category: Normal weight
3) Error: 0.0, 1.80 -> Error: Invalid input
"""
try:
    weight = float(input("Enter weight in kilograms: "))
    height = float(input("Enter height in meters: "))

    if weight <= 0 or height <= 0:
        raise ValueError("Invalid input")

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    else:
        category = "Overweight"

    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")
except ValueError as e:
    print(f"Error: {e}")

"""
conclusion:
This project demonstrates the effective use of 
numbers and boolean logic in Python to solve 
real-world problems. Each program includes input 
validation, calculations, and conditional logic to
provide accurate outputs based on user inputs. 
The test cases ensure that the programs handle
normal, border, and error scenarios appropriately, 
showcasing robust programming practices.
"""    