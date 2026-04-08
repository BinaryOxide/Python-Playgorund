# 17 - Type Conversion (int(), float(), str(), bool())

## What is Type Conversion?
Type conversion (or type casting) is the process of converting a value from one data type to another. Python provides built-in functions for explicit type conversion: `int()`, `float()`, `str()`, and `bool()`.

## Types of Type Conversion

### Implicit Conversion (Automatic)
```python
# Python automatically converts types when needed
x = 10      # int
y = 3.14    # float
result = x + y  # int + float = float (automatic)
print(result, type(result))  # 13.14 <class 'float'>

# int + bool = int
print(10 + True)   # 11 (True converts to 1)
print(10 + False)  # 10 (False converts to 0)

# float + bool = float
print(3.14 + True)   # 4.14

# str + str = str (concatenation)
print("Hello" + " " + "World")
```

### Explicit Conversion (Manual)
```python
# You manually convert using type conversion functions
x = "123"
y = int(x)      # Convert string to int
z = float(x)    # Convert string to float
b = bool(x)     # Convert string to bool
s = str(y)      # Convert int to string

print(f"Original: {x}, type: {type(x)}")
print(f"int(): {y}, type: {type(y)}")
print(f"float(): {z}, type: {type(z)}")
print(f"bool(): {b}, type: {type(b)}")
```

## int() Conversion

### Converting to Integer
```python
# From float (truncates toward zero)
print(int(3.14))    # 3
print(int(3.99))    # 3 (not rounding!)
print(int(-3.14))   # -3
print(int(-3.99))   # -3

# From string
print(int("123"))     # 123
print(int("-456"))    # -456
print(int("  789  ")) # 789 (strips whitespace)

# From boolean
print(int(True))      # 1
print(int(False))     # 0

# From other bases
print(int("1010", 2))    # 10 (binary)
print(int("FF", 16))     # 255 (hexadecimal)
print(int("77", 8))      # 63 (octal)
print(int("A", 16))      # 10

# From bytes
print(int(b'123'))       # 123
```

### int() with Different Bases
```python
# Binary (base 2)
binary_str = "1101"
print(f"Binary {binary_str} = {int(binary_str, 2)}")  # 13

# Octal (base 8)
octal_str = "17"
print(f"Octal {octal_str} = {int(octal_str, 8)}")    # 15

# Hexadecimal (base 16)
hex_str = "1F"
print(f"Hex {hex_str} = {int(hex_str, 16)}")         # 31

# Any base from 2 to 36
print(int("Z", 36))    # 35
print(int("hello", 36)) # 29234652
```

### Common int() Errors
```python
# ValueError - cannot convert
try:
    int("12.34")      # Decimal string not allowed
except ValueError as e:
    print(f"Error: {e}")

try:
    int("abc")        # Non-numeric string
except ValueError as e:
    print(f"Error: {e}")

try:
    int("")           # Empty string
except ValueError as e:
    print(f"Error: {e}")

# TypeError - wrong type
try:
    int([1, 2, 3])    # Cannot convert list
except TypeError as e:
    print(f"Error: {e}")
```

## float() Conversion

### Converting to Float
```python
# From int
print(float(42))        # 42.0
print(float(-10))       # -10.0
print(float(0))         # 0.0

# From string
print(float("3.14"))    # 3.14
print(float("-2.5"))    # -2.5
print(float("1.5e3"))   # 1500.0 (scientific notation)
print(float("  .5  "))  # 0.5
print(float("  42  "))  # 42.0

# From boolean
print(float(True))      # 1.0
print(float(False))     # 0.0

# Special values
print(float("inf"))     # inf
print(float("-inf"))    # -inf
print(float("nan"))     # nan
```

### float() Precision
```python
# Floating-point precision
print(float("0.1"))          # 0.1 (but not exact in binary)
print(float("0.2"))          # 0.2
print(float("0.1") + float("0.2"))  # 0.30000000000000004

# Large numbers
print(float("1e308"))        # 1e+308
# print(float("1e309"))      # OverflowError: too large

# Scientific notation
print(float("1.23e-10"))     # 1.23e-10
```

