# 21 - Assignment Operators in Python

## What are Assignment Operators?
Assignment operators are used to assign values to variables. The most basic is the equals sign `=`, but Python provides several compound assignment operators that combine assignment with arithmetic or bitwise operations.

## Basic Assignment (=)

### Simple Assignment
```python
# Basic assignment
x = 10
name = "Alice"
price = 19.99
is_valid = True

# Multiple assignments in one line
a = b = c = 0
print(a, b, c)  # 0 0 0

# Multiple variables with different values
x, y, z = 10, 20, 30
print(x, y, z)  # 10 20 30

# Swapping variables (no temp needed)
a, b = 5, 10
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Unpacking sequences
point = (10, 20)
x, y = point
print(f"x={x}, y={y}")

# Extended unpacking (Python 3+)
first, *middle, last = [1, 2, 3, 4, 5]
print(f"first={first}, middle={middle}, last={last}")
```

## Arithmetic Assignment Operators

### Addition Assignment (+=)
```python
# Basic addition assignment
x = 10
x += 5      # x = x + 5
print(x)    # 15

# With floats
y = 3.14
y += 2.86   # y = y + 2.86
print(y)    # 6.0

# With strings (concatenation)
text = "Hello"
text += " World"
print(text)  # Hello World

# With lists (extends list)
numbers = [1, 2, 3]
numbers += [4, 5, 6]
print(numbers)  # [1, 2, 3, 4, 5, 6]

# With tuples (creates new tuple)
colors = ("red", "green")
colors += ("blue",)
print(colors)  # ('red', 'green', 'blue')
```

### Subtraction Assignment (-=)
```python
# Basic subtraction assignment
x = 20
x -= 5      # x = x - 5
print(x)    # 15

# With negative numbers
balance = 100
balance -= -20  # balance = balance - (-20)
print(balance)  # 120

# With floats
temp = 98.6
temp -= 1.5
print(temp)  # 97.1

# Cannot use with strings or lists
# text = "Hello"
# text -= "World"  # TypeError!
```

### Multiplication Assignment (*=)
```python
# Basic multiplication assignment
x = 5
x *= 3      # x = x * 3
print(x)    # 15

# With floats
price = 19.99
price *= 1.1  # Add 10%
print(f"${price:.2f}")  # $21.99

# With strings (repetition)
text = "Hi"
text *= 3
print(text)  # HiHiHi

# With lists (repetition)
items = [1, 2]
items *= 3
print(items)  # [1, 2, 1, 2, 1, 2]

# With negative numbers
x = 10
x *= -1
print(x)  # -10
```

### Division Assignment (/=)
```python
# Basic division assignment (always returns float)
x = 10
x /= 3      # x = x / 3
print(x)    # 3.3333333333333335
print(type(x))  # <class 'float'>

# Integer division results in float
x = 10
x /= 2
print(x)    # 5.0 (float, not int)

# With floats
total = 100.0
total /= 4
print(total)  # 25.0

# Division by zero raises error
# x = 10
# x /= 0  # ZeroDivisionError!
```

### Floor Division Assignment (//=)
```python
# Basic floor division assignment
x = 10
x //= 3     # x = x // 3
print(x)    # 3

# With negative numbers (rounds down)
x = -10
x //= 3
print(x)    # -4 (not -3!)

# With floats (result is float)
x = 10.5
x //= 3
print(x)    # 3.0
print(type(x))  # <class 'float'>

# Practical: convert seconds to minutes
seconds = 150
seconds //= 60
print(f"Minutes: {seconds}")  # Minutes: 2
```

### Modulo Assignment (%=)
```python
# Basic modulo assignment
x = 10
x %= 3      # x = x % 3
print(x)    # 1

# With negative numbers
x = -10
x %= 3
print(x)    # 2 (not -1!)

# With floats
x = 10.5
x %= 3
print(x)    # 1.5

# Practical: keep value in range
angle = 450
angle %= 360
print(f"Angle: {angle}°")  # Angle: 90°

# Check if number is even
num = 7
num %= 2
print(f"Is even? {num == 0}")  # Is even? False
```

### Exponentiation Assignment (**=)
```python
# Basic exponentiation assignment
x = 2
x **= 3     # x = x ** 3
print(x)    # 8

# With floats
x = 4.0
x **= 0.5   # Square root
print(x)    # 2.0

# With negative exponents
x = 2
x **= -2
print(x)    # 0.25

# Large exponents
x = 2
x **= 10
print(x)    # 1024

# Growth calculation
population = 1000
growth_rate = 1.05  # 5% growth
population **= 1  # population = population ** 1 (no change)
print(population)  # 1000
```

