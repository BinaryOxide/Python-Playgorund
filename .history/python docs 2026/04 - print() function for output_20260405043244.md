Here's the Python documentation for the `print()` function, following the same style as your previous docs:

# 04 - print() Function for Output in Python

## What is print()?
`print()` is Python's built-in function for displaying output to the console. It's the most commonly used function for showing results, debugging, and communicating with users.

## Basic Syntax

```python
print("Hello, World!")
print(42)
print(3.14159)
print(True)
```

## Simple Examples

```python
# Basic output
print("Python is awesome!")
print(100)
print(3.14)

# Multiple items
print("Hello", "World", "from", "Python")

# Numbers and text together
age = 25
print("I am", age, "years old")
```

## The print() Function Parameters

```python
print(value1, value2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```

| Parameter | Description | Default Value |
|-----------|-------------|---------------|
| `*objects` | Values to print (can be multiple) | Required |
| `sep` | Separator between values | `' '` (space) |
| `end` | What to print at the end | `'\n'` (newline) |
| `file` | Output stream | `sys.stdout` (console) |
| `flush` | Force flush buffer | `False` |

## Printing Different Data Types

### Strings
```python
print("Hello Python")
print('Single quotes work too')
print("""Multi-line
string
here""")
```

### Numbers
```python
print(42)           # Integer
print(3.14159)      # Float
print(1_000_000)    # Underscores for readability
print(0b1010)       # Binary (prints 10)
print(0xFF)         # Hexadecimal (prints 255)
```

### Booleans
```python
print(True)   # Prints: True
print(False)  # Prints: False
print(10 > 5) # Prints: True
```

### Collections
```python
# Lists
print([1, 2, 3, 4, 5])

# Tuples
print((1, 2, 3))

# Dictionaries
print({"name": "Alice", "age": 30})

# Sets
print({1, 2, 3, 4, 5})
```

### Variables
```python
name = "Bob"
age = 25
score = 95.5

print(name)
print(age)
print(score)
```

## The sep Parameter (Separator)

### Default Behavior (space)
```python
print("Apple", "Banana", "Cherry")
# Output: Apple Banana Cherry
```

### Custom Separators
```python
# No separator
print("Apple", "Banana", "Cherry", sep="")
# Output: AppleBananaCherry

# Comma and space
print("Apple", "Banana", "Cherry", sep=", ")
# Output: Apple, Banana, Cherry

# Hyphen
print("Apple", "Banana", "Cherry", sep="-")
# Output: Apple-Banana-Cherry

# Custom string
print("Apple", "Banana", "Cherry", sep=" 🍎 ")
# Output: Apple 🍎 Banana 🍎 Cherry

# Newline separator
print("Line1", "Line2", "Line3", sep="\n")
# Output:
# Line1
# Line2
# Line3
```

### Practical sep Examples
```python
# CSV format
print("Name", "Age", "City", sep=",")
# Output: Name,Age,City

# Path format
print("Users", "Documents", "file.txt", sep="/")
# Output: Users/Documents/file.txt

# Date format
print(2024, 12, 25, sep="-")
# Output: 2024-12-25

# Visual separator
print("=" * 30, sep="")
print("Header", "Content", "Footer", sep=" | ")
print("=" * 30, sep="")
# Output:
# ==============================
# Header | Content | Footer
# ==============================
```

## The end Parameter

### Default Behavior (newline)
```python
print("First line")
print("Second line")
# Output:
# First line
# Second line
```

### Custom Endings
```python
# No newline
print("Hello", end="")
print("World")
# Output: HelloWorld

# Space instead of newline
print("Hello", end=" ")
print("World")
# Output: Hello World

# Custom character
print("Loading", end="...")
print("Done")
# Output: Loading...Done

# Multiple prints on same line
for i in range(5):
    print(i, end=" ")
# Output: 0 1 2 3 4
```

### Practical end Examples
```python
# Progress indicator
import time

print("Processing", end="")
for i in range(3):
    print(".", end="")
    time.sleep(0.5)
print(" Done!")
# Output: Processing... Done!

# Countdown timer
for i in range(5, 0, -1):
    print(i, end=" ", flush=True)
    time.sleep(1)
print("Blast off!")
# Output: 5 4 3 2 1 Blast off!

# Building a string gradually
print("Building:", end=" ")
print("Step 1", end=" -> ")
print("Step 2", end=" -> ")
print("Complete")
# Output: Building: Step 1 -> Step 2 -> Complete
```

## Combining sep and end

