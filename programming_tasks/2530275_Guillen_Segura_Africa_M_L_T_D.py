"""
Universidad Politécnica de Victoria
Materia: Metodología de la Programación
Grupo: IM-03
Alumno: Guillen Segura Africa Citlali
Matrícula: 2530275
Proyecto: Manejo de Listas, Tuplas y Diccionarios en Python
Fecha: 3 de diciembre del 2025
Profesor: Carlos Antonio Tovar García
"""

# Problem 1: Shopping list basics
""""
Descripción:
This problem focuses on managing a list of products 
and their quantities. You must create an initial list 
of products, allow the user to add a new product at 
the end, display the total number of items, and 
check if a specific product is present.

Inputs:
- initial_products: list of tuples (product_name: str, quantity: int)
- new_product: str
- new_quantity: int

Outputs:
- updated_products: list of tuples (product_name: str, quantity: int)
- total_items: int
- product_check: bool

Validations:
- The product name must be a non-empty string.
- The quantity must be a positive integer.
- The output list must reflect the newly added product.

Test cases:
1) Normal: Add "Grapes", 6 -> List updated, total items increased
2) Border: Add "", 0 -> Error: Invalid product name or quantity
3) Error: Check for a product not in the list -> Returns not found
"""

initial_products = [("Apples", 5), ("Bananas", 3), ("Oranges", 4)]
print("Initial product list:")
for product, quantity in initial_products:
    print(f"- {product}: {quantity}")
new_product = input("Enter a new product to add: ")
new_quantity = int(input(f"Enter quantity for {new_product}: "))
initial_products.append((new_product, new_quantity))
print("\nUpdated product list:")
for product, quantity in initial_products:
    print(f"- {product}: {quantity}")
print(f"\nTotal number of items: {len(initial_products)}")
check_product = input("Enter a product to check if it's in the list: ")
if any(product == check_product for product, _ in initial_products):
    print(f"{check_product} is in the list.")
else:
    print(f"{check_product} is not in the list.")

# Problem 2: Points and distances with tuples
""""
Descripción:
In this problem, you will use tuples to represent 
two points in a 2D plane. You must create two 
tuples with the coordinates of the points, 
calculate the Euclidean distance between them, 
and determine the midpoint.

Inputs:
- x1: float
- y1: float
- x2: float
- y2: float

Outputs:
- point1: tuple (x1, y1)
- point2: tuple (x2, y2)
- distance: float
- midpoint: tuple (mid_x, mid_y)

Validations:
- The coordinates must be valid floating-point numbers.

Test cases:
1) Normal: (1,2), (4,6) -> Distance: 5.00, Midpoint: (2.5,4.0)
2) Border: (0,0), (0,0) -> Distance: 0.00, Midpoint: (0.0,0.0)
3) Error: ("a",2), (4,6) -> Error: Invalid input
"""
x1 = float(input("Enter x-coordinate of point 1: "))
y1 = float(input("Enter y-coordinate of point 1: "))
x2 = float(input("Enter x-coordinate of point 2: "))
y2 = float(input("Enter y-coordinate of point 2: "))
point1 = (x1, y1)
point2 = (x2, y2)
print(f"Point 1: {point1}")
print(f"Point 2: {point2}") 
import math
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
print(f"Distance between points: {distance:.2f}")
print(f"Midpoint: {midpoint}")

# Problem 3:  Product catalog with dictionary
"""
Descripción:
This problem involves managing a product catalog 
using a dictionary. The key will be the product 
name, and the value will be its unit price. You 
must allow the user to enter a product and quantity, 
then calculate the total amount due if the product exists.

Inputs:
- product_name: str
- quantity: int

Outputs: 
- total_amount: float
- error_message: str (if product not found)

Validations:
- The product name must exist in the catalog.
- The quantity must be a positive integer.
- the quantity must be greater than zero.

Test cases:
1) Normal: "Laptop", 2 -> Total amount: $1600.00
2) Border: "Smartphone", 0 -> Error: Invalid quantity
3) Error: "Camera", 1 -> Error: Product not found
"""
product_catalog = {
    "Laptop": 800.0,
    "Smartphone": 500.0,
    "Tablet": 300.0,
    "Headphones": 150.0
}
try:
    product_name = input("Enter the product name: ")
    quantity = int(input("Enter the quantity: "))
    if product_name in product_catalog:
        unit_price = product_catalog[product_name]
        total_amount = unit_price * quantity
        print(f"Total amount due for {quantity} {product_name}(s): ${total_amount:.2f}")
    if quantity <= 0:
        print("Error: Invalid quantity.")
    elif product_name not in product_catalog:
        print("Error: Product not found.")
