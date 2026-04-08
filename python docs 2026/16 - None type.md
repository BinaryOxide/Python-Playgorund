# 16 - None Type in Python

## What is None?
`None` is a special constant in Python that represents the absence of a value or a null value. It is an object of its own datatype (`NoneType`) and is often used to signify "nothing", "no value", or "not initialized".

## Basic Characteristics of None

```python
# None is a singleton
none1 = None
none2 = None
print(none1 is none2)  # True (same object)

# None type
print(type(None))       # <class 'NoneType'>

# None is False in boolean context
print(bool(None))       # False

# None represents absence of value
value = None
print(value)            # None
```

## None vs Other "Empty" Values

```python
# None is different from empty values
print(None == 0)        # False
print(None == False)    # False
print(None == "")       # False
print(None == [])       # False
print(None == 0.0)      # False

# None is not the same as "empty"
empty_list = []
empty_string = ""
zero = 0

print(None is empty_list)     # False
print(None is empty_string)   # False
print(None is zero)           # False

# None is a singleton
a = None
b = None
print(a is b)           # True (same object)

# Different empty lists are different objects
c = []
d = []
print(c is d)           # False (different objects)
```

## Common Uses of None

### 1. Default Values for Function Parameters
```python
# Using None as default parameter
def greet(name=None):
    if name is None:
        print("Hello, Guest!")
    else:
        print(f"Hello, {name}!")

greet()           # Hello, Guest!
greet("Alice")    # Hello, Alice!

# Mutable default parameters (common pitfall - don't use [])
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))     # [1]
print(add_item(2))     # [2] (not [1, 2] - each call gets new list)
print(add_item(3, [10, 20]))  # [10, 20, 3]
```

### 2. Return Value for Functions (Default)
```python
# Functions return None if no return statement
def do_nothing():
    pass

result = do_nothing()
print(result)       # None
print(type(result)) # <class 'NoneType'>

# Explicitly returning None
def find_user(user_id):
    if user_id == 123:
        return "Alice"
    return None  # Explicit None for not found

user = find_user(999)
if user is None:
    print("User not found")
else:
    print(f"Found: {user}")
```

### 3. Placeholder for Missing Data
```python
# Database record with optional fields
class User:
    def __init__(self, name, email=None, phone=None):
        self.name = name
        self.email = email      # None means not provided
        self.phone = phone      # None means not provided
    
    def contact_info(self):
        info = f"Name: {self.name}"
        if self.email is not None:
            info += f", Email: {self.email}"
        if self.phone is not None:
            info += f", Phone: {self.phone}"
        return info

user1 = User("Alice", email="alice@example.com")
user2 = User("Bob", phone="123-456-7890")
user3 = User("Charlie")

print(user1.contact_info())  # Name: Alice, Email: alice@example.com
print(user2.contact_info())  # Name: Bob, Phone: 123-456-7890
print(user3.contact_info())  # Name: Charlie
```

### 4. Sentinel Value for Optional Variables
```python
# Using None to indicate "not initialized"
def process_data(data):
    result = None  # Initialize as None
    
    if data:
        result = sum(data) / len(data)
    
    return result

avg = process_data([1, 2, 3, 4, 5])
if avg is None:
    print("No data to process")
else:
    print(f"Average: {avg}")

avg = process_data([])
if avg is None:
    print("No data to process")  # This prints
```

### 5. Removing Variable Reference
```python
# Using None to "clear" a variable
large_data = [i for i in range(1000000)]
print(f"Data exists: {large_data is not None}")

# Free memory by setting to None
large_data = None
print(f"Data exists: {large_data is not None}")

# Helps garbage collector
```

## Checking for None

### Using `is` Operator (Recommended)
```python
# Best practice - use 'is' for None comparison
value = None

if value is None:
    print("Value is None")

if value is not None:
    print("Value is not None")

# Don't use == for None
if value == None:  # Works but not recommended
    print("This works but is less efficient")
```