### Common float() Errors
```python
# ValueError
try:
    float("abc")
except ValueError as e:
    print(f"Error: {e}")

try:
    float("1,234")  # Comma not allowed
except ValueError as e:
    print(f"Error: {e}")

# Works with some special cases
print(float("  1.5  "))      # 1.5 (strips spaces)
print(float("  1.5\n"))      # 1.5 (strips newline)
```

## str() Conversion

### Converting to String
```python
# From int
print(str(42))          # "42"
print(str(-123))        # "-123"
print(str(0))           # "0"

# From float
print(str(3.14))        # "3.14"
print(str(1.5e3))       # "1500.0"
print(str(0.1 + 0.2))   # "0.30000000000000004"

# From bool
print(str(True))        # "True"
print(str(False))       # "False"

# From None
print(str(None))        # "None"

# From collections
print(str([1, 2, 3]))   # "[1, 2, 3]"
print(str((1, 2)))      # "(1, 2)"
print(str({"a": 1}))    # "{'a': 1}"
print(str({1, 2}))      # "{1, 2}"

# From custom objects
class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Person(name={self.name})"

p = Person("Alice")
print(str(p))           # "Person(name=Alice)"
```

### String Formatting vs str()
```python
# str() gives simple representation
num = 3.14159
print(str(num))          # "3.14159"

# Format for control
print(f"{num:.2f}")      # "3.14"
print(f"{num:.4f}")      # "3.1416"

# repr() for detailed representation
print(repr(num))         # "3.14159"
print(repr("Hello"))     # "'Hello'" (includes quotes)
```

## bool() Conversion

### Converting to Boolean
```python
# Falsy values (convert to False)
print(bool(None))        # False
print(bool(False))       # False
print(bool(0))           # False
print(bool(0.0))         # False
print(bool(0j))          # False
print(bool(""))          # False
print(bool([]))          # False
print(bool(()))          # False
print(bool({}))          # False
print(bool(set()))       # False
print(bool(range(0)))    # False

# Truthy values (convert to True)
print(bool(True))        # True
print(bool(1))           # True
print(bool(-1))          # True
print(bool(3.14))        # True
print(bool("Hello"))     # True
print(bool("False"))     # True (non-empty string!)
print(bool([1, 2]))      # True
print(bool((1,)))        # True
print(bool({"a": 1}))    # True
print(bool({1, 2}))      # True
```

### Common bool() Pitfalls
```python
# Be careful with strings
print(bool("False"))     # True (not False!)
print(bool("0"))         # True (not False!)
print(bool("None"))      # True (not False!)

# Empty vs zero
print(bool(0))           # False
print(bool(0.0))         # False
print(bool(0j))          # False

# But any non-zero is True
print(bool(0.0001))      # True
print(bool(-0.001))      # True

# Collections
print(bool([]))          # False (empty)
print(bool([None]))      # True (has one element)
print(bool([[]]))        # True (has one element)
```

## Type Conversion in Practice

### Example 1: User Input Processing
```python
def process_user_input():
    """Convert and validate user input"""
    
    # Get raw input (always string)
    age_str = input("Enter your age: ")
    price_str = input("Enter price: ")
    name_str = input("Enter name: ")
    
    # Convert with validation
    try:
        # String to int
        age = int(age_str)
        if age < 0 or age > 150:
            print(f"Invalid age: {age}")
        else:
            print(f"Age: {age} (type: {type(age)})")
    except ValueError:
        print(f"Invalid age format: {age_str}")
    
    try:
        # String to float
        price = float(price_str)
        if price < 0:
            print(f"Price cannot be negative: {price}")
        else:
            print(f"Price: ${price:.2f} (type: {type(price)})")
    except ValueError:
        print(f"Invalid price format: {price_str}")
    
    # String to bool (custom logic)
    if name_str:
        has_name = True
    else:
        has_name = False
    print(f"Has name: {has_name}")
    
    # Bool to string for display
    print(f"Has name (string): {str(has_name)}")

# process_user_input()
```