except ValueError:
    print("Error: Invalid input.")    


# Problem 4: Student grades with dict and list
"""
Descripción:
Manage the grades of a group of students 
using a dictionary where the key is the 
student's name and the value is a list of 
their grades. You must calculate the grade
point average and determine if the student 
has passed.

Inputs:
-student_name: the name of the student
-grades: list of floats

Outputs:
-Student grade list.
-Grade average.
-Pass/Fail status.

Validations:
-Verify that `student_name` is not empty and that 
it exists in the dictionary.
-Make sure the grade list is not empty before 
calculating the average.

Test cases:
1) Normal: "Alice", [85.0, 90.0, 78.0] -> Average: 84.33, Status: Pass
2) Border: "Bob", [60.0, 59.0, 61.0] -> Average: 60.00, Status: Pass
3) Error: "Charlie", [] -> Error: No grades available
"""

student_grades = {
    "Alice": [85.0, 90.0, 78.0],
    "Bob": [60.0, 59.0, 61.0],
    "Charlie": []
}
student_name = input("Enter the student's name: ")
if student_name in student_grades:
    grades = student_grades[student_name]
    if grades:
        average = sum(grades) / len(grades)
        status = "Pass" if average >= 60 else "Fail"
        print(f"{student_name}'s grades: {grades}")
        print(f"Average: {average:.2f}")
        print(f"Status: {status}")
    else:
        print("Error: No grades available.")
else:
    print("Error: Student not found.")

# Problem 5: Word frequency counter
"""
Descripción:
This problem involves counting the frequency of 
each word in a sentence. You must convert the 
sentence to lowercase, separate it into individual 
words, and build a dictionary containing each word 
and its frequency.

Inputs:
-sentence: la oración a analizar.

Outputs:
-Word list.
-Frequency dictionary.
-The most common word.

Validations:
-Make sure the sentence is not empty and use 
punctuation marks if you choose to do so.

Test cases:
1) Normal: "This is a test. This test is only a test."
2) Border: "" -> Error: Empty sentence
3) Error: "Hello, hello! HELLO?" -> Frequency count should be case insensitive
"""
import string
sentence = input("Enter a sentence: ")
if not sentence:
    print("Error: Empty sentence.")
else:
    sentence = sentence.lower()
    translator = str.maketrans('', '', string.punctuation)
    sentence = sentence.translate(translator)
    words = sentence.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    print("Word list:", words)
    print("Frequency dictionary:", frequency)
    most_common_word = max(frequency, key=frequency.get)
    print(f"The most common word is '{most_common_word}' with a frequency of {frequency[most_common_word]}.")

# Problem 6:  Simple contact book
"""
Descripción:
Implement a contact book using a dictionary 
where the key is the contact name and the value 
is their phone number. You must allow the user 
to add, search, or delete contacts depending on 
the selected action.

Inputs:
-action_text: The action to perform ("ADD", "SEARCH", or "DELETE").
-name: The contact's name (depending on the action).
-phone: The phone number (only for the "ADD" action).

Outputs:
-Success or error message depending on the action performed.

Validations:
-Normalize the action_text to uppercase and verify that it's a valid option.
-Make sure that name and phone are not empty, but only for "ADD".

Test cases:
1) Normal: ADD "John", "1234567890" -> Contact added successfully
2) Border: SEARCH "Jane" -> Error: Contact not found
3) Error: DELETE "" -> Error: Invalid contact name
"""
contact_book = {}
action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()
if action_text == "ADD":
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    if name and phone:
        contact_book[name] = phone
        print(f"Contact {name} added successfully.")
    else:
        print("Error: Invalid contact name or phone number.")
elif action_text == "SEARCH":
    name = input("Enter contact name to search: ").strip()
    if name in contact_book:
        print(f"{name}'s phone number is {contact_book[name]}.")
    else:
        print("Error: Contact not found.")
elif action_text == "DELETE":
    name = input("Enter contact name to delete: ").strip()
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Error: Contact not found.")
else:
    print("Error: Invalid action.")


"""
Conclusión:
In this project, I have successfully implemented
various tasks involving lists, tuples, and
dictionaries in Python. Each problem presented
unique challenges that required careful consideration
and validation of inputs. Through this experience,
I have enhanced my understanding of data structures
and their practical applications in programming.
"""
