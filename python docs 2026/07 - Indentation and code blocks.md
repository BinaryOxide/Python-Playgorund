# 07 - Indentation and Code Blocks in Python

## What is Indentation?
Indentation refers to the spaces or tabs at the beginning of a code line. In Python, indentation is **mandatory** and defines code blocks (groups of statements). Unlike other languages that use braces `{}`, Python uses indentation to show which statements belong together.

## Why Indentation Matters in Python?

### Python vs Other Languages
```python
# C/C++/Java uses braces
if (x > 0) {
    printf("Positive");
    printf("Number");
}

# Python uses indentation
if x > 0:
    print("Positive")
    print("Number")
```

### Indentation Defines Code Blocks
```python
# Different indentation = different blocks
if True:
    print("This is inside the if block")
print("This is outside - always executes")
```

## Basic Rules

### Rule 1: Consistent Indentation
```python
# ✅ Correct - consistent 4 spaces
if x > 0:
    print("Positive")
    print("Great!")

# ❌ Wrong - inconsistent spaces
if x > 0:
    print("Positive")
     print("Great!")  # Mixed spaces!
```

### Rule 2: Indentation After Colon `:`
```python
# Code blocks start after colon
if condition:      # Colon here
    statement1     # Indented
    statement2     # Indented

def my_function(): # Colon here
    body_line1     # Indented
    body_line2     # Indented
```

### Rule 3: No Unnecessary Indentation
```python
# ❌ Wrong - indentation without colon
x = 10
    print(x)  # IndentationError!

# ✅ Correct - no indentation needed
x = 10
print(x)
```

## Standard Indentation Size

### PEP 8 Recommendation: 4 Spaces
```python
# ✅ Recommended - 4 spaces
def calculate_sum(numbers):
    total = 0          # 4 spaces
    for num in numbers:  # 4 spaces
        total += num     # 8 spaces (4 + 4)
    return total        # 4 spaces

# ⚠️ Works but not recommended - 2 spaces
def calculate_sum(numbers):
  total = 0          # 2 spaces
  for num in numbers:  # 2 spaces
    total += num       # 4 spaces (2 + 2)
  return total        # 2 spaces

# ❌ Not recommended - tabs (inconsistent)
def calculate_sum(numbers):
	total = 0          # Tab
	for num in numbers:  # Tab
		total += num     # Tab + space? Inconsistent!
	return total        # Tab
```

### Spaces vs Tabs
```python
# NEVER mix tabs and spaces!
# ✅ Use spaces only (4 spaces recommended)
if True:
····print("4 spaces")

# ✅ Use tabs only (if you must)
if True:
→   print("tab")

# ❌ NEVER mix!
if True:
····→   print("mixed!")  # Error!
```

## Code Blocks with Different Statements

### if Statements
```python
age = 18

if age >= 18:
    print("You can vote")
    print("You are an adult")
    print("You can drive")
    
print("This runs always")

# Output:
# You can vote
# You are an adult
# You can drive
# This runs always
```

### if-elif-else Blocks
```python
score = 85

if score >= 90:
    grade = "A"
    print("Excellent!")
elif score >= 80:
    grade = "B"
    print("Good job!")
elif score >= 70:
    grade = "C"
    print("Not bad")
else:
    grade = "F"
    print("Need improvement")

print(f"Grade: {grade}")

# Output:
# Good job!
# Grade: B
```

### for Loops
```python
# Simple for loop
for i in range(3):
    print(f"Iteration {i}")
    print(f"Square: {i*i}")
print("Loop finished")

# Output:
# Iteration 0
# Square: 0
# Iteration 1
# Square: 1
# Iteration 2
# Square: 4
# Loop finished

# Nested loops
for i in range(3):
    print(f"Outer: {i}")
    for j in range(2):
        print(f"  Inner: {j}")
    print("  ---")

# Output:
# Outer: 0
#   Inner: 0
#   Inner: 1
#   ---
# Outer: 1
#   Inner: 0
#   Inner: 1
#   ---
# Outer: 2
#   Inner: 0
#   Inner: 1
#   ---
```

### while Loops
```python
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1
    print("  Incremented")
print("Loop ended")

# Output:
# Count: 0
#   Incremented
# Count: 1
#   Incremented
# Count: 2
#   Incremented
# Loop ended
```

### Function Definitions
```python
def greet(name):
    """Function body starts here"""
    message = f"Hello, {name}!"
    print(message)
    return len(message)

# Call the function
result = greet("Alice")
print(f"Length: {result}")

# Output:
# Hello, Alice!
# Length: 13
```