## Bitwise Assignment Operators

### Bitwise AND Assignment (&=)
```python
# Bitwise AND assignment
x = 0b1100  # 12 in decimal
x &= 0b1010  # 10 in decimal
print(bin(x))  # 0b1000 (8 in decimal)

# With integers
flags = 0b1111
mask = 0b1010
flags &= mask
print(f"Flags: {bin(flags)}")  # Flags: 0b1010

# Clearing specific bits
value = 0b11111111
mask = 0b00001111
value &= mask
print(bin(value))  # 0b1111
```

### Bitwise OR Assignment (|=)
```python
# Bitwise OR assignment
x = 0b1100  # 12
x |= 0b1010  # 10
print(bin(x))  # 0b1110 (14)

# Setting specific bits
flags = 0b0000
flags |= 0b0011  # Set bits 0 and 1
print(bin(flags))  # 0b11

# Adding permissions
permissions = 0b000
READ = 0b001
WRITE = 0b010
EXECUTE = 0b100

permissions |= READ
permissions |= WRITE
print(f"Permissions: {bin(permissions)}")  # Permissions: 0b11
```

### Bitwise XOR Assignment (^=)
```python
# Bitwise XOR assignment
x = 0b1100  # 12
x ^= 0b1010  # 10
print(bin(x))  # 0b0110 (6)

# Toggle bits
flags = 0b1010
flags ^= 0b1100  # Toggle bits
print(bin(flags))  # 0b0110

# Simple encryption (XOR cipher)
data = 0b10101010
key = 0b11110000
data ^= key  # Encrypt
print(f"Encrypted: {bin(data)}")
data ^= key  # Decrypt
print(f"Decrypted: {bin(data)}")
```

### Left Shift Assignment (<<=)
```python
# Left shift assignment (multiply by 2^n)
x = 5
x <<= 1     # x = x << 1 (multiply by 2)
print(x)    # 10

x = 3
x <<= 2     # Multiply by 4
print(x)    # 12

# Fast multiplication by powers of 2
value = 7
value <<= 3  # Multiply by 8
print(value)  # 56

# Building bit patterns
bits = 0b1
bits <<= 4
print(bin(bits))  # 0b10000
```

### Right Shift Assignment (>>=)
```python
# Right shift assignment (divide by 2^n)
x = 10
x >>= 1     # x = x >> 1 (divide by 2)
print(x)    # 5

x = 16
x >>= 2     # Divide by 4
print(x)    # 4

# Fast division by powers of 2
value = 100
value >>= 2  # Divide by 4
print(value)  # 25

# Extracting bits
value = 0b110100
value >>= 2
print(bin(value))  # 0b1101
```

## Walrus Operator (:=) - Python 3.8+

```python
# Assignment expression (walrus operator)
# Assign and use in same expression

# Without walrus
data = input("Enter data: ")
while data:
    print(f"Processing: {data}")
    data = input("Enter data: ")

# With walrus
while (data := input("Enter data: ")):
    print(f"Processing: {data}")

# In list comprehensions
# Without walrus
results = []
for i in range(10):
    square = i ** 2
    if square > 20:
        results.append(square)

# With walrus
results = [square for i in range(10) if (square := i ** 2) > 20]

# In conditionals
# Without walrus
value = get_value()
if value:
    process(value)

# With walrus
if (value := get_value()):
    process(value)

# Practical example
import re
text = "My email is alice@example.com"
if match := re.search(r'\w+@\w+\.\w+', text):
    print(f"Found email: {match.group()}")
```

## Assignment with Different Data Types

### Assigning to Multiple Variables
```python
# Same value to multiple variables
x = y = z = 0
print(f"x={x}, y={y}, z={z}")  # x=0, y=0, z=0

# Different values in one line
a, b, c = 10, 20, 30
print(f"a={a}, b={b}, c={c}")  # a=10, b=20, c=30

# Swapping variables
a, b = 5, 10
a, b = b, a
print(f"After swap: a={a}, b={b}")  # a=10, b=5

# Unpacking sequences
point = (100, 200)
x, y = point
print(f"x={x}, y={y}")  # x=100, y=200

# Unpacking with star operator
first, *rest = [1, 2, 3, 4, 5]
print(f"first={first}, rest={rest}")  # first=1, rest=[2,3,4,5]

*begin, last = [1, 2, 3, 4, 5]
print(f"begin={begin}, last={last}")  # begin=[1,2,3,4], last=5
```

