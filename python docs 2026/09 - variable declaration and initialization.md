# 09 - Variable Declaration and Initialization in Python

## What are Variables?
Variables are named containers that store data in memory. Unlike C++, Python variables don't require explicit type declaration - they are dynamically typed and can change type during execution.

## Variable Declaration vs Initialization

### Declaration
```python
# In Python, declaration happens automatically when you assign a value
# No explicit "declaration" keyword needed

x = 10          # Declared and initialized in one step
name = "Alice"  # No separate declaration step

# You cannot declare without initialization
# y  # This is just a reference error
```

### Initialization
```python
# Initialization = first assignment to a variable
age = 25                    # Initialize with integer
price = 19.99              # Initialize with float
name = "Bob"               # Initialize with string
is_active = True           # Initialize with boolean
items = [1, 2, 3]          # Initialize with list

# Multiple initialization in one line
a, b, c = 1, 2, 3
x = y = z = 0
```

## Dynamic Typing

### Variables Can Change Type
```python
# Python variables are not tied to a specific type
value = 10          # Integer
print(type(value))  # <class 'int'>

value = "Hello"     # Now a string
print(type(value))  # <class 'str'>

value = 3.14        # Now a float
print(type(value))  # <class 'float'>

value = [1, 2, 3]   # Now a list
print(type(value))  # <class 'list'>

# This is NOT possible in C++!
```

### No Type Declarations Needed
```python
# C++ requires type declarations
# int age = 25;
# string name = "Alice";
# double price = 19.99;

# Python - just assign
age = 25
name = "Alice"
price = 19.99

# Type is inferred from the value assigned
```

## Variable Naming Rules

### Valid Variable Names
```python
# Letters, numbers, underscore (cannot start with number)
name = "Alice"
name2 = "Bob"
_name = "Private"
user_name = "Charlie"
userName = "Dave"  # Camel case (less common in Python)
UserName = "Eve"   # Pascal case (usually for classes)

# Case sensitive
myvar = "lowercase"
myVar = "mixed"
MYVAR = "uppercase"  # Different variable

# Unicode characters (Python 3+)
café = "coffee"
姓名 = "Chinese name"
```

### Invalid Variable Names
```python
# Cannot start with number
# 2name = "Invalid"  # SyntaxError!

# Cannot contain spaces
# my name = "Invalid"  # SyntaxError!

# Cannot use special symbols (except _)
# my-name = "Invalid"  # SyntaxError!
# my$name = "Invalid"  # SyntaxError!
# my@name = "Invalid"  # SyntaxError!

# Cannot use keywords
# class = "Invalid"    # SyntaxError!
# if = "Invalid"       # SyntaxError!
# for = "Invalid"      # SyntaxError!
# while = "Invalid"    # SyntaxError!
```

### Python Keywords (Cannot Use as Variable Names)
```python
# List of Python keywords
False, True, None, and, as, assert, async, await, break, class, continue, 
def, del, elif, else, except, finally, for, from, global, if, import, in, 
is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

# Trying to use them causes SyntaxError
# and = 10  # SyntaxError!
```

## Naming Conventions

### Standard Conventions (PEP 8)
```python
# Variables: snake_case (recommended)
user_name = "Alice"
total_score = 95
max_retries = 3

# Constants: UPPER_CASE
MAX_SIZE = 100
PI = 3.14159
DEFAULT_COLOR = "blue"

# Private variables (internal use): _leading_underscore
_internal_value = 10
_temp_data = []

# Class names: PascalCase
class UserAccount:
    pass

# Function names: snake_case
def calculate_total():
    pass

# Avoid single-letter names except counters
i, j, k = 0, 1, 2  # OK for loops
x, y, z = 1, 2, 3  # OK for coordinates

# But use meaningful names for important variables
# Good: student_count, user_age, product_price
# Bad: s, u, p
```

## Multiple Assignment