### Why `is` instead of `==`?
```python
# 'is' compares identity (faster, more accurate)
# '==' compares value (slower, could be overloaded)

class CustomClass:
    def __eq__(self, other):
        return True  # Always returns True

obj = CustomClass()
print(obj == None)   # True (due to __eq__ overload)
print(obj is None)   # False (correct)

# Always use 'is' for None
```

## None in Collections

```python
# Lists can contain None
mixed_list = [1, None, "text", None, 5]
print(mixed_list)  # [1, None, 'text', None, 5]

# Filter out None values
filtered = [x for x in mixed_list if x is not None]
print(filtered)  # [1, 'text', 5]

# Dictionaries can have None values
user_data = {
    "name": "Alice",
    "email": None,  # Email not provided
    "phone": "123-456",
    "age": None     # Age unknown
}

# Check for None values
for key, value in user_data.items():
    if value is None:
        print(f"{key} is missing")
```

## None in Conditional Statements

```python
# None is falsy
if None:
    print("This won't print")
else:
    print("None is falsy")

# But be careful - other falsy values exist
empty_string = ""
zero = 0
empty_list = []

# This can lead to bugs if None is treated like other falsy values
def process(value):
    if not value:
        return "No value"
    return value

print(process(None))        # No value
print(process(""))          # No value (maybe not intended)
print(process(0))           # No value (maybe not intended)
print(process([]))          # No value (maybe not intended)

# Better - explicit None check
def process_safe(value):
    if value is None:
        return "No value"
    if not value:
        return "Empty but not None"
    return value

print(process_safe(None))   # No value
print(process_safe(""))     # Empty but not None
print(process_safe(0))      # Empty but not None
```

## Practical Examples

### Example 1: Configuration System
```python
class Config:
    """Configuration system using None for unset values"""
    
    def __init__(self):
        self._settings = {}
    
    def set(self, key, value):
        """Set configuration value"""
        self._settings[key] = value
    
    def get(self, key, default=None):
        """Get configuration value, return default if not set"""
        return self._settings.get(key, default)
    
    def has(self, key):
        """Check if configuration exists (even if value is None)"""
        return key in self._settings
    
    def is_set(self, key):
        """Check if configuration has non-None value"""
        return key in self._settings and self._settings[key] is not None
    
    def get_or_prompt(self, key, prompt_func):
        """Get value or prompt user if not set"""
        value = self.get(key)
        if value is None:
            value = prompt_func(key)
            self.set(key, value)
        return value

# Demo
config = Config()

# Set some values
config.set("debug", True)
config.set("timeout", 30)
config.set("api_key", None)  # Explicitly set to None

print(f"debug: {config.get('debug')}")
print(f"timeout: {config.get('timeout')}")
print(f"api_key: {config.get('api_key')}")
print(f"database: {config.get('database')}")

print(f"\nHas 'api_key': {config.has('api_key')}")      # True
print(f"Is 'api_key' set: {config.is_set('api_key')}") # False
print(f"Has 'database': {config.has('database')}")      # False

# Get with default
print(f"Port: {config.get('port', 8080)}")

# Interactive get
def prompt_for_value(key):
    return input(f"Enter {key}: ")

api_key = config.get_or_prompt("api_key", prompt_for_value)
print(f"API Key: {api_key}")
```

### Example 2: Database Row Mapper
```python
class DatabaseRow:
    """Map database rows to objects, handling NULL as None"""
    
    def __init__(self, data):
        self.data = data
        self._null_values = set()
    
    def __getitem__(self, key):
        """Get column value, None for NULL"""
        value = self.data.get(key)
        return value if value is not None else None
    
    def get(self, key, default=None):
        """Get value with default if NULL or missing"""
        value = self[key]
        return value if value is not None else default
    
    def is_null(self, key):
        """Check if column is NULL"""
        return key in self.data and self.data[key] is None
    
    def __str__(self):
        items = []
        for key, value in self.data.items():
            if value is None:
                items.append(f"{key}=NULL")
            else:
                items.append(f"{key}={value}")
        return f"Row({', '.join(items)})"

# Simulate database rows
rows = [
    DatabaseRow({"id": 1, "name": "Alice", "email": "alice@example.com", "age": 30}),
    DatabaseRow({"id": 2, "name": "Bob", "email": None, "age": 25}),
    DatabaseRow({"id": 3, "name": "Charlie", "email": None, "age": None}),
]

print("=== Database Rows ===")
for row in rows:
    print(f"\n{row}")
    print(f"  Name: {row['name']}")
    print(f"  Email: {row.get('email', 'No email')}")
    print(f"  Age: {row.get('age', 'Unknown')}")
    print(f"  Email is NULL? {row.is_null('email')}")
```