### Class Definitions
```python
class Person:
    """Class body indented"""
    species = "Homo sapiens"  # Class attribute
    
    def __init__(self, name):  # Method indented
        self.name = name        # Method body indented
    
    def greet(self):            # Another method
        print(f"Hi, I'm {self.name}")

# Create instance
p = Person("Bob")
p.greet()
# Output: Hi, I'm Bob
```

### try-except Blocks
```python
try:
    x = int(input("Enter number: "))
    result = 10 / x
    print(f"Result: {result}")
except ValueError:
    print("That's not a number!")
    print("Please try again")
except ZeroDivisionError:
    print("Can't divide by zero!")
    print("Try another number")
finally:
    print("Execution complete")

# Output (if user enters 0):
# Can't divide by zero!
# Try another number
# Execution complete
```

## Nested Code Blocks

```python
# Multiple levels of indentation
def process_data(data):
    print("Starting process")
    
    if data:
        print("Data exists")
        
        for item in data:
            print(f"  Processing: {item}")
            
            if item > 0:
                print(f"    Positive: {item}")
            else:
                print(f"    Negative: {item}")
        
        print("Finished processing")
    else:
        print("No data")
    
    print("Process ended")

# Test the function
process_data([5, -2, 10])

# Output:
# Starting process
# Data exists
#   Processing: 5
#     Positive: 5
#   Processing: -2
#     Negative: -2
#   Processing: 10
#     Positive: 10
# Finished processing
# Process ended
```

## Empty Code Blocks

### Using pass Statement
```python
# Empty block - syntax error!
if condition:
    # Nothing here - ERROR!

# Fix with pass
if condition:
    pass  # Does nothing, but valid

# Practical examples
def function_not_implemented_yet():
    pass  # Placeholder

class MyClass:
    pass  # Empty class

for i in range(10):
    if i % 2 == 0:
        pass  # Skip even numbers
    else:
        print(f"Odd: {i}")
```

### Using ... (Ellipsis)
```python
# Ellipsis also works (less common)
def future_function():
    ...  # Placeholder

if True:
    ...  # Empty block
```

## Common Indentation Errors

### Error 1: Missing Indentation
```python
# ❌ Wrong - no indentation after colon
if x > 0:
print("Positive")  # IndentationError!

# ✅ Correct
if x > 0:
    print("Positive")
```

### Error 2: Extra Indentation
```python
# ❌ Wrong - unnecessary indentation
x = 10
    y = 20  # IndentationError!

# ✅ Correct
x = 10
y = 20
```

### Error 3: Inconsistent Indentation
```python
# ❌ Wrong - mixing spaces and tabs
def my_func():
    print("Line 1")    # 4 spaces
	print("Line 2")    # Tab - Inconsistent!

# ✅ Correct - be consistent
def my_func():
    print("Line 1")
    print("Line 2")
```

### Error 4: Wrong Indentation Level
```python
# ❌ Wrong - incorrect nesting
if x > 0:
    print("Positive")
      print("Still positive")  # Wrong level!

# ✅ Correct
if x > 0:
    print("Positive")
    print("Still positive")
```

## Indentation Best Practices

### ✅ Do This
```python
# Use 4 spaces for each level
def calculate_average(numbers):
    total = 0
    count = 0
    
    for num in numbers:
        total += num
        count += 1
    
    if count > 0:
        average = total / count
        return average
    else:
        return 0

# Align continuation lines properly
long_variable_name = (
    "This is a very long string "
    "that spans multiple lines"
)

# Indent for visual alignment
result = (value1 + value2 + value3 +
          value4 + value5 + value6)
```

### ❌ Avoid This
```python
# Avoid - inconsistent indentation
def bad_function():
  print("2 spaces here")
    print("4 spaces here")  # Inconsistent!

# Avoid - too many levels (max 4 recommended)
if a:
    if b:
        if c:
            if d:
                if e:  # Too deep!
                    print("Deep nesting")

# Avoid - mixing tabs and spaces
def mixed():
	print("Tab")
    print("Spaces")  # Visual Studio Code will warn you
```

## Indentation in Different Contexts

### Line Continuation
```python
# Implicit line continuation (inside parentheses)
result = (10 + 20 + 30 + 
          40 + 50 + 60)

# Explicit line continuation with \
result = 10 + 20 + 30 + \
         40 + 50 + 60

# List with line continuation
my_list = [1, 2, 3,
           4, 5, 6]

# Dictionary with line continuation
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}
```

