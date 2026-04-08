# 11 - type() and isinstance() Functions in Python

## What are type() and isinstance()?
`type()` and `isinstance()` are built-in Python functions used for type checking and introspection. They allow you to examine the type of objects at runtime, which is essential in a dynamically typed language like Python.

## The type() Function

### Basic Usage
```python
# Get the type of any object
print(type(10))           # <class 'int'>
print(type(3.14))         # <class 'float'>
print(type("Hello"))      # <class 'str'>
print(type(True))         # <class 'bool'>
print(type([1, 2, 3]))    # <class 'list'>
print(type((1, 2, 3)))    # <class 'tuple'>
print(type({"a": 1}))     # <class 'dict'>
print(type({1, 2, 3}))    # <class 'set'>

# Type of variables
x = 42
print(type(x))            # <class 'int'>

# Type of expressions
print(type(10 + 5))       # <class 'int'>
print(type("Hi" * 3))     # <class 'str'>
```

### Comparing Types
```python
# Direct type comparison
x = 10
if type(x) == int:
    print("x is an integer")

# Check if type matches
name = "Alice"
if type(name) == str:
    print(f"Name is string: {name}")

# Multiple type checking
value = 3.14
if type(value) == int or type(value) == float:
    print("Value is a number")
```

### type() with Custom Classes
```python
class Dog:
    pass

class Cat:
    pass

class Person:
    pass

# Types of instances
my_dog = Dog()
my_cat = Cat()
person = Person()

print(type(my_dog))      # <class '__main__.Dog'>
print(type(my_cat))      # <class '__main__.Cat'>
print(type(person))      # <class '__main__.Person'>

# Compare types
if type(my_dog) == Dog:
    print("This is a Dog object")

# Different classes are different types
print(type(my_dog) == type(my_cat))  # False
```

### type() for Creating Classes Dynamically
```python
# type(name, bases, dict) - creates a new class
# Create a simple class
Person = type('Person', (), {'name': 'Unknown', 'age': 0})

p = Person()
print(p.name)  # Unknown
print(type(p))  # <class '__main__.Person'>

# Create class with methods
def greet(self):
    return f"Hello, I'm {self.name}"

Student = type('Student', (), 
               {'name': 'Student', 
                'greet': greet,
                'study': lambda self: "Studying..."})

s = Student()
print(s.greet())   # Hello, I'm Student
print(s.study())   # Studying...

# Inheritance with type()
class Animal:
    def speak(self):
        return "Some sound"

Dog = type('Dog', (Animal,), {'breed': 'Unknown'})
d = Dog()
print(d.speak())  # Some sound (inherited)
print(d.breed)    # Unknown
```

## The isinstance() Function

### Basic Usage
```python
# Check if object is instance of a class
x = 10
print(isinstance(x, int))      # True
print(isinstance(x, float))    # False
print(isinstance(x, object))   # True (everything is object)

# Check multiple types at once (tuple of types)
value = 3.14
print(isinstance(value, (int, float)))   # True
print(isinstance(value, (str, list)))    # False

# Check against built-in types
name = "Alice"
print(isinstance(name, str))      # True
print(isinstance(name, (int, float, str)))  # True

numbers = [1, 2, 3]
print(isinstance(numbers, list))   # True
print(isinstance(numbers, tuple))  # False
```

### isinstance() with Inheritance
```python
# isinstance() considers inheritance hierarchy
class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

class Cat(Mammal):
    pass

# Create instances
dog = Dog()
cat = Cat()
animal = Animal()

# isinstance() works with inheritance
print(isinstance(dog, Dog))      # True
print(isinstance(dog, Mammal))   # True (Dog is subclass of Mammal)
print(isinstance(dog, Animal))   # True (Dog is subclass of Animal)
print(isinstance(dog, object))   # True (everything inherits from object)

print(isinstance(cat, Dog))      # False (cat is not a Dog)
print(isinstance(animal, Dog))   # False (animal is not a Dog)

# Check against multiple levels
print(isinstance(dog, (Cat, Dog, Bird)))  # True (matches Dog)
```

### type() vs isinstance() with Inheritance
```python
# Critical difference: type() doesn't consider inheritance
class Parent:
    pass

class Child(Parent):
    pass

child = Child()

# type() checks exact type only
print(type(child) == Child)    # True
print(type(child) == Parent)   # False (doesn't consider inheritance)

# isinstance() considers inheritance
print(isinstance(child, Child))   # True
print(isinstance(child, Parent))  # True (child is a Parent too!)

# Best practice: Use isinstance() for inheritance-aware checks
# Use type() only when exact type matters
```

