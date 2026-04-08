# 28 - Walrus Operator (:=) (Python 3.8+)

## What is the Walrus Operator?
The walrus operator (`:=`) is an assignment expression introduced in Python 3.8. It allows you to assign a value to a variable as part of a larger expression. The name comes from the operator's resemblance to the eyes and tusks of a walrus.

## Basic Syntax

```python
# Traditional way
value = 10
print(value)  # 10

# Walrus operator (assign and use in same expression)
print(value := 10)  # 10

# Without walrus
data = get_data()
if data:
    process(data)

# With walrus
if (data := get_data()):
    process(data)
```

## Why Use the Walrus Operator?

### Reducing Code Duplication
```python
# Without walrus - duplicate function call
match = pattern.search(text)
if match:
    print(f"Found: {match.group()}")

# With walrus - single function call
if (match := pattern.search(text)):
    print(f"Found: {match.group()}")

# Without walrus - duplicate calculation
value = expensive_calculation()
if value > 100:
    print(f"Large value: {value}")

# With walrus - single calculation
if (value := expensive_calculation()) > 100:
    print(f"Large value: {value}")
```

### Improving Readability
```python
# Without walrus - temporary variable needed
temp = input("Enter name: ")
while temp:
    print(f"Processing: {temp}")
    temp = input("Enter name: ")

# With walrus - cleaner loop
while (name := input("Enter name: ")):
    print(f"Processing: {name}")
```

## Practical Examples

### Example 1: While Loops
```python
# Reading lines from a file
print("=== Reading File Lines ===")
with open('example.txt', 'w') as f:
    f.write("Line 1\nLine 2\nLine 3\n")

# Without walrus
print("Traditional way:")
with open('example.txt', 'r') as f:
    line = f.readline()
    while line:
        print(f"  {line.strip()}")
        line = f.readline()

# With walrus
print("\nWith walrus operator:")
with open('example.txt', 'r') as f:
    while (line := f.readline()):
        print(f"  {line.strip()}")

# User input loop
print("\n=== User Input Loop ===")
# Without walrus
data = input("Enter something (or 'quit' to exit): ")
while data != 'quit':
    print(f"You entered: {data}")
    data = input("Enter something (or 'quit' to exit): ")

# With walrus
while (data := input("Enter something (or 'quit' to exit): ")) != 'quit':
    print(f"You entered: {data}")
```

### Example 2: List Comprehensions
```python
# Using walrus in list comprehensions
print("=== List Comprehensions ===")

# Without walrus - calculate twice
squares = [x**2 for x in range(10) if x**2 > 10]
print(f"Squares > 10: {squares}")

# With walrus - calculate once
squares = [y for x in range(10) if (y := x**2) > 10]
print(f"Squares > 10: {squares}")

# Filtering with expensive calculation
def expensive_calc(n):
    print(f"Calculating for {n}")
    return n ** 2

# Without walrus (calculates twice)
result1 = [expensive_calc(x) for x in range(5) if expensive_calc(x) > 5]

# With walrus (calculates once)
result2 = [y for x in range(5) if (y := expensive_calc(x)) > 5]
print(f"\nResult: {result2}")

# Nested comprehensions
data = [1, 2, 3, 4, 5]
# Without walrus
processed = [x * 2 for x in data if x * 2 > 5]
print(f"Processed: {processed}")

# With walrus
processed = [y for x in data if (y := x * 2) > 5]
print(f"Processed: {processed}")
```

### Example 3: Regular Expressions
```python
import re

print("=== Regular Expression Matching ===")

text = "My email is alice@example.com and my phone is 555-123-4567"

# Without walrus
email_match = re.search(r'\w+@\w+\.\w+', text)
if email_match:
    print(f"Email found: {email_match.group()}")

phone_match = re.search(r'\d{3}-\d{3}-\d{4}', text)
if phone_match:
    print(f"Phone found: {phone_match.group()}")

# With walrus
if (email_match := re.search(r'\w+@\w+\.\w+', text)):
    print(f"Email found: {email_match.group()}")

if (phone_match := re.search(r'\d{3}-\d{3}-\d{4}', text)):
    print(f"Phone found: {phone_match.group()}")

# Multiple matches
print("\n=== Multiple Matches ===")
text = "The cat and the hat sat on the mat"

# Without walrus
matches = []
pattern = re.compile(r'\w+at')
for word in text.split():
    if pattern.match(word):
        matches.append(word)
print(f"Words ending with 'at': {matches}")

# With walrus (list comprehension)
matches = [word for word in text.split() if (pattern.match(word))]
print(f"Words ending with 'at': {matches}")

# While loop with regex
print("\n=== Finding All Matches ===")
text = "Numbers: 123, 4567, 89, 1000"
pattern = re.compile(r'\d+')
pos = 0

# Without walrus
matches = []
while True:
    match = pattern.search(text, pos)
    if not match:
        break
    matches.append(match.group())
    pos = match.end()
print(f"Numbers: {matches}")

# With walrus
pos = 0
matches = []
while (match := pattern.search(text, pos)):
    matches.append(match.group())
    pos = match.end()
print(f"Numbers: {matches}")
```