### Example 3: Optional Chain Implementation
```python
class Maybe:
    """Simple Maybe monad for handling None safely"""
    
    def __init__(self, value):
        self.value = value
    
    def map(self, func):
        """Apply function if value is not None"""
        if self.value is None:
            return Maybe(None)
        try:
            return Maybe(func(self.value))
        except (AttributeError, KeyError, TypeError):
            return Maybe(None)
    
    def get_or(self, default):
        """Return value or default if None"""
        return default if self.value is None else self.value
    
    def __str__(self):
        return f"Maybe({self.value})"

# Safe navigation
def safe_get(obj, *keys):
    """Safely navigate nested dictionaries"""
    current = obj
    for key in keys:
        if current is None:
            return None
        current = current.get(key)
    return current

# Demo nested data
user_data = {
    "user": {
        "profile": {
            "address": {
                "city": "New York",
                "zip": "10001"
            },
            "phone": None
        },
        "settings": None
    }
}

print("=== Safe Navigation ===")
print(f"City: {safe_get(user_data, 'user', 'profile', 'address', 'city')}")
print(f"Phone: {safe_get(user_data, 'user', 'profile', 'phone')}")
print(f"Theme: {safe_get(user_data, 'user', 'settings', 'theme')}")

# Using Maybe
maybe_user = Maybe(user_data)
city = (maybe_user
        .map(lambda x: x.get('user'))
        .map(lambda x: x.get('profile'))
        .map(lambda x: x.get('address'))
        .map(lambda x: x.get('city'))
        .get_or('Unknown'))

print(f"\nMaybe monad result: {city}")

phone = (maybe_user
         .map(lambda x: x.get('user'))
         .map(lambda x: x.get('profile'))
         .map(lambda x: x.get('phone'))
         .get_or('No phone'))

print(f"Phone: {phone}")
```

### Example 4: Cache System with None
```python
from datetime import datetime, timedelta

class Cache:
    """Cache system using None for missing values"""
    
    def __init__(self, ttl_seconds=300):
        self._cache = {}
        self.ttl = timedelta(seconds=ttl_seconds)
    
    def set(self, key, value):
        """Set cache value (None is valid value)"""
        self._cache[key] = {
            'value': value,
            'timestamp': datetime.now()
        }
    
    def get(self, key):
        """Get cache value, return None if missing or expired"""
        if key not in self._cache:
            return None
        
        entry = self._cache[key]
        age = datetime.now() - entry['timestamp']
        
        if age > self.ttl:
            del self._cache[key]
            return None
        
        return entry['value']
    
    def get_or_compute(self, key, compute_func):
        """Get value or compute if missing"""
        value = self.get(key)
        if value is None:
            value = compute_func()
            self.set(key, value)
        return value
    
    def exists(self, key):
        """Check if key exists (even if value is None)"""
        if key not in self._cache:
            return False
        
        entry = self._cache[key]
        age = datetime.now() - entry['timestamp']
        return age <= self.ttl
    
    def is_cached_none(self, key):
        """Check if None is explicitly cached"""
        return self.exists(key) and self.get(key) is None

# Demo
cache = Cache(ttl_seconds=10)

print("=== Cache Demo ===")
print(f"Get missing: {cache.get('user')}")

# Cache None explicitly
cache.set('user', None)
print(f"Get cached None: {cache.get('user')}")
print(f"Exists? {cache.exists('user')}")
print(f"Is cached None? {cache.is_cached_none('user')}")

# Cache with computation
def expensive_compute():
    print("Computing expensive value...")
    return "Database Result"

value = cache.get_or_compute('data', expensive_compute)
print(f"First get: {value}")

value = cache.get_or_compute('data', expensive_compute)
print(f"Second get (cached): {value}")

# Cache differentiates between missing and None
cache.set('empty_result', None)
print(f"\n'empty_result' exists: {cache.exists('empty_result')}")
print(f"'empty_result' value: {cache.get('empty_result')}")

print(f"'missing' exists: {cache.exists('missing')}")
print(f"'missing' value: {cache.get('missing')}")
```

