
"""
Universidad Politécnica de Victoria
Materia: Metodología de la Programación
Grupo: IM-03
Alumno: Guillen Segura Africa Citlali
Matrícula: 2530275
Proyecto: Manejo de funciones en Python 
Fecha: 5 de diciembre del 2025
Profesor: Carlos Antonio Tovar García
"""



# PROBLEM 1: Rectangle area and perimeter

"""
Description:
Compute the area and perimeter of a rectangle using two functions.

Inputs:
- width (float), height (float)

Outputs:
- Area
- Perimeter

Validations:
- width > 0
- height > 0

Test cases:
1) Normal: width=5, height=3 → area=15, perimeter=16
2) Border: width=0.1, height=0.1
3) Error: width=-2, height=4
"""

def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

# Main test execution
width = 5
height = 3
if width > 0 and height > 0:
    print("Area:", calculate_area(width, height))
    print("Perimeter:", calculate_perimeter(width, height))
else:
    print("Error: invalid input")


# PROBLEM 2: Grade classifier

"""
Description:
Classify a numeric grade into A–F.

Inputs:
- score (0–100)

Outputs:
- Category letter

Validations:
- 0 <= score <= 100

Test cases:
1) Normal: score=85 → "B"
2) Border: score=90 → "A"
3) Error: score=150 → error
"""

def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score = 85
if 0 <= score <= 100:
    print("Score:", score)
    print("Category:", classify_grade(score))
else:
    print("Error: invalid input")



# PROBLEM 3: List statistics (min, max, average)

"""
Description:
Return statistics (min, max, average) from a list.

Inputs:
- numbers_list

Outputs:
- min, max, average

Validations:
- list not empty
- all numeric

Test cases:
1) Normal: [10,20,30]
2) Border: [5]
3) Error: ["a",3,4]
"""

def summarize_numbers(numbers_list):
    stats = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return stats

numbers_text = "10,20,30"
try:
    numbers_list = [float(x) for x in numbers_text.split(",")]

    if len(numbers_list) == 0:
        print("Error: invalid input")
    else:
        result = summarize_numbers(numbers_list)
        print("Min:", result["min"])
        print("Max:", result["max"])
        print("Average:", result["average"])
except:
    print("Error: invalid input")



# PROBLEM 4: Apply discount list (pure function)

"""
Description:
Apply a discount to a list of prices and return a new list.

Inputs:
- prices_list
- discount_rate (0–1)

Outputs:
- original prices
- discounted prices

Validations:
- prices_list not empty
- each price > 0
- discount_rate between 0 and 1

Test cases:
1) Normal: [100,200,300], rate=0.1
2) Border: [1], rate=0
3) Error: [-20,30]
"""

def apply_discount(prices_list, discount_rate):
    return [price * (1 - discount_rate) for price in prices_list]

prices_text = "100,200,300"
discount_rate = 0.10

try:
    prices_list = [float(x) for x in prices_text.split(",")]

    if len(prices_list) == 0 or any(p <= 0 for p in prices_list) or not (0 <= discount_rate <= 1):
        print("Error: invalid input")
    else:
        discounted = apply_discount(prices_list, discount_rate)
        print("Original prices:", prices_list)
        print("Discounted prices:", discounted)
except:
    print("Error: invalid input")



# PROBLEM 5: Greeting function with default parameter

"""
Description:
Create a greeting message using optional title.

Inputs:
- name
- title (optional)

Outputs:
- greeting message

Validations:
- name not empty

Test cases:
1) Normal: name="Alice", title="Dr."
2) Border: name="Bob", title=""
3) Error: name=""
"""

def greet(name, title=""):
    full_name = (title.strip() + " " + name.strip()).strip()
    return f"Hello, {full_name}!"

name = "Alice"
title = "Dr."
if name.strip() != "":
    print("Greeting:", greet(name, title))
else:
    print("Error: invalid input")


# PROBLEM 6: Factorial function (iterative)

"""
Description:
Return n! using an iterative loop.

Inputs:
- n (int >= 0)

Outputs:
- factorial value

Validations:
- n integer
- n >= 0
- optional max: n <= 20

Test cases:
1) Normal: n=5 → 120
2) Border: n=0 → 1
3) Error: n=-3
"""

def factorial(n):
    """Iterative factorial implementation."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = 5
if isinstance(n, int) and n >= 0 and n <= 20:
    print("n:", n)
    print("Factorial:", factorial(n))
else:
    print("Error: invalid input")