### Example 4: Data Validation
```python
class DataValidator:
    """Validate data using walrus operator"""
    
    @staticmethod
    def validate_user(user_data):
        """Validate user data with multiple checks"""
        
        errors = []
        
        # Name validation
        if not (name := user_data.get('name')):
            errors.append("Name is required")
        elif len(name) < 2:
            errors.append("Name too short")
        elif len(name) > 50:
            errors.append("Name too long")
        
        # Age validation
        if (age := user_data.get('age')) is None:
            errors.append("Age is required")
        elif not isinstance(age, (int, float)):
            errors.append("Age must be a number")
        elif not (0 <= age <= 150):
            errors.append("Age must be between 0 and 150")
        
        # Email validation
        if (email := user_data.get('email')):
            if '@' not in email:
                errors.append("Invalid email format")
        else:
            errors.append("Email is required")
        
        # Score validation (optional)
        if (score := user_data.get('score')) is not None:
            if not (0 <= score <= 100):
                errors.append("Score must be between 0 and 100")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def validate_form(form_data):
        """Validate form fields with walrus operator"""
        
        # Check required fields
        required_fields = ['username', 'password', 'email']
        missing = [field for field in required_fields if not form_data.get(field)]
        
        if missing:
            return False, f"Missing fields: {', '.join(missing)}"
        
        # Validate username
        if not (3 <= len(username := form_data['username']) <= 20):
            return False, "Username must be 3-20 characters"
        
        if not username.isalnum():
            return False, "Username must be alphanumeric"
        
        # Validate password
        if len(password := form_data['password']) < 8:
            return False, "Password must be at least 8 characters"
        
        # Check password strength
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        
        if not (has_upper and has_lower and has_digit):
            return False, "Password must have uppercase, lowercase, and digit"
        
        # Validate email
        if '@' not in (email := form_data['email']):
            return False, "Invalid email format"
        
        return True, "Form is valid"

# Demo
validator = DataValidator()

print("=== Data Validation Demo ===")
print("-" * 40)

# Test cases
test_users = [
    {"name": "Alice", "age": 25, "email": "alice@example.com", "score": 95},
    {"name": "A", "age": 25, "email": "alice@example.com"},  # Name too short
    {"name": "Bob", "age": -5, "email": "bob@example.com"},  # Invalid age
    {"name": "Charlie", "email": "invalid"},  # Missing age
    {"name": "VeryLongNameThatExceedsFiftyCharactersLimit", "age": 30, "email": "test@test.com"},  # Name too long
]

for i, user in enumerate(test_users, 1):
    valid, errors = validator.validate_user(user)
    print(f"\nUser {i}:")
    print(f"  Valid: {valid}")
    if not valid:
        print(f"  Errors: {errors}")

# Form validation
print("\n=== Form Validation ===")
test_forms = [
    {"username": "alice123", "password": "Pass1234", "email": "alice@example.com"},
    {"username": "ab", "password": "Pass1234", "email": "alice@example.com"},  # Username too short
    {"username": "bob", "password": "weak", "email": "bob@example.com"},  # Password weak
    {"username": "charlie", "password": "Pass1234", "email": "invalid"},  # Invalid email
    {"username": "dave", "password": "Pass1234"},  # Missing email
]

for i, form in enumerate(test_forms, 1):
    valid, message = validator.validate_form(form)
    print(f"\nForm {i}:")
    print(f"  Valid: {valid}")
    print(f"  Message: {message}")
```

