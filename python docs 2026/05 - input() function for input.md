# 05 - input() Function for Input in Python

## What is input()?
`input()` is Python's built-in function for reading user input from the keyboard. It pauses program execution and waits for the user to type something and press Enter.

## Basic Syntax

```python
input()
input(prompt)
```

## Simple Examples

```python
# Basic input
input()

# With prompt message
input("Enter your name: ")

# Storing input in a variable
name = input("What is your name? ")
print(f"Hello, {name}!")
```

## How input() Works

```python
# Program pauses and waits for user input
print("Before input")
name = input("Enter something: ")  # Waits here
print("After input")
print(f"You entered: {name}")
```

## The prompt Parameter

```python
# Without prompt
name = input()  # Just waits, no message

# With string prompt
name = input("Enter your name: ")

# With formatted prompt
age = 25
prompt = f"User {age} years old, enter name: "
name = input(prompt)

# Multi-line prompt
name = input("""Please enter your full name:
First Last: """)
```

## input() Always Returns a String

```python
# input() ALWAYS returns a string
age = input("Enter your age: ")
print(type(age))  # <class 'str'>

# Even numbers come as strings
number = input("Enter a number: ")
print(number + 5)  # TypeError! Can't add str and int
```

## Converting Input Types

### Convert to Integer
```python
# Basic conversion
age = input("Enter your age: ")
age = int(age)  # Convert string to integer

# One-line conversion
age = int(input("Enter your age: "))

# With error handling
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError:
    print("Please enter a valid number!")
```

### Convert to Float
```python
# Convert to float
price = float(input("Enter price: "))
print(f"Price: ${price:.2f}")

# Calculate with float
radius = float(input("Enter circle radius: "))
area = 3.14159 * radius ** 2
print(f"Area: {area:.2f}")
```

### Convert to Boolean
```python
# String to boolean
response = input("Enter yes/no: ").lower()
is_yes = response == "yes"
print(f"You said yes: {is_yes}")

# Using bool() - careful!
value = bool(input("Enter something: "))  # Empty string = False, anything else = True
```

### Convert to List
```python
# Convert comma-separated input to list
items = input("Enter items separated by commas: ")
item_list = items.split(",")
print(item_list)

# Convert space-separated numbers to list of ints
numbers = input("Enter numbers: ")
num_list = [int(x) for x in numbers.split()]
print(num_list)
```

## Practical Examples

### Example 1: Simple Greeting
```python
# Get user's name and greet them
name = input("What is your name? ")
print(f"Hello, {name}! Nice to meet you!")

# Output:
# What is your name? Alice
# Hello, Alice! Nice to meet you!
```

### Example 2: Age Calculator
```python
from datetime import datetime

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_year = datetime.now().year
age = current_year - birth_year

print(f"Hello {name}, you are {age} years old!")
print(f"In 5 years, you'll be {age + 5}")

# Output:
# Enter your name: Bob
# Enter your birth year: 1990
# Hello Bob, you are 34 years old!
# In 5 years, you'll be 39
```

### Example 3: Simple Calculator
```python
# Get two numbers and perform operations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\n{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")

# Output:
# Enter first number: 10
# Enter second number: 3
# 
# 10.0 + 3.0 = 13.0
# 10.0 - 3.0 = 7.0
# 10.0 * 3.0 = 30.0
# 10.0 / 3.0 = 3.3333333333333335
```

### Example 4: Area Calculator
```python
# Calculate area of different shapes
print("Area Calculator")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = input("Choose shape (1-3): ")

if choice == "1":
    radius = float(input("Enter radius: "))
    area = 3.14159 * radius ** 2
    print(f"Circle area: {area:.2f}")
    
elif choice == "2":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    print(f"Rectangle area: {area:.2f}")
    
elif choice == "3":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print(f"Triangle area: {area:.2f}")
    
else:
    print("Invalid choice!")

# Output:
# Area Calculator
# 1. Circle
# 2. Rectangle
# 3. Triangle
# Choose shape (1-3): 1
# Enter radius: 5
# Circle area: 78.54
```

### Example 5: Login System
```python
# Simple username/password check
correct_username = "admin"
correct_password = "secret123"

username = input("Username: ")
password = input("Password: ")

if username == correct_username and password == correct_password:
    print("Login successful!")
    print(f"Welcome, {username}!")
else:
    print("Login failed!")
    print("Invalid username or password")

# Output:
# Username: admin
# Password: secret123
# Login successful!
# Welcome, admin!
```

### Example 6: Shopping List
```python
# Build a shopping list
shopping_list = []

print("Shopping List Creator")
print("Enter 'done' when finished")

while True:
    item = input("Add item: ")
    if item.lower() == "done":
        break
    if item:  # Don't add empty strings
        shopping_list.append(item)

print("\nYour Shopping List:")
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item}")

print(f"\nTotal items: {len(shopping_list)}")

# Output:
# Shopping List Creator
# Enter 'done' when finished
# Add item: apples
# Add item: milk
# Add item: bread
# Add item: done
# 
# Your Shopping List:
# 1. apples
# 2. milk
# 3. bread
# 
# Total items: 3
```

