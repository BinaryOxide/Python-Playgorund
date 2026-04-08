# 12 - Integer Types (int) in Python

## What are Integers?
Integers are whole numbers (positive, negative, or zero) without decimal points. In Python, the `int` type represents integers and has **arbitrary precision** - meaning it can store numbers of any size (limited only by available memory).

## Basic Integer Declaration

```python
# Positive integers
a = 10
b = 42
c = 1000

# Negative integers
d = -5
e = -100
f = -999

# Zero
g = 0

# Print and check types
print(a, type(a))  # 10 <class 'int'>
print(d, type(d))  # -5 <class 'int'>
```

## Integer Literals (Different Bases)

### Decimal (Base 10) - Default
```python
# Regular decimal numbers
decimal = 42
print(decimal)      # 42
print(type(decimal))  # <class 'int'>
```

### Binary (Base 2) - Prefix 0b or 0B
```python
# Binary literals
binary1 = 0b1010    # Binary 1010 = decimal 10
binary2 = 0B1111    # Binary 1111 = decimal 15
binary3 = 0b10000000  # Binary = decimal 128

print(binary1)      # 10
print(binary2)      # 15
print(binary3)      # 128

# Converting binary string to int
binary_str = "1010"
value = int(binary_str, 2)
print(value)        # 10
```

### Octal (Base 8) - Prefix 0o or 0O
```python
# Octal literals
octal1 = 0o10      # Octal 10 = decimal 8
octal2 = 0O77      # Octal 77 = decimal 63
octal3 = 0o100     # Octal 100 = decimal 64

print(octal1)      # 8
print(octal2)      # 63
print(octal3)      # 64

# Converting octal string to int
octal_str = "77"
value = int(octal_str, 8)
print(value)       # 63
```

### Hexadecimal (Base 16) - Prefix 0x or 0X
```python
# Hexadecimal literals
hex1 = 0x0A       # Hex 0A = decimal 10
hex2 = 0XFF       # Hex FF = decimal 255
hex3 = 0x10       # Hex 10 = decimal 16
hex4 = 0xFFFF     # Hex FFFF = decimal 65535

print(hex1)       # 10
print(hex2)       # 255
print(hex3)       # 16
print(hex4)       # 65535

# Converting hex string to int
hex_str = "FF"
value = int(hex_str, 16)
print(value)      # 255
```

### Underscores for Readability (Python 3.6+)
```python
# Use underscores to make large numbers readable
million = 1_000_000
billion = 1_000_000_000
credit_card = 1234_5678_9012_3456
hex_value = 0xFF_FF_FF_FF
binary_value = 0b1111_0000_1111_0000

print(million)     # 1000000
print(credit_card) # 1234567890123456

# Underscores don't affect value
print(1_000 == 1000)  # True
```

## Arbitrary Precision (Big Integers)

```python
# Python can handle extremely large integers
small = 10
large = 10 ** 100  # 1 followed by 100 zeros
huge = 10 ** 1000  # 1 followed by 1000 zeros

print(f"10^10: {10**10}")
print(f"10^50: {10**50}")
print(f"10^100: {10**100}")

# Factorial of 100 (huge number)
import math
factorial_100 = math.factorial(100)
print(f"100! has {len(str(factorial_100))} digits")
print(f"First 20 digits: {str(factorial_100)[:20]}...")

# No overflow errors!
# In C++, int would overflow at ~2 billion
# In Python, you can go as big as memory allows
```

## Integer Operations

### Arithmetic Operations
```python
a = 10
b = 3

# Addition
print(a + b)      # 13

# Subtraction
print(a - b)      # 7

# Multiplication
print(a * b)      # 30

# Division (always returns float)
print(a / b)      # 3.3333333333333335

# Integer division (floor division)
print(a // b)     # 3

# Modulo (remainder)
print(a % b)      # 1

# Exponentiation
print(a ** b)     # 1000 (10^3)

# Negation
print(-a)         # -10

# Absolute value
print(abs(-10))   # 10
```

### Compound Assignment Operators
```python
x = 10

x += 5    # x = x + 5
print(x)  # 15

x -= 3    # x = x - 3
print(x)  # 12

x *= 2    # x = x * 2
print(x)  # 24

x //= 4   # x = x // 4
print(x)  # 6

x %= 4    # x = x % 4
print(x)  # 2

x **= 3   # x = x ** 3
print(x)  # 8
```

