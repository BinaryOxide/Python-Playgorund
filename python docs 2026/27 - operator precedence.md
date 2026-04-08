# 27 - Operator Precedence in Python

## What is Operator Precedence?
Operator precedence determines the order in which operators are evaluated in an expression. Operators with higher precedence are evaluated before operators with lower precedence. When operators have the same precedence, associativity determines the evaluation order (left-to-right or right-to-left).

## Complete Precedence Table (Highest to Lowest)

| Precedence | Operators | Description | Associativity |
|------------|-----------|-------------|---------------|
| 1 | `()` `[]` `{}` | Parentheses, indexing, dict/set display | Left-to-right |
| 2 | `x[index]`, `x[index:index]`, `x(arguments...)`, `x.attribute` | Subscription, slicing, call, attribute | Left-to-right |
| 3 | `await x` | Await expression | N/A |
| 4 | `**` | Exponentiation | Right-to-left |
| 5 | `+x`, `-x`, `~x` | Positive, negative, bitwise NOT | Right-to-left |
| 6 | `*`, `/`, `//`, `%` | Multiplication, division, floor division, modulo | Left-to-right |
| 7 | `+`, `-` | Addition, subtraction | Left-to-right |
| 8 | `<<`, `>>` | Bitwise shifts | Left-to-right |
| 9 | `&` | Bitwise AND | Left-to-right |
| 10 | `^` | Bitwise XOR | Left-to-right |
| 11 | `\|` | Bitwise OR | Left-to-right |
| 12 | `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Comparisons, identity, membership | Left-to-right |
| 13 | `not x` | Boolean NOT | Right-to-left |
| 14 | `and` | Boolean AND | Left-to-right |
| 15 | `or` | Boolean OR | Left-to-right |
| 16 | `if`-`else` | Conditional expression | Right-to-left |
| 17 | `lambda` | Lambda expression | N/A |

## Basic Arithmetic Precedence

### PEMDAS Rule
```python
# Parentheses first
print(2 + 3 * 4)      # 14 (multiplication first)
print((2 + 3) * 4)    # 20 (parentheses first)

# Exponents next
print(2 + 3 ** 2)     # 11 (3**2=9, 2+9=11)
print((2 + 3) ** 2)   # 25 (5**2=25)

# Multiplication/Division before Addition/Subtraction
print(10 - 3 * 2)     # 4 (3*2=6, 10-6=4)
print(10 / 2 + 3)     # 8.0 (10/2=5, 5+3=8)
print(10 + 5 - 3)     # 12 (left to right)
```

### Complex Arithmetic Examples
```python
# Multiple operations
result = 2 + 3 * 4 ** 2 - 10 / 2
# Step by step:
# 1. 4 ** 2 = 16
# 2. 3 * 16 = 48
# 3. 10 / 2 = 5
# 4. 2 + 48 = 50
# 5. 50 - 5 = 45
print(result)  # 45.0

# With parentheses
result = ((2 + 3) * (4 ** 2 - 10)) / 2
# 1. 2 + 3 = 5
# 2. 4 ** 2 = 16
# 3. 16 - 10 = 6
# 4. 5 * 6 = 30
# 5. 30 / 2 = 15
print(result)  # 15.0
```

## Exponentiation Precedence (**)

### Right-to-Left Associativity
```python
# Exponentiation is right-associative
print(2 ** 3 ** 2)    # 512 (2 ** (3 ** 2) = 2 ** 9)
print((2 ** 3) ** 2)  # 64 (8 ** 2)

# Without parentheses
result = 2 ** 2 ** 3
# Evaluated as: 2 ** (2 ** 3) = 2 ** 8 = 256
print(result)  # 256

# With explicit grouping
result = (2 ** 2) ** 3  # 4 ** 3 = 64
print(result)  # 64

# Multiple exponents
print(2 ** 1 ** 2 ** 3)  # 2 ** (1 ** (2 ** 3)) = 2 ** 1 = 2
```

### Negative Numbers with Exponentiation
```python
# Unary minus has lower precedence than exponentiation
print(-3 ** 2)      # -9 (-(3**2))
print((-3) ** 2)    # 9

# Confusion example
x = 3
print(-x ** 2)      # -9
print((-x) ** 2)    # 9
```

## Unary Operators (+, -, ~)

### Right-to-Left Associativity
```python
# Unary operators are right-associative
x = 5
print(++x)    # 5 (+(+5))
print(--x)    # 5 (-(-5)) but careful with decrement!