### Assignment with Type Hints
```python
# Variable with type hint
x: int = 10
name: str = "Alice"
prices: list[float] = [19.99, 29.99, 39.99]

# Multiple with type hints
a: int = 5
b: float = 3.14
c: str = "Hello"

# Type hints don't enforce types (just documentation)
x: int = "hello"  # Works! (but type checker would complain)
```

## Practical Examples

### Example 1: Counter with Assignment Operators
```python
class Counter:
    """Demonstrate assignment operators with a counter"""
    
    def __init__(self):
        self.count = 0
        self.total = 0
    
    def increment(self, amount=1):
        self.count += amount
        return self.count
    
    def decrement(self, amount=1):
        self.count -= amount
        return self.count
    
    def multiply(self, factor):
        self.count *= factor
        return self.count
    
    def divide(self, divisor):
        if divisor != 0:
            self.count /= divisor
        return self.count
    
    def reset(self):
        self.count = 0
        return self.count
    
    def add_to_total(self, value):
        self.total += value
        return self.total
    
    def __str__(self):
        return f"Counter(count={self.count}, total={self.total})"

# Demo
counter = Counter()
print("=== Counter Demo ===")

print(f"Initial: {counter}")
counter.increment(5)
print(f"After +5: {counter}")
counter.decrement(2)
print(f"After -2: {counter}")
counter.multiply(3)
print(f"After ×3: {counter}")
counter.divide(2)
print(f"After ÷2: {counter}")
counter.add_to_total(100)
print(f"After total +100: {counter}")
counter.reset()
print(f"After reset: {counter}")
```

### Example 2: Shopping Cart with Compound Assignment
```python
class ShoppingCart:
    """Shopping cart using assignment operators"""
    
    def __init__(self):
        self.items = []
        self.total = 0.0
        self.discount = 0.0
    
    def add_item(self, name, price, quantity=1):
        """Add item to cart"""
        self.items += [name] * quantity
        self.total += price * quantity
        print(f"Added {quantity}x {name} (${price:.2f} each)")
    
    def remove_item(self, name, quantity=1):
        """Remove item from cart"""
        count = self.items.count(name)
        if count >= quantity:
            for _ in range(quantity):
                self.items.remove(name)
            # Need to recalculate total
            self.total = 0.0
            # Recalculate total (simplified)
            print(f"Removed {quantity}x {name}")
        else:
            print(f"Cannot remove {quantity}x {name} (only {count} in cart)")
    
    def apply_discount(self, percent):
        """Apply percentage discount"""
        self.discount = percent
        self.total *= (1 - percent / 100)
        print(f"Applied {percent}% discount")
    
    def add_tax(self, tax_rate):
        """Add tax to total"""
        tax = self.total * (tax_rate / 100)
        self.total += tax
        print(f"Added {tax_rate}% tax (${tax:.2f})")
    
    def clear_cart(self):
        """Clear entire cart"""
        self.items = []
        self.total = 0.0
        self.discount = 0.0
        print("Cart cleared")
    
    def display(self):
        """Display cart contents"""
        print("\n" + "=" * 40)
        print(f"Items: {len(self.items)}")
        if self.items:
            from collections import Counter
            item_counts = Counter(self.items)
            for item, count in item_counts.items():
                print(f"  {item}: {count}")
        print(f"Total: ${self.total:.2f}")
        if self.discount:
            print(f"Discount: {self.discount}%")
        print("=" * 40)

# Demo
cart = ShoppingCart()

print("=== Shopping Cart Demo ===")
cart.add_item("Laptop", 999.99, 1)
cart.add_item("Mouse", 29.99, 2)
cart.add_item("Keyboard", 79.99, 1)

cart.display()

cart.apply_discount(10)
cart.add_tax(8)
cart.display()

cart.remove_item("Mouse", 1)
cart.display()
```