### Comparison Operations
```python
a = 10
b = 20

print(a == b)   # False (equal)
print(a != b)   # True (not equal)
print(a < b)    # True (less than)
print(a > b)    # False (greater than)
print(a <= b)   # True (less than or equal)
print(a >= b)   # False (greater than or equal)

# Chained comparisons
x = 5
print(1 < x < 10)     # True (1 < 5 and 5 < 10)
print(0 < x < 5)      # False
print(x == 5 < 10)    # True (5 == 5 and 5 < 10)
```

## Bitwise Operations

```python
a = 0b1010  # 10 in decimal
b = 0b1100  # 12 in decimal

# Bitwise AND (&) - both bits must be 1
print(bin(a & b))   # 0b1000 (8)

# Bitwise OR (|) - at least one bit is 1
print(bin(a | b))   # 0b1110 (14)

# Bitwise XOR (^) - bits are different
print(bin(a ^ b))   # 0b0110 (6)

# Bitwise NOT (~) - invert all bits
print(bin(~a))      # -0b1011 (-11)

# Left shift (<<) - shift bits left (multiply by 2^n)
print(a << 1)       # 20 (10 * 2)
print(bin(a << 2))  # 0b101000 (40)

# Right shift (>>) - shift bits right (divide by 2^n)
print(a >> 1)       # 5 (10 // 2)
print(bin(b >> 2))  # 0b11 (3)
```

## Type Conversion

### Converting to int
```python
# From float (truncates decimal)
print(int(3.14))     # 3
print(int(3.99))     # 3 (not rounding)
print(int(-3.14))    # -3

# From string
print(int("123"))     # 123
print(int("-456"))    # -456
print(int("  789  ")) # 789 (strips whitespace)

# From different bases
print(int("1010", 2))    # 10 (binary)
print(int("77", 8))      # 63 (octal)
print(int("FF", 16))     # 255 (hexadecimal)

# From boolean
print(int(True))     # 1
print(int(False))    # 0

# From other types
print(int(3+4j))     # TypeError: can't convert complex to int
```

### Converting from int to other types
```python
x = 42

# To float
print(float(x))      # 42.0

# To string
print(str(x))        # "42"
print(repr(x))       # "42"

# To boolean
print(bool(x))       # True (non-zero)
print(bool(0))       # False

# To hex
print(hex(x))        # "0x2a"
print(hex(255))      # "0xff"

# To binary
print(bin(x))        # "0b101010"
print(bin(255))      # "0b11111111"

# To octal
print(oct(x))        # "0o52"
print(oct(64))       # "0o100"

# To character (ASCII)
print(chr(65))       # "A"
print(chr(97))       # "a"
```

## Practical Examples

### Example 1: Basic Calculator
```python
def simple_calculator():
    """Perform basic integer operations"""
    
    print("Integer Calculator")
    print("=" * 30)
    
    # Get input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    # Perform operations
    print(f"\n{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
    print(f"{num1} / {num2} = {num1 / num2}")
    print(f"{num1} // {num2} = {num1 // num2} (floor division)")
    print(f"{num1} % {num2} = {num1 % num2} (remainder)")
    print(f"{num1} ** {num2} = {num1 ** num2} (power)")
    
    # Comparison
    print(f"\n{num1} == {num2}: {num1 == num2}")
    print(f"{num1} < {num2}: {num1 < num2}")
    print(f"{num1} > {num2}: {num1 > num2}")

# simple_calculator()
```

### Example 2: Number System Converter
```python
def number_system_converter():
    """Convert numbers between different bases"""
    
    print("Number System Converter")
    print("=" * 40)
    
    # Get decimal number
    decimal = int(input("Enter a decimal number: "))
    
    print(f"\nDecimal: {decimal}")
    print(f"Binary: {bin(decimal)}")
    print(f"Octal: {oct(decimal)}")
    print(f"Hexadecimal: {hex(decimal)}")
    
    # Convert from other bases
    print("\n" + "=" * 40)
    print("Convert TO decimal:")
    
    binary_str = input("Enter binary number (e.g., 1010): ")
    print(f"Binary {binary_str} = {int(binary_str, 2)} decimal")
    
    octal_str = input("Enter octal number (e.g., 77): ")
    print(f"Octal {octal_str} = {int(octal_str, 8)} decimal")
    
    hex_str = input("Enter hex number (e.g., FF): ")
    print(f"Hex {hex_str} = {int(hex_str, 16)} decimal")

# number_system_converter()
```