## Practical Examples

### Example 1: Type-Based Function Behavior
```python
def process_data(data):
    """Process data differently based on type"""
    
    if isinstance(data, (int, float)):
        # Numeric data
        return data * 2
    
    elif isinstance(data, str):
        # String data
        return data.upper()
    
    elif isinstance(data, list):
        # List data
        return [item * 2 for item in data]
    
    elif isinstance(data, dict):
        # Dictionary data
        return {k: v * 2 for k, v in data.items()}
    
    else:
        return f"Unsupported type: {type(data).__name__}"

# Test with different types
print(process_data(10))           # 20
print(process_data(3.14))         # 6.28
print(process_data("hello"))      # HELLO
print(process_data([1, 2, 3]))    # [2, 4, 6]
print(process_data({"a": 1, "b": 2}))  # {'a': 2, 'b': 4}
print(process_data({1, 2, 3}))    # Unsupported type: set
```

### Example 2: Type Validation Function
```python
def validate_user_data(user_data):
    """Validate user data types"""
    
    errors = []
    
    # Check name
    if 'name' not in user_data:
        errors.append("Missing 'name' field")
    elif not isinstance(user_data['name'], str):
        errors.append(f"Name must be string, got {type(user_data['name']).__name__}")
    elif len(user_data['name']) < 2:
        errors.append("Name too short (min 2 characters)")
    
    # Check age
    if 'age' not in user_data:
        errors.append("Missing 'age' field")
    elif not isinstance(user_data['age'], (int, float)):
        errors.append(f"Age must be number, got {type(user_data['age']).__name__}")
    elif user_data['age'] < 0 or user_data['age'] > 150:
        errors.append("Age must be between 0 and 150")
    
    # Check email
    if 'email' not in user_data:
        errors.append("Missing 'email' field")
    elif not isinstance(user_data['email'], str):
        errors.append(f"Email must be string, got {type(user_data['email']).__name__}")
    elif '@' not in user_data['email']:
        errors.append("Invalid email format")
    
    # Check scores (optional)
    if 'scores' in user_data:
        if not isinstance(user_data['scores'], (list, tuple)):
            errors.append(f"Scores must be list/tuple, got {type(user_data['scores']).__name__}")
        else:
            for i, score in enumerate(user_data['scores']):
                if not isinstance(score, (int, float)):
                    errors.append(f"Score at index {i} must be number, got {type(score).__name__}")
    
    return errors if errors else "Valid!"

# Test data
test_users = [
    {"name": "Alice", "age": 25, "email": "alice@email.com"},
    {"name": "B", "age": 25, "email": "bob@email.com"},  # Name too short
    {"name": "Charlie", "age": -5, "email": "charlie@email.com"},  # Negative age
    {"name": "Diana", "age": "30", "email": "diana@email.com"},  # Age as string
    {"name": "Eve", "age": 28, "email": "invalid"},  # Invalid email
    {"name": "Frank", "age": 35, "email": "frank@email.com", "scores": [85, "92", 78]}  # Invalid score
]

for i, user in enumerate(test_users, 1):
    print(f"\nUser {i}: {user}")
    result = validate_user_data(user)
    print(f"Validation: {result}")
```

### Example 3: Type-Based Serializer
```python
def serialize(obj):
    """Convert object to string representation based on type"""
    
    if obj is None:
        return "null"
    
    elif isinstance(obj, bool):
        return "true" if obj else "false"
    
    elif isinstance(obj, (int, float)):
        return str(obj)
    
    elif isinstance(obj, str):
        return f'"{obj}"'
    
    elif isinstance(obj, (list, tuple)):
        items = [serialize(item) for item in obj]
        return "[" + ", ".join(items) + "]"
    
    elif isinstance(obj, dict):
        items = [f'{serialize(k)}: {serialize(v)}' for k, v in obj.items()]
        return "{" + ", ".join(items) + "}"
    
    elif hasattr(obj, '__dict__'):
        # Custom object - serialize its attributes
        return serialize(obj.__dict__)
    
    else:
        return f'"{str(obj)}"'

# Test with different types
data = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "scores": [95, 87, 92],
    "address": {
        "street": "123 Main St",
        "city": "Boston",
        "zip": 02101
    },
    "optional": None,
    "tags": ("python", "coding")
}

print(serialize(data))
# Output: {"name": "Alice", "age": 30, "is_student": false, "scores": [95, 87, 92], "address": {"street": "123 Main St", "city": "Boston", "zip": 2101}, "optional": null, "tags": ["python", "coding"]}
```