### Example 5: Data Processing Pipeline
```python
class DataPipeline:
    """Data processing with walrus operator"""
    
    @staticmethod
    def process_numbers(numbers):
        """Process numbers with filtering and transformation"""
        
        # Without walrus
        print("Traditional approach:")
        result = []
        for n in numbers:
            squared = n ** 2
            if squared > 50:
                result.append(squared)
        print(f"  Result: {result}")
        
        # With walrus in list comprehension
        print("\nWith walrus (list comprehension):")
        result = [squared for n in numbers if (squared := n ** 2) > 50]
        print(f"  Result: {result}")
        
        # With walrus and multiple operations
        print("\nWith walrus (multiple operations):")
        result = []
        for n in numbers:
            if (squared := n ** 2) > 50:
                if (halved := squared // 2) < 100:
                    result.append((n, squared, halved))
        print(f"  Result: {result}")
        
        return result
    
    @staticmethod
    def process_strings(strings):
        """Process strings with walrus operator"""
        
        # Filter and transform
        result = [upper for s in strings if len(s) > 3 and (upper := s.upper())]
        print(f"\nUppercase strings (length > 3): {result}")
        
        # Find first match
        if (found := next((s for s in strings if 'python' in s.lower()), None)):
            print(f"Found 'python' in: {found}")
        else:
            print("No 'python' found")
        
        # Count with condition
        count = sum(1 for s in strings if len(s) > 3 and (s.upper()))
        print(f"Strings longer than 3 characters: {count}")
    
    @staticmethod
    def process_dictionary(data):
        """Process dictionary with walrus operator"""
        
        # Filter items with condition
        filtered = {k: v for k, v in data.items() if (isinstance(v, int)) and v > 10}
        print(f"\nItems with integer > 10: {filtered}")
        
        # Transform values
        transformed = {k: (squared := v**2) for k, v in data.items() if isinstance(v, (int, float))}
        print(f"Squared values: {transformed}")
        
        # Find max with condition
        if (max_val := max((v for v in data.values() if isinstance(v, (int, float))), default=None)):
            print(f"Maximum numeric value: {max_val}")

# Demo
pipeline = DataPipeline()

print("=== Data Processing Pipeline Demo ===")
print("-" * 40)

# Process numbers
numbers = [1, 5, 8, 12, 3, 15, 7]
print(f"Numbers: {numbers}")
pipeline.process_numbers(numbers)

# Process strings
strings = ["python", "code", "hello world", "hi", "programming", "data"]
print(f"\nStrings: {strings}")
pipeline.process_strings(strings)

# Process dictionary
data = {"a": 5, "b": 15, "c": "text", "d": 25, "e": 3, "f": 30}
print(f"\nDictionary: {data}")
pipeline.process_dictionary(data)
```

### Example 6: Caching and Memoization
```python
import time
from functools import lru_cache

class CacheWithWalrus:
    """Demonstrate caching with walrus operator"""
    
    def __init__(self):
        self.cache = {}
    
    def expensive_operation(self, n):
        """Simulate expensive calculation"""
        print(f"  Calculating for {n}...")
        time.sleep(0.5)  # Simulate work
        return n ** 2
    
    def get_value(self, n):
        """Get value with caching using walrus"""
        
        # Traditional way
        # if n in self.cache:
        #     return self.cache[n]
        # result = self.expensive_operation(n)
        # self.cache[n] = result
        # return result
        
        # With walrus operator
        if (result := self.cache.get(n)) is not None:
            return result
        
        result = self.expensive_operation(n)
        self.cache[n] = result
        return result
    
    def get_multiple(self, numbers):
        """Get multiple values with walrus in list comprehension"""
        
        # Using walrus to cache while processing
        return [self.get_value(n) for n in numbers]

# Simple memoization decorator with walrus
def memoize(func):
    """Simple memoization decorator using walrus"""
    cache = {}
    
    def wrapper(*args):
        key = str(args)
        # Walrus operator for cache lookup
        if (result := cache.get(key)) is not None:
            print(f"  Cache hit for {args}")
            return result
        
        print(f"  Computing for {args}")
        result = func(*args)
        cache[key] = result
        return result
    
    return wrapper

@memoize
def fibonacci(n):
    """Fibonacci with memoization"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Demo
print("=== Caching with Walrus Demo ===")
print("-" * 40)

cache_demo = CacheWithWalrus()

print("First calls (computing):")
for n in [5, 10, 5, 15, 10]:
    result = cache_demo.get_value(n)
    print(f"  get_value({n}) = {result}")

print("\nSecond calls (from cache):")
for n in [5, 10, 15]:
    result = cache_demo.get_value(n)
    print(f"  get_value({n}) = {result}")

print("\nGetting multiple values:")
numbers = [3, 7, 3, 12, 7, 5]
results = cache_demo.get_multiple(numbers)
print(f"  Results: {results}")

print("\n=== Memoization Decorator Demo ===")
print("Fibonacci with memoization:")
for n in [10, 5, 10, 8, 5]:
    result = fibonacci(n)
    print(f"  fibonacci({n}) = {result}")
```