### Assign Multiple Variables at Once
```python
# Same value to multiple variables
x = y = z = 0
print(x, y, z)  # 0 0 0

# Different values in one line
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

# Swap variables (no temp variable needed)
a, b = 5, 10
print(f"Before: a={a}, b={b}")  # Before: a=5, b=10
a, b = b, a
print(f"After: a={a}, b={b}")   # After: a=10, b=5

# Unpacking sequences
point = (10, 20)
x, y = point
print(f"x={x}, y={y}")  # x=10, y=20

colors = ["red", "green", "blue"]
first, second, third = colors
print(first, second, third)  # red green blue
```

### Extended Unpacking (Python 3+)
```python
# Use * to collect remaining items
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# Ignore values with _
a, _, b = (1, 2, 3)
print(a, b)  # 1 3

# Ignore multiple
first, *_, last = [10, 20, 30, 40, 50]
print(first, last)  # 10 50
```

## Variable Scope

### Local Variables
```python
def my_function():
    x = 10  # Local variable - only exists inside function
    print(f"Inside function: {x}")

my_function()
# print(x)  # NameError! x doesn't exist outside
```

### Global Variables
```python
# Variable defined outside any function
global_var = 100

def show_global():
    print(f"Inside function: {global_var}")  # Can access

show_global()
print(f"Outside: {global_var}")  # Can access
```

### Modifying Global Variables
```python
counter = 0

def increment():
    global counter  # Need global keyword to modify
    counter += 1

def no_modify():
    # Without global, creates local variable
    counter = 5  # This is local, not global
    print(f"Local counter: {counter}")

print(f"Before: {counter}")  # 0
increment()
print(f"After increment: {counter}")  # 1
no_modify()
print(f"Still: {counter}")  # 1
```

### Nonlocal Variables (Nested Functions)
```python
def outer():
    x = "outer"
    
    def inner():
        nonlocal x  # Modify variable from outer scope
        x = "inner"
    
    inner()
    print(x)  # "inner" (modified by inner function)

outer()

# Without nonlocal
def outer2():
    x = "outer"
    
    def inner2():
        x = "inner"  # Creates new local variable
        print(f"Inner: {x}")
    
    inner2()
    print(f"Outer: {x}")  # Still "outer"

outer2()
```

## Type Annotations (Type Hints)

### Basic Type Annotations
```python
# Python 3.5+ supports type hints (optional, not enforced)
name: str = "Alice"
age: int = 25
price: float = 19.99
is_active: bool = True

# Function annotations
def greet(name: str) -> str:
    return f"Hello, {name}"

def calculate(x: int, y: int) -> int:
    return x + y

# Type hints are just hints - Python ignores them
age: int = "twenty"  # No error! Still works
print(age)  # twenty
```

### Complex Type Hints
```python
from typing import List, Dict, Tuple, Optional, Union

# Lists
numbers: List[int] = [1, 2, 3, 4, 5]
mixed: List[Union[int, str]] = [1, "two", 3]

# Dictionaries
scores: Dict[str, int] = {"Alice": 95, "Bob": 87}

# Tuples
point: Tuple[int, int] = (10, 20)

# Optional (can be None)
value: Optional[int] = None
value = 10

# Any type
from typing import Any
anything: Any = 42
anything = "string"
```

## Memory Management

### Variables are References
```python
# Variables reference objects in memory
x = 10
y = x  # y references the same object
print(id(x))  # Memory address
print(id(y))  # Same address

# Changing immutable types creates new object
x = 20  # x now references new object
print(id(x))  # Different address
print(id(y))  # Still original address

# Mutable types share reference
list1 = [1, 2, 3]
list2 = list1  # Both reference same list
list2.append(4)
print(list1)  # [1, 2, 3, 4] - Changed!
print(list2)  # [1, 2, 3, 4]
```

### Reference Counting
```python
import sys

x = 10
print(sys.getrefcount(x))  # Number of references

y = x  # Increase reference count
z = x  # Increase again

# Deleting references
del y   # Decrease reference count
del z   # Decrease reference count
# When count reaches 0, object is garbage collected
```

