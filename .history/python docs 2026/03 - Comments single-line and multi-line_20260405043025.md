

# 03 - Comments: Single-line and Multi-line in Python

## What are Comments?
Comments are explanatory text in code that the Python interpreter ignores. They help humans understand what the code does, why certain decisions were made, or provide documentation.

## Why Use Comments?

### 1. Explain Complex Logic
```python
# Without comment - confusing
total = price * 0.92 + 5.99

# With comment - clear
total = price * 0.92 + 5.99  # Apply 8% discount + shipping fee
```

### 2. Document Assumptions
```python
MAX_RETRIES = 3  # API rate limit allows max 3 retries per minute
```

### 3. TODO and Notes
```python
# TODO: Add error handling for network timeout
# FIXME: This calculation overflows with large numbers
# NOTE: This function assumes Python 3.8+
```

### 4. Debugging
```python
# print(f"Debug: x = {x}, y = {y}")  # Temporarily disable debugging
```

## Single-line Comments

### Basic Syntax
```python
# This is a single-line comment
x = 10  # Comment after code
# Comment before code
y = 20
```

### Examples

```python
# Calculate area of a circle
radius = 5
area = 3.14159 * radius ** 2  # π * r²

# Check if user is eligible
age = 25
if age >= 18:  # Legal age check
    print("You can vote!")
```

### Inline Comments (End of Line)
```python
price = 100  # Original price in dollars
discount = 0.2  # 20% discount
final_price = price * (1 - discount)  # Apply discount

# Use sparingly - don't state the obvious
x = 5  # Set x to 5  (❌ Useless comment)
x = 5  # Counter for loop (✅ Helpful context)
```

## Multi-line Comments

### Method 1: Multiple Single-line Comments
```python
# This is a multi-line comment
# using multiple single-line comment characters
# Each line needs its own # symbol

def calculate_interest(principal, rate, time):
    # Calculate simple interest
    # Formula: I = P * R * T
    # Where:
    #   P = principal amount
    #   R = annual interest rate
    #   T = time in years
    return principal * rate * time
```

### Method 2: Triple Quotes (''' or """)
```python
"""
This is a multi-line comment using triple double-quotes.
Python ignores this string if it's not assigned to a variable.
You can write multiple lines here.
"""

'''
This also works with triple single-quotes.
Both styles are commonly used for docstrings and multi-line comments.
'''
```

### Important Note About Triple Quotes
```python
# Triple quotes create a string literal, not a true comment
"""
This is actually a string that does nothing
But Python still creates it in memory (minor performance impact)
"""

# For true comments, use # at start of each line
# This is preferred for actual comments
# No string object is created

# Best practice: Use # for comments, """ for docstrings
```

## Docstrings (Documentation Strings)

### Function Docstrings
```python
def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

print(greet.__doc__)  # Access the docstring
```

### Multi-line Docstrings
```python
def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).
    
    Parameters:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: BMI value
    
    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    return weight / (height ** 2)
```

### Class Docstrings
```python
class BankAccount:
    """
    A simple bank account class.
    
    Attributes:
        owner (str): Account owner's name
        balance (float): Current account balance
    """
    
    def __init__(self, owner, balance=0):
        """Initialize account with owner name and optional balance."""
        self.owner = owner
        self.balance = balance
```

### Module Docstrings
```python
"""
Module: calculator.py

Provides basic mathematical operations.

Functions:
    add(x, y): Returns sum of x and y
    subtract(x, y): Returns difference of x and y
    multiply(x, y): Returns product of x and y
    divide(x, y): Returns quotient of x and y

Author: Your Name
Date: 2024
"""

def add(x, y):
    return x + y
```

## Practical Examples

### Example 1: Explaining Algorithm
```python
def is_prime(n):
    """
    Check if a number is prime.
    
    A prime number is only divisible by 1 and itself.
    This function implements trial division algorithm.
    """
    if n < 2:
        return False  # Numbers less than 2 are not prime
    
    # Check divisibility from 2 to square root of n
    # If any divisor found, number is not prime
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Found a divisor
    
    return True  # No divisors found
```