### Example 7: Real-World Scenarios
```python
import re
from datetime import datetime

class RealWorldExamples:
    """Real-world examples using walrus operator"""
    
    @staticmethod
    def parse_log_line(line):
        """Parse log line with walrus operator"""
        
        # Extract timestamp
        if (timestamp_match := re.search(r'\[(.*?)\]', line)):
            timestamp = timestamp_match.group(1)
        else:
            timestamp = None
        
        # Extract log level
        if (level_match := re.search(r'(INFO|WARNING|ERROR|DEBUG)', line)):
            level = level_match.group(1)
        else:
            level = "UNKNOWN"
        
        # Extract message
        if (message_match := re.search(r']\s*(.*?)$', line)):
            message = message_match.group(1)
        else:
            message = line
        
        return {"timestamp": timestamp, "level": level, "message": message}
    
    @staticmethod
    def process_logs(logs):
        """Process multiple logs with walrus"""
        
        errors = []
        warnings = []
        
        for log in logs:
            parsed = RealWorldExamples.parse_log_line(log)
            
            # Collect errors and warnings
            if parsed['level'] == 'ERROR':
                errors.append(parsed)
            elif parsed['level'] == 'WARNING':
                warnings.append(parsed)
            
            # Display critical errors immediately
            if (msg := parsed['message']) and 'critical' in msg.lower():
                print(f"CRITICAL: {msg}")
        
        return errors, warnings
    
    @staticmethod
    def process_user_input():
        """Process user input with validation using walrus"""
        
        print("\n=== User Input Processing ===")
        
        # Get and validate age
        while not ((age_str := input("Enter age: ")).isdigit() and (age := int(age_str)) >= 0):
            print("Invalid age. Please enter a positive number.")
        
        print(f"Age accepted: {age}")
        
        # Get and validate email
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        while not (email := input("Enter email: ")) or not email_pattern.match(email):
            print("Invalid email format.")
        
        print(f"Email accepted: {email}")
        
        # Get and validate yes/no
        while (response := input("Continue? (yes/no): ").lower()) not in ('yes', 'no'):
            print("Please enter 'yes' or 'no'")
        
        return age, email, response == 'yes'
    
    @staticmethod
    def calculate_discount(price, customer_tier):
        """Calculate discount with multiple conditions"""
        
        # Tier-based discount
        if (tier_discount := {'premium': 0.2, 'gold': 0.15, 'silver': 0.1}.get(customer_tier, 0)):
            print(f"Tier discount: {tier_discount * 100}%")
        else:
            tier_discount = 0
        
        # Apply additional discount for large orders
        if (price > 1000) and (extra_discount := 0.05):
            print(f"Large order discount: {extra_discount * 100}%")
        else:
            extra_discount = 0
        
        total_discount = tier_discount + extra_discount
        final_price = price * (1 - total_discount)
        
        return final_price, total_discount

# Demo
print("=== Real-World Examples Demo ===")
print("-" * 40)

# Log processing
log_entries = [
    "[2024-01-15 10:30:00] INFO Application started",
    "[2024-01-15 10:31:00] WARNING High memory usage detected",
    "[2024-01-15 10:32:00] ERROR Database connection failed",
    "[2024-01-15 10:33:00] INFO CRITICAL: System recovery initiated",
    "[2024-01-15 10:34:00] DEBUG Processing request",
]

print("Processing logs:")
errors, warnings = RealWorldExamples.process_logs(log_entries)
print(f"Found {len(errors)} errors and {len(warnings)} warnings")

# User input (simulated with pre-defined inputs)
print("\n=== Simulated User Input ===")
import sys
from io import StringIO

# Save original input
original_input = __builtins__.input

try:
    # Mock input for demo
    inputs = iter(["25", "user@example.com", "yes"])
    __builtins__.input = lambda prompt="": next(inputs)
    
    age, email, continue_processing = RealWorldExamples.process_user_input()
    print(f"\nProcessed: Age={age}, Email={email}, Continue={continue_processing}")
finally:
    # Restore original input
    __builtins__.input = original_input

# Discount calculation
print("\n=== Discount Calculation ===")
prices = [500, 1200, 800]
tiers = ['standard', 'silver', 'gold']

for price, tier in zip(prices, tiers):
    final, discount = RealWorldExamples.calculate_discount(price, tier)
    print(f"Price: ${price}, Tier: {tier}, Discount: {discount*100:.0f}%, Final: ${final:.2f}")
```

