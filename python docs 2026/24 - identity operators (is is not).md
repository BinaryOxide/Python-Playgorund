# 24 - Identity Operators (is, is not)

## What are Identity Operators?
Identity operators compare the memory locations of two objects. They check if two variables reference the **same object** in memory, not just if they have the same value. Python has two identity operators: `is` and `is not`.

## The is Operator

### Basic Usage
```python
# is returns True if both variables reference the same object
a = [1, 2, 3]
b = a  # b references the same object as a
c = [1, 2, 3]  # c references a different object with same value

print(a is b)  # True (same object)
print(a is c)  # False (different objects)
print(a is a)  # True (same object)

# With None (most common use)
x = None
print(x is None)  # True
print(x is not None)  # False
```

### Identity vs Equality
```python
# == compares values (equality)
# is compares identity (same object)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 == list2: {list1 == list2}")  # True (same values)
print(f"list1 is list2: {list1 is list2}")  # False (different objects)

print(f"list1 == list3: {list1 == list3}")  # True (same values)
print(f"list1 is list3: {list1 is list3}")  # True (same object)

# Strings can be tricky due to interning
str1 = "hello"
str2 = "hello"
print(str1 is str2)  # Often True (interned by Python)

str3 = "hello world"
str4 = "hello world"
print(str3 is str4)  # May be False (not always interned)
```

## The is not Operator

### Basic Usage
```python
# is not returns True if variables reference different objects
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is not b)  # False (same object)
print(a is not c)  # True (different objects)

# Most common: checking if not None
value = get_value()
if value is not None:
    process(value)
```

## Integer Caching (Small Integers)

```python
# Python caches small integers (-5 to 256)
# This is an implementation detail, not guaranteed!

# Small integers are cached
a = 100
b = 100
print(a is b)  # True (cached)

# Larger integers may not be cached
a = 1000
b = 1000
print(a is b)  # May be False (implementation dependent)

# But don't rely on this for integers!
# Always use == for value comparison

# Even small integers from calculations
a = 100
b = 50 + 50
print(a is b)  # True (same cached object)
```

## String Interning

```python
# Python interns some strings automatically
# This saves memory for frequently used strings

# Identical string literals often reference same object
s1 = "hello"
s2 = "hello"
print(s1 is s2)  # Usually True (interned)

# Strings created at runtime may not be interned
s3 = "hello world"
s4 = "hello world"
print(s3 is s4)  # May be False

# Explicit interning
import sys
s5 = sys.intern("hello world")
s6 = sys.intern("hello world")
print(s5 is s6)  # True (explicitly interned)

# Best practice: use == for string comparison
# Use is only for comparing with None or singletons
```

## Singleton Objects

```python
# None is a singleton (only one instance)
a = None
b = None
print(a is b)  # True
print(a is None)  # True

# True and False are singletons
print(True is True)  # True
print(False is False)  # True
print(True is False)  # False

# Ellipsis (...) is a singleton
e1 = ...
e2 = ...
print(e1 is e2)  # True

# NotImplemented is a singleton
print(NotImplemented is NotImplemented)  # True
```

## When to Use is vs ==

### Use is for:
```python
# 1. Comparing with None
if value is None:
    print("No value")

# 2. Comparing with True/False (but usually just use the boolean)
if flag is True:  # Works, but 'if flag:' is better
    print("Flag is True")

# 3. Checking against singletons
SENTINEL = object()
def process(value):
    if value is SENTINEL:
        return "Default"
    return value

# 4. Type checking with class objects (rare)
if type(obj) is list:  # Exact type, not subclass
    print("It's exactly a list")
```

### Use == for:
```python
# 1. Value equality (most cases)
if a == b:
    print("Values are equal")

# 2. String comparison
if name == "Alice":
    print("Hello Alice")

# 3. Numeric comparison
if score == 100:
    print("Perfect score!")

# 4. List/tuple/dict comparison
if list1 == list2:
    print("Same contents")

# 5. Comparing with True/False (just use the variable)
if is_valid:  # not 'if is_valid == True'
    print("Valid")
```

## Practical Examples

### Example 1: Singleton Pattern
```python
class Singleton:
    """Singleton pattern using identity operators"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            print("Singleton initialized")

# Demo
s1 = Singleton()
s2 = Singleton()
s3 = Singleton()

print(f"s1 is s2: {s1 is s2}")  # True
print(f"s2 is s3: {s2 is s3}")  # True
print(f"All same object: {s1 is s2 is s3}")  # True

# They are the same instance
s1.value = 42
print(f"s2.value: {s2.value}")  # 42
print(f"s3.value: {s3.value}")  # 42
```