### Example 2: Configuration Comments
```python
# Application Settings
DEBUG_MODE = True      # Enable debug logging (set to False in production)
MAX_USERS = 100        # Free tier limit (increase for premium)
TIMEOUT = 30           # Seconds before connection times out

# API Configuration
API_KEY = "xyz123"     # Get from environment variables in production
API_URL = "https://api.example.com/v1"  # Production endpoint
```

### Example 3: Warning and Caution Comments
```python
def delete_user(user_id):
    """
    Permanently delete user from database.
    
    WARNING: This action cannot be undone!
    All user data will be permanently removed.
    """
    # CAUTION: Verify user_id exists before deletion
    if user_id in database:
        # TODO: Add confirmation dialog before deletion
        database.remove(user_id)
        # NOTE: Also need to delete associated files
```

### Example 4: Complex Logic Documentation
```python
def calculate_shipping_cost(weight, distance, is_international):
    """
    Calculate shipping cost based on multiple factors.
    
    Formula:
        Base cost = $5 + ($0.50 per kg) + ($0.10 per km)
        International orders: +50% surcharge
        Heavy items (>20kg): +$10 handling fee
    
    Example:
        weight=10kg, distance=100km, domestic
        = 5 + (0.5*10) + (0.1*100) = 5 + 5 + 10 = $20
    """
    # Base calculation
    base_cost = 5 + (0.5 * weight) + (0.1 * distance)
    
    # Apply international surcharge if needed
    if is_international:
        base_cost *= 1.5  # 50% surcharge
    
    # Add heavy item handling fee
    if weight > 20:
        base_cost += 10  # Extra handling for heavy packages
    
    return round(base_cost, 2)
```

### Example 5: Debugging with Comments
```python
def process_data(data):
    # Debug: Print input data
    # print(f"Input: {data}")  # Uncomment for debugging
    
    result = []
    for item in data:
        # Debug: Track iteration
        # print(f"Processing item {item}")
        
        if item > 0:
            result.append(item * 2)
            # print(f"Added {item*2} to result")  # Debug output
    
    # Debug: Show final result
    # print(f"Result: {result}")
    return result
```

## Commenting Best Practices

### ✅ Do This
```python
# Calculate total with tax (8%)
total = subtotal * 1.08

# Check if user has admin privileges
if user.role == 'admin':
    grant_access()

# TODO: Implement caching for better performance
def get_user_data(user_id):
    pass

def calculate_discount(price, customer_type):
    """Calculate discount based on customer type."""
    if customer_type == 'premium':
        return price * 0.8  # 20% discount for premium
    return price  # No discount for regular
```

### ❌ Avoid This
```python
# Set x to 5 (Obvious - don't state the obvious)
x = 5

# This is a comment (Useless)
# Next line adds two numbers (Don't explain simple operations)
a = 10 + 20

# Bad comment (Outdated - code changed but comment didn't)
# Multiply by 2 to double the value
result = value * 3  # Actually triples it now

# Commented out code without explanation
# old_function()
# another_function()
# third_function()
```

## Special Comment Types

### TODO Comments
```python
# TODO: Add input validation
# TODO(John): Refactor this function by Q2 2024
# TODO: Optimize this loop for large datasets

def process_orders():
    # TODO: Implement order sorting by priority
    # TODO: Add email notification for each order
    pass
```

### FIXME Comments
```python
# FIXME: This calculation fails for negative numbers
# FIXME: Memory leak in this function
def buggy_function(x):
    return x / 0  # FIXME: Division by zero error
```

### NOTE Comments
```python
# NOTE: This function requires Python 3.7+
# NOTE: Assumes input is already validated
# NOTE: Performance critical - optimize carefully
```

### BUG Comments
```python
# BUG: Incorrect result when x > 100
# BUG: Race condition when multiple threads access
```

### HACK Comments
```python
# HACK: Quick fix for demo - refactor properly later
# HACK: Workaround for API limitation
```