### Example 3: Bit Manipulation
```python
def bit_operations_demo():
    """Demonstrate bitwise operations"""
    
    print("Bitwise Operations Demo")
    print("=" * 40)
    
    # Get numbers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    # Show binary representations
    print(f"\n{num1} in binary: {bin(num1)}")
    print(f"{num2} in binary: {bin(num2)}")
    
    # Bitwise operations
    print(f"\nAND (&): {num1} & {num2} = {num1 & num2}")
    print(f"Binary: {bin(num1)} & {bin(num2)} = {bin(num1 & num2)}")
    
    print(f"\nOR (|): {num1} | {num2} = {num1 | num2}")
    print(f"Binary: {bin(num1)} | {bin(num2)} = {bin(num1 | num2)}")
    
    print(f"\nXOR (^): {num1} ^ {num2} = {num1 ^ num2}")
    print(f"Binary: {bin(num1)} ^ {bin(num2)} = {bin(num1 ^ num2)}")
    
    print(f"\nNOT (~): ~{num1} = {~num1}")
    print(f"Binary: ~{bin(num1)} = {bin(~num1)}")
    
    # Shifts
    shift = int(input("\nEnter shift amount: "))
    print(f"\nLeft shift: {num1} << {shift} = {num1 << shift}")
    print(f"Binary: {bin(num1)} << {shift} = {bin(num1 << shift)}")
    
    print(f"\nRight shift: {num1} >> {shift} = {num1 >> shift}")
    print(f"Binary: {bin(num1)} >> {shift} = {bin(num1 >> shift)}")

# bit_operations_demo()
```

### Example 4: Prime Number Checker
```python
def is_prime(n: int) -> bool:
    """Check if a number is prime"""
    
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

def prime_factors(n: int) -> list:
    """Find prime factors of a number"""
    
    factors = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    
    return factors

# Test prime functions
numbers = [1, 2, 3, 4, 5, 16, 17, 18, 19, 97, 100]

print("Prime Number Checker")
print("=" * 30)
for num in numbers:
    if is_prime(num):
        print(f"{num:3} is PRIME")
    else:
        print(f"{num:3} is NOT prime")
        print(f"   Factors: {prime_factors(num)}")

print("\n" + "=" * 30)
large_num = 2**31 - 1  # Mersenne prime?
print(f"Checking large number: {large_num}")
print(f"Is prime? {is_prime(large_num)}")
```

### Example 5: Factorial and Combinatorics
```python
import math
from functools import lru_cache

# Recursive factorial with caching
@lru_cache(maxsize=None)
def factorial(n: int) -> int:
    """Calculate factorial recursively"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Iterative factorial
def factorial_iterative(n: int) -> int:
    """Calculate factorial iteratively"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Combinations C(n, k)
def combinations(n: int, k: int) -> int:
    """Calculate n choose k"""
    return math.comb(n, k)

# Permutations P(n, k)
def permutations(n: int, k: int) -> int:
    """Calculate n permute k"""
    return math.perm(n, k)

print("Factorial and Combinatorics")
print("=" * 40)

# Test factorial
for n in range(0, 11):
    print(f"{n}! = {factorial(n):,}")

print("\n" + "=" * 40)

# Large factorial
n = 20
print(f"{n}! = {factorial(n):,}")
print(f"Number of digits: {len(str(factorial(n)))}")

print("\n" + "=" * 40)
print("Combinations (n choose k):")

# Test combinations
test_cases = [(5, 2), (10, 3), (52, 5), (100, 2)]
for n, k in test_cases:
    result = combinations(n, k)
    print(f"C({n}, {k}) = {result:,}")

print("\n" + "=" * 40)
print("Permutations (n permute k):")

for n, k in test_cases:
    result = permutations(n, k)
    print(f"P({n}, {k}) = {result:,}")
```