### Example 4: Type-Based Calculator
```python
class Calculator:
    def add(self, a, b):
        """Add with type checking"""
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        elif isinstance(a, list) and isinstance(b, list):
            return a + b
        else:
            raise TypeError(f"Cannot add {type(a).__name__} and {type(b).__name__}")
    
    def multiply(self, a, b):
        """Multiply with type checking"""
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a * b
        elif isinstance(a, str) and isinstance(b, int):
            return a * b
        elif isinstance(a, list) and isinstance(b, int):
            return a * b
        else:
            raise TypeError(f"Cannot multiply {type(a).__name__} and {type(b).__name__}")
    
    def describe(self, value):
        """Describe the value's type and capabilities"""
        type_name = type(value).__name__
        
        if isinstance(value, (int, float)):
            return f"{type_name}: {value} (numeric, can do math)"
        elif isinstance(value, str):
            return f"{type_name}: '{value}' (length: {len(value)})"
        elif isinstance(value, list):
            return f"{type_name}: {value} (length: {len(value)}, can append)"
        elif isinstance(value, dict):
            return f"{type_name}: {value} (keys: {list(value.keys())})"
        elif isinstance(value, bool):
            return f"{type_name}: {value} (boolean)"
        else:
            return f"{type_name}: {value} (unknown capabilities)"

calc = Calculator()

# Test different type combinations
print(calc.add(5, 3))           # 8
print(calc.add("Hello", " World"))  # Hello World
print(calc.add([1, 2], [3, 4]))     # [1, 2, 3, 4]

print(calc.multiply(5, 3))      # 15
print(calc.multiply("Hi", 3))    # HiHiHi
print(calc.multiply([1, 2], 3))  # [1, 2, 1, 2, 1, 2]

# Describe different values
print(calc.describe(42))
print(calc.describe(3.14))
print(calc.describe("Python"))
print(calc.describe([1, 2, 3]))
print(calc.describe({"a": 1, "b": 2}))
print(calc.describe(True))
```

### Example 5: Type-Based Formatter
```python
def format_value(value, format_type="auto"):
    """Format value based on its type and requested format"""
    
    # Get type information
    value_type = type(value).__name__
    
    if format_type == "auto":
        # Auto-format based on type
        if isinstance(value, int):
            return f"{value:,}"  # Add thousand separators
        elif isinstance(value, float):
            return f"{value:.2f}"  # 2 decimal places
        elif isinstance(value, str):
            return value.title()  # Title case
        elif isinstance(value, bool):
            return "Yes" if value else "No"
        elif isinstance(value, (list, tuple)):
            return ", ".join(str(item) for item in value)
        elif isinstance(value, dict):
            return "; ".join(f"{k}={v}" for k, v in value.items())
        else:
            return str(value)
    
    elif format_type == "debug":
        # Detailed debug format
        return f"{value_type}: {repr(value)}"
    
    elif format_type == "json":
        # JSON-like format
        if isinstance(value, (int, float, bool)):
            return str(value).lower()
        elif isinstance(value, str):
            return f'"{value}"'
        elif isinstance(value, (list, tuple)):
            return "[" + ", ".join(format_value(item, "json") for item in value) + "]"
        elif isinstance(value, dict):
            items = [f'"{k}": {format_value(v, "json")}' for k, v in value.items()]
            return "{" + ", ".join(items) + "}"
        else:
            return f'"{value}"'
    
    else:
        return str(value)

# Test data
test_values = [
    1234567,
    3.14159,
    "hello world",
    True,
    False,
    [1, 2, 3, 4, 5],
    ("a", "b", "c"),
    {"name": "Alice", "age": 30, "active": True}
]

print("=== AUTO FORMAT ===")
for value in test_values:
    print(f"{type(value).__name__:10} → {format_value(value)}")

print("\n=== DEBUG FORMAT ===")
for value in test_values:
    print(format_value(value, "debug"))

print("\n=== JSON FORMAT ===")
for value in test_values:
    print(format_value(value, "json"))
```