### Garbage Collection
```python
import gc

# Python automatically manages memory
def create_objects():
    data = [1, 2, 3]  # Created
    return  # data deleted when function ends

# Manual garbage collection (rarely needed)
gc.collect()
```

## Constants in Python

### By Convention (No True Constants)
```python
# Python doesn't have real constants
# Use UPPER_CASE to indicate "don't change"
MAX_USERS = 100
PI = 3.14159
APP_NAME = "MyApp"

# But you CAN change them (no enforcement)
MAX_USERS = 200  # This works! (but violates convention)

# Use property or class for true constants
class Constants:
    MAX_SIZE = 100
    
Constants.MAX_SIZE = 200  # Still can change

# Third-party solutions (if needed)
from dataclasses import dataclass

@dataclass(frozen=True)
class FrozenConstants:
    MAX_SIZE: int = 100
    APP_NAME: str = "MyApp"

const = FrozenConstants()
# const.MAX_SIZE = 200  # dataclasses.FrozenInstanceError
```

## None (Null Value)

```python
# None represents absence of value (similar to null in other languages)
result = None

# Check for None
if result is None:
    print("No result yet")

# None is not the same as False, 0, or empty
print(None == 0)      # False
print(None == False)  # False
print(None == "")     # False

# None is a singleton
a = None
b = None
print(a is b)  # True (same object)

# Functions return None by default
def do_nothing():
    pass

result = do_nothing()
print(result)  # None
```

## Deleting Variables

```python
# Delete variable with del statement
x = 10
print(x)  # 10
del x
# print(x)  # NameError: name 'x' is not defined

# Delete multiple variables
a, b, c = 1, 2, 3
del a, b, c

# Delete from collections
my_list = [1, 2, 3, 4, 5]
del my_list[2]  # Delete element at index 2
print(my_list)  # [1, 2, 4, 5]

del my_list[1:3]  # Delete slice
print(my_list)  # [1, 5]

# Delete attribute
class MyClass:
    value = 10

obj = MyClass()
print(obj.value)  # 10
del obj.value
# print(obj.value)  # AttributeError
```

## Variable Inspection

```python
# Check type
x = 10
print(type(x))  # <class 'int'>

# Check if variable exists
if 'x' in locals():
    print("x exists locally")

if 'x' in globals():
    print("x exists globally")

# List all variables in current scope
print(dir())  # List local variables
print(globals())  # Dictionary of global variables
print(locals())   # Dictionary of local variables

# Get variable identity (memory address)
print(id(x))

# Check if two variables reference same object
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)   # True (same object)
print(a is c)   # False (different objects)
print(a == c)   # True (same content)
```

## Practical Examples

### Example 1: Temperature Converter
```python
# Variable declaration and initialization
celsius: float = 25.0
fahrenheit: float = 0.0
kelvin: float = 0.0

# Calculate conversions
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"{celsius}°C = {fahrenheit}°F")
print(f"{celsius}°C = {kelvin}K")

# Dynamic typing in action
temperature = celsius
print(f"Temp type: {type(temperature)}")  # float
temperature = "Hot"
print(f"Now type: {type(temperature)}")   # str
```

### Example 2: Bank Account
```python
# Initialize account variables
account_balance = 1000.00
account_holder = "Alice Smith"
account_number = "ACC123456"
interest_rate = 0.025  # 2.5% annual interest

# Multiple assignment for transaction
deposit_amount, withdrawal_amount = 500.00, 200.00

# Process transactions
print(f"Initial balance: ${account_balance:.2f}")

account_balance += deposit_amount
print(f"After deposit: ${account_balance:.2f}")

account_balance -= withdrawal_amount
print(f"After withdrawal: ${account_balance:.2f}")

# Calculate interest
interest = account_balance * interest_rate
account_balance += interest
print(f"After interest: ${account_balance:.2f}")

# Swap for display
formatted_balance, formatted_holder = account_balance, account_holder
print(f"Account {account_number}: {formatted_holder} has ${formatted_balance:.2f}")
```

