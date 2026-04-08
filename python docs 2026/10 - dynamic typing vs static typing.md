# 10 - Dynamic Typing vs Static Typing in Python

## What is Typing?
Typing refers to how a programming language handles data types. Some languages check types at compile-time (static typing), while others check at runtime (dynamic typing). Python is **dynamically typed**, while languages like C++, Java, and Rust are **statically typed**.

## Static Typing (C++, Java, Rust)

### How Static Typing Works
```cpp
// C++ example - types are fixed at compile-time
int age = 25;           // Must declare type
string name = "Alice";  // Type cannot change
double price = 19.99;

// Type mismatch causes compilation error
// age = "twenty";  // ❌ Compiler error!

// Function signatures include types
int add(int a, int b) {
    return a + b;
}

// add(5, "3");  // ❌ Compiler error!
```

### Characteristics of Static Typing
```cpp
// 1. Type declared at declaration
int count = 10;

// 2. Type cannot change
// count = "hello";  // Error!

// 3. Type checking at compile-time
// All type errors caught before running

// 4. Better performance (no runtime type checks)
// 5. Better IDE support (autocomplete, refactoring)
// 6. Self-documenting code
```

## Dynamic Typing (Python)

### How Dynamic Typing Works
```python
# Python example - types are determined at runtime
age = 25            # age is int
print(type(age))    # <class 'int'>

age = "twenty"      # Now age is str - perfectly valid!
print(type(age))    # <class 'str'>

age = 19.99         # Now age is float
print(type(age))    # <class 'float'>

# No type declarations needed
# Type can change freely
```

### Characteristics of Dynamic Typing
```python
# 1. No type declaration needed
x = 10

# 2. Type can change at runtime
x = "now a string"  # Works fine!

# 3. Type checking at runtime
def add(a, b):
    return a + b

print(add(5, 3))        # 8 (int + int)
print(add("Hello", " World"))  # "Hello World" (str + str)
# add(5, "3")  # Runtime error when executed!

# 4. Slower (runtime type checks)
# 5. More flexible
# 6. Less verbose code
```

## Key Differences

### Variable Declaration
```python
# Python (dynamic) - no type needed
name = "Alice"
age = 25
price = 19.99
items = [1, 2, 3]
```

```cpp
// C++ (static) - types required
string name = "Alice";
int age = 25;
double price = 19.99;
vector<int> items = {1, 2, 3};
```

### Type Reassignment
```python
# Python - type can change
value = 10        # int
value = "Hello"   # str - allowed
value = [1, 2, 3] # list - allowed
value = 3.14      # float - allowed
```

```cpp
// C++ - type cannot change
int value = 10;     // int
// value = "Hello";  // ❌ Compiler error!
// value = 3.14;      // ❌ Truncation warning (but allowed)
```

### Function Arguments
```python
# Python - flexible function arguments
def multiply(a, b):
    return a * b

# Works with different types
print(multiply(5, 3))           # 15 (int * int)
print(multiply("Hi", 3))        # HiHiHi (str * int)
print(multiply([1, 2], 2))      # [1, 2, 1, 2] (list * int)
# print(multiply("Hi", "Hi"))    # Runtime error (str * str)
```

```cpp
// C++ - types must match exactly
int multiply(int a, int b) {
    return a * b;
}

// multiply(5, 3);      // OK
// multiply("Hi", 3);   // ❌ Compiler error
// multiply(5.5, 3);    // ❌ Type mismatch (double vs int)
```

### Type Checking Time
```python
# Python - runtime type checking
def divide(a, b):
    return a / b

# This line doesn't cause error until executed
result = divide(10, "2")  # Runtime TypeError
```

```cpp
// C++ - compile-time type checking
double divide(double a, double b) {
    return a / b;
}

// divide(10, "2");  // ❌ Compiler catches this immediately
```

## Python's Type System Features

### Duck Typing
```python
# "If it walks like a duck and quacks like a duck, it's a duck"
# Python cares about behavior, not type

class Duck:
    def speak(self):
        return "Quack!"

class Person:
    def speak(self):
        return "Hello!"

def make_speak(thing):
    # Doesn't care about type, just that object has speak()
    return thing.speak()

duck = Duck()
person = Person()

print(make_speak(duck))    # Quack!
print(make_speak(person))  # Hello!
```

### Type Introspection
```python
# Python can inspect types at runtime
value = 42
print(type(value))           # <class 'int'>
print(isinstance(value, int))  # True
print(isinstance(value, str))  # False

# Check multiple types
def process(data):
    if isinstance(data, (int, float)):
        return data * 2
    elif isinstance(data, str):
        return data + data
    elif isinstance(data, list):
        return data + data
    else:
        return "Unknown type"
```

