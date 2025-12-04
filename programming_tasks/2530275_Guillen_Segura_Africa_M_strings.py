"""
Universidad politécnica de Victoria
Materia: Metodología de la Programación
Grupo: IM-03
Alumno: Guillen Segura Africa Citlali 
Matrícula: 2530275
Proyecto: Manejo de strings en Python
Fecha: 3 de diciembre del 2025
Profesor: Carlos Antonio Tovar García
"""

# Problem 1: Full name formatter
"""
Descripción:
The program takes a full name and normalizes it, 
removing extra spaces and adjusting the capitalization. 
Then, it displays the name in "Title Case" format along 
with the initials of the name.

Inputs:
- full_name: string

Outputs:
- initials: string

Validations:
- The input cannot be empty.
- The input must contain at least two words.

Test cases:
1) Normal: "Africa Citlali Guillen Segura" -> Formatted name: Juan Carlos Tovar | Initials: A.C.G.S.
2) Border: "  lia garcia " -> Ana Perez | L.G.    
3) Error: "   " -> Error: invalid input

"""

full_name =input("Enter ful name ").strip()
print(full_name.title())

if len(full_name) <2 or "":
    print("ERROR: That's not a valid name.")
else:
    initials = ".".join([word[0].upper() for word in full_name.split()]) + "."
    print(initials)


# Problem 2: Simple email validator
"""
Descripción:
This program validates whether an 
email address has a correct basic format.
Make sure it contains exactly one '@' 
and that there is at least one '.' after it.

Inputs:
- email_text: string

Outputs:
- Valid email: true/false
- Domain: <...> (if valid)

Validations:
- The email cannot be empty.
- Must have exactly one '@'.
- No spaces allowed.

Test cases:
1) Normal: "africa@gmail.com" -> Valid email: true 
2) Border: "africa@gmail -> Valid email: false
3) Error: "africa at gmail.com" -> Invalid email format.

"""
email = input("Enter your email address: ").strip()
if email == "" or email.count("@") != 1 or " " in email:
    print("Invalid email format.")
else:
    local_part, domain_part = email.split("@")
    if "." in domain_part:
        print("Valid email.")
        print(f"Domain: {domain_part}")
    else:
        print("Invalid email format.") 


#Problem 3 Palindrome checker (ignoring spaces and case)

"""
Descripción:
This program checks if a given phrase is a palindrome,
ignoring spaces and case sensitivity.

Inputs:
- frase: string

Outputs:
- Palindrome: true/false

Validations:
- The input cannot be empty.

Test cases:
1) Normal: "A man a plan a canal Panama" -> Palindrome: true
2) Border: "racecar" -> Palindrome: true
3) Error: "" -> Error: input cannot be empty.
"""

frase = input("Enter your frase".lower())
frase = frase.replace(" ", "")
if frase == frase[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")


# Problem 4: Sentence word stats (lengths and first/last word)
"""
Descripción:
This program analyzes a 
sentence to provide statistics
about the words it contains, 
including the total number of words,
the length of each word, and the f
irst and last words in the sentence.

Inputs:
- sentence: string

Outputs:
- Total words: int
- Word lengths: list of int
- First word: string
- Last word: string

Validations:
- The input cannot be empty.

Test cases:
1) Normal: "Hello world from Python" -> Total words: 4, Word lengths: [5, 5, 4, 6], First word: "Hello", Last word: "Python"
2) Border: "Single" -> Total words: 1, Word lengths: [6], First word: "Single", Last word: "Single"
3) Error: "" -> Error: input cannot be empty.
"""

sentence = input("Enter a sentence: ").strip()
if sentence == "":  
    print("Error: Input cannot be empty.")
else:
    words = sentence.split()
    total_words = len(words)
    word_lengths = [len(word) for word in words]
    first_word = words[0]
    last_word = words[-1]

    print(f"Total words: {total_words}")
    print(f"Word lengths: {word_lengths}")
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")



# Problem 5: Password strength classifier
"""
Descripción:
This program classifies the strength of a password
based on its length and character composition.

Inputs:
- password: string

Outputs:
- Strength: "Weak", "Moderate", "Strong"

Validations:
- The input cannot be empty.

Test cases:
1) Normal: "P@ssw0rd" -> Strength: Strong
2) Border: "pass" -> Strength: Weak
3) Error: "" -> Error: input cannot be empty.
"""
password = input("Enter your password: ").strip()
if password == "":
    print("Error: Password cannot be empty.")
else:
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    if length < 6:
        strength = "Weak"
    elif length >= 6 and (has_upper + has_lower + has_digit + has_special) >= 2:
        strength = "Moderate"
    elif length >= 8 and (has_upper + has_lower + has_digit + has_special) >= 3:
        strength = "Strong"
    else:
        strength = "Weak"

    print(f"Password strength: {strength}")

# Problem 6: Product label formatter (fixed-width text)
"""
Descripción:
This program formats product labels
with fixed-width fields for name, price, and quantity.

Inputs:
- product_name: string
- price: float
- quantity: int

Outputs:
- Formatted label: string

Validations:
- The product name cannot be empty.
- Price and quantity must be non-negative.

Test cases:
1) Normal: "Widget", 19.99, 5 -> Formatted label: "Product: Widget | Price: $19.99 | Quantity: 5   "
2) Border: "Gadget", 0.0, 0 -> Formatted label: "Product: Gadget   | Price: $0.00  | Quantity: 0   "
3) Error: "", -5.0, -1 -> Error: invalid input
"""
product_name = input("Enter product name: ").strip()
try:
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    if product_name == "" or price < 0 or quantity < 0:
        print("Error: Invalid input.")
    else:
        formatted_label = f"Product: {product_name:<15} | Price: ${price:<7.2f} | Quantity: {quantity:<5}"
        print(formatted_label)
except ValueError:
    print("Error: Invalid input.")  

# Conclusion
"""
When using strings, it is important 
to use the following methods (strip,rtrip,lstrip) 
as they help prevent spaces from 
being marked as errors or extra characters.


It is also important to use the following methods 
(upper, lower, title, capitalize)
depending on what the code asks for, as they can 
convert everything to uppercase, lowercase, the 
first letters of the paragraph to uppercase, etc.
"""