### Example 3: Bank Account with Assignment Operations
```python
class BankAccount:
    """Bank account using assignment operators"""
    
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
        self.transaction_count = 0
        self.interest_rate = 0.02  # 2%
    
    def deposit(self, amount):
        """Deposit money"""
        if amount > 0:
            self.balance += amount
            self.transaction_count += 1
            print(f"Deposited: ${amount:.2f}")
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_count += 1
            print(f"Withdrew: ${amount:.2f}")
            return True
        print(f"Insufficient funds! (Balance: ${self.balance:.2f})")
        return False
    
    def apply_interest(self):
        """Apply annual interest"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: ${interest:.2f}")
        return interest
    
    def compound_interest(self, years):
        """Compound interest annually"""
        for year in range(years):
            self.balance *= (1 + self.interest_rate)
            print(f"Year {year + 1}: ${self.balance:.2f}")
    
    def transfer(self, other_account, amount):
        """Transfer money to another account"""
        if self.withdraw(amount):
            other_account.deposit(amount)
            print(f"Transferred ${amount:.2f} to {other_account.owner}")
            return True
        return False
    
    def __str__(self):
        return f"Account({self.owner}): ${self.balance:.2f} ({self.transaction_count} transactions)"

# Demo
print("=== Bank Account Demo ===")

# Create accounts
alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 500)

print(f"Initial: {alice}")
print(f"Initial: {bob}")

# Transactions
print("\n--- Transactions ---")
alice.deposit(500)
alice.withdraw(200)
alice.apply_interest()

bob.deposit(300)
bob.withdraw(100)

print(f"\nAfter transactions:")
print(alice)
print(bob)

# Transfer
print("\n--- Transfer ---")
alice.transfer(bob, 300)

print(f"\nAfter transfer:")
print(alice)
print(bob)

# Compound interest
print("\n--- Compound Interest (5 years) ---")
savings = BankAccount("Savings", 1000)
savings.compound_interest(5)
```

### Example 4: Statistics Tracker with Assignment Operators
```python
class StatisticsTracker:
    """Track statistics using assignment operators"""
    
    def __init__(self):
        self.count = 0
        self.sum = 0
        self.sum_squares = 0
        self.min_value = float('inf')
        self.max_value = float('-inf')
    
    def add_value(self, value):
        """Add a value to statistics"""
        self.count += 1
        self.sum += value
        self.sum_squares += value ** 2
        
        if value < self.min_value:
            self.min_value = value
        if value > self.max_value:
            self.max_value = value
        
        return self
    
    def add_multiple(self, values):
        """Add multiple values"""
        for value in values:
            self.add_value(value)
        return self
    
    def mean(self):
        """Calculate mean"""
        if self.count == 0:
            return 0
        return self.sum / self.count
    
    def variance(self):
        """Calculate variance"""
        if self.count < 2:
            return 0
        mean = self.mean()
        variance = (self.sum_squares / self.count) - (mean ** 2)
        return variance
    
    def std_dev(self):
        """Calculate standard deviation"""
        return self.variance() ** 0.5
    
    def reset(self):
        """Reset all statistics"""
        self.count = 0
        self.sum = 0
        self.sum_squares = 0
        self.min_value = float('inf')
        self.max_value = float('-inf')
        return self
    
    def __str__(self):
        return (f"Stats(count={self.count}, sum={self.sum:.2f}, "
                f"mean={self.mean():.2f}, std={self.std_dev():.2f}, "
                f"min={self.min_value}, max={self.max_value})")

# Demo
stats = StatisticsTracker()

print("=== Statistics Tracker Demo ===")

# Add single values
stats.add_value(10)
stats.add_value(20)
stats.add_value(30)
print(f"After adding: {stats}")

# Add multiple values
stats.add_multiple([15, 25, 35])
print(f"After adding multiple: {stats}")

# Chain operations
stats.add_value(40).add_value(50).add_value(60)
print(f"After chaining: {stats}")

# Track game scores
print("\n--- Game Score Tracker ---")
game_stats = StatisticsTracker()
scores = [85, 92, 78, 95, 88, 91, 84, 89, 93, 87]

for score in scores:
    game_stats.add_value(score)

print(f"Game Statistics:")
print(f"  Total games: {game_stats.count}")
print(f"  Total points: {game_stats.sum}")
print(f"  Average: {game_stats.mean():.1f}")
print(f"  Standard deviation: {game_stats.std_dev():.2f}")
print(f"  Highest score: {game_stats.max_value}")
print(f"  Lowest score: {game_stats.min_value}")

# Running average
print("\n--- Running Average ---")
running = StatisticsTracker()
data = [10, 20, 30, 40, 50]
for value in data:
    running.add_value(value)
    print(f"Added {value}: mean={running.mean():.1f}")
```