### Example 6: Integer Properties and Sequences
```python
def number_properties(n: int):
    """Display various properties of an integer"""
    
    print(f"Number: {n}")
    print(f"Type: {type(n).__name__}")
    print(f"Binary: {bin(n)}")
    print(f"Octal: {oct(n)}")
    print(f"Hex: {hex(n)}")
    print(f"Absolute value: {abs(n)}")
    
    # Sign
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")
    
    # Even/Odd
    print(f"Even: {n % 2 == 0}")
    print(f"Odd: {n % 2 == 1}")
    
    # Divisibility
    print(f"Divisible by 2: {n % 2 == 0}")
    print(f"Divisible by 3: {n % 3 == 0}")
    print(f"Divisible by 5: {n % 5 == 0}")
    print(f"Divisible by 10: {n % 10 == 0}")
    
    # Number of digits
    if n != 0:
        digits = len(str(abs(n)))
        print(f"Number of digits: {digits}")
    
    # Digit sum
    digit_sum = sum(int(d) for d in str(abs(n)))
    print(f"Sum of digits: {digit_sum}")
    
    # Palindrome?
    str_n = str(abs(n))
    print(f"Palindrome: {str_n == str_n[::-1]}")
    
    # Perfect square?
    root = int(math.sqrt(abs(n)))
    print(f"Perfect square: {root * root == abs(n)}")
    
    return

def generate_sequence(start: int, end: int, sequence_type: str):
    """Generate different integer sequences"""
    
    if sequence_type == "even":
        return [x for x in range(start, end + 1) if x % 2 == 0]
    elif sequence_type == "odd":
        return [x for x in range(start, end + 1) if x % 2 == 1]
    elif sequence_type == "prime":
        return [x for x in range(start, end + 1) if is_prime(x)]
    elif sequence_type == "square":
        return [x * x for x in range(start, int(math.sqrt(end)) + 1)]
    elif sequence_type == "fibonacci":
        fib = [0, 1]
        while fib[-1] <= end:
            fib.append(fib[-1] + fib[-2])
        return [x for x in fib if start <= x <= end]
    else:
        return []

# Test number properties
print("Number Properties")
print("=" * 50)
test_numbers = [42, -17, 0, 12321, 144, 2**16]
for num in test_numbers:
    number_properties(num)
    print("-" * 50)

print("\nInteger Sequences")
print("=" * 50)
print(f"Even numbers 1-20: {generate_sequence(1, 20, 'even')}")
print(f"Odd numbers 1-20: {generate_sequence(1, 20, 'odd')}")
print(f"Prime numbers 1-50: {generate_sequence(1, 50, 'prime')}")
print(f"Square numbers 1-100: {generate_sequence(1, 100, 'square')}")
print(f"Fibonacci up to 100: {generate_sequence(0, 100, 'fibonacci')}")
```

### Example 7: Integer Range and Limits Demo
```python
import sys

def integer_limits_demo():
    """Demonstrate Python integer capabilities"""
    
    print("Python Integer Limits Demo")
    print("=" * 50)
    
    # Size of int in memory
    small_int = 0
    large_int = 10**100
    
    print(f"Size of 0: {sys.getsizeof(small_int)} bytes")
    print(f"Size of 10^100: {sys.getsizeof(large_int)} bytes")
    
    # Maximum and minimum? (Python has no fixed limit)
    print("\nPython integers have NO fixed maximum!")
    print("They can grow as large as available memory")
    
    # Memory usage grows with number size
    print("\nMemory usage for different sized integers:")
    for power in range(0, 101, 10):
        num = 10 ** power
        size = sys.getsizeof(num)
        print(f"10^{power:3} uses {size:3} bytes")
    
    # Practical limits (memory dependent)
    print("\n" + "=" * 50)
    print("Practical demonstration:")
    
    try:
        # Calculate 2^1000000 (very large number)
        huge = 2 ** 1000000
        print(f"2^1,000,000 has {len(str(huge))} digits")
        print(f"Memory used: {sys.getsizeof(huge):,} bytes")
        
        # Even larger
        bigger = 2 ** 10_000_000
        print(f"\n2^10,000,000 has {len(str(bigger))} digits")
        print(f"Memory used: {sys.getsizeof(bigger):,} bytes")
        
    except MemoryError:
        print("Number too large for available memory!")

# integer_limits_demo()
```

## Integer Methods and Functions

### Useful Built-in Functions
```python
# abs() - absolute value
print(abs(-42))       # 42

# pow() - power with modulo
print(pow(2, 10))     # 1024 (2^10)
print(pow(2, 10, 100)) # 24 (2^10 % 100)

# divmod() - quotient and remainder
quotient, remainder = divmod(10, 3)
print(f"10 // 3 = {quotient}, 10 % 3 = {remainder}")  # 3, 1

# round() - rounding (returns int for .0)
print(round(3.14))    # 3
print(round(3.99))    # 4

# sum() - sum of iterable
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))    # 15

# min() and max()
print(min(10, 20, 5))  # 5
print(max(10, 20, 5))  # 20
```