# Bitwise NOT
print(~-x)    # ~(-5) = 4
print(-~x)    # -(-6) = 6

# Chained unary operators
result = +-+-x
# Evaluated as: +(-(+(-5))) = +(-(-5)) = +5 = 5
print(result)  # 5
```

## Multiplication, Division, Modulo

### Left-to-Right Associativity
```python
# Same precedence, left to right
print(100 / 10 * 2)    # 20.0 ((100/10)*2)
print(100 * 10 / 2)    # 500.0 ((100*10)/2)

# Mixed operations
print(10 * 4 // 3)     # 13 ((10*4)//3 = 40//3)
print(10 * (4 // 3))   # 10 (10 * 1)

# Modulo with multiplication
print(10 % 3 * 2)      # 2 ((10%3)*2 = 1*2)
print(10 % (3 * 2))    # 4 (10%6)
```

### Floor Division and Modulo
```python
# Floor division and modulo have same precedence as multiplication
print(20 // 3 * 2)     # 12 ((20//3)*2 = 6*2)
print(20 // (3 * 2))   # 3 (20//6)

# Complex example
result = 20 % 3 + 10 // 2
# 1. 20 % 3 = 2
# 2. 10 // 2 = 5
# 3. 2 + 5 = 7
print(result)  # 7
```

## Addition and Subtraction

### Left-to-Right Associativity
```python
# Simple left to right
print(10 - 5 + 3)     # 8 ((10-5)+3)
print(10 - (5 + 3))   # 2

# Mixed with higher precedence operators
result = 10 + 3 * 5 - 4 / 2
# 1. 3 * 5 = 15
# 2. 4 / 2 = 2
# 3. 10 + 15 = 25
# 4. 25 - 2 = 23
print(result)  # 23.0
```

## Bitwise Shifts (<<, >>)

### Left-to-Right Associativity
```python
# Shifts are left-associative
print(1 << 2 << 1)    # 8 ((1<<2)<<1 = 4<<1)
print(1 << (2 << 1))  # 1<<4 = 16

# With arithmetic
result = 10 + 2 << 1
# 10 + (2 << 1) = 10 + 4 = 14
print(result)  # 14

result = (10 + 2) << 1  # 12 << 1 = 24
print(result)  # 24
```

## Bitwise AND, XOR, OR

### Precedence: & > ^ > |
```python
# AND has higher precedence than XOR and OR
a = 0b1100  # 12
b = 0b1010  # 10
c = 0b0110  # 6

print(a & b | c)      # (a & b) | c = 8 | 6 = 14
print(a & (b | c))    # 12 & (10|6) = 12 & 14 = 12

print(a ^ b & c)      # a ^ (b & c) = 12 ^ 2 = 14
print((a ^ b) & c)    # 6 & 6 = 6

# Complex example
result = 0b1111 & 0b1100 | 0b1010 ^ 0b0011
# Step by step:
# 1. 0b1111 & 0b1100 = 0b1100 (12)
# 2. 0b1010 ^ 0b0011 = 0b1001 (9)
# 3. 0b1100 | 0b1001 = 0b1101 (13)
print(bin(result))  # 0b1101
```

## Comparison Operators

### Chain Comparisons
```python
# Comparisons can be chained (evaluated left to right with AND logic)
x = 5
print(1 < x < 10)      # True (1 < 5 and 5 < 10)
print(1 < x > 10)      # False (1 < 5 and 5 > 10)

# Chained comparisons are more efficient
# a < b < c is equivalent to a < b and b < c (but b evaluated once)

# Mixed comparisons
result = 5 == 5 < 10
# Evaluated as: (5 == 5) and (5 < 10) = True and True = True
print(result)  # True

# With arithmetic
result = 5 + 3 > 7 - 2
# (5+3) > (7-2) = 8 > 5 = True
print(result)  # True
```

### Identity and Membership
```python
# in, not in, is, is not have same precedence as comparisons
numbers = [1, 2, 3, 4, 5]
x = 3

# Chained with other operators
result = x in numbers and x > 0
print(result)  # True

# Without parentheses
result = 5 in numbers == True  # (5 in numbers) and (numbers == True)
print(result)  # False (numbers == True is False)

# With parentheses
result = (5 in numbers) == True
print(result)  # True
```

## Boolean Operators (not, and, or)

### Precedence: not > and > or
```python
# not has highest precedence among booleans
print(not True and False)     # (not True) and False = False and False = False
print(not (True and False))   # not False = True

# and before or
result = True or False and False
# True or (False and False) = True or False = True
print(result)  # True

result = (True or False) and False  # True and False = False
print(result)  # False

# Complex example
x = 5
y = 10
z = 15
result = x > 0 and y > 5 or z < 10
# (x>0 and y>5) or z<10 = (True and True) or False = True
print(result)  # True
```

### Short-Circuit Evaluation
```python
# and short-circuits on first False
def false_func():
    print("False function called")
    return False

def true_func():
    print("True function called")
    return True

result = false_func() and true_func()  # true_func NOT called
print(f"Result: {result}")

# or short-circuits on first True
result = true_func() or false_func()   # false_func NOT called
print(f"Result: {result}")

# This affects precedence in complex expressions
x = 5
y = 0
result = x > 0 or (y / 0 > 0)  # No division by zero (short-circuits)
print(result)  # True
```

## Conditional Expression (if-else)

### Right-to-Left Associativity
```python
# Conditional expression has lowest precedence among operators
x = 5
y = 10
result = x if x > y else y
print(result)  # 10

# With arithmetic
result = 10 + (5 if x > y else 3)
print(result)  # 13 (10 + 3)

# Nested conditional (right-associative)
score = 85
grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'F'
# Evaluated as: 'A' if score>=90 else ('B' if score>=80 else ('C' if score>=70 else 'F'))
print(grade)  # B

# Without parentheses (works due to associativity)
result = 10 + 5 if x > y else 3
# Evaluated as: (10 + 5) if x>y else 3 = 15 if False else 3 = 3
print(result)  # 3
```

## Lambda Expressions

```python
# Lambda has the lowest precedence
x = 5
func = lambda x: x + 1
print(func(10))  # 11

# Lambda with operators
result = (lambda x: x * 2)(5)
print(result)  # 10

# Lambda in expressions (needs parentheses)
# Without parentheses - syntax error
# result = lambda x: x * 2 5

# With parentheses
result = (lambda x: x * 2)(5)
```

## Complex Expression Examples

### Example 1: Mathematical Expression
```python
# Complex formula: (a + b) * c - d / e ** f
a, b, c, d, e, f = 2, 3, 4, 10, 2, 3

# Without parentheses (using precedence)
result = a + b * c - d / e ** f
# Step by step:
# 1. e ** f = 2 ** 3 = 8
# 2. b * c = 3 * 4 = 12
# 3. d / 8 = 10 / 8 = 1.25
# 4. a + 12 = 14
# 5. 14 - 1.25 = 12.75
print(result)  # 12.75

# With parentheses (explicit)
result = (a + b) * c - d / (e ** f)
# 1. a + b = 5
# 2. e ** f = 8
# 3. 5 * c = 20
# 4. d / 8 = 1.25
# 5. 20 - 1.25 = 18.75
print(result)  # 18.75
```

### Example 2: Bitwise and Logical Mix
```python
flags = 0b1100
mask = 0b1010
debug = True

# Complex condition
result = flags & mask or debug and flags
# Precedence: & > and > or
# 1. flags & mask = 0b1000 (8)
# 2. debug and flags = True and 12 = 12
# 3. 8 or 12 = 8
print(result)  # 8

# With parentheses
result = (flags & mask) or (debug and flags)
print(result)  # 8

# Different grouping
result = flags & (mask or debug) and flags
# 1. mask or debug = 10 or True = 10
# 2. flags & 10 = 8
# 3. 8 and flags = 8 and 12 = 12
print(result)  # 12
```

### Example 3: Multiple Operators
```python
# Evaluate step by step
x = 10
y = 3
z = 2

result = x + y * z ** 2 - x // y + x % y
# Step by step:
# 1. z ** 2 = 4
# 2. y * 4 = 12
# 3. x // y = 10 // 3 = 3
# 4. x % y = 10 % 3 = 1
# 5. x + 12 = 22
# 6. 22 - 3 = 19
# 7. 19 + 1 = 20
print(result)  # 20

# Verification
print(10 + 3 * 4 - 3 + 1)  # 20

# With parentheses to change order
result = (x + y) * (z ** 2 - x) // (y + x % y)
# 1. x + y = 13
# 2. z ** 2 = 4
# 3. 4 - x = -6
# 4. 13 * -6 = -78
# 5. x % y = 1
# 6. y + 1 = 4
# 7. -78 // 4 = -20
print(result)  # -20
```

## Practical Examples

### Example 1: Temperature Converter with Logic
```python
def temperature_decision(temp, scale, is_night):
    """Complex temperature decision using operator precedence"""
    
    # Without parentheses (relies on precedence)
    result1 = temp > 30 and scale == 'C' or scale == 'F' and temp > 86
    # Precedence: comparisons > and > or
    # Evaluated as: (temp>30 and scale=='C') or (scale=='F' and temp>86)
    
    # With parentheses (explicit)
    result2 = (temp > 30 and scale == 'C') or (scale == 'F' and temp > 86)
    
    # Combine with night condition
    is_hot = result1
    should_use_ac = is_hot and not is_night
    
    return should_use_ac, is_hot

# Test cases
test_cases = [
    (35, 'C', False),  # Hot day
    (35, 'C', True),   # Hot night
    (25, 'C', False),  # Mild day
    (95, 'F', False),  # Hot Fahrenheit day
    (80, 'F', False),  # Mild Fahrenheit day
]

print("=== Temperature Decision Demo ===")
for temp, scale, is_night in test_cases:
    use_ac, is_hot = temperature_decision(temp, scale, is_night)
    print(f"Temp: {temp}°{scale}, Night: {is_night}")
    print(f"  Is hot: {is_hot}, Use AC: {use_ac}")
```

### Example 2: Expression Evaluator
```python
class ExpressionEvaluator:
    """Demonstrate operator precedence with different expressions"""
    
    @staticmethod
    def evaluate_expression(a, b, c):
        """Evaluate multiple expressions to show precedence"""
        
        expressions = [
            ("a + b * c", a + b * c),
            ("(a + b) * c", (a + b) * c),
            ("a ** b ** c", a ** b ** c),
            ("(a ** b) ** c", (a ** b) ** c),
            ("a & b | c", a & b | c),
            ("a & (b | c)", a & (b | c)),
            ("a > b and b > c", a > b and b > c),
            ("a > b > c", a > b > c),
            ("a or b and c", a or b and c),
            ("(a or b) and c", (a or b) and c),
        ]
        
        return expressions
    
    @staticmethod
    def show_evaluation_steps(expression, result):
        """Show evaluation steps for complex expression"""
        print(f"{expression:25} = {result}")

# Demo
evaluator = ExpressionEvaluator()

print("=== Expression Evaluation Demo ===")
print("-" * 50)

# Test values
a, b, c = 5, 3, 2

print(f"a = {a}, b = {b}, c = {c}\n")

for expr, result in evaluator.evaluate_expression(a, b, c):
    evaluator.show_evaluation_steps(expr, result)

# Complex example
print("\n=== Complex Expression Breakdown ===")
expr = "10 + 3 * 4 ** 2 - 8 // 2 + 5 % 3"
result = 10 + 3 * 4 ** 2 - 8 // 2 + 5 % 3

print(f"Expression: {expr}")
print(f"Result: {result}")
print("\nEvaluation steps:")
print("  1. 4 ** 2 = 16")
print("  2. 3 * 16 = 48")
print("  3. 8 // 2 = 4")
print("  4. 5 % 3 = 2")
print("  5. 10 + 48 = 58")
print("  6. 58 - 4 = 54")
print("  7. 54 + 2 = 56")
```

### Example 3: Bitwise Flag Checker
```python
class BitwiseFlagChecker:
    """Check permissions using bitwise operators with precedence"""
    
    PERM_READ = 0b001
    PERM_WRITE = 0b010
    PERM_EXEC = 0b100
    
    @staticmethod
    def check_permissions(user_perms, required_read=False, required_write=False, required_exec=False):
        """Check permissions considering operator precedence"""
        
        # Build required mask
        required_mask = 0
        if required_read:
            required_mask |= BitwiseFlagChecker.PERM_READ
        if required_write:
            required_mask |= BitwiseFlagChecker.PERM_WRITE
        if required_exec:
            required_mask |= BitwiseFlagChecker.PERM_EXEC
        
        # Complex condition without parentheses (relies on precedence)
        # Note: & has higher precedence than |, and both higher than and/or
        has_perms = user_perms & required_mask == required_mask
        
        return has_perms
    
    @staticmethod
    def complex_check(user_perms, is_admin, is_owner):
        """Complex permission check with multiple operators"""
        
        # Without parentheses - relies on precedence
        # Precedence: comparisons > not > and > or
        result = user_perms & BitwiseFlagChecker.PERM_WRITE or is_admin and not is_owner
        
        # Equivalent with parentheses
        result_explicit = (user_perms & BitwiseFlagChecker.PERM_WRITE) or (is_admin and not is_owner)
        
        return result

# Demo
checker = BitwiseFlagChecker()

print("=== Permission Check Demo ===")
print("-" * 40)

# Test users
users = [
    ("User1", checker.PERM_READ | checker.PERM_WRITE, False, True),
    ("User2", checker.PERM_READ, True, False),
    ("User3", checker.PERM_EXEC, False, False),
    ("Admin", checker.PERM_READ | checker.PERM_WRITE | checker.PERM_EXEC, True, True),
]

for name, perms, is_admin, is_owner in users:
    can_write = checker.check_permissions(perms, required_write=True)
    complex_result = checker.complex_check(perms, is_admin, is_owner)
    
    print(f"{name}:")
    print(f"  Permissions: {bin(perms)}")
    print(f"  Can write: {can_write}")
    print(f"  Complex check: {complex_result}")
```

### Example 4: Mathematical Formula Parser
```python
class FormulaCalculator:
    """Calculate various mathematical formulas respecting precedence"""
    
    @staticmethod
    def quadratic_formula(a, b, c):
        """Calculate quadratic formula: (-b ± √(b² - 4ac)) / (2a)"""
        
        # Without parentheses (uses precedence)
        discriminant1 = b ** 2 - 4 * a * c
        # Precedence: ** > * > -
        # b**2 - (4*a*c)
        
        # With parentheses (explicit)
        discriminant2 = (b ** 2) - (4 * a * c)
        
        if discriminant1 < 0:
            return None
        
        root1 = (-b + discriminant1 ** 0.5) / (2 * a)
        root2 = (-b - discriminant1 ** 0.5) / (2 * a)
        
        return root1, root2
    
    @staticmethod
    def compound_interest(P, r, n, t):
        """Compound interest: A = P(1 + r/n)^(nt)"""
        
        # Without parentheses
        amount1 = P * (1 + r / n) ** (n * t)
        
        # Step by step
        rate_per_period = 1 + r / n
        periods = n * t
        amount2 = P * rate_per_period ** periods
        
        return amount1
    
    @staticmethod
    def distance_formula(x1, y1, x2, y2):
        """Distance between points: √((x2-x1)² + (y2-y1)²)"""
        
        # Without parentheses
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        
        return distance

# Demo
calculator = FormulaCalculator()

print("=== Formula Calculator Demo ===")
print("-" * 40)

# Quadratic formula
print("Quadratic Formula (x² - 5x + 6 = 0):")
roots = calculator.quadratic_formula(1, -5, 6)
if roots:
    print(f"  Roots: {roots[0]:.2f}, {roots[1]:.2f}")

# Compound interest
principal = 1000
rate = 0.05
compounds = 12
years = 10
amount = calculator.compound_interest(principal, rate, compounds, years)
print(f"\nCompound Interest:")
print(f"  Principal: ${principal}")
print(f"  Rate: {rate*100}%")
print(f"  After {years} years: ${amount:.2f}")

# Distance formula
x1, y1 = 0, 0
x2, y2 = 3, 4
distance = calculator.distance_formula(x1, y1, x2, y2)
print(f"\nDistance Formula:")
print(f"  Distance between ({x1},{y1}) and ({x2},{y2}): {distance:.2f}")
```

### Example 5: Precedence Visualization
```python
class PrecedenceVisualizer:
    """Visualize operator precedence with step-by-step evaluation"""
    
    @staticmethod
    def evaluate_with_steps(expression, variables=None):
        """Evaluate expression and show steps (simplified)"""
        
        if variables is None:
            variables = {}
        
        print(f"\nExpression: {expression}")
        print("Variables:", variables)
        print("-" * 50)
        
        # This is a simplified demonstration
        # Real evaluation would need a proper parser
        
        steps = [
            ("Parentheses first", "( )"),
            ("Exponentiation", "**"),
            ("Unary operators", "+x, -x, ~x"),
            ("Multiplication/Division/Modulo", "*, /, //, %"),
            ("Addition/Subtraction", "+, -"),
            ("Bitwise shifts", "<<, >>"),
            ("Bitwise AND", "&"),
            ("Bitwise XOR", "^"),
            ("Bitwise OR", "|"),
            ("Comparisons", "<, >, <=, >=, ==, !="),
            ("Identity/Membership", "is, in"),
            ("Boolean NOT", "not"),
            ("Boolean AND", "and"),
            ("Boolean OR", "or"),
        ]
        
        for priority, ops in steps:
            print(f"Priority {steps.index(ops) + 1}: {ops}")
        
        print("-" * 50)
        print("Note: Use parentheses to override precedence")

# Demo
visualizer = PrecedenceVisualizer()

print("=== Operator Precedence Visualization ===")
visualizer.evaluate_with_steps("a + b * c ** d", {"a": 2, "b": 3, "c": 4, "d": 2})

# Complex examples with different groupings
expressions = [
    "2 + 3 * 4",
    "(2 + 3) * 4",
    "2 ** 3 ** 2",
    "(2 ** 3) ** 2",
    "10 - 5 - 2",
    "10 - (5 - 2)",
    "5 & 3 | 2",
    "5 & (3 | 2)",
]

print("\n=== Different Groupings ===")
for expr in expressions:
    result = eval(expr)
    print(f"{expr:20} = {result}")
```

## Common Mistakes

### Mistake 1: Assuming Left-to-Right for All Operators
```python
# Wrong - exponentiation is right-associative
print(2 ** 3 ** 2)  # 512, not 64

# Right - use parentheses for clarity
print((2 ** 3) ** 2)  # 64
```

### Mistake 2: Misunderstanding Precedence in Conditions
```python
# Wrong - bitwise AND has higher precedence than comparisons
x = 5
if x & 3 == 1:  # Evaluated as x & (3 == 1) = 5 & False = 0
    print("True")

# Right - use parentheses
if (x & 3) == 1:
    print("True")  # (5 & 3) = 1, 1 == 1 is True
```

### Mistake 3: Confusing 'and'/'or' with '&'/'|'
```python
# Wrong - using bitwise operators for logic
x = 5
y = 10
if x & y:  # Bitwise AND (0), not logical
    print("Both non-zero")

# Right - use logical operators
if x and y:
    print("Both non-zero")
```

### Mistake 4: Forgetting Parentheses in Complex Expressions
```python
# Wrong - unclear precedence
result = a + b if c else d - e

# Right - add parentheses
result = (a + b) if c else (d - e)
```

### Mistake 5: Chaining Comparisons Incorrectly
```python
# Wrong - works but confusing
x = 5
y = 10
z = 15
if x < y > z:  # x < y and y > z (not what it looks like)
    print("Not typical")

# Right - be explicit
if x < y and y > z:
    print("Clear intent")
```

## Precedence Cheat Sheet

```python
# Quick reference (highest to lowest)
precedence_chart = """
1. () [] {}          # Parentheses, indexing
2. **                # Exponentiation
3. +x -x ~x          # Unary operators
4. * / // %          # Multiplication, division
5. + -               # Addition, subtraction
6. << >>             # Bitwise shifts
7. &                 # Bitwise AND
8. ^                 # Bitwise XOR
9. |                 # Bitwise OR
10. < <= > >= == !=  # Comparisons
11. in not in is is not  # Membership, identity
12. not              # Boolean NOT
13. and              # Boolean AND
14. or               # Boolean OR
15. if-else          # Conditional
16. lambda           # Lambda
"""

print(precedence_chart)
```

## Best Practices

### ✅ Do This
```python
# Use parentheses for clarity, even when not required
result = (a + b) * c  # Clear intent

# Break complex expressions into steps
step1 = a + b
step2 = step1 * c
step3 = step2 - d
result = step3 / e

# Use descriptive variable names
base_amount = principal * (1 + rate)
total = base_amount ** years

# Parentheses in conditions
if (x > 0 and y > 0) or (z > 0):
    process()

# Explicit grouping in bitwise operations
if (flags & MASK) == MASK:
    print("All bits set")
```

### ❌ Avoid This
```python
# Avoid - relying on obscure precedence
result = a + b * c ** d // e % f

# Avoid - overly complex one-liners
result = a if b else c if d else e if f else g

# Avoid - unclear bitwise conditions
if flags & MASK == MASK:  # Wrong precedence!
    print("Bug!")

# Avoid - mixing operators without parentheses
if a and b or c and d:
    print("Unclear")

# Avoid - using bitwise operators for boolean logic
if a & b:  # Probably meant 'and'
    print("Confusing")
```

## Summary

- **Parentheses have the highest precedence** - use them to override default order
- **Exponentiation (**)** is right-associative
- **Unary operators** (+, -, ~) have higher precedence than binary
- **Multiplication, division, floor division, modulo** have same precedence (left-associative)
- **Addition and subtraction** have same precedence (left-associative)
- **Bitwise shifts** have lower precedence than arithmetic
- **Bitwise AND (&)** has higher precedence than XOR (^) and OR (|)
- **Comparisons** chain with AND logic
- **Boolean not** has higher precedence than and, which has higher than or
- **Conditional expression** has very low precedence
- **Lambda** has the lowest precedence
- **Use parentheses** to make code clear and avoid bugs

## Basic Template
```python
#!/usr/bin/env python3

def precedence_demo():
    """Demonstrate operator precedence with examples"""
    
    a, b, c = 10, 5, 2
    
    print(f"a = {a}, b = {b}, c = {c}\n")
    
    # Arithmetic precedence
    print("=== Arithmetic Precedence ===")
    print(f"a + b * c = {a + b * c}")
    print(f"(a + b) * c = {(a + b) * c}")
    print(f"a ** b ** c = {a ** b ** c}")
    print(f"(a ** b) ** c = {(a ** b) ** c}")
    
    # Bitwise precedence
    print("\n=== Bitwise Precedence ===")
    print(f"a & b | c = {a & b | c}")
    print(f"a & (b | c) = {a & (b | c)}")
    
    # Logical precedence
    print("\n=== Logical Precedence ===")
    x, y, z = True, False, True
    print(f"x or y and z = {x or y and z}")
    print(f"(x or y) and z = {(x or y) and z}")
    
    # Comparison chaining
    print("\n=== Comparison Chaining ===")
    n = 5
    print(f"1 < n < 10 = {1 < n < 10}")
    print(f"1 < n and n < 10 = {1 < n and n < 10}")

def complex_calculation():
    """Calculate complex expression step by step"""
    
    expression = "10 + 3 * 4 ** 2 - 8 // 2 + 5 % 3"
    result = 10 + 3 * 4 ** 2 - 8 // 2 + 5 % 3
    
    print(f"\nExpression: {expression}")
    print(f"Result: {result}")
    
    print("\nEvaluation steps:")
    print("  1. 4 ** 2 =", 4 ** 2)
    print("  2. 3 * 16 =", 3 * 16)
    print("  3. 8 // 2 =", 8 // 2)
    print("  4. 5 % 3 =", 5 % 3)
    print("  5. 10 + 48 =", 10 + 48)
    print("  6. 58 - 4 =", 58 - 4)
    print("  7. 54 + 2 =", 54 + 2)

def best_practices():
    """Demonstrate best practices for operator precedence"""
    
    # Use parentheses for clarity
    x, y, z = 10, 5, 2
    result1 = (x + y) * z
    result2 = x + (y * z)
    print(f"\n(x + y) * z = {result1}")
    print(f"x + (y * z) = {result2}")
    
    # Break down complex expressions
    step1 = x + y
    step2 = step1 * z
    print(f"Broken down: ({x}+{y})*{z} = {step2}")
    
    # Parentheses in conditions
    age = 25
    has_license = True
    has_permit = False
    
    if (age >= 18) and (has_license or has_permit):
        print("Can drive")
    
    # Explicit bitwise conditions
    flags = 0b1100
    mask = 0b1000
    if (flags & mask) == mask:
        print("Bit is set")

if __name__ == "__main__":
    precedence_demo()
    complex_calculation()
    best_practices()
```

*This documentation belongs to https://github.com/InterCentury*