### Example 5: Bit Manipulation with Assignment
```python
class BitFlags:
    """Bit flags management using bitwise assignment"""
    
    def __init__(self):
        self.flags = 0
    
    def set_flag(self, flag):
        """Set a flag (|=)"""
        self.flags |= flag
        return self
    
    def clear_flag(self, flag):
        """Clear a flag (&~)"""
        self.flags &= ~flag
        return self
    
    def toggle_flag(self, flag):
        """Toggle a flag (^=)"""
        self.flags ^= flag
        return self
    
    def has_flag(self, flag):
        """Check if flag is set"""
        return (self.flags & flag) == flag
    
    def set_multiple(self, *flags):
        """Set multiple flags"""
        for flag in flags:
            self.flags |= flag
        return self
    
    def clear_all(self):
        """Clear all flags"""
        self.flags = 0
        return self
    
    def __str__(self):
        return f"BitFlags({bin(self.flags)})"

# Define flags
READ = 0b001
WRITE = 0b010
EXECUTE = 0b100
ALL = READ | WRITE | EXECUTE

print("=== Bit Flags Demo ===")

# Create flag manager
perms = BitFlags()
print(f"Initial: {perms}")

# Set flags
perms.set_flag(READ)
print(f"After set READ: {perms}")
print(f"Has READ? {perms.has_flag(READ)}")

perms.set_flag(WRITE)
print(f"After set WRITE: {perms}")

# Toggle flag
perms.toggle_flag(EXECUTE)
print(f"After toggle EXECUTE: {perms}")

# Clear flag
perms.clear_flag(READ)
print(f"After clear READ: {perms}")

# Set multiple
perms.set_multiple(READ, WRITE, EXECUTE)
print(f"After set all: {perms}")

# Practical example: File permissions
print("\n--- File Permissions ---")
file_perms = BitFlags()

# Set owner permissions
OWNER_READ = 0b100000000
OWNER_WRITE = 0b010000000
OWNER_EXEC = 0b001000000

GROUP_READ = 0b000100000
GROUP_WRITE = 0b000010000
GROUP_EXEC = 0b000001000

OTHER_READ = 0b000000100
OTHER_WRITE = 0b000000010
OTHER_EXEC = 0b000000001

# Set rwxr-xr-x permissions
file_perms.set_flag(OWNER_READ | OWNER_WRITE | OWNER_EXEC)
file_perms.set_flag(GROUP_READ | GROUP_EXEC)
file_perms.set_flag(OTHER_READ | OTHER_EXEC)

print(f"Permissions: {file_perms}")
print(f"Owner can read: {file_perms.has_flag(OWNER_READ)}")
print(f"Group can write: {file_perms.has_flag(GROUP_WRITE)}")
```

### Example 6: Data Processing Pipeline
```python
class DataPipeline:
    """Data processing using assignment operators"""
    
    def __init__(self, data=None):
        self.data = data if data is not None else []
        self.processed_count = 0
        self.total = 0
    
    def load(self, data):
        """Load data into pipeline"""
        self.data = data
        self.processed_count = 0
        self.total = len(data)
        print(f"Loaded {self.total} items")
        return self
    
    def filter_positive(self):
        """Filter positive numbers"""
        self.data = [x for x in self.data if x > 0]
        self.processed_count += 1
        print(f"After positive filter: {len(self.data)} items")
        return self
    
    def multiply(self, factor):
        """Multiply all values"""
        self.data = [x * factor for x in self.data]
        self.processed_count += 1
        print(f"After multiply by {factor}: {len(self.data)} items")
        return self
    
    def add(self, value):
        """Add value to all items"""
        self.data = [x + value for x in self.data]
        self.processed_count += 1
        return self
    
    def square(self):
        """Square all values"""
        self.data = [x ** 2 for x in self.data]
        self.processed_count += 1
        return self
    
    def normalize(self):
        """Normalize to 0-1 range"""
        if self.data:
            min_val = min(self.data)
            max_val = max(self.data)
            if max_val != min_val:
                self.data = [(x - min_val) / (max_val - min_val) for x in self.data]
            else:
                self.data = [0.5] * len(self.data)
            self.processed_count += 1
        return self
    
    def sum(self):
        """Calculate sum"""
        return sum(self.data)
    
    def average(self):
        """Calculate average"""
        if not self.data:
            return 0
        return sum(self.data) / len(self.data)
    
    def get_stats(self):
        """Get processing statistics"""
        return {
            'original_count': self.total,
            'processed_count': self.processed_count,
            'current_count': len(self.data),
            'sum': self.sum(),
            'average': self.average()
        }
    
    def __str__(self):
        return f"Pipeline({len(self.data)} items, {self.processed_count} operations)"

# Demo
print("=== Data Processing Pipeline Demo ===")

# Create and process data
pipeline = DataPipeline()
pipeline.load([-5, -2, 0, 2, 5, 8, 10, -3, 7, 12])
print(pipeline)

# Chain operations
result = (pipeline
          .filter_positive()
          .multiply(2)
          .add(1)
          .square()
          .normalize())

print(f"\nAfter processing: {pipeline}")
print(f"Final data: {result.data[:5]}...")  # Show first 5
print(f"Statistics: {pipeline.get_stats()}")

# Different pipeline
print("\n--- Another Pipeline ---")
pipeline2 = (DataPipeline()
             .load([1, 2, 3, 4, 5])
             .multiply(10)
             .add(5)
             .square())

print(f"Processed: {pipeline2}")
print(f"Results: {pipeline2.data}")
print(f"Sum: {pipeline2.sum()}")
print(f"Average: {pipeline2.average():.2f}")
```