```python
# Custom separator and ending
print("A", "B", "C", sep=", ", end="!\n")
# Output: A, B, C!

# Table formatting
print("Name", "Age", "City", sep=" | ", end="\n" + "-" * 20 + "\n")
print("Alice", "25", "NYC", sep=" | ")
print("Bob", "30", "LA", sep=" | ")
# Output:
# Name | Age | City
# --------------------
# Alice | 25 | NYC
# Bob | 30 | LA

# Creating a menu
print("1", "Start Game", sep=". ", end="\n")
print("2", "Load Game", sep=". ", end="\n")
print("3", "Settings", sep=". ", end="\n")
print("4", "Exit", sep=". ")
# Output:
# 1. Start Game
# 2. Load Game
# 3. Settings
# 4. Exit
```

## Printing Multiple Lines

### Method 1: Multiple print statements
```python
print("Line 1")
print("Line 2")
print("Line 3")
```

### Method 2: Triple quotes
```python
print("""
Line 1
Line 2
Line 3
""")
```

### Method 3: Escape sequences
```python
print("Line 1\nLine 2\nLine 3")
```

### Method 4: Join with newlines
```python
lines = ["Line 1", "Line 2", "Line 3"]
print("\n".join(lines))
```

## Escape Sequences in print()

```python
# Newline
print("Hello\nWorld")
# Output:
# Hello
# World

# Tab
print("Name:\tJohn")
# Output: Name:    John

# Backslash
print("Path: C:\\Users\\Name")
# Output: Path: C:\Users\Name

# Single quote
print('It\'s Python')
# Output: It's Python

# Double quote
print("He said \"Hello\"")
# Output: He said "Hello"

# Raw string (ignores escape sequences)
print(r"C:\Users\Name\Documents")
# Output: C:\Users\Name\Documents
```

## Formatting Output

### Method 1: Comma separation
```python
name = "Alice"
age = 25
print("Name:", name, "Age:", age)
# Output: Name: Alice Age: 25
```

### Method 2: String concatenation (+)
```python
name = "Alice"
age = 25
print("Name: " + name + ", Age: " + str(age))
# Output: Name: Alice, Age: 25
```

### Method 3: f-strings (Python 3.6+) - RECOMMENDED
```python
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")
# Output: Name: Alice, Age: 25

# With expressions
price = 49.99
tax = 0.08
print(f"Total: ${price * (1 + tax):.2f}")
# Output: Total: $53.99

# With formatting
pi = 3.14159265
print(f"Pi to 2 decimals: {pi:.2f}")
# Output: Pi to 2 decimals: 3.14
```

### Method 4: .format() method
```python
name = "Alice"
age = 25
print("Name: {}, Age: {}".format(name, age))
# Output: Name: Alice, Age: 25

# Positional arguments
print("{1} is {0} years old".format(25, "Alice"))
# Output: Alice is 25 years old

# Named arguments
print("{name} is {age} years old".format(name="Alice", age=25))
# Output: Alice is 25 years old
```

### Method 5: % formatting (old style)
```python
name = "Alice"
age = 25
print("Name: %s, Age: %d" % (name, age))
# Output: Name: Alice, Age: 25

price = 49.99
print("Price: $%.2f" % price)
# Output: Price: $49.99
```

## Practical Examples

### Example 1: User Greeting
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"\nWelcome, {name}!")
print(f"You are {age} years old")
print(f"Next year you'll be {age + 1}")

# Output:
# Enter your name: Alice
# Enter your age: 25
# 
# Welcome, Alice!
# You are 25 years old
# Next year you'll be 26
```

### Example 2: Shopping Cart
```python
items = ["Laptop", "Mouse", "Keyboard"]
prices = [999.99, 29.99, 79.99]
quantities = [1, 2, 1]

print("Shopping Cart")
print("=" * 30)

total = 0
for item, price, qty in zip(items, prices, quantities):
    subtotal = price * qty
    total += subtotal
    print(f"{item:<10} x{qty} @ ${price:>7.2f} = ${subtotal:>8.2f}")

print("=" * 30)
print(f"{'TOTAL':<10} {'':>15} ${total:>8.2f}")

# Output:
# Shopping Cart
# ==============================
# Laptop     x1 @ $  999.99 = $  999.99
# Mouse      x2 @ $   29.99 = $   59.98
# Keyboard   x1 @ $   79.99 = $   79.99
# ==============================
# TOTAL                       $ 1139.96
```

### Example 3: Progress Bar
```python
import time