## Scope and Limitations

### Scope of Walrus Variables
```python
# Variables assigned with walrus are available in the enclosing scope
if (x := 10) > 5:
    print(f"x is {x}")  # x is accessible here

print(f"x is still {x}")  # x is accessible here too

# In list comprehensions, variable is local to comprehension
[y for x in range(3) if (y := x * 2) > 2]
# print(y)  # NameError: y not defined

# In generator expressions, variable is local
gen = (z for x in range(3) if (z := x * 2) > 2)
# print(z)  # NameError: z not defined
```

### Parentheses Requirement
```python
# Walrus operator requires parentheses in many contexts

# Wrong - syntax error
# if value := get_value() > 10:  # Error!

# Right - with parentheses
if (value := get_value()) > 10:
    print(f"Value {value} > 10")

# Wrong in list comprehension
# [x for x in range(10) if y := x**2 > 10]  # Error!

# Right in list comprehension
[y for x in range(10) if (y := x**2) > 10]
```

## Common Mistakes

### Mistake 1: Missing Parentheses
```python
# Wrong - missing parentheses
# if result := expensive() > threshold:  # Assigns (expensive() > threshold) to result

# Right - proper grouping
if (result := expensive()) > threshold:
    print(f"Result {result} exceeds threshold")
```

### Mistake 2: Using Walrus When Not Needed
```python
# Unnecessary - simple assignment
# if (x := 5) > 0:  # Overkill

# Better
x = 5
if x > 0:
    pass

# Unnecessary - simple loop
# while (i := i + 1) < 10:  # Confusing

# Better
i = 0
while i < 10:
    i += 1
```

### Mistake 3: Overusing in Complex Expressions
```python
# Bad - too many walrus operators
if (a := get_a()) and (b := get_b()) and (c := get_c()):
    result = a + b + c

# Better - traditional approach
a = get_a()
if a:
    b = get_b()
    if b:
        c = get_c()
        if c:
            result = a + b + c
```

### Mistake 4: Assuming Walrus Creates New Scope
```python
# Variable leaks to outer scope
if (temp := calculate()):
    pass

print(temp)  # temp is still accessible! (may be unexpected)

# Use traditional approach if you want to limit scope
temp = calculate()
if temp:
    pass
# temp still accessible, but more explicit
```

## Performance Considerations

```python
import time

# Walrus can improve performance by avoiding duplicate calculations
def expensive_calculation(n):
    time.sleep(0.001)  # Simulate work
    return n ** 2

# Without walrus (calculates twice)
def without_walrus(numbers):
    result = []
    for n in numbers:
        if expensive_calculation(n) > 100:
            result.append(expensive_calculation(n))
    return result

# With walrus (calculates once)
def with_walrus(numbers):
    result = []
    for n in numbers:
        if (value := expensive_calculation(n)) > 100:
            result.append(value)
    return result

numbers = list(range(50, 60))

start = time.time()
result1 = without_walrus(numbers)
time1 = time.time() - start

start = time.time()
result2 = with_walrus(numbers)
time2 = time.time() - start

print(f"Without walrus: {time1:.3f}s")
print(f"With walrus: {time2:.3f}s")
print(f"Walrus is {time1/time2:.1f}x faster")
```

## Best Practices

### ✅ Do This
```python
# Use walrus to avoid duplicate expensive calls
if (data := expensive_operation()):
    process(data)

# Use walrus in while loops with sentinel values
while (line := file.readline()):
    process(line)

# Use walrus in list comprehensions for efficiency
results = [y for x in data if (y := process(x)) is not None]

# Use walrus for regex matches
if (match := pattern.search(text)):
    print(match.group())

# Use walrus for input validation loops
while (name := input("Name: ")).strip() and len(name) < 2:
    print("Name too short")
```