### Example 3: Student Grades
```python
# Variable declarations with type hints
student_name: str = "Bob Johnson"
scores: List[int] = [85, 92, 78, 88, 95]
average: float = 0.0
letter_grade: str = ""
is_passing: bool = False

# Calculate average
total = 0
for score in scores:
    total += score
average = total / len(scores)

# Determine letter grade
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

is_passing = average >= 60

# Display results
print(f"Student: {student_name}")
print(f"Scores: {scores}")
print(f"Average: {average:.1f}")
print(f"Grade: {letter_grade}")
print(f"Passing: {is_passing}")

# Multiple assignment for summary
subject, semester, year = "Math", "Fall", 2024
print(f"{subject} {semester} {year}")
```

### Example 4: Shopping Cart
```python
# Initialize variables
cart_items = []
cart_total = 0.0
discount_rate = 0.10
tax_rate = 0.08

# Add items using tuple unpacking
item1 = ("Laptop", 999.99, 1)
item2 = ("Mouse", 29.99, 2)
item3 = ("Keyboard", 79.99, 1)

# Add to cart
cart_items.extend([item1, item2, item3])

# Calculate total
for name, price, quantity in cart_items:
    subtotal = price * quantity
    cart_total += subtotal
    print(f"{name}: ${price:.2f} x {quantity} = ${subtotal:.2f}")

print(f"Subtotal: ${cart_total:.2f}")

# Apply discount
discount = cart_total * discount_rate
cart_total -= discount
print(f"Discount (10%): -${discount:.2f}")

# Apply tax
tax = cart_total * tax_rate
cart_total += tax
print(f"Tax (8%): +${tax:.2f}")

# Final total
print(f"Total: ${cart_total:.2f}")

# Clear cart (reset variables)
cart_items.clear()
cart_total = 0.0
print(f"Cart cleared. Items: {len(cart_items)}, Total: ${cart_total:.2f}")
```

### Example 5: Temperature Readings
```python
import statistics
from typing import List

# Initialize readings
temperatures: List[float] = []
readings_count = 0
min_temp = float('inf')
max_temp = float('-inf')
sum_temp = 0.0

# Simulate temperature readings
readings = [23.5, 24.1, 22.8, 25.3, 24.7, 23.9, 24.5]

# Process each reading
for temp in readings:
    temperatures.append(temp)
    readings_count += 1
    sum_temp += temp
    
    # Update min and max
    if temp < min_temp:
        min_temp = temp
    if temp > max_temp:
        max_temp = temp

# Calculate statistics
avg_temp = sum_temp / readings_count
median_temp = statistics.median(temperatures)

# Display results using multiple variables
print(f"Readings: {readings_count}")
print(f"Temperatures: {temperatures}")
print(f"Min: {min_temp:.1f}°C")
print(f"Max: {max_temp:.1f}°C")
print(f"Average: {avg_temp:.1f}°C")
print(f"Median: {median_temp:.1f}°C")

# Convert to Fahrenheit using list comprehension
fahrenheit = [(temp * 9/5) + 32 for temp in temperatures]
print(f"Fahrenheit: {fahrenheit}")

# Reset all variables (using multiple assignment)
temperatures, readings_count, sum_temp = [], 0, 0.0
min_temp, max_temp = float('inf'), float('-inf')
print(f"Reset: Count={readings_count}, Min={min_temp}, Max={max_temp}")
```

## Common Mistakes

### Mistake 1: Using Undeclared Variables
```python
# Wrong - variable not defined
print(x)  # NameError: name 'x' is not defined

# Right - define first
x = 10
print(x)
```

### Mistake 2: Confusing Variable Names
```python
# Wrong - overwriting built-in functions
list = [1, 2, 3]  # Don't use 'list' as variable
str = "hello"     # Don't use 'str' as variable
print = 5         # Don't override print!

# Right - use descriptive names
my_list = [1, 2, 3]
my_string = "hello"
print_value = 5
```