### Conditional Expressions
```python
# Long condition - proper indentation
if (this_is_a_very_long_condition and
    another_long_condition and
    final_condition):
    print("All conditions met")

# Alternative style
if (this_is_a_very_long_condition 
    and another_long_condition 
    and final_condition):
    print("All conditions met")
```

### List Comprehensions
```python
# Short - one line
squares = [x**2 for x in range(10)]

# Long - multi-line with indentation
squares = [
    x**2 
    for x in range(10)
    if x % 2 == 0
]

# Nested comprehension
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [
    num 
    for row in matrix 
    for num in row
]
```

## Practical Examples

### Example 1: Grade Calculator with Nested Logic
```python
def calculate_grade(score, extra_credit=False):
    """Calculate letter grade with optional extra credit"""
    
    # Apply extra credit if enabled
    if extra_credit:
        score += 5
        print(f"Extra credit applied! New score: {score}")
    
    # Determine letter grade
    if score >= 90:
        grade = "A"
        if score >= 97:
            grade += "+"
        elif score <= 93:
            grade += "-"
    elif score >= 80:
        grade = "B"
        if score >= 87:
            grade += "+"
        elif score <= 83:
            grade += "-"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    return grade

# Test the function
scores = [85, 92, 78, 45, 95]
for score in scores:
    grade = calculate_grade(score, extra_credit=(score > 90))
    print(f"Score: {score} → Grade: {grade}")
    print("-" * 20)

# Output:
# Score: 85 → Grade: B
# --------------------
# Score: 92 → Grade: A-
# --------------------
# Extra credit applied! New score: 83
# Score: 78 → Grade: C
# --------------------
# Score: 45 → Grade: F
# --------------------
# Extra credit applied! New score: 100
# Score: 95 → Grade: A+
# --------------------
```

### Example 2: Menu System with Nested Conditionals
```python
def main_menu():
    """Display and process main menu"""
    print("\n=== MAIN MENU ===")
    print("1. User Management")
    print("2. Data Processing")
    print("3. Reports")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        print("\n--- User Management ---")
        print("1. Add User")
        print("2. Delete User")
        print("3. List Users")
        subchoice = input("Your choice: ")
        
        if subchoice == "1":
            print("Adding new user...")
            name = input("Enter name: ")
            email = input("Enter email: ")
            print(f"User {name} added!")
        elif subchoice == "2":
            print("Deleting user...")
            user_id = input("User ID: ")
            print(f"User {user_id} deleted!")
        elif subchoice == "3":
            print("Listing all users...")
            print("1. Alice (alice@email.com)")
            print("2. Bob (bob@email.com)")
        else:
            print("Invalid subchoice!")
    
    elif choice == "2":
        print("\n--- Data Processing ---")
        print("Processing data...")
        for i in range(3):
            print(f"  Processing item {i+1}")
            # Simulate work
            pass
        print("Processing complete!")
    
    elif choice == "3":
        print("\n--- Reports ---")
        report_type = input("Report type (summary/detail): ")
        if report_type == "summary":
            print("Generating summary report...")
            print("Total users: 10")
            print("Active users: 8")
        elif report_type == "detail":
            print("Generating detailed report...")
            print("User details:")
            for i in range(3):
                print(f"  User {i+1}: Details here")
        else:
            print("Unknown report type!")
    
    elif choice == "4":
        print("Goodbye!")
        return False
    else:
        print("Invalid choice!")
    
    return True

# Run menu
running = True
while running:
    running = main_menu()

# Output depends on user choices
```