### ❌ Avoid This
```python
# Avoid - unnecessary walrus (simple assignment)
if (x := 5) > 0:  # Just use x = 5

# Avoid - too many walrus operators in one expression
if (a := get_a()) and (b := get_b()) and (c := get_c()):

# Avoid - walrus in confusing contexts
result = (x := 5) + (y := 3) * (z := 2)

# Avoid - walrus when traditional approach is clearer
while (i := i + 1) < 10:  # Use i += 1 in loop body

# Avoid - relying on walrus for side effects
[(print(x), None) for x in data if (x := x * 2)]  # Use regular loop
```

## Quick Reference Table

| Use Case | Without Walrus | With Walrus |
|----------|----------------|-------------|
| While loop with sentinel | `line = f.readline()`<br>`while line:`<br>`    process(line)`<br>`    line = f.readline()` | `while (line := f.readline()):`<br>`    process(line)` |
| Regex match | `match = pattern.search(text)`<br>`if match:`<br>`    print(match.group())` | `if (match := pattern.search(text)):`<br>`    print(match.group())` |
| List comprehension filter | `[func(x) for x in data`<br>`    if func(x) > threshold]` | `[y for x in data`<br>`    if (y := func(x)) > threshold]` |
| Input validation | `value = input("Enter: ")`<br>`while not value:`<br>`    value = input("Enter: ")` | `while not (value := input("Enter: ")):`<br>`    pass` |

## Summary

- **Walrus operator (`:=`)** assigns values as part of an expression
- **Introduced in Python 3.8** (PEP 572)
- **Reduces code duplication** by avoiding repeated calculations
- **Improves readability** in certain patterns (loops, conditionals)
- **Requires parentheses** in many contexts
- **Variables are scoped** to the enclosing function/scope
- **Useful for while loops** with sentinel values
- **Efficient in list comprehensions** to avoid double calculation
- **Great for regex matches** and data validation
- **Not a replacement** for simple assignment statements

## Basic Template
```python
#!/usr/bin/env python3

def walrus_basics():
    """Basic walrus operator examples"""
    
    # Simple assignment in expression
    print("Value:", (x := 10))  # Assigns 10 to x and prints it
    print(f"x = {x}")
    
    # In if statement
    if (value := len("hello")) > 3:
        print(f"Length {value} > 3")
    
    # In while loop
    numbers = [1, 2, 3, 4, 5]
    i = 0
    while (num := numbers[i]) < 4:
        print(f"Number: {num}")
        i += 1

def walrus_comprehension():
    """Walrus operator in comprehensions"""
    
    # List comprehension with filter
    squares = [y for x in range(10) if (y := x**2) > 20]
    print(f"Squares > 20: {squares}")
    
    # Dictionary comprehension
    data = [1, 2, 3, 4, 5]
    squared_dict = {x: y for x in data if (y := x**2) > 10}
    print(f"Squared dict: {squared_dict}")

def walrus_validation():
    """Walrus operator for validation"""
    
    import re
    
    # Regex validation
    text = "Email: user@example.com"
    if (match := re.search(r'\w+@\w+\.\w+', text)):
        print(f"Found email: {match.group()}")
    
    # Input validation (simulated)
    def get_valid_age():
        while not ((age_str := input("Enter age: ")).isdigit() and 
                   (age := int(age_str)) >= 0):
            print("Invalid age")
        return age
    
    # Uncomment to test:
    # age = get_valid_age()
    # print(f"Age: {age}")

def performance_example():
    """Performance benefit of walrus"""
    
    import time
    
    def expensive(n):
        time.sleep(0.01)
        return n ** 2
    
    numbers = range(1, 6)
    
    # Without walrus (calculates twice)
    start = time.time()
    result1 = [expensive(n) for n in numbers if expensive(n) > 10]
    time1 = time.time() - start
    
    # With walrus (calculates once)
    start = time.time()
    result2 = [y for n in numbers if (y := expensive(n)) > 10]
    time2 = time.time() - start
    
    print(f"Without walrus: {time1:.3f}s")
    print(f"With walrus: {time2:.3f}s")
    print(f"Speedup: {time1/time2:.1f}x")

if __name__ == "__main__":
    print("=== WALRUS BASICS ===")
    walrus_basics()
    
    print("\n=== WALRUS COMPREHENSION ===")
    walrus_comprehension()
    
    print("\n=== WALRUS VALIDATION ===")
    walrus_validation()
    
    print("\n=== PERFORMANCE EXAMPLE ===")
    performance_example()
```

*This documentation belongs to https://github.com/InterCentury*