### Mistake 3: Incorrect Scope Usage
```python
# Wrong - modifying global without global keyword
count = 0
def increment():
    count += 1  # UnboundLocalError!

# Right
count = 0
def increment():
    global count
    count += 1
```

### Mistake 4: Assuming Type is Fixed
```python
# Wrong - assuming variable stays same type
user_id = 123
# ... many lines later
user_id = "ABC123"  # Changes type - may cause bugs

# Right - keep consistent type
user_id_numeric = 123
user_id_string = "ABC123"
```

### Mistake 5: Not Using Meaningful Names
```python
# Wrong - cryptic names
a = 100
b = 0.08
c = a * b

# Right - descriptive names
price = 100
tax_rate = 0.08
tax = price * tax_rate
```

## Best Practices

### ✅ Do This
```python
# Use descriptive variable names
user_age = 25
total_price = 199.99
is_logged_in = True

# Initialize variables before use
counter = 0
result = None

# Use snake_case for variables
first_name = "Alice"
last_name = "Smith"

# Use meaningful single-letter names in loops
for i in range(10):  # i for index
    pass

for key, value in dict.items():
    pass

# Use constants for magic numbers
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30

# Type hints for clarity (optional but helpful)
def calculate_area(radius: float) -> float:
    return 3.14159 * radius ** 2

# Unpack tuples meaningfully
name, age, city = ("Alice", 25, "NYC")
```

### ❌ Avoid This
```python
# Avoid - single letters for important variables
d = 100  # What is d?
t = 0.08 # What is t?

# Avoid - overwriting built-in names
len = 10
max = 100

# Avoid - using reserved keywords
class = "Math"  # SyntaxError

# Avoid - ambiguous names
data = get_info()  # Too vague
temp = process()   # What is temp?

# Avoid - starting with numbers
2nd_place = "Bob"  # Invalid

# Avoid - spaces in names
user name = "Alice"  # Invalid

# Avoid - Hungarian notation (type in name)
strName = "Alice"  # Not Pythonic
intAge = 25        # Not needed
```

## Quick Reference Table

| Concept | Syntax | Example |
|---------|--------|---------|
| Variable assignment | `name = value` | `x = 10` |
| Multiple assignment | `a, b = 1, 2` | `x, y = 10, 20` |
| Same value to multiple | `a = b = c = 0` | `x = y = z = 0` |
| Type annotation | `name: type = value` | `age: int = 25` |
| Delete variable | `del name` | `del x` |
| Check type | `type(var)` | `type(x)` |
| Check existence | `'var' in locals()` | `'x' in globals()` |
| None/null | `None` | `result = None` |
| Global keyword | `global var` | `global counter` |
| Nonlocal keyword | `nonlocal var` | `nonlocal x` |

## Summary

- **No explicit declaration** - variables created by assignment
- **Dynamic typing** - variables can change type at runtime
- **Initialization required** - must assign before use
- **Snake_case** convention for variable names (PEP 8)
- **Case sensitive** - `myVar` and `myvar` are different
- **Global vs local** scope rules
- **`global` keyword** to modify global variables
- **`None`** represents absence of value
- **`del` statement** removes variables
- **Type hints** optional (not enforced)
- **Multiple assignment** allows swapping without temp
- **References** - variables reference objects in memory

## Basic Template
```python
#!/usr/bin/env python3

# Variable declarations (initialization)
name = "John Doe"
age = 30
height = 5.9
is_student = False
scores = [85, 92, 78]
person_info = {"name": name, "age": age}

# Multiple assignment
x, y, z = 10, 20, 30
a = b = c = 0

# Type hints (Python 3.5+)
user_id: int = 12345
username: str = "johndoe"
is_active: bool = True

# Constants (by convention)
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30

# Scope example
global_counter = 0

def increment():
    global global_counter
    global_counter += 1

# None value
result = None

# Variable inspection
print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Scores: {scores}, Type: {type(scores)}")

# Delete variable when done
del temp_variable

# Check if variable exists
if 'name' in locals():
    print(f"name exists: {name}")
```

*This documentation belongs to https://github.com/InterCentury*