### Example 5: XML/JSON Parser with None
```python
import json
from typing import Any, Optional

class SafeParser:
    """Parse data with safe None handling"""
    
    @staticmethod
    def parse_json(json_str: str) -> Optional[dict]:
        """Parse JSON, return None if invalid"""
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            return None
    
    @staticmethod
    def get_nested(data: dict, path: str, default=None):
        """Get nested value using dot notation"""
        keys = path.split('.')
        current = data
        
        for key in keys:
            if current is None:
                return default
            if not isinstance(current, dict):
                return default
            current = current.get(key)
        
        return current if current is not None else default
    
    @staticmethod
    def safe_int(value: Any, default=None) -> Optional[int]:
        """Convert to int, return None if fails"""
        try:
            return int(value)
        except (ValueError, TypeError):
            return default
    
    @staticmethod
    def safe_float(value: Any, default=None) -> Optional[float]:
        """Convert to float, return None if fails"""
        try:
            return float(value)
        except (ValueError, TypeError):
            return default

# Demo
parser = SafeParser()

print("=== JSON Parsing ===")
valid_json = '{"user": {"name": "Alice", "age": "30", "email": null}}'
invalid_json = '{"invalid": json}'

data = parser.parse_json(valid_json)
print(f"Valid JSON: {data}")

invalid = parser.parse_json(invalid_json)
print(f"Invalid JSON: {invalid}")

print("\n=== Safe Navigation ===")
if data:
    print(f"user.name: {parser.get_nested(data, 'user.name')}")
    print(f"user.email: {parser.get_nested(data, 'user.email')}")
    print(f"user.phone: {parser.get_nested(data, 'user.phone', 'Unknown')}")
    print(f"missing.path: {parser.get_nested(data, 'missing.path')}")

print("\n=== Type Conversion ===")
age = parser.get_nested(data, 'user.age')
age_int = parser.safe_int(age)
print(f"Age as string: {age}, type: {type(age)}")
print(f"Age as int: {age_int}, type: {type(age_int)}")

invalid_age = parser.safe_int("not a number")
print(f"Invalid age: {invalid_age}")

# Working with None values
email = parser.get_nested(data, 'user.email')
if email is None:
    print("Email not provided")
```

### Example 6: Lazy Initialization Pattern
```python
class LazyProperty:
    """Property that initializes only when accessed"""
    
    def __init__(self, initializer):
        self.initializer = initializer
        self._value = None
        self._initialized = False
    
    def get(self):
        """Get value, initialize if needed"""
        if not self._initialized:
            self._value = self.initializer()
            self._initialized = True
        return self._value
    
    def reset(self):
        """Reset to uninitialized state"""
        self._value = None
        self._initialized = False
    
    def is_initialized(self):
        """Check if already initialized"""
        return self._initialized

class DatabaseConnection:
    """Database connection with lazy initialization"""
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self._connection = LazyProperty(self._create_connection)
        self._pool = LazyProperty(self._create_pool)
    
    def _create_connection(self):
        print(f"Creating actual connection to {self.connection_string}")
        return f"Connection({self.connection_string})"
    
    def _create_pool(self):
        print(f"Creating connection pool to {self.connection_string}")
        return f"Pool({self.connection_string})"
    
    @property
    def connection(self):
        return self._connection.get()
    
    @property
    def pool(self):
        return self._pool.get()
    
    def reconnect(self):
        self._connection.reset()
        self._pool.reset()
        print("Reconnection ready on next access")

# Demo
print("=== Lazy Initialization ===")
db = DatabaseConnection("postgresql://localhost/mydb")

print("Database object created (no connections yet)")
print(f"Connection initialized? {db._connection.is_initialized()}")
print(f"Pool initialized? {db._pool.is_initialized()}")

print("\nAccessing connection...")
conn = db.connection
print(f"Got connection: {conn}")
print(f"Connection initialized? {db._connection.is_initialized()}")

print("\nAccessing connection again...")
conn2 = db.connection
print(f"Got connection: {conn2}")
print("No new connection created (cached)")

print("\nAccessing pool...")
pool = db.pool
print(f"Got pool: {pool}")

print("\nReconnecting...")
db.reconnect()
print("Connection reset")
print(f"Connection initialized? {db._connection.is_initialized()}")

print("\nAccessing connection after reset...")
conn3 = db.connection
print(f"Got new connection: {conn3}")
```