### Example 2: Sentinel Values
```python
class Sentinel:
    """Using sentinel values with identity comparison"""
    
    # Define sentinels as unique objects
    MISSING = object()
    EMPTY = object()
    DEFAULT = object()
    
    @classmethod
    def get_value(cls, value, default=DEFAULT):
        """Get value with sentinel handling"""
        if value is cls.MISSING:
            return "Value is missing"
        elif value is cls.EMPTY:
            return "Value is empty"
        elif value is cls.DEFAULT:
            return "Using default"
        else:
            return f"Value: {value}"
    
    @classmethod
    def process_data(cls, data=MISSING):
        """Process data with sentinel default"""
        if data is cls.MISSING:
            return "No data provided"
        if data is cls.EMPTY:
            return "Empty data"
        if not data:
            return "Falsy data"
        return f"Processing: {data}"

# Demo
print("=== Sentinel Values Demo ===")
print(f"MISSING: {Sentinel.get_value(Sentinel.MISSING)}")
print(f"EMPTY: {Sentinel.get_value(Sentinel.EMPTY)}")
print(f"DEFAULT: {Sentinel.get_value(Sentinel.DEFAULT)}")
print(f"Custom: {Sentinel.get_value(42)}")

print("\n=== Process Data ===")
print(f"process_data(): {Sentinel.process_data()}")
print(f"process_data(MISSING): {Sentinel.process_data(Sentinel.MISSING)}")
print(f"process_data(EMPTY): {Sentinel.process_data(Sentinel.EMPTY)}")
print(f"process_data(None): {Sentinel.process_data(None)}")
print(f"process_data([]): {Sentinel.process_data([])}")
print(f"process_data('hello'): {Sentinel.process_data('hello')}")
```

### Example 3: Caching System
```python
class ObjectCache:
    """Cache system using identity for object reuse"""
    
    def __init__(self):
        self._cache = {}
    
    def get_or_create(self, key, creator_func):
        """Get object from cache or create new one"""
        if key in self._cache:
            return self._cache[key]
        
        obj = creator_func()
        self._cache[key] = obj
        return obj
    
    def get_cached_object(self, key):
        """Get cached object, return None if not found"""
        return self._cache.get(key)
    
    def is_cached(self, key, obj):
        """Check if specific object instance is cached"""
        cached = self._cache.get(key)
        return cached is obj  # Identity check
    
    def clear(self):
        """Clear cache"""
        self._cache.clear()

# Demo
cache = ObjectCache()

def create_user(name):
    return {"name": name, "id": id(name)}

print("=== Cache Demo ===")

# Get or create objects
alice1 = cache.get_or_create("alice", lambda: create_user("Alice"))
alice2 = cache.get_or_create("alice", lambda: create_user("Alice"))
bob = cache.get_or_create("bob", lambda: create_user("Bob"))

print(f"alice1 is alice2: {alice1 is alice2}")  # True (same object)
print(f"alice1 == alice2: {alice1 == alice2}")  # True (same values)
print(f"alice1 is bob: {alice1 is bob}")        # False (different)

# Check if specific instance is cached
cached_alice = cache.get_cached_object("alice")
print(f"cached_alice is alice1: {cached_alice is alice1}")  # True

# Modify cached object
alice1["email"] = "alice@example.com"
print(f"alice2 email: {alice2.get('email')}")  # Modified in both!

# Cache invalidation
cache.clear()
alice3 = cache.get_or_create("alice", lambda: create_user("Alice"))
print(f"After clear, alice1 is alice3: {alice1 is alice3}")  # False (new object)
```