### Example 7: Number Guessing Game
```python
import random

# Generate random number
secret = random.randint(1, 100)
attempts = 0

print("Guess the number (1-100)!")

while True:
    guess = input("Your guess: ")
    
    # Check if input is valid
    if not guess.isdigit():
        print("Please enter a valid number!")
        continue
    
    guess = int(guess)
    attempts += 1
    
    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts!")
        break

# Output:
# Guess the number (1-100)!
# Your guess: 50
# Too low! Try again.
# Your guess: 75
# Too high! Try again.
# Your guess: 62
# Correct! You guessed it in 3 attempts!
```

## Input Validation

### Check if Input is Number
```python
# Using isdigit() for integers
age = input("Enter age: ")
if age.isdigit():
    age = int(age)
    print(f"Age: {age}")
else:
    print("Please enter a valid number!")

# Using try/except for floats
try:
    price = float(input("Enter price: "))
    print(f"Price: ${price:.2f}")
except ValueError:
    print("Invalid price!")
```

### Check if Input is Not Empty
```python
# Ensure input is not empty
name = input("Enter name: ")
while name == "":
    print("Name cannot be empty!")
    name = input("Enter name: ")

print(f"Hello, {name}!")
```

### Validate Range
```python
# Ensure number is within range
score = int(input("Enter score (0-100): "))
while score < 0 or score > 100:
    print("Score must be between 0 and 100!")
    score = int(input("Enter score (0-100): "))

print(f"Score: {score}")
```

### Validate Choice from Menu
```python
# Ensure user picks valid option
print("1. Start")
print("2. Load")
print("3. Exit")

choice = input("Choose option (1-3): ")
while choice not in ["1", "2", "3"]:
    print("Invalid choice!")
    choice = input("Choose option (1-3): ")

print(f"You chose option {choice}")
```

## Handling Multiple Inputs

### Space-Separated Input
```python
# Get multiple values in one line
data = input("Enter name age score: ").split()
name, age, score = data[0], int(data[1]), float(data[2])
print(f"Name: {name}, Age: {age}, Score: {score}")

# More elegant
name, age, score = input("Enter name age score: ").split()
age = int(age)
score = float(score)
```

### Comma-Separated Input
```python
# Get list of items
items = input("Enter items (comma-separated): ").split(",")
items = [item.strip() for item in items]  # Remove extra spaces
print(f"Items: {items}")
```

### Unknown Number of Inputs
```python
# Get variable number of numbers
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(x) for x in numbers]
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers)/len(numbers):.2f}")
```

## Stripping and Cleaning Input

### Remove Extra Spaces
```python
# strip() removes leading/trailing spaces
name = input("Enter name: ").strip()
print(f"'{name}'")

# lstrip() - remove left spaces
# rstrip() - remove right spaces
```

### Convert to Lowercase/Uppercase
```python
# Case-insensitive input
response = input("Continue? (yes/no): ").lower()
if response == "yes":
    print("Continuing...")

# Uppercase for commands
command = input("Enter command: ").upper()
if command == "QUIT":
    print("Exiting...")
```

### Remove Punctuation
```python
# Clean input for comparison
import string

user_input = input("Enter something: ")
clean_input = user_input.translate(str.maketrans('', '', string.punctuation))
print(f"Cleaned: {clean_input}")
```

## Advanced Input Techniques

### Password Input (Hidden)
```python
# Using getpass for hidden input
import getpass

username = input("Username: ")
password = getpass.getpass("Password: ")  # Characters not shown

print(f"Logging in {username}...")

# Output:
# Username: admin
# Password: ········
# Logging in admin...
```

### Timeout for Input
```python
# Input with timeout (Windows and Unix)
import sys

if sys.platform == 'win32':
    import msvcrt
    import time
    
    def input_timeout(prompt, timeout=5):
        print(prompt, end='', flush=True)
        start = time.time()
        result = ''
        while time.time() - start < timeout:
            if msvcrt.kbhit():
                result = input()
                return result
            time.sleep(0.1)
        print("\nTimeout!")
        return None
else:
    import select
    
    def input_timeout(prompt, timeout=5):
        print(prompt, end='', flush=True)
        ready, _, _ = select.select([sys.stdin], [], [], timeout)
        if ready:
            return sys.stdin.readline().rstrip('\n')
        print("\nTimeout!")
        return None

# Usage
response = input_timeout("Enter something (5 seconds): ", 5)
if response:
    print(f"You entered: {response}")
```

### Reading from Input with Default Value
```python
# Provide default value if user just presses Enter
def input_default(prompt, default=""):
    user_input = input(f"{prompt} [{default}]: ").strip()
    return user_input if user_input else default

name = input_default("Enter name", "Guest")
print(f"Hello, {name}!")

# Output if user presses Enter:
# Enter name [Guest]: 
# Hello, Guest!
```

## Common Mistakes