### Example 2: Data Validator
```python
class DataValidator:
    """Validate and convert data types"""
    
    @staticmethod
    def to_int(value, default=0):
        """Safe conversion to int"""
        try:
            if isinstance(value, bool):
                return int(value)
            if isinstance(value, (int, float)):
                return int(value)
            if isinstance(value, str):
                # Remove whitespace
                cleaned = value.strip()
                if not cleaned:
                    return default
                return int(cleaned)
            return default
        except (ValueError, TypeError):
            return default
    
    @staticmethod
    def to_float(value, default=0.0):
        """Safe conversion to float"""
        try:
            if isinstance(value, bool):
                return float(value)
            if isinstance(value, (int, float)):
                return float(value)
            if isinstance(value, str):
                cleaned = value.strip()
                if not cleaned:
                    return default
                return float(cleaned)
            return default
        except (ValueError, TypeError):
            return default
    
    @staticmethod
    def to_bool(value, default=False):
        """Safe conversion to bool"""
        if isinstance(value, bool):
            return value
        
        if isinstance(value, (int, float)):
            return value != 0
        
        if isinstance(value, str):
            cleaned = value.lower().strip()
            if cleaned in ('true', 'yes', '1', 'on'):
                return True
            if cleaned in ('false', 'no', '0', 'off', ''):
                return False
            return default
        
        if value is None:
            return False
        
        return bool(value)
    
    @staticmethod
    def to_str(value, default=""):
        """Safe conversion to string"""
        if value is None:
            return default
        try:
            return str(value)
        except:
            return default

# Demo validator
validator = DataValidator()

test_values = [
    "123", "12.34", "true", "false", "yes", "no", 
    "  45  ", "", None, True, False, 100, 0, 3.14
]

print("=== Data Validator Demo ===")
for value in test_values:
    print(f"\nInput: {repr(value)} (type: {type(value).__name__})")
    print(f"  → int: {validator.to_int(value)}")
    print(f"  → float: {validator.to_float(value)}")
    print(f"  → bool: {validator.to_bool(value)}")
    print(f"  → str: {repr(validator.to_str(value))}")
```

### Example 3: CSV Parser
```python
import csv
from io import StringIO

class CSVParser:
    """Parse CSV with type conversion"""
    
    @staticmethod
    def parse_with_types(row, type_map):
        """Convert CSV row to typed values"""
        converted = {}
        for i, (key, value) in enumerate(row.items()):
            if key in type_map:
                type_func = type_map[key]
                try:
                    converted[key] = type_func(value)
                except (ValueError, TypeError):
                    converted[key] = None
            else:
                converted[key] = value
        return converted
    
    @staticmethod
    def parse_file(csv_content, type_map=None):
        """Parse CSV file with automatic type conversion"""
        if type_map is None:
            type_map = {}
        
        result = []
        reader = csv.DictReader(StringIO(csv_content))
        
        for row in reader:
            typed_row = CSVParser.parse_with_types(row, type_map)
            result.append(typed_row)
        
        return result

# Demo CSV data
csv_data = """name,age,score,active,gpa
Alice,25,95.5,true,3.8
Bob,30,87.2,false,3.2
Charlie,35,92.1,true,3.9
Diana,28,88.7,false,3.5
"""

# Define type conversions
type_map = {
    'name': str,
    'age': int,
    'score': float,
    'active': lambda x: x.lower() == 'true',
    'gpa': float
}

print("=== CSV Parser Demo ===")
parsed_data = CSVParser.parse_file(csv_data, type_map)

for i, record in enumerate(parsed_data, 1):
    print(f"\nRecord {i}:")
    for key, value in record.items():
        print(f"  {key}: {value} (type: {type(value).__name__})")
```