## Commenting Conventions (PEP 8)

### Block Comments
```python
# Block comments explain following code
# They are indented to the same level as the code
# Each line starts with # and a space

if condition:
    # This comment applies to the indented block
    do_something()
```

### Inline Comments
```python
x = x + 1  # Increment counter (sparse, not dense)
# Use inline comments sparingly and only when helpful
```

### Documentation Strings
```python
def public_function():
    """Single line docstring for simple functions."""
    pass

def complex_function():
    """
    Multi-line docstring for complex functions.
    
    More detailed explanation here.
    Use triple double-quotes by convention.
    """
    pass
```

## Comment Tools and Shortcuts

### VS Code / PyCharm Shortcuts
```python
# Ctrl + / (Windows/Linux) - Toggle comment
# Cmd + / (Mac) - Toggle comment

# Select multiple lines and press shortcut to comment/uncomment all
# line 1
# line 2
# line 3
```

### Comment Templates
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module docstring with:
- Purpose of module
- Main functions/classes
- Author and date
- Version info
"""

def function_name(param1, param2):
    """
    Function description.
    
    Args:
        param1 (type): Description
        param2 (type): Description
    
    Returns:
        type: Description
    
    Raises:
        Exception: Description
    
    Examples:
        >>> function_name(1, 2)
        3
    """
    pass
```

## Quick Reference Table

| Comment Type | Syntax | Use Case |
|--------------|--------|----------|
| Single-line | `# comment` | Brief explanations |
| Inline | `code # comment` | Explain specific line |
| Multi-line (method 1) | Multiple `#` lines | Long explanations |
| Multi-line (method 2) | `"""comment"""` | Temporary blocks |
| Docstring | `"""docstring"""` | Function/class documentation |
| TODO | `# TODO: task` | Future improvements |
| FIXME | `# FIXME: issue` | Known bugs |
| NOTE | `# NOTE: info` | Important notes |

## Common Mistakes

### Mistake 1: Stating the Obvious
```python
# Wrong
i = i + 1  # Add 1 to i

# Right
i = i + 1  # Increment counter for next iteration
```

### Mistake 2: Outdated Comments
```python
# Wrong
# Returns user's full name
def get_user_info():
    return user.email  # Changed but comment not updated

# Right
# Returns user's email address
def get_user_info():
    return user.email
```

### Mistake 3: Over-commenting
```python
# Wrong
x = 5  # Set x to 5
y = 10  # Set y to 10
z = x + y  # Add x and y

# Right - clear code needs less comments
counter = 5
limit = 10
total = counter + limit
```

### Mistake 4: Commented Out Dead Code
```python
# Wrong - keep old code around
# def old_function():
#     # 50 lines of old code
#     pass

# Right - use version control (git)
def new_function():
    pass
# Delete old code, Git remembers it
```

## Summary

- **Single-line comments** start with `#`
- **Multi-line comments** use multiple `#` or triple quotes
- **Docstrings** (`"""doc"""`) document functions/classes/modules
- **Comments explain WHY**, not WHAT (code shows what)
- **Keep comments updated** when code changes
- **Use TODO/FIXME/NOTE** for special markers
- **Don't state the obvious** - let code speak
- **Use version control** instead of commented-out code
- **Follow PEP 8** for comment style
- **Docstrings are accessible** via `help()` and `.__doc__`

## Basic Template
```python
#!/usr/bin/env python3
"""
Module: example.py

Brief description of what this module does.
"""

# Import statements
import sys

# Constants (with comments)
MAX_RETRIES = 3  # Maximum number of API retry attempts
TIMEOUT = 30     # Connection timeout in seconds

def main():
    """
    Main function - entry point of the program.
    
    This function orchestrates the program flow.
    """
    # TODO: Add command line argument parsing
    
    # Calculate something
    result = 10 + 20
    
    # Display result
    print(f"Result: {result}")  # Debug: Check calculation
    
    return result

if __name__ == "__main__":
    # Execute main function when script runs directly
    main()
```

*This documentation belongs to https://github.com/InterCentury*