def progress_bar(percent):
    bar_length = 50
    filled = int(bar_length * percent // 100)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"\rProgress: |{bar}| {percent}%", end="", flush=True)

# Simulate progress
for i in range(0, 101, 10):
    progress_bar(i)
    time.sleep(0.5)

print("\nComplete!")

# Output (animated):
# Progress: |██████████████████████████████████████████████████| 100%
# Complete!
```

### Example 4: Table Formatting
```python
# Student grades
students = [
    ("Alice", 85, 92, 88),
    ("Bob", 78, 85, 80),
    ("Charlie", 92, 88, 94)
]

print("Student Grades Report")
print("-" * 50)
print(f"{'Name':<10} {'Math':>6} {'Science':>8} {'English':>8} {'Average':>8}")
print("-" * 50)

for name, math, science, english in students:
    avg = (math + science + english) / 3
    print(f"{name:<10} {math:>6} {science:>8} {english:>8} {avg:>8.1f}")

print("-" * 50)

# Output:
# Student Grades Report
# --------------------------------------------------
# Name         Math  Science  English  Average
# --------------------------------------------------
# Alice         85       92       88     88.3
# Bob           78       85       80     81.0
# Charlie       92       88       94     91.3
# --------------------------------------------------
```

### Example 5: Debugging with print()
```python
def calculate(x, y):
    print(f"[DEBUG] calculate({x}, {y}) called")  # Debug entry
    result = x + y
    print(f"[DEBUG] Intermediate result: {result}")  # Debug intermediate
    result = result * 2
    print(f"[DEBUG] Final result: {result}")  # Debug exit
    return result

# Using the function
value = calculate(5, 3)
print(f"Returned value: {value}")

# Output:
# [DEBUG] calculate(5, 3) called
# [DEBUG] Intermediate result: 8
# [DEBUG] Final result: 16
# Returned value: 16
```

### Example 6: Formatted Time Display
```python
import time
from datetime import datetime

# Current timestamp
current_time = datetime.now()
print(f"Current time: {current_time}")
print(f"Date: {current_time:%Y-%m-%d}")
print(f"Time: {current_time:%H:%M:%S}")
print(f"12-hour format: {current_time:%I:%M %p}")

# Elapsed time
start = time.time()
# Simulate work
time.sleep(2)
end = time.time()
print(f"Elapsed time: {end - start:.3f} seconds")

# Output:
# Current time: 2024-01-15 14:30:25.123456
# Date: 2024-01-15
# Time: 14:30:25
# 12-hour format: 02:30 PM
# Elapsed time: 2.001 seconds
```

## Special Print Techniques

### Printing to a File
```python
# Write to file instead of console
with open("output.txt", "w") as f:
    print("This goes to file", file=f)
    print("Another line", file=f)

# Append to file
with open("output.txt", "a") as f:
    print("This line is appended", file=f)
```

### Printing Without Buffer (flush)
```python
import time

# Without flush (may buffer)
for i in range(5):
    print(i, end=" ")
    time.sleep(0.5)
# Output appears all at once after loop

# With flush (real-time)
for i in range(5):
    print(i, end=" ", flush=True)
    time.sleep(0.5)
# Output appears one number at a time
```

### Pretty Printing (pprint)
```python
from pprint import pprint

# Complex nested data
data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "coding", "hiking"],
    "address": {
        "street": "123 Main St",
        "city": "NYC",
        "zip": "10001"
    }
}

# Regular print (hard to read)
print(data)

# Pretty print (easy to read)
pprint(data)

# Output (pretty):
# {'address': {'city': 'NYC', 'street': '123 Main St', 'zip': '10001'},
#  'age': 30,
#  'hobbies': ['reading', 'coding', 'hiking'],
#  'name': 'Alice'}
```

### Printing Colors (ANSI codes)
```python
# Color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

print(f"{RED}Error: Something went wrong!{RESET}")
print(f"{GREEN}Success: Operation completed!{RESET}")
print(f"{YELLOW}Warning: Low disk space{RESET}")
print(f"{BLUE}Info: Update available{RESET}")

# Bold text
BOLD = '\033[1m'
print(f"{BOLD}Important message{RESET}")
```

## Common Mistakes

### Mistake 1: Forgetting to convert non-strings
```python
# Wrong
age = 25
print("Age: " + age)  # TypeError!

# Right
print("Age: " + str(age))
print("Age:", age)  # print handles it automatically
print(f"Age: {age}")  # f-string handles it
```

### Mistake 2: Mixing print with return
```python
# Wrong - misunderstanding
def add(x, y):
    print(x + y)  # Prints but returns None