### Example 4: Configuration Loader
```python
import json
import os

class ConfigLoader:
    """Load configuration with type conversion"""
    
    def __init__(self):
        self.config = {}
    
    def load_from_dict(self, data, type_hints=None):
        """Load from dictionary with type hints"""
        if type_hints is None:
            type_hints = {}
        
        for key, value in data.items():
            if key in type_hints:
                hint = type_hints[key]
                if hint == 'int':
                    self.config[key] = int(value)
                elif hint == 'float':
                    self.config[key] = float(value)
                elif hint == 'bool':
                    if isinstance(value, str):
                        self.config[key] = value.lower() in ('true', 'yes', '1')
                    else:
                        self.config[key] = bool(value)
                elif hint == 'str':
                    self.config[key] = str(value)
                elif hint == 'list':
                    if isinstance(value, str):
                        self.config[key] = [x.strip() for x in value.split(',')]
                    else:
                        self.config[key] = list(value)
            else:
                self.config[key] = value
        
        return self.config
    
    def load_from_json(self, json_str, type_hints=None):
        """Load from JSON string"""
        data = json.loads(json_str)
        return self.load_from_dict(data, type_hints)
    
    def get(self, key, default=None):
        """Get config value with type preserved"""
        return self.config.get(key, default)
    
    def get_int(self, key, default=0):
        """Get value as int"""
        value = self.config.get(key, default)
        try:
            return int(value)
        except (ValueError, TypeError):
            return default
    
    def get_float(self, key, default=0.0):
        """Get value as float"""
        value = self.config.get(key, default)
        try:
            return float(value)
        except (ValueError, TypeError):
            return default
    
    def get_bool(self, key, default=False):
        """Get value as bool"""
        value = self.config.get(key, default)
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value.lower() in ('true', 'yes', '1', 'on')
        return bool(value)
    
    def get_str(self, key, default=""):
        """Get value as string"""
        value = self.config.get(key, default)
        if value is None:
            return default
        return str(value)

# Demo
loader = ConfigLoader()

# Configuration data
config_json = '''
{
    "debug": true,
    "port": "8080",
    "timeout": "30.5",
    "name": "MyApp",
    "hosts": "localhost,127.0.0.1,192.168.1.1",
    "max_connections": "100"
}
'''

# Type hints
type_hints = {
    'debug': 'bool',
    'port': 'int',
    'timeout': 'float',
    'name': 'str',
    'hosts': 'list',
    'max_connections': 'int'
}

print("=== Configuration Loader Demo ===")
loader.load_from_json(config_json, type_hints)

print("\nRaw config:")
for key, value in loader.config.items():
    print(f"  {key}: {value} (type: {type(value).__name__})")

print(f"\nGet typed values:")
print(f"  debug: {loader.get_bool('debug')} (type: {type(loader.get_bool('debug')).__name__})")
print(f"  port: {loader.get_int('port')} (type: {type(loader.get_int('port')).__name__})")
print(f"  timeout: {loader.get_float('timeout')} (type: {type(loader.get_float('timeout')).__name__})")
print(f"  name: {loader.get_str('name')} (type: {type(loader.get_str('name')).__name__})")
print(f"  hosts: {loader.get('hosts')} (type: {type(loader.get('hosts')).__name__})")
```

### Example 5: Database Query Builder
```python
class QueryBuilder:
    """Build SQL queries with type conversion"""
    
    @staticmethod
    def escape_string(value):
        """Escape string for SQL"""
        if value is None:
            return 'NULL'
        return f"'{str(value).replace(\"'\", \"''\")}'"
    
    @staticmethod
    def format_value(value):
        """Format value for SQL based on type"""
        if value is None:
            return 'NULL'
        
        if isinstance(value, bool):
            return 'TRUE' if value else 'FALSE'
        
        if isinstance(value, (int, float)):
            return str(value)
        
        if isinstance(value, str):
            return QueryBuilder.escape_string(value)
        
        if isinstance(value, (list, tuple)):
            return ', '.join(QueryBuilder.format_value(v) for v in value)
        
        return QueryBuilder.escape_string(str(value))
    
    @staticmethod
    def build_insert(table, data):
        """Build INSERT query with type conversion"""
        columns = ', '.join(data.keys())
        values = ', '.join(QueryBuilder.format_value(v) for v in data.values())
        return f"INSERT INTO {table} ({columns}) VALUES ({values});"
    
    @staticmethod
    def build_update(table, data, where):
        """Build UPDATE query with type conversion"""
        set_clause = ', '.join(f"{k} = {QueryBuilder.format_value(v)}" 
                               for k, v in data.items())
        where_clause = ' AND '.join(f"{k} = {QueryBuilder.format_value(v)}" 
                                    for k, v in where.items())
        return f"UPDATE {table} SET {set_clause} WHERE {where_clause};"

# Demo
builder = QueryBuilder()

print("=== Query Builder Demo ===")

# Insert data with type conversion
user_data = {
    'id': 1,
    'name': "Alice O'Connor",
    'age': 25,
    'gpa': 3.8,
    'is_active': True,
    'email': None,
    'tags': ['python', 'sql']
}

print("\nINSERT Query:")
print(builder.build_insert('users', user_data))

# Update data
update_data = {
    'age': 26,
    'gpa': 3.9,
    'is_active': False
}

where_condition = {
    'id': 1,
    'name': "Alice O'Connor"
}

print("\nUPDATE Query:")
print(builder.build_update('users', update_data, where_condition))

# Type conversion examples
print("\nType Conversion Examples:")
test_values = [
    None,
    True,
    False,
    42,
    3.14,
    "Hello 'World'",
    [1, 2, 3],
    ("a", "b")
]

for value in test_values:
    formatted = builder.format_value(value)
    print(f"{repr(value):20} → {formatted}")
```

