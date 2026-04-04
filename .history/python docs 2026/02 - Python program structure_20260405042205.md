
# 02 - Python Program Structure

## What is Program Structure?
Program structure refers to how a Python file is organized - where imports go, where functions are defined, and how code is executed.

## Basic Structure Template
```python
#!/usr/bin/env python3
"""Module docstring - explains what this program does"""

import sys
import math

MAX_VALUE = 100
DEFAULT_NAME = "Guest"

def greet(name):
    """Function docstring"""
    return f"Hello, {name}!"

class Person:
    """Class docstring"""
    pass

if __name__ == "__main__":
    print("Program starts here")
```

## Simple Example
```python
"""Simple greeting program"""

def say_hello(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(say_hello(user_name))
```

## Why Program Structure Matters?

### 1. Code Organization
```python
# Bad structure - messy
import sys
print("Hello")
def my_func():
    return 5
import math
x = 10

# Good structure - organized
import sys
import math

MAX_SIZE = 100

def my_func():
    return 5

if __name__ == "__main__":
    x = 10
    print("Hello")
```

### 2. Reusability
```python
# Functions and classes can be imported by other files
# Main guard prevents unwanted execution

# mymodule.py
def useful_function():
    return 42

if __name__ == "__main__":
    # This only runs when executed directly
    print(useful_function())
```

### 3. Readability
```python
# Clear structure tells others where to find things
# Imports at top
# Constants next
# Functions then classes
# Main execution at bottom
```

## Different Parts of Python Program Structure

### Part 1: Shebang Line
```python
#!/usr/bin/env python3
#!/usr/bin/python3
#!/usr/bin/env python
```

**Purpose:** Tells the system which interpreter to use (Linux/Mac only)

```python
#!/usr/bin/env python3
print("This runs with Python 3")
```

### Part 2: Module Docstring
```python
"""This module handles user authentication.

It provides functions for login, logout, and password reset.
"""
```

**Purpose:** Documents what the module does

```python
"""Calculator module - basic arithmetic operations."""

def add(a, b):
    return a + b
```

### Part 3: Imports
```python
# Different ways to import
import math                     # Import whole module
from os import path            # Import specific function
import random as rnd           # Import with alias
from datetime import datetime, date  # Import multiple
```

**Purpose:** Bring in functionality from other files

```python
import sys
import os
from math import pi, sqrt
from collections import defaultdict

print(pi)
print(sqrt(16))
```

### Part 4: Constants
```python
MAX_CONNECTIONS = 100
API_KEY = "abc123"
DEFAULT_TIMEOUT = 30
PI = 3.14159
```

**Purpose:** Store values that don't change

```python
MAX_USERS = 1000
TIMEOUT_SECONDS = 60
DEFAULT_PORT = 8080

print(f"Max users: {MAX_USERS}")
```

### Part 5: Global Variables (Use Sparingly)
```python
# Avoid when possible, but sometimes needed
global_counter = 0
database_connection = None
```

**Purpose:** Shared state across functions (use cautiously)

### Part 6: Function Definitions
```python
def calculate_area(radius):
    """Calculate area of a circle."""
    return 3.14159 * radius * radius

def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"
```

**Purpose:** Reusable blocks of code

### Part 7: Class Definitions
```python
class Student:
    """Represents a student."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"I'm {self.name}"
```

**Purpose:** Define custom data types

### Part 8: Main Guard
```python
if __name__ == "__main__":
    # Code here runs only when script executed directly
    main()
```

**Purpose:** Prevents code from running when imported

## Practical Examples

### Example 1: Simple Utility Program
```python
#!/usr/bin/env python3
"""File size calculator - shows file sizes in different units."""

import os
import sys

# Constants
KB = 1024
MB = 1024 * KB
GB = 1024 * MB

def get_size_in_mb(size_bytes):
    """Convert bytes to megabytes."""
    return size_bytes / MB

def get_size_in_gb(size_bytes):
    """Convert bytes to gigabytes."""
    return size_bytes / GB

def main():
    """Main program function."""
    if len(sys.argv) < 2:
        print("Usage: python filesize.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    size = os.path.getsize(filename)
    
    print(f"File: {filename}")
    print(f"Size in bytes: {size}")
    print(f"Size in KB: {size / KB:.2f}")
    print(f"Size in MB: {get_size_in_mb(size):.2f}")
    print(f"Size in GB: {get_size_in_gb(size):.2f}")

if __name__ == "__main__":
    main()
```

### Example 2: Module for Import
```python
# math_utils.py - can be imported by other files
"""Mathematical utility functions."""

PI = 3.14159265359
E = 2.71828182846

def circle_area(radius):
    """Calculate area of circle."""
    return PI * radius ** 2

def circle_circumference(radius):
    """Calculate circumference of circle."""
    return 2 * PI * radius

def factorial(n):
    """Calculate factorial of n."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    # Test code - only runs when executed directly
    print(f"PI = {PI}")
    print(f"Circle area (r=5): {circle_area(5)}")
    print(f"Factorial of 5: {factorial(5)}")
```