### Example 3: Data Validation with Multiple Levels
```python
def validate_user_data(username, age, email):
    """Validate user input with nested conditions"""
    
    print(f"Validating user: {username}")
    
    # Check username
    if len(username) < 3:
        print("  ✗ Username too short (min 3 characters)")
        return False
    elif len(username) > 20:
        print("  ✗ Username too long (max 20 characters)")
        return False
    elif not username.isalnum():
        print("  ✗ Username must be alphanumeric")
        return False
    else:
        print("  ✓ Username valid")
    
    # Check age
    if age < 0:
        print("  ✗ Age cannot be negative")
        return False
    elif age < 13:
        print("  ✗ Age must be at least 13")
        return False
    elif age > 120:
        print("  ✗ Age seems unrealistic")
        return False
    else:
        print("  ✓ Age valid")
        
        # Additional age-based checks
        if age < 18:
            print("    Note: Minor - parental consent needed")
        elif age >= 65:
            print("    Note: Senior citizen benefits available")
    
    # Check email
    if "@" not in email:
        print("  ✗ Invalid email (missing @)")
        return False
    elif "." not in email.split("@")[1]:
        print("  ✗ Invalid email (missing domain dot)")
        return False
    else:
        print("  ✓ Email valid")
        
        # Extract domain
        domain = email.split("@")[1]
        if domain == "gmail.com":
            print("    Note: Gmail user detected")
        elif domain == "company.com":
            print("    Note: Internal company email")
    
    print("✓ All validations passed!")
    return True

# Test the function
test_data = [
    ("alice", 25, "alice@gmail.com"),
    ("a", 30, "a@test.com"),  # Too short username
    ("bob", 15, "bob@test.com"),  # Minor
    ("charlie", 130, "charlie@test.com"),  # Too old
    ("dave", 30, "invalid-email")  # Invalid email
]

for username, age, email in test_data:
    print("\n" + "=" * 40)
    result = validate_user_data(username, age, email)
    print(f"Result: {'PASSED' if result else 'FAILED'}")

# Output:
# ========================================
# Validating user: alice
#   ✓ Username valid
#   ✓ Age valid
#   ✓ Email valid
#     Note: Gmail user detected
# ✓ All validations passed!
# Result: PASSED
# 
# ========================================
# Validating user: a
#   ✗ Username too short (min 3 characters)
# Result: FAILED
# ... etc
```

### Example 4: Shopping Cart with Nested Loops
```python
def process_shopping_cart(cart, discounts):
    """Process shopping cart with nested loops"""
    
    print("=== ORDER SUMMARY ===")
    total = 0
    item_count = 0
    
    # Outer loop - categories
    for category, items in cart.items():
        print(f"\n{category.upper()}:")
        print("-" * 30)
        
        # Inner loop - items in category
        for item in items:
            name = item["name"]
            price = item["price"]
            quantity = item["quantity"]
            
            # Apply discount if applicable
            discount = discounts.get(name, 0)
            discounted_price = price * (1 - discount)
            subtotal = discounted_price * quantity
            
            total += subtotal
            item_count += quantity
            
            # Display item details
            print(f"  {name}:")
            print(f"    Price: ${price:.2f}")
            if discount > 0:
                print(f"    Discount: {discount*100:.0f}%")
                print(f"    Discounted: ${discounted_price:.2f}")
            print(f"    Quantity: {quantity}")
            print(f"    Subtotal: ${subtotal:.2f}")
    
    # Summary
    print("\n" + "=" * 30)
    print(f"Total items: {item_count}")
    print(f"Total cost: ${total:.2f}")
    
    # Apply shipping based on total
    if total == 0:
        print("Empty cart!")
    elif total < 50:
        shipping = 5.99
        print(f"Shipping: ${shipping:.2f}")
        print(f"Grand total: ${total + shipping:.2f}")
    elif total < 100:
        shipping = 2.99
        print(f"Shipping: ${shipping:.2f}")
        print(f"Grand total: ${total + shipping:.2f}")
    else:
        print("Free shipping!")
        print(f"Grand total: ${total:.2f}")

# Shopping cart data
cart = {
    "electronics": [
        {"name": "Laptop", "price": 999.99, "quantity": 1},
        {"name": "Mouse", "price": 29.99, "quantity": 2}
    ],
    "books": [
        {"name": "Python Book", "price": 49.99, "quantity": 1}
    ],
    "clothing": [
        {"name": "T-Shirt", "price": 19.99, "quantity": 3}
    ]
}

discounts = {
    "Mouse": 0.10,  # 10% off
    "Python Book": 0.15  # 15% off
}

process_shopping_cart(cart, discounts)

# Output:
# === ORDER SUMMARY ===
# 
# ELECTRONICS:
# ------------------------------
#   Laptop:
#     Price: $999.99
#     Quantity: 1
#     Subtotal: $999.99
#   Mouse:
#     Price: $29.99
#     Discount: 10%
#     Discounted: $26.99
#     Quantity: 2
#     Subtotal: $53.98
# 
# BOOKS:
# ------------------------------
#   Python Book:
#     Price: $49.99
#     Discount: 15%
#     Discounted: $42.49
#     Quantity: 1
#     Subtotal: $42.49
# 
# CLOTHING:
# ------------------------------
#   T-Shirt:
#     Price: $19.99
#     Quantity: 3
#     Subtotal: $59.97
# 
# ==============================
# Total items: 7
# Total cost: $1156.43
# Free shipping!
# Grand total: $1156.43
```