### Type Conversion (Explicit)
```python
# Python requires explicit type conversion
age_str = "25"
# age_int = age_str + 5  # TypeError!
age_int = int(age_str) + 5  # Explicit conversion needed

# Common conversions
int("123")        # String to int
float("3.14")     # String to float
str(123)          # Int to string
list("abc")       # String to list ['a', 'b', 'c']
tuple([1, 2, 3])  # List to tuple
```

## Type Hints (Optional Static Typing)

### Basic Type Hints (Python 3.5+)
```python
# Type hints are optional and not enforced
name: str = "Alice"      # Hint says str, but...
name = 123               # This works! (no error)

age: int = 25
price: float = 19.99
is_valid: bool = True

# Function type hints
def greet(name: str) -> str:
    return f"Hello, {name}"

# These all work despite hints
greet(123)           # No error!
greet([1, 2, 3])     # No error!
```

### Using Type Checkers (mypy)
```python
# With mypy type checker, hints are enforced
# Run: mypy script.py

def add_numbers(a: int, b: int) -> int:
    return a + b

# mypy will catch this error:
# result = add_numbers(5, "3")  # mypy error!

# But Python itself ignores it
result = add_numbers(5, "3")  # Runtime error only when executed
```

### Complex Type Hints
```python
from typing import List, Dict, Tuple, Optional, Union, Any

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Dictionary with string keys and int values
scores: Dict[str, int] = {"Alice": 95, "Bob": 87}

# Tuple of mixed types
person: Tuple[str, int, float] = ("Alice", 25, 5.6)

# Optional (can be None)
value: Optional[int] = None
value = 10

# Union (multiple possible types)
id: Union[int, str] = 123
id = "ABC123"

# Any (no type checking)
anything: Any = 42
anything = "string"
anything = [1, 2, 3]
```

## Performance Comparison

### Static Typing (Faster)
```python
# Python with dynamic typing - slower
def sum_numbers(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Python can't optimize as well
# Type checks happen in each iteration
```

```cpp
// C++ with static typing - faster
int sum_numbers(int n) {
    int total = 0;
    for (int i = 0; i < n; i++) {
        total += i;
    }
    return total;
}

// Compiler optimizes heavily
// No runtime type checks
```

### Python Optimization with Type Hints
```python
# Type hints don't improve performance
def fast_add(a: int, b: int) -> int:
    return a + b

# Still dynamic at runtime - same speed
# Type hints are just for documentation/tooling

# Use tools like Cython, Numba for performance
from numba import jit

@jit
def fast_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total
# Now it's faster (JIT compiled)
```

## Advantages of Dynamic Typing (Python)

### 1. Faster Development
```python
# No time spent on type declarations
def process_data(data):
    # Just write logic, not types
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
    return result

# Works with lists, tuples, any iterable
process_data([1, 2, 3])
process_data((4, 5, 6))
process_data(range(10))
```

### 2. More Flexible Code
```python
# Generic functions work with many types
def double(x):
    return x * 2

print(double(5))        # 10
print(double(3.14))     # 6.28
print(double("Hi"))     # HiHi
print(double([1, 2]))   # [1, 2, 1, 2]
print(double((1, 2)))   # (1, 2, 1, 2)
```

### 3. Easier Metaprogramming
```python
# Create classes dynamically
def create_class(name, attributes):
    return type(name, (), attributes)

Person = create_class("Person", {"name": "Alice", "age": 25})
p = Person()
print(p.name, p.age)

# Modify classes at runtime
class MyClass:
    pass

MyClass.new_method = lambda self: "Added at runtime"
obj = MyClass()
print(obj.new_method())
```

### 4. Less Boilerplate
```python
# Python - simple and clean
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(10, 20)
```

```java
// Java - verbose with types
public class Point {
    private int x;
    private int y;
    
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
    
    public int getX() { return x; }
    public int getY() { return y; }
    public void setX(int x) { this.x = x; }
    public void setY(int y) { this.y = y; }
}

Point p = new Point(10, 20);
```

### 5. Great for Prototyping
```python
# Quick experimentation
# Start with simple data structures
user = {"name": "Alice", "age": 25}

# Easily add fields as needed
user["email"] = "alice@email.com"
user["phone"] = "123-456-7890"

# Change structure dynamically
user["address"] = {"street": "123 Main", "city": "NYC"}
```

## Advantages of Static Typing (C++/Java)

### 1. Early Error Detection
```cpp
// Errors caught at compile-time
int calculate(int x, int y) {
    return x + y;
}

calculate("5", 3);  // ❌ Compiler error - won't even compile
```