## Assignment vs Equality

```python
# = is assignment (not equality)
x = 10  # Assignment

# == is equality comparison
if x == 10:  # Comparison
    print("x is 10")

# Common mistake: using = instead of ==
# if x = 10:  # SyntaxError! (Python 3.8+ allows := for assignment expression)

# Correct way
if x == 10:
    print("Equal")

# Assignment expression (walrus) for inline assignment
if (y := 20) > 10:
    print(f"y is {y}, which is > 10")
```

## Common Mistakes

### Mistake 1: Confusing = with ==
```python
# Wrong - assignment instead of comparison
x = 5
if x = 10:  # SyntaxError (or assignment in condition)
    print("x is 10")

# Right
if x == 10:
    print("x is 10")
```

### Mistake 2: Chaining Assignments Incorrectly
```python
# Works but be careful with mutable objects
a = b = c = []  # All reference the SAME list
a.append(1)
print(b)  # [1] (b affected!)
print(c)  # [1] (c affected!)

# Better for independent copies
a = []
b = []
c = []
```

### Mistake 3: Using += with Immutable Types
```python
# Strings are immutable - creates new object
text = "Hello"
print(id(text))
text += " World"
print(id(text))  # Different id (new object)

# Lists are mutable - modifies in place
items = [1, 2, 3]
print(id(items))
items += [4, 5]
print(id(items))  # Same id (modified in place)
```

### Mistake 4: Division Assignment Type Change
```python
# Wrong - expecting int to stay int
x = 10
x /= 2
print(type(x))  # <class 'float'> (not int!)

# Right - use //= for integer division
x = 10
x //= 2
print(type(x))  # <class 'int'>
```

### Mistake 5: Bitwise vs Logical Operators
```python
# Wrong - using bitwise for logical operations
x = 5
x &= 2  # Bitwise AND, not logical AND

# Logical AND doesn't have assignment form
# x and= 2  # SyntaxError!

# Right - use regular assignment for logical operations
x = x and 2
```

## Performance Considerations

```python
import time

# Compound assignment vs regular assignment
iterations = 10_000_000

# Using compound assignment
start = time.time()
x = 0
for i in range(iterations):
    x += 1
compound_time = time.time() - start

# Using regular assignment
start = time.time()
x = 0
for i in range(iterations):
    x = x + 1
regular_time = time.time() - start

print(f"Compound assignment: {compound_time:.3f}s")
print(f"Regular assignment: {regular_time:.3f}s")
print(f"Difference: {abs(compound_time - regular_time):.3f}s")

# Compound assignment is slightly faster (bytecode optimization)
# But difference is negligible for most applications
```

## Quick Reference Table