### Example 6: Form Data Processor
```python
class FormProcessor:
    """Process web form data with type conversion"""
    
    def __init__(self):
        self.fields = {}
        self.errors = {}
    
    def add_field(self, name, type_func, required=False, default=None, validator=None):
        """Add field definition"""
        self.fields[name] = {
            'type': type_func,
            'required': required,
            'default': default,
            'validator': validator
        }
    
    def process(self, form_data):
        """Process and convert form data"""
        result = {}
        self.errors = {}
        
        for name, config in self.fields.items():
            raw_value = form_data.get(name)
            
            # Check required
            if raw_value is None or raw_value == '':
                if config['required']:
                    self.errors[name] = f"{name} is required"
                    continue
                else:
                    result[name] = config['default']
                    continue
            
            # Type conversion
            try:
                converted = config['type'](raw_value)
                
                # Custom validation
                if config['validator']:
                    is_valid, error_msg = config['validator'](converted)
                    if not is_valid:
                        self.errors[name] = error_msg
                        continue
                
                result[name] = converted
            except (ValueError, TypeError):
                self.errors[name] = f"Invalid {name} format"
        
        return result
    
    def is_valid(self):
        """Check if processing had errors"""
        return len(self.errors) == 0

# Demo
processor = FormProcessor()

# Define form fields
processor.add_field('name', str, required=True, validator=lambda x: (len(x) >= 2, "Name too short"))
processor.add_field('age', int, required=True, validator=lambda x: (0 <= x <= 150, "Invalid age"))
processor.add_field('gpa', float, required=False, default=0.0, validator=lambda x: (0 <= x <= 4.0, "GPA must be 0-4"))
processor.add_field('is_student', bool, required=False, default=False)
processor.add_field('email', str, required=True, validator=lambda x: ('@' in x, "Invalid email"))

# Test form submissions
test_forms = [
    {'name': 'Alice', 'age': '25', 'gpa': '3.8', 'email': 'alice@example.com'},
    {'name': 'A', 'age': '25', 'gpa': '3.8', 'email': 'alice@example.com'},  # Name too short
    {'name': 'Bob', 'age': '-5', 'gpa': '3.8', 'email': 'bob@example.com'},    # Invalid age
    {'name': 'Charlie', 'age': '30', 'gpa': '5.0', 'email': 'charlie@example.com'}, # Invalid GPA
    {'name': 'Diana', 'age': '28', 'email': 'invalid'},  # Invalid email
    {},  # Empty form
]

print("=== Form Processor Demo ===")
for i, form in enumerate(test_forms, 1):
    print(f"\nForm {i}: {form}")
    
    result = processor.process(form)
    
    if processor.is_valid():
        print(f"  ✓ Valid!")
        for key, value in result.items():
            print(f"    {key}: {value} (type: {type(value).__name__})")
    else:
        print(f"  ✗ Invalid!")
        for field, error in processor.errors.items():
            print(f"    {field}: {error}")
```

## Type Conversion Best Practices

### ✅ Do This
```python
# Use try-except for safe conversion
def safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

# Check type before conversion
def process(value):
    if isinstance(value, str):
        value = int(value)
    return value * 2

# Use default values
age = int(input("Age: ")) if input("Age: ").strip() else 0

# Validate after conversion
value = int(user_input)
if 0 <= value <= 100:
    process(value)

# Use appropriate conversion for context
user_id = str(user_id)  # Convert to string for display
price = float(price_str)  # Convert to float for calculation
is_valid = bool(data)  # Convert to bool for condition
```