## Indentation Styles

### Style 1: Standard (4 spaces)
```python
def my_function():
    if condition:
        do_something()
        do_something_else()
```

### Style 2: Hanging Indent
```python
# Function arguments
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# List elements
my_list = [
    1, 2, 3,
    4, 5, 6
]

# Dictionary
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'NYC'
}
```

### Style 3: Aligned with Opening Delimiter
```python
# Aligned with opening parenthesis
def long_function_name(var_one, var_two,
                       var_three, var_four):
    print(var_one)

# Aligned with opening bracket
result = some_function(arg1, arg2,
                       arg3, arg4)
```

## Tools for Managing Indentation

### Using IDEs/Auto-formatters
```python
# Most editors auto-indent after colon
if x > 0:
    # Editor automatically adds indentation
    print("Indented")

# Black formatter (standardizes to 4 spaces)
# black myfile.py

# autopep8 (fixes indentation issues)
# autopep8 --in-place myfile.py
```

### Checking Indentation
```python
# Python's -t flag warns about inconsistent tabs/spaces
# python -t myfile.py

# -tt flag treats inconsistent tabs/spaces as error
# python -tt myfile.py
```

## Quick Reference Table

| Concept | Syntax | Example |
|---------|--------|---------|
| Block start | `:` followed by newline + indent | `if x:⏎····print(x)` |
| Empty block | `pass` | `if x: pass` |
| Standard indent | 4 spaces | `····print("hi")` |
| Nested block | Increase indent | `if x:⏎····if y:⏎········print(z)` |
| Line continuation | Inside `()`, `[]`, `{}` | `result = (a + b +⏎·········c + d)` |
| No block needed | Simple statement | `if x: print(x)` |

## Common Pitfalls and Solutions

### Pitfall 1: Mixing Spaces and Tabs
```python
# Problem
def bad():
	print("Tab")  # Tab character
    print("Spaces")  # Spaces

# Solution - use spaces consistently
def good():
    print("Spaces")
    print("Spaces")
```

### Pitfall 2: Wrong Indentation After Comment
```python
# Problem
if condition:
    # This comment is fine
    print("Works")
  # This comment wrong level
    print("Also works but confusing")

# Solution - consistent level
if condition:
    # All comments at same level
    print("Works")
    # Clear and consistent
    print("Also works")
```

### Pitfall 3: Indentation in REPL
```python
# In Python interactive shell
>>> if True:
...     print("Indented")  # REPL adds ... and spaces
...     print("Works")
... 
Indented
Works
```

## Summary

- **Indentation is mandatory** in Python (no braces allowed)
- **4 spaces** is the standard (PEP 8 recommendation)
- **NEVER mix tabs and spaces** (causes hard-to-find errors)
- **Colon `:`** indicates the start of an indented block
- **Consistent indentation** defines code blocks
- **`pass`** statement for empty blocks
- **Too much nesting** (>4 levels) indicates need for refactoring
- **Most IDEs** auto-indent correctly after colon
- **Line continuations** have special indentation rules
- **Use tools** like Black or autopep8 to fix indentation

## Basic Template
```python
#!/usr/bin/env python3

def main():
    """Main function with proper indentation"""
    
    # Variable declarations (no indentation needed)
    name = "Alice"
    age = 25
    
    # Conditional block
    if age >= 18:
        print(f"{name} is an adult")
        print(f"They are {age} years old")
        
        # Nested block
        if age >= 65:
            print("Senior citizen benefits apply")
        elif age >= 21:
            print("Can purchase alcohol")
        else:
            print("Minor restrictions apply")
    else:
        print(f"{name} is a minor")
    
    # Loop block
    for i in range(3):
        print(f"Count: {i}")
        
        # Nested loop
        for j in range(2):
            print(f"  Inner: {j}")
    
    # Try-except block
    try:
        result = 10 / 2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    finally:
        print("Execution complete")
    
    return True

# Class definition
class MyClass:
    """Class with proper indentation"""
    
    def __init__(self, value):
        self.value = value
    
    def display(self):
        print(f"Value: {self.value}")

# Run main function
if __name__ == "__main__":
    main()

# Single-line block (allowed but not common)
if True: print("Single line block")

# Empty block placeholder
def future_function():
    pass
```

*This documentation belongs to https://github.com/InterCentury*