### Example 4: Object Pool
```python
class Connection:
    """Database connection object"""
    _instances = []
    _max_instances = 5
    
    def __new__(cls, *args, **kwargs):
        # Reuse existing connections if available
        if cls._instances:
            return cls._instances.pop()
        return super().__new__(cls)
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.is_open = True
    
    def close(self):
        """Return connection to pool"""
        if not self.is_open:
            return
        self.is_open = False
        Connection._instances.append(self)
    
    def __repr__(self):
        return f"Connection(db={self.db_name}, open={self.is_open})"

class ConnectionPool:
    """Manage connection objects with identity checking"""
    
    def __init__(self, db_name, pool_size=3):
        self.db_name = db_name
        self.pool_size = pool_size
        self.active_connections = []
        self.available_connections = []
        
        # Create initial connections
        for _ in range(pool_size):
            conn = Connection(db_name)
            self.available_connections.append(conn)
    
    def acquire(self):
        """Acquire a connection from pool"""
        if not self.available_connections:
            if len(self.active_connections) < self.pool_size:
                # Create new connection
                conn = Connection(self.db_name)
            else:
                return None  # No available connections
        else:
            conn = self.available_connections.pop()
        
        conn.is_open = True
        self.active_connections.append(conn)
        return conn
    
    def release(self, connection):
        """Release connection back to pool"""
        if connection in self.active_connections:
            self.active_connections.remove(connection)
            connection.close()
            self.available_connections.append(connection)
            return True
        return False
    
    def is_active(self, connection):
        """Check if connection is currently active (identity check)"""
        return connection in self.active_connections
    
    def is_from_pool(self, connection):
        """Check if connection belongs to this pool (identity check)"""
        return (connection in self.active_connections or 
                connection in self.available_connections)
    
    def get_stats(self):
        """Get pool statistics"""
        return {
            'active': len(self.active_connections),
            'available': len(self.available_connections),
            'total': len(self.active_connections) + len(self.available_connections)
        }

# Demo
print("=== Connection Pool Demo ===")

pool = ConnectionPool("my_database", pool_size=2)
print(f"Initial stats: {pool.get_stats()}")

# Acquire connections
conn1 = pool.acquire()
conn2 = pool.acquire()
print(f"\nAfter acquiring 2 connections: {pool.get_stats()}")
print(f"conn1 is from pool: {pool.is_from_pool(conn1)}")
print(f"conn2 is from pool: {pool.is_from_pool(conn2)}")

# Try to acquire third (should fail)
conn3 = pool.acquire()
print(f"Third connection: {conn3} (None = no available)")

# Release one connection
pool.release(conn1)
print(f"\nAfter releasing conn1: {pool.get_stats()}")
print(f"conn1 is active: {pool.is_active(conn1)}")

# Acquire again (should reuse conn1)
conn4 = pool.acquire()
print(f"Acquired conn4: {conn4}")
print(f"conn1 is conn4: {conn1 is conn4}")  # True (reused)
print(f"After acquire: {pool.get_stats()}")
```

### Example 5: Flyweight Pattern
```python
class Flyweight:
    """Flyweight pattern using object reuse"""
    _pool = {}
    
    def __new__(cls, key):
        # Return existing object if it exists
        if key in cls._pool:
            return cls._pool[key]
        
        # Create new object
        obj = super().__new__(cls)
        cls._pool[key] = obj
        return obj
    
    def __init__(self, key):
        # Only initialize once
        if not hasattr(self, 'initialized'):
            self.key = key
            self.initialized = True
            print(f"Created new flyweight for key: {key}")
    
    def __repr__(self):
        return f"Flyweight(key='{self.key}')"

class Character:
    """Character flyweight factory"""
    _characters = {}
    
    def __new__(cls, char, font, size):
        key = (char, font, size)
        if key in cls._characters:
            return cls._characters[key]
        
        obj = super().__new__(cls)
        cls._characters[key] = obj
        return obj
    
    def __init__(self, char, font, size):
        if not hasattr(self, 'initialized'):
            self.char = char
            self.font = font
            self.size = size
            self.initialized = True
    
    def render(self, x, y):
        """Render character at position"""
        print(f"Rendering '{self.char}' at ({x},{y}) with {self.font} {self.size}pt")
    
    def __repr__(self):
        return f"Character('{self.char}', '{self.font}', {self.size})"

# Demo
print("=== Flyweight Pattern Demo ===")

# Create flyweight objects
f1 = Flyweight("shared")
f2 = Flyweight("shared")
f3 = Flyweight("unique")

print(f"f1 is f2: {f1 is f2}")  # True (same object)
print(f"f1 is f3: {f1 is f3}")  # False (different)
print(f"f1 == f2: {f1 == f2}")  # True (same object)

print("\n=== Character Flyweight Demo ===")

# Create characters (same char/font/size will reuse)
c1 = Character('A', 'Arial', 12)
c2 = Character('A', 'Arial', 12)
c3 = Character('B', 'Arial', 12)
c4 = Character('A', 'Times', 12)

print(f"c1 is c2: {c1 is c2}")  # True (same char/font/size)
print(f"c1 is c3: {c1 is c3}")  # False (different char)
print(f"c1 is c4: {c1 is c4}")  # False (different font)

# Render characters
print("\nRendering:")
c1.render(10, 20)
c2.render(30, 40)  # Same object as c1
c3.render(50, 60)
```