## None vs Other Languages' Null

```python
# Python's None vs JavaScript's null
# Python: None is a singleton object
# JavaScript: null is a primitive value

# Python's None vs Java's null
# Java: null can be assigned to any object reference
# Python: None is a specific object of NoneType

# Python's None vs C's NULL
# C: NULL is a macro for 0
# Python: None is not 0

# None is an object
print(id(None))  # Same memory address everywhere

# None cannot be overwritten (built-in)
# None = 42  # SyntaxError!
```

## Common Mistakes

### Mistake 1: Using == instead of is
```python
# Wrong
value = None
if value == None:  # Works but not recommended
    print("Is None")

# Right
if value is None:
    print("Is None")

# Wrong for checking not None
if value != None:  # Works but not recommended
    print("Is not None")

# Right
if value is not None:
    print("Is not None")
```

### Mistake 2: Treating None as False
```python
# Wrong - assumes None is the only falsy value
def get_name(user):
    name = user.get('name')
    if not name:  # Will also reject "", 0, []
        return "Anonymous"
    return name

# Right - explicit None check
def get_name(user):
    name = user.get('name')
    if name is None:
        return "Anonymous"
    return name

# Or if empty string is valid
def get_name(user):
    name = user.get('name')
    if name is None:
        return "Anonymous"
    return name
```

### Mistake 3: Returning None for Errors
```python
# Bad - ambiguous
def divide(a, b):
    if b == 0:
        return None  # What does None mean? Error?
    return a / b

result = divide(10, 0)
if result is None:
    print("Error")  # But None could also be valid result?

# Better - raise exception
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

# Or use Optional with clear meaning
from typing import Optional

def divide(a: float, b: float) -> Optional[float]:
    """Returns None if division not possible"""
    if b == 0:
        return None
    return a / b
```

### Mistake 4: Mutable Default Arguments
```python
# Wrong - mutable default
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

# Wrong
def bad_function(items=[]):  # Same list reused!
    items.append(1)
    return items

print(bad_function())  # [1]
print(bad_function())  # [1, 1] - bug!

# Right
def good_function(items=None):
    if items is None:
        items = []
    items.append(1)
    return items
```

### Mistake 5: Not Handling None in Sequences
```python
# Wrong - assumes no None
def process_items(items):
    return sum(items)  # TypeError if any item is None

# Right - filter out None
def process_items(items):
    valid_items = [x for x in items if x is not None]
    return sum(valid_items)

# Or handle None
def process_items(items):
    total = 0
    for item in items:
        if item is not None:
            total += item
    return total
```

## Best Practices

### ✅ Do This
```python
# Use 'is' for None comparison
if value is None:
    pass

if value is not None:
    pass

# Use None for optional/default parameters
def func(param=None):
    if param is None:
        param = default_value

# Use None to indicate missing/unset values
config = {
    'timeout': None,  # Not configured
    'retries': 3
}

# Use None as sentinel for function returns
def find_item(items, target):
    for item in items:
        if item == target:
            return item
    return None

# Clear large objects when done
large_data = load_data()
process(large_data)
large_data = None  # Help garbage collector
```