### 2. Better Performance
```cpp
// No runtime type checking overhead
// Compiler optimizations
// Direct memory access
int sum = 0;
for (int i = 0; i < 1000000; i++) {
    sum += i;
}
// Very fast - no type checks in loop
```

### 3. Better IDE Support
```cpp
// IDE knows exact types
// Autocomplete works perfectly
// Refactoring is safe and easy
// Find all usages, rename variables safely
```

### 4. Self-Documenting Code
```cpp
// Types document intent
int getUserAge();           // Returns int
string getUserName();       // Returns string
vector<int> getScores();    // Returns list of ints

// No ambiguity about what functions return
```

### 5. Better for Large Codebases
```cpp
// Types help manage complexity
// Interfaces and contracts are explicit
// Easier to understand data flow
// Catch integration errors early
```

## Practical Comparison Examples

### Example 1: Adding Numbers
```python
# Python - flexible but can hide bugs
def add(a, b):
    return a + b

# Works, but might not be what you want
print(add(5, 3))        # 8
print(add("5", "3"))    # "53" (string concatenation)
print(add(5, "3"))      # TypeError at runtime
```

```cpp
// C++ - strict but safe
int add(int a, int b) {
    return a + b;
}

// add("5", "3");  // Compiler error - won't compile
// add(5, "3");    // Compiler error - won't compile
```

### Example 2: List Processing
```python
# Python - duck typing
def process_items(items):
    result = []
    for item in items:
        result.append(item.upper())
    return result

# Works with strings
print(process_items(["a", "b", "c"]))  # ['A', 'B', 'C']

# But fails at runtime with numbers
# print(process_items([1, 2, 3]))  # AttributeError
```

```cpp
// C++ - template with concepts (C++20)
#include <concepts>
#include <vector>
#include <string>

template<typename T>
concept Stringable = requires(T t) {
    { t.upper() } -> std::convertible_to<std::string>;
};

template<Stringable T>
std::vector<std::string> process_items(const std::vector<T>& items) {
    std::vector<std::string> result;
    for (const auto& item : items) {
        result.push_back(item.upper());
    }
    return result;
}
// Won't compile with ints - type error at compile time
```

### Example 3: Data Validation
```python
# Python - runtime validation
def create_user(name, age, email):
    # Must validate types at runtime
    if not isinstance(name, str):
        raise TypeError("name must be string")
    if not isinstance(age, int):
        raise TypeError("age must be integer")
    if not isinstance(email, str):
        raise TypeError("email must be string")
    
    return {"name": name, "age": age, "email": email}

# Validation only happens when function is called
create_user("Alice", 25, "alice@email.com")  # OK
# create_user("Alice", "25", "alice@email.com")  # Runtime error
```

```cpp
// C++ - compile-time type safety
#include <string>

struct User {
    std::string name;
    int age;
    std::string email;
};

User create_user(std::string name, int age, std::string email) {
    return {name, age, email};
}

// create_user("Alice", "25", "alice@email.com");  // Compiler error!
// Types are enforced without any validation code
```

## Hybrid Approaches

### Type Hints + Runtime Checking
```python
from typing import Union, TypeVar
import functools

# Using decorators for runtime type checking
def type_check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get type hints
        hints = func.__annotations__
        
        # Check argument types
        for arg_name, arg_value in zip(hints.keys(), args):
            expected_type = hints[arg_name]
            if not isinstance(arg_value, expected_type):
                raise TypeError(f"{arg_name} must be {expected_type}")
        
        return func(*args, **kwargs)
    return wrapper

@type_check
def divide(a: float, b: float) -> float:
    return a / b

# Now this raises TypeError
# divide(10, "2")  # TypeError: b must be <class 'float'>
```

### Pydantic for Runtime Validation
```python
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name: str
    age: int
    email: str

# Pydantic validates types at runtime
try:
    user = User(name="Alice", age="25", email="alice@email.com")
except ValidationError as e:
    print(e)  # age must be integer

# Works correctly
user = User(name="Alice", age=25, email="alice@email.com")
print(user)
```

## When to Use Each Approach

### Use Dynamic Typing (Python) when:
```python
# 1. Rapid prototyping and development
def quick_solution(data):
    # Just get it working quickly
    pass

# 2. Scripts and automation
# Simple file processing, data cleaning

# 3. Data science and analysis
import pandas as pd
df = pd.read_csv("data.csv")  # Flexible data structures

# 4. Web development (Django, Flask)
# Rapid iteration, flexibility

# 5. Small to medium projects
# Less overhead, faster development
```