### Example 6: Reference Tracking System
```python
import weakref
from datetime import datetime

class ReferenceTracker:
    """Track object references using identity operators"""
    
    def __init__(self):
        self.objects = {}  # id -> weakref
        self.references = {}  # id -> list of referrers
    
    def track(self, obj, owner=None):
        """Track an object"""
        obj_id = id(obj)
        
        # Store weak reference to avoid preventing garbage collection
        if obj_id not in self.objects:
            self.objects[obj_id] = weakref.ref(obj)
        
        # Track who references this object
        if obj_id not in self.references:
            self.references[obj_id] = set()
        
        if owner is not None:
            owner_id = id(owner)
            self.references[obj_id].add(owner_id)
            self.track(owner)  # Also track the owner
    
    def is_tracked(self, obj):
        """Check if object is tracked (identity check)"""
        obj_id = id(obj)
        if obj_id not in self.objects:
            return False
        
        ref = self.objects[obj_id]
        return ref() is obj  # Check if still alive and same object
    
    def get_referrers(self, obj):
        """Get objects that reference this object"""
        obj_id = id(obj)
        if obj_id not in self.references:
            return []
        
        referrers = []
        for ref_id in self.references[obj_id]:
            if ref_id in self.objects:
                ref = self.objects[ref_id]()
                if ref is not None:
                    referrers.append(ref)
        return referrers
    
    def get_stats(self):
        """Get tracking statistics"""
        alive = 0
        for obj_id, ref in self.objects.items():
            if ref() is not None:
                alive += 1
        
        return {
            'total_tracked': len(self.objects),
            'alive_objects': alive,
            'dead_objects': len(self.objects) - alive,
            'reference_count': sum(len(refs) for refs in self.references.values())
        }

# Demo
tracker = ReferenceTracker()

print("=== Reference Tracking Demo ===")

# Create objects
class Data:
    def __init__(self, name):
        self.name = name
        self.created_at = datetime.now()
    
    def __repr__(self):
        return f"Data('{self.name}')"

# Track objects
obj1 = Data("Object 1")
obj2 = Data("Object 2")
obj3 = Data("Object 3")

tracker.track(obj1)
tracker.track(obj2)
tracker.track(obj3, owner=obj1)  # obj1 references obj3

print(f"Initial stats: {tracker.get_stats()}")
print(f"obj1 tracked: {tracker.is_tracked(obj1)}")
print(f"obj2 tracked: {tracker.is_tracked(obj2)}")
print(f"obj3 tracked: {tracker.is_tracked(obj3)}")

print(f"\nReferrers of obj3: {tracker.get_referrers(obj3)}")

# Create reference cycle
obj1.ref = obj2
obj2.ref = obj1
tracker.track(obj1)  # Update tracking

# Delete some objects
del obj2
import gc
gc.collect()

print(f"\nAfter deleting obj2: {tracker.get_stats()}")
print(f"obj1 tracked: {tracker.is_tracked(obj1)}")
print(f"obj2 still tracked: {tracker.is_tracked(obj2) if 'obj2' in locals() else 'deleted'}")

# Identity vs equality in tracking
list1 = [1, 2, 3]
list2 = [1, 2, 3]
tracker.track(list1)
tracker.track(list2)

print(f"\nlist1 is list2: {list1 is list2}")  # False (different objects)
print(f"Both tracked: {tracker.is_tracked(list1)} and {tracker.is_tracked(list2)}")
```

## Common Mistakes

### Mistake 1: Using is for Value Comparison
```python
# Wrong - using is for value equality
a = 1000
b = 1000
if a is b:  # May be False (not guaranteed)
    print("Equal")

# Right - use == for value comparison
if a == b:
    print("Equal")
```

### Mistake 2: Comparing Strings with is
```python
# Wrong - unreliable string comparison
name = input("Enter name: ")
if name is "Alice":  # May be False even when value matches
    print("Hello Alice")

# Right - use == for string comparison
if name == "Alice":
    print("Hello Alice")
```

### Mistake 3: Using is with Numeric Values
```python
# Wrong - relying on integer caching
x = 257
y = 257
if x is y:  # May be False (implementation dependent)
    print("Same object")

# Right - use == for numeric values
if x == y:
    print("Same value")
```

### Mistake 4: Not Using is for None
```python
# Wrong - using == for None
if value == None:  # Works but not recommended
    print("None")

# Right - use is for None
if value is None:
    print("None")
```

### Mistake 5: Confusing is with == in Collections
```python
# Wrong - checking membership with is
items = [1, 2, 3]
if 2 is in items:  # Syntax error!
    pass

# Right - use in operator
if 2 in items:
    print("Found")
```

## Identity vs Equality Comparison Table

| Operation | Checks | Use Case | Example |
|-----------|--------|----------|---------|
| `a is b` | Same object (identity) | None, singletons | `x is None` |
| `a == b` | Same value (equality) | Most comparisons | `x == 5` |
| `a is not b` | Different objects | None check | `x is not None` |
| `a != b` | Different values | Value inequality | `x != 5` |