### Mistake 1: Forgetting to Convert Type
```python
# Wrong
age = input("Enter age: ")
next_age = age + 1  # TypeError: can only concatenate str to str

# Right
age = int(input("Enter age: "))
next_age = age + 1
```

### Mistake 2: Not Handling Empty Input
```python
# Wrong - empty string causes issues
name = input("Enter name: ")
print(f"Hello, {name[0]}")  # IndexError if empty

# Right
name = input("Enter name: ")
if name:
    print(f"Hello, {name[0]}")
else:
    print("No name entered")
```

### Mistake 3: Assuming input() Returns Numbers
```python
# Wrong
num1 = input("Enter number: ")
num2 = input("Enter number: ")
print(num1 + num2)  # Concatenates strings, not addition

# Right
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
print(num1 + num2)  # Actual addition
```

### Mistake 4: Not Using strip()
```python
# Wrong - extra spaces cause issues
color = input("Favorite color: ")
if color == "blue":  # Fails if user typed "blue " with space
    print("Good choice!")

# Right
color = input("Favorite color: ").strip().lower()
if color == "blue":
    print("Good choice!")
```

### Mistake 5: Not Validating Numeric Input
```python
# Wrong - crashes if input not numeric
age = int(input("Age: "))  # ValueError if user types "twenty"

# Right
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a valid number!")
```

## Best Practices

### ✅ Do This
```python
# Always convert types explicitly
age = int(input("Enter age: "))

# Strip whitespace
name = input("Enter name: ").strip()

# Validate input
while True:
    try:
        age = int(input("Enter age: "))
        if age > 0:
            break
        print("Age must be positive")
    except ValueError:
        print("Please enter a number!")

# Use descriptive prompts
password = input("Enter password (min 8 chars): ")

# Handle empty input
text = input("Enter message: ")
if not text:
    text = "Default message"

# Case-insensitive comparisons
response = input("Continue? ").lower()
if response in ['yes', 'y']:
    print("Continuing...")
```

### ❌ Avoid This
```python
# Avoid - no prompt (user confused)
data = input()

# Avoid - no type conversion
age = input("Age: ")
if age > 18:  # TypeError!

# Avoid - trusting user input
command = input("Command: ")
eval(command)  # Dangerous!

# Avoid - no validation
file = input("Filename: ")
open(file)  # Could crash

# Avoid - raw input without cleaning
query = input("Search: ")
# User might enter special characters
```

## input() vs sys.stdin

```python
import sys

# Basic input() - reads one line
name = input("Name: ")

# sys.stdin.read() - reads until EOF
data = sys.stdin.read()

# sys.stdin.readline() - reads one line (includes newline)
line = sys.stdin.readline()

# Reading multiple lines
lines = sys.stdin.readlines()

# Performance comparison
import time

# Slower for many inputs
start = time.time()
for i in range(1000):
    data = input()
print(f"input(): {time.time() - start:.4f}s")

# Faster for many inputs
start = time.time()
for i in range(1000):
    data = sys.stdin.readline()
print(f"sys.stdin.readline(): {time.time() - start:.4f}s")
```

## Quick Reference Table

| Feature | Syntax | Example |
|---------|--------|---------|
| Basic input | `input()` | `input()` |
| With prompt | `input("msg")` | `input("Name: ")` |
| To integer | `int(input())` | `int(input("Age: "))` |
| To float | `float(input())` | `float(input("Price: "))` |
| Strip spaces | `input().strip()` | `name = input().strip()` |
| Lowercase | `input().lower()` | `input().lower()` |
| Split input | `input().split()` | `input().split(",")` |
| Hidden input | `getpass.getpass()` | `getpass.getpass("PW: ")` |
| Default value | Custom function | See example above |

## Summary

- **input()** reads user input as a **string**
- Always **convert types** explicitly (int, float, etc.)
- Use **strip()** to remove extra spaces
- **Validate input** to prevent crashes
- Use **try/except** for safe number conversion
- **getpass** module for hidden password input
- Empty input returns empty string `""`
- Use **split()** to parse multiple values
- **Lowercase/uppercase** for case-insensitive comparison
- Provide **clear prompts** so users know what to enter

## Basic Template
```python
#!/usr/bin/env python3

# Basic input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Numeric input with validation
while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0:
            break
        print("Age must be positive")
    except ValueError:T
        print("Please enter a valid number!")

# Multiple inputs
data = input("Enter name and age: ").split()
if len(data) == 2:
    name, age = data[0], int(data[1])
    print(f"{name} is {age} years old")

# Menu choice with validation
print("\n1. Start")
print("2. Load")
print("3. Exit")

choice = input("Choose: ").strip()
while choice not in ["1", "2", "3"]:
    choice = input("Invalid. Choose 1-3: ")

print(f"You chose option {choice}")

# Case-insensitive yes/no
confirm = input("Continue? (yes/no): ").lower()
if confirm in ['yes', 'y']:
    print("Continuing...")
else:
    print("Exiting...")
```

*This documentation belongs to https://github.com/InterCentury*