### Use Static Typing (C++/Java) when:
```cpp
// 1. Large codebases (millions of lines)
// Types help manage complexity

// 2. Performance-critical applications
// Games, trading systems, embedded systems

// 3. System programming
// Operating systems, drivers

// 4. When type safety is critical
// Banking, medical, aerospace

// 5. Long-term maintenance
// Types document and enforce contracts
```

## Python Tools for Static Typing

### mypy - Static Type Checker
```bash
# Install mypy
pip install mypy

# Run type checking
mypy myfile.py
```

```python
# myfile.py
def greet(name: str) -> str:
    return f"Hello, {name}"

# mypy will catch this
result: int = greet("Alice")  # Warning: Incompatible type
```

### Pyright (Microsoft)
```python
# Used by VSCode Pylance
# Real-time type checking in editor

def process(items: list[int]) -> int:
    return sum(items)

process([1, 2, 3])     # OK
process(["a", "b"])    # Warning in editor
```

### Pyre (Facebook)
```bash
# Install Pyre
pip install pyre-check

# Initialize and run
pyre init
pyre check
```

## Common Misconceptions

### Misconception 1: Dynamic Typing Means No Types
```python
# Python HAS types, they're just checked at runtime
x = 10
print(type(x))  # <class 'int'> - types exist!

# Types are just not enforced at compile-time
```

### Misconception 2: Type Hints Make Python Static
```python
# Type hints are just annotations - Python ignores them
def add(a: int, b: int) -> int:
    return a + b

# This still works! (Python doesn't enforce)
result = add("5", "3")  # "53" at runtime
```

### Misconception 3: Dynamic Typing is Always Slower
```python
# For many operations, overhead is minimal
# Bottlenecks are usually I/O or algorithms
# Use profiling to find real bottlenecks

import time

# Dynamic typing overhead is often negligible
start = time.time()
for i in range(1000000):
    x = i + 1
print(f"Time: {time.time() - start:.3f}s")
```

## Quick Reference Table

| Feature | Dynamic Typing (Python) | Static Typing (C++) |
|---------|------------------------|---------------------|
| Type declaration | Not required | Required |
| Type can change | Yes | No |
| Type checking time | Runtime | Compile-time |
| Performance | Slower | Faster |
| Development speed | Faster | Slower |
| Error detection | Runtime | Compile-time |
| Flexibility | High | Low |
| IDE support | Good | Excellent |
| Code verbosity | Low | High |
| Learning curve | Easier | Steeper |
| Metaprogramming | Easy | Difficult |
| Large project safety | Less | More |

## Summary

- **Dynamic typing**: Types checked at runtime, can change
- **Static typing**: Types fixed at compile-time, cannot change
- **Python is dynamically typed** - no type declarations needed
- **Type hints** provide optional static typing (not enforced)
- **Duck typing** focuses on behavior, not type
- **Dynamic typing** advantages: flexibility, speed of development
- **Static typing** advantages: performance, safety, tooling
- **Type checkers** (mypy, Pyright) add static checking to Python
- **Choose based on project**: Prototyping vs production
- **Hybrid approaches** combine both benefits

## Basic Template
```python
#!/usr/bin/env python3

# Dynamic typing in action
# Same variable, multiple types
value = 10
print(f"Value: {value}, Type: {type(value)}")

value = "Hello"
print(f"Value: {value}, Type: {type(value)}")

value = [1, 2, 3]
print(f"Value: {value}, Type: {type(value)}")

# Duck typing example
class Bird:
    def fly(self):
        return "Flying high!"

class Airplane:
    def fly(self):
        return "Taking off!"

def make_it_fly(entity):
    # Doesn't care about type, just needs fly method
    return entity.fly()

bird = Bird()
plane = Airplane()

print(make_it_fly(bird))   # Flying high!
print(make_it_fly(plane))  # Taking off!

# Type hints (optional, for documentation)
def add_numbers(a: int, b: int) -> int:
    """Add two numbers (hints show expected types)"""
    return a + b

# Type introspection
def describe(data):
    print(f"Type: {type(data).__name__}")
    if isinstance(data, (int, float)):
        print(f"Value: {data}")
    elif isinstance(data, str):
        print(f"Length: {len(data)}")
    elif isinstance(data, list):
        print(f"Length: {len(data)}, Items: {data}")

describe(42)
describe("Python")
describe([1, 2, 3])

# Runtime type checking (when needed)
def safe_divide(a, b):
    if not isinstance(b, (int, float)):
        raise TypeError("Divisor must be a number")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

print(safe_divide(10, 2))  # 5.0
# safe_divide(10, "2")  # TypeError
```

*This documentation belongs to https://github.com/InterCentury*