### Example 6: Plugin System with Type Checking
```python
from typing import List, Dict, Any

class Plugin:
    """Base plugin class"""
    def process(self, data):
        raise NotImplementedError("Subclasses must implement process()")

class UppercasePlugin(Plugin):
    def process(self, data):
        if isinstance(data, str):
            return data.upper()
        elif isinstance(data, list):
            return [item.upper() if isinstance(item, str) else item for item in data]
        else:
            return data

class DoublePlugin(Plugin):
    def process(self, data):
        if isinstance(data, (int, float)):
            return data * 2
        elif isinstance(data, str):
            return data + data
        elif isinstance(data, list):
            return data + data
        else:
            return data

class FilterPlugin(Plugin):
    def __init__(self, filter_type):
        self.filter_type = filter_type
    
    def process(self, data):
        if not isinstance(data, list):
            return data
        
        if self.filter_type == "numbers":
            return [item for item in data if isinstance(item, (int, float))]
        elif self.filter_type == "strings":
            return [item for item in data if isinstance(item, str)]
        else:
            return data

class PluginManager:
    def __init__(self):
        self.plugins: List[Plugin] = []
    
    def register(self, plugin: Plugin):
        if not isinstance(plugin, Plugin):
            raise TypeError(f"Plugin must be Plugin instance, got {type(plugin).__name__}")
        self.plugins.append(plugin)
    
    def process(self, data: Any) -> Any:
        result = data
        for plugin in self.plugins:
            try:
                result = plugin.process(result)
                print(f"  {type(plugin).__name__}: {result}")
            except Exception as e:
                print(f"  Error in {type(plugin).__name__}: {e}")
        return result

# Create plugin manager
manager = PluginManager()

# Register plugins
manager.register(UppercasePlugin())
manager.register(DoublePlugin())
manager.register(FilterPlugin("numbers"))

# Process different data types
test_data = [
    "hello world",
    [1, 2, 3, "a", "b", 4],
    {"text": "mixed data", "numbers": [1, 2, 3]}
]

print("=== PLUGIN SYSTEM ===")
for data in test_data:
    print(f"\nInput ({type(data).__name__}): {data}")
    result = manager.process(data)
    print(f"Final: {result}")
```

## type() vs isinstance() Comparison

```python
# Key differences
class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

obj = Child()

# type() - exact type only
print(type(obj) == Child)        # True
print(type(obj) == Parent)       # False
print(type(obj) == Grandparent)  # False

# isinstance() - considers inheritance
print(isinstance(obj, Child))       # True
print(isinstance(obj, Parent))      # True (Child is Parent)
print(isinstance(obj, Grandparent)) # True (Child is Grandparent)
print(isinstance(obj, object))      # True (everything is object)

# When to use which
# Use isinstance() for most cases (supports polymorphism)
# Use type() when exact type matters (e.g., serialization)

# Example where exact type matters
def serialize(obj):
    if type(obj) is dict:  # Exact type, not subclass
        return "dict"
    elif type(obj) is list:
        return "list"
    else:
        return "other"

class MyDict(dict):
    pass

print(serialize({}))           # dict
print(serialize(MyDict()))     # other (not dict exactly)
```

## Type Checking Best Practices

### ✅ Do This
```python
# Use isinstance() for most type checks
def process(data):
    if isinstance(data, (int, float)):
        return data * 2
    elif isinstance(data, str):
        return data.upper()

# Check for None explicitly
if value is None:
    print("No value")

# Use type() for exact type matching
def exact_type_check(obj):
    if type(obj) is dict:  # Must be exact dict, not subclass
        return "exact dict"

# Check multiple types with tuple
if isinstance(value, (int, float, str)):
    print("Number or string")

# Use hasattr() for duck typing when appropriate
if hasattr(obj, 'speak'):
    obj.speak()  # Don't care about type
```

### ❌ Avoid This
```python
# Avoid - type() with inheritance
class MyList(list):
    pass

data = MyList()
if type(data) == list:  # False - misses MyList
    print("This won't print")

# Avoid - comparing to string of type name
if type(x).__name__ == "int":  # Fragile!
    print("Is int")

# Better
if isinstance(x, int):
    print("Is int")

# Avoid - type checking when duck typing works
def make_sound(animal):
    if isinstance(animal, Dog):
        animal.bark()
    elif isinstance(animal, Cat):
        animal.meow()
    # Better: animal.speak()

# Avoid - over-checking types
def add(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    # Just try and let it fail
```

## Common Mistakes

### Mistake 1: Using type() for Inheritance Checks
```python
# Wrong
class Animal: pass
class Dog(Animal): pass

d = Dog()
if type(d) == Animal:  # False - doesn't work!
    print("Is animal")

# Right
if isinstance(d, Animal):  # True
    print("Is animal")
```

### Mistake 2: Forgetting None is a Type
```python
# Wrong
x = None
if type(x) == None:  # TypeError!
    pass

# Right
if x is None:
    pass

# Or
if isinstance(x, type(None)):
    pass
```