### int Methods
```python
# bit_length() - number of bits needed
x = 42
print(f"{x} needs {x.bit_length()} bits")  # 6 bits (101010)

# to_bytes() - convert to bytes
x = 1024
bytes_representation = x.to_bytes(2, 'big')
print(bytes_representation)  # b'\x04\x00'

# from_bytes() - create int from bytes
recovered = int.from_bytes(bytes_representation, 'big')
print(recovered)  # 1024

# as_integer_ratio() - ratio of two integers (for floats)
print(3.14.as_integer_ratio())  # (7070651414971679, 2251799813685248)
```

## Common Integer Patterns

### Number Range Checking
```python
def in_range(n: int, min_val: int, max_val: int) -> bool:
    """Check if n is between min_val and max_val (inclusive)"""
    return min_val <= n <= max_val

# Usage
age = 25
if in_range(age, 0, 120):
    print("Valid age")

# Clamping values
def clamp(n: int, min_val: int, max_val: int) -> int:
    """Restrict n to range [min_val, max_val]"""
    return max(min_val, min(n, max_val))

print(clamp(150, 0, 100))  # 100
print(clamp(-10, 0, 100))  # 0
print(clamp(50, 0, 100))   # 50
```

### Digit Manipulation
```python
def get_digits(n: int) -> list:
    """Get list of digits"""
    return [int(d) for d in str(abs(n))]

def reverse_number(n: int) -> int:
    """Reverse digits of a number"""
    sign = -1 if n < 0 else 1
    reversed_str = str(abs(n))[::-1]
    return sign * int(reversed_str)

def is_palindrome(n: int) -> bool:
    """Check if number reads same backwards"""
    str_n = str(abs(n))
    return str_n == str_n[::-1]

# Test digit functions
num = 12345
print(f"Digits of {num}: {get_digits(num)}")
print(f"Reversed: {reverse_number(num)}")
print(f"Is palindrome? {is_palindrome(num)}")
print(f"Is 12321 palindrome? {is_palindrome(12321)}")
```

## Common Mistakes

### Mistake 1: Division Always Returns Float
```python
# Wrong - expecting integer
result = 10 / 2
print(type(result))  # <class 'float'>, not int!

# Right - use integer division
result = 10 // 2
print(type(result))  # <class 'int'>
```

### Mistake 2: Integer Division with Negative Numbers
```python
# Floor division rounds DOWN (toward negative infinity)
print(10 // 3)   # 3
print(-10 // 3)  # -4 (not -3!)
print(10 // -3)  # -4

# Modulo with negatives
print(10 % 3)    # 1
print(-10 % 3)   # 2 (not -1!)
```

### Mistake 3: Comparing int with string
```python
# Wrong - always False or TypeError
age = 25
if age == "25":  # False (int vs str)
    print("Match")

# Right - convert or compare correctly
if age == int("25"):
    print("Match")
```

### Mistake 4: Forgetting int() Doesn't Round
```python
# int() truncates toward zero, doesn't round
print(int(3.9))   # 3 (not 4)
print(int(-3.9))  # -3 (not -4)

# Use round() for rounding
print(round(3.9))   # 4
print(round(-3.9))  # -4
```

### Mistake 5: Octal Literal Confusion
```python
# In Python 2, 010 was octal for 8
# In Python 3, 010 is syntax error
# Wrong
# num = 010  # SyntaxError!

# Right - use 0o prefix
num = 0o10  # 8
```

## Performance Considerations

```python
import time

# Small ints are cached (-5 to 256)
a = 100
b = 100
print(a is b)  # True (cached)

c = 1000
d = 1000
print(c is d)  # May be False (not cached)

# Performance of different operations
def performance_test():
    iterations = 10_000_000
    
    # Addition
    start = time.time()
    x = 0
    for i in range(iterations):
        x += 1
    print(f"Addition: {time.time() - start:.3f}s")
    
    # Multiplication
    start = time.time()
    x = 1
    for i in range(iterations):
        x *= 2
    print(f"Multiplication: {time.time() - start:.3f}s")
    
    # Division
    start = time.time()
    x = 1000
    for i in range(iterations):
        x //= 2
    print(f"Division: {time.time() - start:.3f}s")
    
    # Bit operations (fastest)
    start = time.time()
    x = 1
    for i in range(iterations):
        x <<= 1
    print(f"Bit shift: {time.time() - start:.3f}s")

# performance_test()
```