### ❌ Avoid This
```python
# Avoid - assuming conversion works
age = int(input("Age: "))  # Crashes if input not number

# Avoid - using bool() on strings for logic
if bool(user_input):  # "False" becomes True!
    process()

# Avoid - losing precision
value = int(3.999)  # 3, not 4

# Avoid - unnecessary conversion
if bool(x) == True:  # Just use 'if x:'

# Avoid - conversion in loops when not needed
for i in range(len(str_list)):
    num = int(str_list[i])  # Convert once before loop
```

## Type Conversion Reference Table

| From/To | int() | float() | str() | bool() |
|---------|-------|---------|-------|--------|
| int | - | `42 → 42.0` | `42 → "42"` | `42 → True`<br>`0 → False` |
| float | `3.14 → 3` | - | `3.14 → "3.14"` | `3.14 → True`<br>`0.0 → False` |
| str | `"123" → 123`<br>`"12.3" → Error` | `"12.3" → 12.3` | - | `"Hello" → True`<br>`"" → False` |
| bool | `True → 1`<br>`False → 0` | `True → 1.0`<br>`False → 0.0` | `True → "True"` | - |
| None | Error | Error | `"None"` | `False` |
| list | Error | Error | `"[1, 2]"` | `[] → False`<br>`[1] → True` |

## Summary

- **int()**: Converts to integer (truncates floats, parses strings)
- **float()**: Converts to floating-point number
- **str()**: Converts to string representation
- **bool()**: Converts to boolean (falsy vs truthy)
- **Implicit conversion**: Happens automatically (int + float = float)
- **Explicit conversion**: Use conversion functions
- **Error handling**: Use try-except for safe conversion
- **Validation**: Always validate after conversion
- **Base conversion**: int() supports binary, octal, hex
- **Special values**: float() handles inf, -inf, nan
- **Truthiness**: Empty/zero values are False, others True

## Basic Template
```python
#!/usr/bin/env python3

def type_conversion_demo():
    """Demonstrate basic type conversions"""
    
    # Integer conversions
    print("=== int() Conversion ===")
    print(f"int(3.14) = {int(3.14)}")
    print(f"int('123') = {int('123')}")
    print(f"int(True) = {int(True)}")
    print(f"int('FF', 16) = {int('FF', 16)}")
    
    # Float conversions
    print("\n=== float() Conversion ===")
    print(f"float(42) = {float(42)}")
    print(f"float('3.14') = {float('3.14')}")
    print(f"float(True) = {float(True)}")
    print(f"float('1.5e3') = {float('1.5e3')}")
    
    # String conversions
    print("\n=== str() Conversion ===")
    print(f"str(42) = '{str(42)}'")
    print(f"str(3.14) = '{str(3.14)}'")
    print(f"str(True) = '{str(True)}'")
    print(f"str([1,2,3]) = '{str([1,2,3])}'")
    
    # Boolean conversions
    print("\n=== bool() Conversion ===")
    print(f"bool(42) = {bool(42)}")
    print(f"bool(0) = {bool(0)}")
    print(f"bool('Hello') = {bool('Hello')}")
    print(f"bool('') = {bool('')}")
    print(f"bool([]) = {bool([])}")
    print(f"bool(None) = {bool(None)}")

def safe_conversion():
    """Demonstrate safe conversion with error handling"""
    
    def safe_int(value, default=0):
        try:
            return int(value)
        except (ValueError, TypeError):
            return default
    
    test_values = ["123", "12.34", "abc", None, [1, 2], ""]
    
    print("\n=== Safe Conversion ===")
    for value in test_values:
        result = safe_int(value)
        print(f"safe_int({repr(value):15}) = {result}")

def practical_example():
    """Practical example of type conversion"""
    
    # Simulate form data (always strings)
    form_data = {
        'name': 'Alice',
        'age': '25',
        'gpa': '3.8',
        'is_active': 'true'
    }
    
    print("\n=== Form Processing ===")
    print(f"Raw data: {form_data}")
    
    # Convert to proper types
    processed = {
        'name': str(form_data['name']),
        'age': int(form_data['age']),
        'gpa': float(form_data['gpa']),
        'is_active': form_data['is_active'].lower() == 'true'
    }
    
    print(f"Processed: {processed}")
    for key, value in processed.items():
        print(f"  {key}: {value} (type: {type(value).__name__})")

if __name__ == "__main__":
    type_conversion_demo()
    safe_conversion()
    practical_example()
```

*This documentation belongs to https://github.com/InterCentury*