### Mistake 3: Comparing to Type Name Strings
```python
# Wrong - fragile
value = 10
if type(value).__name__ == "int":
    print("Is int")  # Works but bad practice

# Right
if isinstance(value, int):
    print("Is int")
```

### Mistake 4: Not Using Tuple for Multiple Types
```python
# Wrong - repetitive
if isinstance(x, int) or isinstance(x, float) or isinstance(x, str):
    pass

# Right - clean
if isinstance(x, (int, float, str)):
    pass
```

## Performance Considerations

```python
import time

# type() is slightly faster than isinstance() for exact checks
# But difference is negligible for most applications

def test_type(x):
    return type(x) is int

def test_isinstance(x):
    return isinstance(x, int)

# Performance test
iterations = 10000000
x = 10

start = time.time()
for _ in range(iterations):
    test_type(x)
type_time = time.time() - start

start = time.time()
for _ in range(iterations):
    test_isinstance(x)
isinstance_time = time.time() - start

print(f"type() time: {type_time:.3f}s")
print(f"isinstance() time: {isinstance_time:.3f}s")
print(f"Difference: {abs(type_time - isinstance_time):.3f}s")

# However, isinstance() is more flexible and preferred
# Performance difference rarely matters
```

## Quick Reference Table

| Feature | type() | isinstance() |
|---------|--------|--------------|
| Checks exact type | ✅ Yes | ❌ No (considers inheritance) |
| Checks inheritance | ❌ No | ✅ Yes |
| Multiple types | ❌ No (need `or`) | ✅ Yes (tuple) |
| Returns | Type object | Boolean |
| Use for | Exact type matching | Most type checks |
| Speed | Slightly faster | Slightly slower |
| With builtins | ✅ Yes | ✅ Yes |
| With custom classes | ✅ Yes | ✅ Yes |

## Summary

- **type()** returns the exact type of an object
- **isinstance()** checks if object is instance of class (including inheritance)
- **isinstance() is preferred** for most type checks
- **Use type()** when exact type matters (not subclasses)
- **Both work with built-in and custom types**
- **Use tuples** with isinstance() to check multiple types
- **Duck typing** (check behavior) is often better than type checking
- **None** requires special handling (`is None`)
- **Performance difference** is negligible for most use cases

## Basic Template
```python
#!/usr/bin/env python3

# Basic type checking
def check_type(value):
    """Demonstrate type checking functions"""
    
    # Get type
    value_type = type(value)
    print(f"Value: {value}")
    print(f"Type: {value_type}")
    print(f"Type name: {value_type.__name__}")
    
    # isinstance() checks
    if isinstance(value, (int, float)):
        print(f"  → Numeric: {value * 2}")
    elif isinstance(value, str):
        print(f"  → String: {value.upper()}")
    elif isinstance(value, bool):
        print(f"  → Boolean: {'Yes' if value else 'No'}")
    elif isinstance(value, (list, tuple)):
        print(f"  → Sequence: {len(value)} items")
    elif isinstance(value, dict):
        print(f"  → Dictionary: {len(value)} keys")
    elif value is None:
        print("  → None value")
    else:
        print(f"  → Unknown type")

# Test different values
test_values = [
    42,
    3.14,
    "Hello Python",
    True,
    False,
    [1, 2, 3],
    (4, 5, 6),
    {"name": "Alice", "age": 30},
    None,
    type  # Type of type is 'type'
]

print("=== TYPE CHECKING DEMO ===\n")
for value in test_values:
    check_type(value)
    print()

# type() for exact matching
class MyList(list):
    pass

my_list = MyList([1, 2, 3])
regular_list = [1, 2, 3]

print("=== EXACT TYPE VS INHERITANCE ===")
print(f"type(my_list) is list: {type(my_list) is list}")  # False
print(f"isinstance(my_list, list): {isinstance(my_list, list)}")  # True
print(f"type(regular_list) is list: {type(regular_list) is list}")  # True
print(f"isinstance(regular_list, list): {isinstance(regular_list, list)}")  # True

# Creating classes with type()
print("\n=== DYNAMIC CLASS CREATION ===")
Person = type('Person', (), 
              {'name': 'Unknown', 
               'greet': lambda self: f"Hello, I'm {self.name}"})
p = Person()
p.name = "Alice"
print(p.greet())
print(f"Type of p: {type(p)}")
```

*This documentation belongs to https://github.com/InterCentury*