## Quick Reference Table

| Operation | Syntax | Example | Result |
|-----------|--------|---------|--------|
| Addition | `a + b` | `10 + 3` | `13` |
| Subtraction | `a - b` | `10 - 3` | `7` |
| Multiplication | `a * b` | `10 * 3` | `30` |
| Division (float) | `a / b` | `10 / 3` | `3.333` |
| Floor division | `a // b` | `10 // 3` | `3` |
| Modulo | `a % b` | `10 % 3` | `1` |
| Power | `a ** b` | `10 ** 3` | `1000` |
| Binary | `0b...` | `0b1010` | `10` |
| Octal | `0o...` | `0o12` | `10` |
| Hex | `0x...` | `0xA` | `10` |
| Bitwise AND | `a & b` | `5 & 3` | `1` |
| Bitwise OR | `a \| b` | `5 \| 3` | `7` |
| Bitwise XOR | `a ^ b` | `5 ^ 3` | `6` |
| Left shift | `a << b` | `5 << 1` | `10` |
| Right shift | `a >> b` | `5 >> 1` | `2` |

## Summary

- **int** represents whole numbers (no decimal point)
- **Arbitrary precision** - no size limits (unlimited memory)
- **Multiple bases**: binary (0b), octal (0o), hex (0x)
- **Underscores** for readability: `1_000_000`
- **Integer division** (`//`) returns floor (rounded down)
- **Modulo** (`%`) returns remainder
- **Bitwise operations** available for low-level manipulation
- **Automatic type conversion** in mixed operations
- **Small integers (-5 to 256)** are cached for performance
- **No overflow errors** - Python handles big numbers gracefully

## Basic Template
```python
#!/usr/bin/env python3

# Basic integer operations
def integer_basics():
    """Demonstrate basic integer operations"""
    
    # Declaration
    a = 10
    b = 3
    
    # Arithmetic
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    print(f"{a} // {b} = {a // b} (floor division)")
    print(f"{a} % {b} = {a % b} (remainder)")
    print(f"{a} ** {b} = {a ** b} (power)")
    
    # Different bases
    print(f"\nBinary 0b1010 = {0b1010}")
    print(f"Octal 0o12 = {0o12}")
    print(f"Hex 0xA = {0xA}")
    
    # Large numbers with underscores
    million = 1_000_000
    billion = 1_000_000_000
    print(f"Million: {million:,}")
    print(f"Billion: {billion:,}")

# Type conversion
def type_conversion():
    """Demonstrate integer type conversion"""
    
    # To int
    print(f"int(3.14) = {int(3.14)}")
    print(f"int('123') = {int('123')}")
    print(f"int('1010', 2) = {int('1010', 2)}")
    print(f"int(True) = {int(True)}")
    
    # From int
    x = 42
    print(f"float({x}) = {float(x)}")
    print(f"str({x}) = '{str(x)}'")
    print(f"bin({x}) = {bin(x)}")
    print(f"oct({x}) = {oct(x)}")
    print(f"hex({x}) = {hex(x)}")
    print(f"chr({x}) = '{chr(x)}'")

# Integer properties
def integer_properties():
    """Check integer properties"""
    
    num = 42
    
    print(f"Number: {num}")
    print(f"Type: {type(num).__name__}")
    print(f"Binary: {bin(num)}")
    print(f"Bit length: {num.bit_length()}")
    print(f"Absolute: {abs(num)}")
    print(f"Even: {num % 2 == 0}")
    print(f"Odd: {num % 2 == 1}")
    print(f"Positive: {num > 0}")
    print(f"Negative: {num < 0}")
    print(f"Zero: {num == 0}")

# Run examples
if __name__ == "__main__":
    print("=== INTEGER BASICS ===")
    integer_basics()
    
    print("\n=== TYPE CONVERSION ===")
    type_conversion()
    
    print("\n=== INTEGER PROPERTIES ===")
    integer_properties()
```

*This documentation belongs to https://github.com/InterCentury*