### Example 3: Using the Module
```python
# main.py - imports and uses math_utils
"""Main program using math utilities."""

from math_utils import circle_area, factorial, PI

def main():
    radius = 10
    area = circle_area(radius)
    print(f"Circle area: {area}")
    
    num = 5
    fact = factorial(num)
    print(f"{num}! = {fact}")
    
    print(f"PI value: {PI}")

if __name__ == "__main__":
    main()
```

### Example 4: Multi-file Project Structure
```python
# config.py - configuration constants
"""Application configuration."""

APP_NAME = "MyApp"
VERSION = "1.0.0"
DEBUG = True
MAX_RETRIES = 3
```

```python
# database.py - database operations
"""Database handling module."""

from config import DEBUG, MAX_RETRIES

class Database:
    def __init__(self, connection_string):
        self.conn_string = connection_string
    
    def connect(self):
        if DEBUG:
            print(f"Connecting to {self.conn_string}")
        # Connection logic here
        return True

def query(sql):
    """Execute SQL query."""
    print(f"Executing: {sql}")
    return []

if __name__ == "__main__":
    # Test database module
    db = Database("localhost:5432")
    db.connect()
```

```python
# main.py - entry point
"""Main application entry point."""

from config import APP_NAME, VERSION
from database import Database, query

def main():
    print(f"Starting {APP_NAME} v{VERSION}")
    
    db = Database("localhost:5432")
    db.connect()
    
    results = query("SELECT * FROM users")
    print(f"Found {len(results)} users")

if __name__ == "__main__":
    main()
```

## Common Mistakes

### Mistake 1: Circular Imports
```python
# file_a.py
from file_b import func_b

def func_a():
    return func_b()

# file_b.py
from file_a import func_a  # ❌ Circular import!

def func_b():
    return func_a()
```

**Fix:** Restructure or import inside function
```python
# file_b.py
def func_b():
    from file_a import func_a
    return func_a()
```

### Mistake 2: Importing Inside Loop
```python
# ❌ Bad - imports repeatedly
for i in range(1000):
    import math
    print(math.sqrt(i))

# ✅ Good - import once at top
import math
for i in range(1000):
    print(math.sqrt(i))
```

### Mistake 3: Missing Main Guard
```python
# mymodule.py
def helper():
    return 42

print(helper())  # ❌ Runs when imported!

# Correct version
def helper():
    return 42

if __name__ == "__main__":
    print(helper())  # ✅ Only runs when executed directly
```

### Mistake 4: Modifying Constants
```python
MAX_SIZE = 100
MAX_SIZE = 200  # ❌ Should not change constants

# Use regular variable if it changes
max_size = 100
max_size = 200  # ✅ OK
```

### Mistake 5: Wrong Import Order
```python
# ❌ Bad order
print("Starting")
import sys  # Imports should be at top
from math import pi

# ✅ Good order
import sys
from math import pi

print("Starting")
```

## Best Practices

### ✅ Do This
```python
#!/usr/bin/env python3
"""Module docstring explaining purpose."""

# Standard library imports
import sys
import os
import math

# Third-party imports (if any)
# import requests
# import numpy

# Local imports
# from mymodule import helper

# Constants
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

# Functions
def main():
    pass

# Main guard
if __name__ == "__main__":
    main()
```

### ❌ Avoid This
```python
# No docstring
import math
MAX=100  # Unclear constant name
def myfunc(): pass  # No docstring
print("Hello")  # Code at module level
if __name__=="__main__":  # Main guard not at bottom
    pass
```

## Quick Reference Table

| Component | Placement | Syntax | Purpose |
|-----------|-----------|--------|---------|
| Shebang | Very first line | `#!/usr/bin/env python3` | Specify interpreter |
| Docstring | After shebang | `"""text"""` | Document module |
| Imports | After docstring | `import module` | Use external code |
| Constants | After imports | `NAME = value` | Store fixed values |
| Functions | After constants | `def name():` | Define reusable logic |
| Classes | After functions | `class Name:` | Define objects |
| Main guard | Bottom of file | `if __name__ == "__main__":` | Control execution |

## When to Use Each Structure

| File Type | Has Shebang? | Has Main Guard? | Example |
|-----------|--------------|-----------------|---------|
| Script (executable) | ✅ Yes | ✅ Yes | `script.py` |
| Module (importable) | ❌ No | ❌ No (or for tests) | `mymodule.py` |
| Package __init__ | ❌ No | ❌ No | `__init__.py` |
| Test file | ❌ No | ✅ Yes | `test_*.py` |

## Summary

- **Shebang** - for Linux/Mac executables
- **Docstring** - explains module purpose
- **Imports** - always at top of file
- **Constants** - UPPER_CASE names
- **Functions/Classes** - define before use
- **Main guard** - prevents execution on import
- **Order matters** - imports → constants → functions → main guard
- **One purpose per file** - keep modules focused

## Basic Template for Any Python File

### For Executable Scripts:
```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

import sys

def main():
    """Main entry point."""
    print("Script running")

if __name__ == "__main__":
    main()
```

### For Importable Modules:
```python
"""Module description - functions and classes provided."""

def useful_function():
    """What this function does."""
    return "result"

class UsefulClass:
    """What this class does."""
    pass

# Optional test code
if __name__ == "__main__":
    # Test the module
    print(useful_function())
```

*This documentation belongs to https://github.com/InterCentury*
```

---

Is this the correct format now?