## Best Practices

### ✅ Do This
```python
# Use is for None
if value is None:
    pass

# Use is for singleton comparison
SENTINEL = object()
if result is SENTINEL:
    pass

# Use == for value comparison
if a == b:
    pass

# Use is for checking against True/False (rare)
if flag is True:  # Works, but 'if flag:' is better
    pass

# Use type() with is for exact type checking (rare)
if type(obj) is list:  # Exactly list, not subclass
    pass
```

### ❌ Avoid This
```python
# Avoid - using is for numeric values
if x is 100:  # Unreliable
    pass

# Avoid - using is for strings from input
if name is "Alice":  # Unreliable
    pass

# Avoid - using == for None
if value == None:  # Works but not Pythonic
    pass

# Avoid - using is for list/dict comparison
if list1 is list2:  # Probably not what you want
    pass

# Avoid - relying on integer caching
if 1000 is 1000:  # Implementation dependent
    pass
```

## Quick Reference Table

| Expression | Meaning | Best Practice |
|------------|---------|---------------|
| `x is None` | Check if x is None | ✅ Always use `is` |
| `x is not None` | Check if x is not None | ✅ Always use `is not` |
| `x is y` | Check if same object | 🔲 Use for singletons |
| `x == y` | Check if same value | ✅ Use for most cases |
| `x is True` | Check if x is True | ⚠️ Use `if x:` instead |
| `x is False` | Check if x is False | ⚠️ Use `if not x:` instead |

## Summary

- **`is`** checks if two variables reference the same object (identity)
- **`==`** checks if two objects have the same value (equality)
- **Use `is` for `None`**, `True`, `False`, and singletons
- **Use `==` for strings, numbers, lists, dictionaries, and most types**
- **Small integers (-5 to 256)** are cached (implementation detail)
- **String interning** may cause unexpected `is` results
- **Don't rely on integer/string interning** for identity comparison
- **`is not`** is the negative form of `is`
- **Singleton pattern** relies on identity for uniqueness

## Basic Template
```python
#!/usr/bin/env python3

def identity_demo():
    """Demonstrate identity operators"""
    
    # Basic identity
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    
    print(f"a is b: {a is b}")  # True (same object)
    print(f"a is c: {a is c}")  # False (different objects)
    print(f"a == c: {a == c}")  # True (same values)

def none_check():
    """Check for None using is"""
    
    def get_value(return_none=False):
        return None if return_none else 42
    
    value = get_value(True)
    
    # Correct way to check None
    if value is None:
        print("Value is None")
    
    if value is not None:
        print(f"Value is {value}")

def singleton_check():
    """Using is with singletons"""
    
    # None singleton
    print(f"None is None: {None is None}")  # True
    
    # True/False singletons
    print(f"True is True: {True is True}")  # True
    print(f"False is False: {False is False}")  # True
    
    # Custom singleton
    SENTINEL = object()
    result = SENTINEL
    
    if result is SENTINEL:
        print("Got sentinel value")

def integer_caching():
    """Integer caching behavior (implementation detail)"""
    
    # Small integers are cached
    a = 100
    b = 100
    print(f"100 is 100: {a is b}")  # Usually True
    
    # Larger integers may not be cached
    a = 1000
    b = 1000
    print(f"1000 is 1000: {a is b}")  # May be False
    
    # Don't rely on this! Use == for values
    print(f"1000 == 1000: {a == b}")  # True

def best_practices():
    """Best practices for identity operators"""
    
    # ✅ Good - using is for None
    value = None
    if value is None:
        print("None detected")
    
    # ✅ Good - using is for singletons
    DEFAULT = object()
    config = DEFAULT
    if config is DEFAULT:
        print("Using default config")
    
    # ✅ Good - using == for values
    name = "Alice"
    if name == "Alice":
        print("Hello Alice")
    
    # ❌ Bad - using is for string values
    # if name is "Alice":  # Unreliable!
    #     print("Hello Alice")
    
    # ❌ Bad - using == for None
    # if value == None:  # Works but not recommended
    #     print("None")

if __name__ == "__main__":
    print("=== IDENTITY DEMO ===")
    identity_demo()
    
    print("\n=== NONE CHECK ===")
    none_check()
    
    print("\n=== SINGLETON CHECK ===")
    singleton_check()
    
    print("\n=== INTEGER CACHING ===")
    integer_caching()
    
    print("\n=== BEST PRACTICES ===")
    best_practices()
```

*This documentation belongs to https://github.com/InterCentury*