| Operator | Name | Example | Equivalent |
|----------|------|---------|------------|
| `=` | Assignment | `x = 5` | `x = 5` |
| `+=` | Add and assign | `x += 3` | `x = x + 3` |
| `-=` | Subtract and assign | `x -= 3` | `x = x - 3` |
| `*=` | Multiply and assign | `x *= 3` | `x = x * 3` |
| `/=` | Divide and assign | `x /= 3` | `x = x / 3` |
| `//=` | Floor divide and assign | `x //= 3` | `x = x // 3` |
| `%=` | Modulo and assign | `x %= 3` | `x = x % 3` |
| `**=` | Power and assign | `x **= 3` | `x = x ** 3` |
| `&=` | Bitwise AND and assign | `x &= 3` | `x = x & 3` |
| `|=` | Bitwise OR and assign | `x |= 3` | `x = x | 3` |
| `^=` | Bitwise XOR and assign | `x ^= 3` | `x = x ^ 3` |
| `<<=` | Left shift and assign | `x <<= 3` | `x = x << 3` |
| `>>=` | Right shift and assign | `x >>= 3` | `x = x >> 3` |
| `:=` | Walrus (assignment expression) | `if (x := 5):` | Assign and use |

## Summary

- **=** is the basic assignment operator
- **Compound operators** combine operation with assignment
- **Arithmetic assignments** (`+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`)
- **Bitwise assignments** (`&=`, `|=`, `^=`, `<<=`, `>>=`)
- **Multiple assignment** for swapping and unpacking
- **Walrus operator (`:=`)** for assignment in expressions (Python 3.8+)
- **Mutable vs immutable** affects how assignment works
- **Chained assignment** works but careful with mutable objects
- **No increment/decrement** operators (`++`, `--`) in Python

## Basic Template
```python
#!/usr/bin/env python3

def basic_assignment():
    """Demonstrate basic assignment"""
    
    # Simple assignment
    x = 10
    name = "Python"
    
    # Multiple assignment
    a = b = c = 0
    print(f"a={a}, b={b}, c={c}")
    
    # Tuple unpacking
    x, y, z = 10, 20, 30
    print(f"x={x}, y={y}, z={z}")
    
    # Swapping
    a, b = 5, 10
    a, b = b, a
    print(f"After swap: a={a}, b={b}")

def compound_operators():
    """Demonstrate compound assignment operators"""
    
    x = 10
    print(f"x = {x}")
    
    x += 5
    print(f"x += 5 → {x}")
    
    x -= 3
    print(f"x -= 3 → {x}")
    
    x *= 2
    print(f"x *= 2 → {x}")
    
    x /= 4
    print(f"x /= 4 → {x}")
    
    x //= 2
    print(f"x //= 2 → {x}")
    
    x %= 3
    print(f"x %= 3 → {x}")
    
    x **= 2
    print(f"x **= 2 → {x}")

def bitwise_operators():
    """Demonstrate bitwise assignment operators"""
    
    x = 0b1010
    print(f"x = {bin(x)}")
    
    x &= 0b1100
    print(f"x &= 0b1100 → {bin(x)}")
    
    x |= 0b0001
    print(f"x |= 0b0001 → {bin(x)}")
    
    x ^= 0b1111
    print(f"x ^= 0b1111 → {bin(x)}")
    
    x <<= 1
    print(f"x <<= 1 → {bin(x)}")
    
    x >>= 2
    print(f"x >>= 2 → {bin(x)}")

def practical_usage():
    """Practical examples of assignment operators"""
    
    # Counter
    count = 0
    count += 1
    count += 1
    print(f"Count: {count}")
    
    # Running total
    total = 0
    for i in range(5):
        total += i
    print(f"Total: {total}")
    
    # String building
    message = "Hello"
    message += " "
    message += "World"
    print(f"Message: {message}")
    
    # List building
    numbers = []
    for i in range(5):
        numbers += [i]
    print(f"Numbers: {numbers}")
    
    # Bit flags
    permissions = 0b000
    READ = 0b001
    WRITE = 0b010
    
    permissions |= READ
    permissions |= WRITE
    print(f"Permissions: {bin(permissions)}")
    print(f"Can read: {bool(permissions & READ)}")

if __name__ == "__main__":
    print("=== BASIC ASSIGNMENT ===")
    basic_assignment()
    
    print("\n=== COMPOUND OPERATORS ===")
    compound_operators()
    
    print("\n=== BITWISE OPERATORS ===")
    bitwise_operators()
    
    print("\n=== PRACTICAL USAGE ===")
    practical_usage()
```

*This documentation belongs to https://github.com/InterCentury*