### ❌ Avoid This
```python
# Avoid - using == for None
if value == None:
    pass

# Avoid - treating None as False without checking
if not value:  # May reject valid falsy values
    pass

# Avoid - returning None for multiple error conditions
def process(data):
    if not data:
        return None  # Error? Empty data?
    if invalid(data):
        return None  # Different error?
    return result

# Avoid - mutable defaults
def bad(items=[]):
    pass

# Avoid - ignoring None in sequences
data = [1, None, 3, None, 5]
total = sum(data)  # TypeError!
```

## Quick Reference Table

| Operation | Syntax | Result |
|-----------|--------|--------|
| None literal | `None` | `None` |
| Check None | `value is None` | `True`/`False` |
| Check not None | `value is not None` | `True`/`False` |
| Type of None | `type(None)` | `<class 'NoneType'>` |
| Boolean context | `bool(None)` | `False` |
| Equality | `None == None` | `True` |
| Identity | `None is None` | `True` |
| String representation | `str(None)` | `"None"` |
| Default parameter | `def f(x=None)` | Parameter optional |
| Return value | `return None` | Function returns None |

## Summary

- **None** represents absence of value (null/nothing)
- **Singleton**: Only one None object exists
- **Type**: `NoneType` (built-in)
- **Use `is`** for comparison, not `==`
- **Falsy**: `bool(None)` is `False`
- **Default parameters**: Use None to avoid mutable defaults
- **Return value**: Functions return None if no return
- **Sentinel**: Indicates missing/undefined values
- **Not equal to**: 0, False, empty string, empty list
- **Memory**: Can set variables to None for garbage collection

## Basic Template
```python
#!/usr/bin/env python3

# None basics
def none_basics():
    """Demonstrate None basics"""
    
    # None is a singleton
    x = None
    y = None
    print(f"x is y: {x is y}")  # True
    print(f"Type: {type(x)}")
    
    # None is falsy
    if None:
        print("This won't print")
    else:
        print("None is falsy")
    
    # Comparing None
    value = None
    if value is None:
        print("Value is None")
    
    if value is not None:
        print("Value is not None")

# None as default parameter
def greet(name=None):
    """Greet with default name"""
    if name is None:
        name = "Guest"
    return f"Hello, {name}!"

# None as return value
def find_user(users, target):
    """Find user, return None if not found"""
    for user in users:
        if user == target:
            return user
    return None

# None in data structures
def none_in_collections():
    """Using None in collections"""
    
    # List with None
    data = [1, None, 3, None, 5]
    print(f"Original: {data}")
    
    # Filter out None
    filtered = [x for x in data if x is not None]
    print(f"Filtered: {filtered}")
    
    # Dictionary with None values
    config = {
        "debug": True,
        "timeout": None,  # Not configured
        "retries": 3
    }
    
    for key, value in config.items():
        if value is None:
            print(f"{key} is not set")
        else:
            print(f"{key} = {value}")

# Safe handling of None
def safe_process(data):
    """Process data safely"""
    if data is None:
        return "No data"
    
    if not data:
        return "Empty data"
    
    return f"Processing: {data}"

# Main demo
if __name__ == "__main__":
    print("=== NONE BASICS ===")
    none_basics()
    
    print("\n=== DEFAULT PARAMETER ===")
    print(greet())
    print(greet("Alice"))
    
    print("\n=== FIND USER ===")
    users = ["Alice", "Bob", "Charlie"]
    print(f"Found Bob: {find_user(users, 'Bob')}")
    print(f"Found Dave: {find_user(users, 'Dave')}")
    
    print("\n=== NONE IN COLLECTIONS ===")
    none_in_collections()
    
    print("\n=== SAFE PROCESSING ===")
    print(safe_process(None))
    print(safe_process(""))
    print(safe_process([1, 2, 3]))
```

*This documentation belongs to https://github.com/InterCentury*