result = add(5, 3)
print(result)  # Prints: 8 (from inside) then None

# Right
def add(x, y):
    return x + y  # Returns value

result = add(5, 3)
print(result)  # Prints: 8
```

### Mistake 3: Wrong end parameter usage
```python
# Wrong - expecting newline
print("Hello", end="")
print("World")  # Output: HelloWorld (no space)

# Right - add space if needed
print("Hello", end=" ")
print("World")  # Output: Hello World
```

### Mistake 4: Forgetting f-string prefix
```python
name = "Alice"

# Wrong
print("{name}")  # Prints: {name}

# Right
print(f"{name}")  # Prints: Alice
print("{name}".format(name=name))  # Alternative
```

### Mistake 5: Unnecessary string concatenation
```python
# Inefficient
name = "Alice"
age = 25
print("Name: " + name + ", Age: " + str(age))

# Better (more readable and efficient)
print(f"Name: {name}, Age: {age}")
```

## Best Practices

### ✅ Do This
```python
# Use f-strings for formatting (Python 3.6+)
name = "Alice"
score = 95.5
print(f"{name} scored {score:.1f}%")

# Use sep parameter for separators
print("apple", "banana", "orange", sep=", ")

# Use descriptive debug prints
print(f"[DEBUG] Variable x = {x}, y = {y}")

# Use end parameter for progress indicators
for i in range(10):
    print(".", end="", flush=True)

# Use triple quotes for multi-line output
print("""
Line 1
Line 2
Line 3
""")
```

### ❌ Avoid This
```python
# Avoid - manual string building
print("Value is " + str(x) + " and " + str(y))

# Avoid - using print for debugging in production
print("x =", x)  # Remove before production

# Avoid - too many print statements in loops
for i in range(1000000):
    print(i)  # Will be extremely slow

# Avoid - print without flush in real-time applications
for i in range(10):
    print(i, end=" ")  # May buffer
    time.sleep(0.1)
```

## Performance Considerations

```python
import time

# Slow - many print calls
start = time.time()
for i in range(1000):
    print(i, end=" ")
print()
print(f"Time: {time.time() - start:.4f}s")

# Fast - build string first
start = time.time()
output = " ".join(str(i) for i in range(1000))
print(output)
print(f"Time: {time.time() - start:.4f}s")

# For very large output, write to file directly
with open("output.txt", "w") as f:
    for i in range(10000):
        f.write(f"{i}\n")  # Faster than print
```

## Quick Reference Table

| Feature | Syntax | Example |
|---------|--------|---------|
| Basic print | `print(value)` | `print("Hello")` |
| Multiple values | `print(a, b, c)` | `print(1, 2, 3)` |
| Custom separator | `sep='x'` | `print(1,2,3, sep='-')` |
| Custom ending | `end='x'` | `print("Hi", end='!')` |
| No newline | `end=''` | `print("Hi", end='')` |
| f-string | `f"{var}"` | `print(f"Age: {age}")` |
| Format method | `"{}".format()` | `print("{}".format(x))` |
| Old style | `"%s" % var` | `print("%d" % x)` |
| To file | `file=open()` | `print("Hi", file=f)` |
| Force flush | `flush=True` | `print(".", flush=True)` |

## Summary

- **print()** is Python's primary output function
- Can print multiple values separated by commas
- **sep** parameter controls spacing between values
- **end** parameter controls what prints at the end (default newline)
- **f-strings** are the modern way to format output (Python 3.6+)
- Use **flush=True** for real-time output (progress bars)
- **pprint** module for pretty-printing complex data
- Print to files using the **file** parameter
- Avoid excessive print statements in production code
- Use descriptive debug prints with `[DEBUG]` markers

## Basic Template
```python
#!/usr/bin/env python3

# Simple output
print("Hello, World!")

# Variables
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")

# Multiple items with custom separator
print("Apple", "Banana", "Cherry", sep=", ")

# No newline (progress indicator)
import time
print("Loading", end="")
for i in range(3):
    print(".", end="", flush=True)
    time.sleep(0.5)
print(" Done!")

# Formatted table
print(f"{'Name':<10} {'Score':>6}")
print("-" * 17)
print(f"{'Alice':<10} {95:>6}")
print(f"{'Bob':<10} {87:>6}")

# Debug printing
DEBUG = True
if DEBUG:
    print(f"[DEBUG] Current value: {value}")
```

*This documentation belongs to https://github.com/InterCentury*