# 13 - Floating-Point Types (float) in Python

## What are Floating-Point Numbers?
Floating-point numbers (floats) represent real numbers with decimal points. In Python, `float` uses double-precision (64-bit) IEEE 754 format, similar to `double` in C++.

## Basic Float Declaration

```python
# Basic floats
a = 3.14
b = -2.5
c = 0.0
d = 42.0

# Scientific notation
e = 1.5e3      # 1.5 × 10³ = 1500.0
f = 2.5e-2     # 2.5 × 10⁻² = 0.025
g = -1.2e4     # -12000.0

# Print and check types
print(a, type(a))  # 3.14 <class 'float'>
print(e, type(e))  # 1500.0 <class 'float'>
```

## Float Literals

### Decimal Format
```python
# Standard decimal notation
regular = 3.14159
negative = -42.5
zero = 0.0
trailing = 42.     # Same as 42.0
leading = .5       # Same as 0.5

print(regular)  # 3.14159
print(trailing) # 42.0
print(leading)  # 0.5
```

### Scientific Notation
```python
# E or e notation
million = 1e6        # 1,000,000.0
micro = 1e-6         # 0.000001
avogadro = 6.022e23  # 6.022 × 10²³
plank = 6.626e-34    # 6.626 × 10⁻³⁴

print(million)  # 1000000.0
print(micro)    # 1e-06

# Multiple formats
print(1.5e3)    # 1500.0
print(1.5E3)    # 1500.0 (uppercase E works too)
print(1.5e-3)   # 0.0015
```

### Underscores for Readability
```python
# Group digits for readability
large = 1_000_000.5
scientific = 1.234_567e6
pi_approx = 3.141_592_653_59

print(large)      # 1000000.5
print(scientific) # 1234567.0
print(pi_approx)  # 3.14159265359
```

## Special Float Values

### Infinity
```python
# Positive infinity
inf_pos = float('inf')
inf_pos2 = float('Inf')
inf_pos3 = 1e1000  # Overflow to infinity

# Negative infinity
inf_neg = float('-inf')

# Check for infinity
print(inf_pos)                    # inf
print(inf_pos == float('inf'))    # True
print(inf_pos > 1e100)            # True

# Operations with infinity
print(inf_pos + 100)              # inf
print(inf_pos * 2)                # inf
print(inf_pos / inf_pos)          # nan (not a number)

# Useful functions
import math
print(math.isinf(inf_pos))        # True
```

### NaN (Not a Number)
```python
# Creating NaN
nan1 = float('nan')
nan2 = float('NaN')
nan3 = float('NAN')
nan4 = 0.0 / 0.0      # Division by zero
nan5 = math.sqrt(-1)  # Square root of negative

print(nan1)           # nan

# NaN properties (important!)
print(nan1 == nan1)   # False! NaN is not equal to itself
print(nan1 is nan1)   # True (same object)
print(nan1 != nan1)   # True

# Check for NaN
print(math.isnan(nan1))  # True
print(math.isnan(5.0))   # False

# NaN in operations
print(nan1 + 5)       # nan
print(nan1 * 2)       # nan
print(nan1 > 0)       # False
print(nan1 < 0)       # False
```

## Float Precision and Limitations

### Precision Issues (Important!)
```python
# Binary representation limitations
print(0.1 + 0.2)           # 0.30000000000000004 (not 0.3!)
print(0.1 + 0.2 == 0.3)    # False!

print(1.0 / 3.0)           # 0.3333333333333333
print(1.0 / 3.0 * 3.0)     # 1.0 (but not exactly)

# Accumulated errors
total = 0.0
for i in range(10):
    total += 0.1
print(total)               # 0.9999999999999999 (not 1.0)

# Machine epsilon (smallest difference)
epsilon = 2.22e-16
print(1.0 + epsilon == 1.0)    # False
print(1.0 + epsilon/2 == 1.0)  # True
```

### Decimal Module for Precise Calculations
```python
from decimal import Decimal, getcontext

# Decimal for precise decimal arithmetic
d1 = Decimal('0.1')
d2 = Decimal('0.2')
print(d1 + d2)              # 0.3 (exact!)
print(d1 + d2 == 0.3)       # False (Decimal vs float)
print(d1 + d2 == Decimal('0.3'))  # True

# Set precision
getcontext().prec = 28      # 28 decimal places
print(Decimal(1) / Decimal(7))  # 0.1428571428571428571428571429

# Floating-point vs Decimal
float_sum = 0.1 + 0.2
decimal_sum = Decimal('0.1') + Decimal('0.2')
print(f"Float: {float_sum:.30f}")     # 0.3000000000000000444089209850
print(f"Decimal: {decimal_sum}")       # 0.3
```

### Fraction Module for Rational Numbers
```python
from fractions import Fraction

# Exact rational representation
f1 = Fraction(1, 10)
f2 = Fraction(1, 5)
print(f1 + f2)              # 3/10
print(float(f1 + f2))       # 0.3

# Avoid floating-point errors
result = Fraction(1, 3) * 3
print(result)               # 1 (exact)
print(float(result))        # 1.0
```

## Float Operations

### Arithmetic Operations
```python
a = 10.5
b = 3.2

# Basic operations
print(a + b)      # 13.7
print(a - b)      # 7.3
print(a * b)      # 33.6
print(a / b)      # 3.28125
print(a // b)     # 3.0 (floor division)
print(a % b)      # 0.9000000000000004 (remainder)
print(a ** b)     # 10.5 ** 3.2

# Compound assignment
x = 5.0
x += 2.5    # x = x + 2.5
x *= 2      # x = x * 2
x /= 3      # x = x / 3
print(x)    # 5.0
```

### Comparison Operations
```python
a = 3.14
b = 3.14

# Basic comparisons
print(a == b)       # True
print(a != b)       # False
print(a < 4.0)      # True
print(a > 3.0)      # True

# Comparing floats with tolerance (recommended)
def almost_equal(x, y, tolerance=1e-10):
    """Check if two floats are approximately equal"""
    return abs(x - y) < tolerance

x = 0.1 + 0.2
y = 0.3
print(x == y)                     # False
print(almost_equal(x, y))         # True
print(math.isclose(x, y))         # True (Python 3.5+)

# math.isclose with custom tolerances
print(math.isclose(x, y, rel_tol=1e-9, abs_tol=0.0))  # True
```

## Type Conversion

### Converting to float
```python
# From int
print(float(42))        # 42.0
print(float(-10))       # -10.0

# From string
print(float("3.14"))    # 3.14
print(float("1.5e3"))   # 1500.0
print(float("  42.5  ")) # 42.5 (strips whitespace)
print(float("inf"))     # inf
print(float("nan"))     # nan

# From bool
print(float(True))      # 1.0
print(float(False))     # 0.0

# Invalid conversions
# float("abc")          # ValueError
# float("1,234")        # ValueError
```

### Converting from float
```python
x = 3.14159

# To int (truncates toward zero)
print(int(x))           # 3
print(int(-3.14))       # -3

# To string
print(str(x))           # "3.14159"
print(repr(x))          # "3.14159"

# To bool
print(bool(x))          # True (non-zero)
print(bool(0.0))        # False

# Rounding
print(round(x))         # 3
print(round(x, 2))      # 3.14
print(round(3.99))      # 4
print(round(2.5))       # 2 (bankers rounding!)
print(round(3.5))       # 4

# Floor and ceiling
import math
print(math.floor(x))    # 3 (rounds down)
print(math.ceil(x))     # 4 (rounds up)
print(math.trunc(x))    # 3 (truncates)
```

## Math Module Functions

### Basic Math Functions
```python
import math

x = 2.5

# Rounding
print(math.floor(x))    # 2 (floor)
print(math.ceil(x))     # 3 (ceiling)
print(math.trunc(x))    # 2 (truncate)

# Power and roots
print(math.pow(2, 3))   # 8.0 (2³)
print(math.sqrt(16))    # 4.0 (square root)
print(math.cbrt(27))    # 3.0 (cube root, Python 3.11+)
print(math.exp(1))      # 2.718281828459045 (e¹)
print(math.expm1(1))    # 1.718281828459045 (e¹ - 1)

# Logarithms
print(math.log(100, 10))  # 2.0 (log base 10)
print(math.log(100))      # 4.605170185988092 (natural log)
print(math.log10(100))    # 2.0 (log base 10)
print(math.log2(8))       # 3.0 (log base 2)
print(math.log1p(0.1))    # 0.09531017980432493 (ln(1+x))

# Trigonometric functions (radians)
angle = math.pi / 2  # 90 degrees
print(math.sin(angle))    # 1.0
print(math.cos(angle))    # 6.123233995736766e-17 (~0)
print(math.tan(angle))    # 1.633123935319537e16 (~inf)

# Inverse trig
print(math.asin(1))       # 1.5707963267948966 (π/2)
print(math.acos(0))       # 1.5707963267948966
print(math.atan(1))       # 0.7853981633974483 (π/4)

# Degrees/radians conversion
print(math.radians(180))  # 3.141592653589793
print(math.degrees(math.pi))  # 180.0
```

### Advanced Math Functions
```python
import math

# Hyperbolic functions
x = 1.0
print(math.sinh(x))       # 1.1752011936438014
print(math.cosh(x))       # 1.5430806348152437
print(math.tanh(x))       # 0.7615941559557649

# Special functions
print(math.erf(1.0))      # 0.8427007929497149 (error function)
print(math.erfc(1.0))     # 0.1572992070502851
print(math.gamma(5))      # 24.0 (gamma function: (n-1)!)
print(math.lgamma(5))     # 3.1780538303479458 (log gamma)

# Constants
print(math.pi)            # 3.141592653589793
print(math.e)             # 2.718281828459045
print(math.tau)           # 6.283185307179586 (2π)
print(math.inf)           # inf
print(math.nan)           # nan

# Combinations and permutations
print(math.comb(10, 3))   # 120 (10 choose 3)
print(math.perm(10, 3))   # 720 (10 permute 3)
print(math.factorial(5))  # 120 (5!)
```

## Practical Examples

### Example 1: Scientific Calculator
```python
import math

def scientific_calculator():
    """Basic scientific calculator for floats"""
    
    print("Scientific Calculator")
    print("=" * 50)
    
    while True:
        print("\nOperations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (^)")
        print("6. Square root (√)")
        print("7. Sin (degrees)")
        print("8. Cos (degrees)")
        print("9. Tan (degrees)")
        print("10. Log (base 10)")
        print("11. Natural log (ln)")
        print("12. Exit")
        
        choice = input("\nEnter choice (1-12): ")
        
        if choice == '12':
            print("Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4', '5']:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"{a} + {b} = {a + b}")
            elif choice == '2':
                print(f"{a} - {b} = {a - b}")
            elif choice == '3':
                print(f"{a} * {b} = {a * b}")
            elif choice == '4':
                if b == 0:
                    print("Error: Division by zero!")
                else:
                    print(f"{a} / {b} = {a / b}")
            elif choice == '5':
                print(f"{a} ^ {b} = {a ** b}")
        
        elif choice == '6':
            num = float(input("Enter number: "))
            if num < 0:
                print("Error: Cannot take square root of negative!")
            else:
                print(f"√{num} = {math.sqrt(num)}")
        
        elif choice in ['7', '8', '9']:
            degrees = float(input("Enter angle in degrees: "))
            radians = math.radians(degrees)
            
            if choice == '7':
                print(f"sin({degrees}°) = {math.sin(radians)}")
            elif choice == '8':
                print(f"cos({degrees}°) = {math.cos(radians)}")
            elif choice == '9':
                print(f"tan({degrees}°) = {math.tan(radians)}")
        
        elif choice == '10':
            num = float(input("Enter number: "))
            if num <= 0:
                print("Error: Log only defined for positive numbers!")
            else:
                print(f"log10({num}) = {math.log10(num)}")
        
        elif choice == '11':
            num = float(input("Enter number: "))
            if num <= 0:
                print("Error: Natural log only defined for positive numbers!")
            else:
                print(f"ln({num}) = {math.log(num)}")
        
        else:
            print("Invalid choice!")

# scientific_calculator()
```

### Example 2: Circle Calculator
```python
import math

class Circle:
    """Circle calculations with floats"""
    
    def __init__(self, radius):
        self.radius = float(radius)
    
    @property
    def diameter(self):
        return 2 * self.radius
    
    @property
    def circumference(self):
        return 2 * math.pi * self.radius
    
    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    def distance_between_centers(self, other_circle):
        """Calculate distance between circle centers"""
        return abs(self.radius - other_circle.radius)
    
    def circles_intersect(self, other_circle):
        """Check if two circles intersect"""
        distance = self.distance_between_centers(other_circle)
        return distance <= (self.radius + other_circle.radius)
    
    def __str__(self):
        return (f"Circle(r={self.radius:.2f}, "
                f"d={self.diameter:.2f}, "
                f"C={self.circumference:.2f}, "
                f"A={self.area:.2f})")

# Create circles
circle1 = Circle(5.0)
circle2 = Circle(3.0)

print("Circle 1:", circle1)
print("Circle 2:", circle2)
print(f"Distance between centers: {circle1.distance_between_centers(circle2):.2f}")
print(f"Circles intersect? {circle1.circles_intersect(circle2)}")

# Calculate with precision
radius = 1e-6  # Very small circle
tiny_circle = Circle(radius)
print(f"\nTiny circle: {tiny_circle}")
print(f"Area: {tiny_circle.area:.10e}")

# Large numbers
huge_circle = Circle(1e6)
print(f"\nHuge circle: {huge_circle}")
```

### Example 3: Temperature Converter
```python
def temperature_converter():
    """Convert between Celsius, Fahrenheit, and Kelvin"""
    
    print("Temperature Converter")
    print("=" * 40)
    
    print("Convert from:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    
    choice = input("Choose (1-3): ")
    temp = float(input("Enter temperature: "))
    
    if choice == '1':
        celsius = temp
        fahrenheit = celsius * 9/5 + 32
        kelvin = celsius + 273.15
        
        print(f"\n{celsius:.2f}°C = {fahrenheit:.2f}°F")
        print(f"{celsius:.2f}°C = {kelvin:.2f}K")
        
    elif choice == '2':
        fahrenheit = temp
        celsius = (fahrenheit - 32) * 5/9
        kelvin = celsius + 273.15
        
        print(f"\n{fahrenheit:.2f}°F = {celsius:.2f}°C")
        print(f"{fahrenheit:.2f}°F = {kelvin:.2f}K")
        
    elif choice == '3':
        kelvin = temp
        celsius = kelvin - 273.15
        fahrenheit = celsius * 9/5 + 32
        
        print(f"\n{kelvin:.2f}K = {celsius:.2f}°C")
        print(f"{kelvin:.2f}K = {fahrenheit:.2f}°F")
        
    else:
        print("Invalid choice!")

# Demonstrate precision issues
print("\n" + "=" * 40)
print("Precision Demonstration:")
print("0.1°C in Fahrenheit:", 0.1 * 9/5 + 32)
print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.3 == 0.1 + 0.2?", 0.3 == 0.1 + 0.2)

# temperature_converter()
```

### Example 4: Statistical Calculator
```python
import math
import statistics

def statistical_analysis(data):
    """Perform statistical analysis on float data"""
    
    if not data:
        return "No data"
    
    # Basic statistics
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = math.sqrt(variance)
    
    # Min, max, range
    minimum = min(data)
    maximum = max(data)
    data_range = maximum - minimum
    
    # Quartiles
    sorted_data = sorted(data)
    q1 = statistics.quantiles(sorted_data, n=4)[0]
    q3 = statistics.quantiles(sorted_data, n=4)[2]
    iqr = q3 - q1
    
    # Median
    median = statistics.median(sorted_data)
    
    return {
        'count': n,
        'sum': sum(data),
        'mean': mean,
        'median': median,
        'variance': variance,
        'std_dev': std_dev,
        'min': minimum,
        'max': maximum,
        'range': data_range,
        'q1': q1,
        'q3': q3,
        'iqr': iqr
    }

def print_statistics(stats):
    """Pretty print statistics"""
    
    print("Statistical Analysis")
    print("=" * 40)
    print(f"Count: {stats['count']}")
    print(f"Sum: {stats['sum']:.4f}")
    print(f"Mean: {stats['mean']:.4f}")
    print(f"Median: {stats['median']:.4f}")
    print(f"Variance: {stats['variance']:.4f}")
    print(f"Std Dev: {stats['std_dev']:.4f}")
    print(f"Min: {stats['min']:.4f}")
    print(f"Max: {stats['max']:.4f}")
    print(f"Range: {stats['range']:.4f}")
    print(f"Q1 (25th): {stats['q1']:.4f}")
    print(f"Q3 (75th): {stats['q3']:.4f}")
    print(f"IQR: {stats['iqr']:.4f}")

# Sample data
test_data = [1.2, 2.3, 3.1, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0, 10.1]
stats = statistical_analysis(test_data)
print_statistics(stats)

# Demonstrate with larger dataset
import random
random.seed(42)
large_data = [random.gauss(100, 15) for _ in range(1000)]
large_stats = statistical_analysis(large_data)
print("\nLarge Dataset (1000 samples):")
print(f"Mean: {large_stats['mean']:.2f}")
print(f"Std Dev: {large_stats['std_dev']:.2f}")
print(f"Min: {large_stats['min']:.2f}")
print(f"Max: {large_stats['max']:.2f}")
```

### Example 5: Financial Calculator
```python
import math

class FinancialCalculator:
    """Financial calculations with floats"""
    
    @staticmethod
    def compound_interest(principal, rate, time, compounds_per_year=1):
        """Calculate compound interest"""
        rate_decimal = rate / 100
        amount = principal * (1 + rate_decimal / compounds_per_year) ** (compounds_per_year * time)
        interest = amount - principal
        return amount, interest
    
    @staticmethod
    def loan_payment(principal, annual_rate, years):
        """Calculate monthly loan payment"""
        monthly_rate = annual_rate / 100 / 12
        months = years * 12
        
        if monthly_rate == 0:
            payment = principal / months
        else:
            payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
        
        total_paid = payment * months
        total_interest = total_paid - principal
        
        return payment, total_paid, total_interest
    
    @staticmethod
    def investment_growth(initial, monthly_contribution, annual_return, years):
        """Calculate investment growth with monthly contributions"""
        monthly_rate = annual_return / 100 / 12
        months = years * 12
        
        # Future value of initial investment
        future_initial = initial * (1 + monthly_rate) ** months
        
        # Future value of monthly contributions
        if monthly_rate == 0:
            future_contributions = monthly_contribution * months
        else:
            future_contributions = monthly_contribution * ((1 + monthly_rate) ** months - 1) / monthly_rate
        
        total = future_initial + future_contributions
        total_contributions = initial + (monthly_contribution * months)
        total_gain = total - total_contributions
        
        return total, total_contributions, total_gain

# Demonstrate financial calculations
calc = FinancialCalculator()

print("Financial Calculator")
print("=" * 50)

# Compound interest
principal = 10000
rate = 5
years = 10
amount, interest = calc.compound_interest(principal, rate, years)
print(f"\nCompound Interest:")
print(f"Principal: ${principal:,.2f}")
print(f"Rate: {rate}%")
print(f"Years: {years}")
print(f"Final amount: ${amount:,.2f}")
print(f"Interest earned: ${interest:,.2f}")

# Loan payment
loan_amount = 200000
annual_rate = 4.5
loan_years = 30
payment, total_paid, total_interest = calc.loan_payment(loan_amount, annual_rate, loan_years)
print(f"\nLoan Payment:")
print(f"Loan amount: ${loan_amount:,.2f}")
print(f"Annual rate: {annual_rate}%")
print(f"Term: {loan_years} years")
print(f"Monthly payment: ${payment:,.2f}")
print(f"Total paid: ${total_paid:,.2f}")
print(f"Total interest: ${total_interest:,.2f}")

# Investment growth
initial = 5000
monthly = 500
return_rate = 8
invest_years = 20
total, contributions, gain = calc.investment_growth(initial, monthly, return_rate, invest_years)
print(f"\nInvestment Growth:")
print(f"Initial: ${initial:,.2f}")
print(f"Monthly contribution: ${monthly:,.2f}")
print(f"Annual return: {return_rate}%")
print(f"Years: {invest_years}")
print(f"Total value: ${total:,.2f}")
print(f"Total contributions: ${contributions:,.2f}")
print(f"Total gain: ${gain:,.2f}")
```

### Example 6: Geometry Calculator
```python
import math

class GeometryCalculator:
    """Geometry calculations with floats"""
    
    @staticmethod
    def distance(x1, y1, x2, y2):
        """Distance between two points"""
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    @staticmethod
    def slope(x1, y1, x2, y2):
        """Slope of line through two points"""
        if x2 - x1 == 0:
            return float('inf')  # Vertical line
        return (y2 - y1) / (x2 - x1)
    
    @staticmethod
    def triangle_area(x1, y1, x2, y2, x3, y3):
        """Area of triangle using coordinates"""
        return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)
    
    @staticmethod
    def circle_intersection(x1, y1, r1, x2, y2, r2):
        """Check if two circles intersect and find intersection points"""
        d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        # No intersection
        if d > r1 + r2 or d < abs(r1 - r2) or d == 0:
            return None
        
        # Intersection points
        a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
        h = math.sqrt(r1 ** 2 - a ** 2)
        
        x0 = x1 + a * (x2 - x1) / d
        y0 = y1 + a * (y2 - y1) / d
        
        rx = -(y2 - y1) * (h / d)
        ry = -(x2 - x1) * (h / d)
        
        point1 = (x0 + rx, y0 - ry)
        point2 = (x0 - rx, y0 + ry)
        
        return point1, point2

# Test geometry functions
geo = GeometryCalculator()

print("Geometry Calculator")
print("=" * 50)

# Distance
x1, y1 = 0, 0
x2, y2 = 3, 4
dist = geo.distance(x1, y1, x2, y2)
print(f"Distance between ({x1},{y1}) and ({x2},{y2}): {dist}")

# Slope
slope = geo.slope(x1, y1, x2, y2)
print(f"Slope: {slope}")

# Triangle area
x1, y1 = 0, 0
x2, y2 = 4, 0
x3, y3 = 0, 3
area = geo.triangle_area(x1, y1, x2, y2, x3, y3)
print(f"Triangle area: {area}")

# Circle intersection
points = geo.circle_intersection(0, 0, 5, 8, 0, 5)
if points:
    print(f"Circle intersection points: {points}")
else:
    print("Circles do not intersect")

# Demonstrate floating-point precision
print("\n" + "=" * 50)
print("Precision in Geometry:")
x = 1e-10
y = 1e-10
dist = geo.distance(0, 0, x, y)
print(f"Distance to ({x}, {y}): {dist}")
```

## Float Formatting

### String Formatting Methods
```python
x = 123.456789

# f-strings (Python 3.6+)
print(f"{x:.2f}")     # 123.46 (2 decimal places)
print(f"{x:.0f}")     # 123 (0 decimal places)
print(f"{x:.3e}")     # 1.235e+02 (scientific)
print(f"{x:10.2f}")   # "    123.46" (width 10)
print(f"{x:<10.2f}")  # "123.46    " (left align)
print(f"{x:>10.2f}")  # "    123.46" (right align)
print(f"{x:^10.2f}")  # " 123.46   " (center)

# format() method
print(format(x, ".2f"))       # 123.46
print(format(x, "10.2f"))     # "    123.46"
print(format(x, "e"))         # 1.234568e+02

# % formatting (old style)
print("%.2f" % x)             # 123.46
print("%10.2f" % x)           # "    123.46"

# Thousands separator
large = 1234567.89
print(f"{large:,.2f}")        # 1,234,567.89
print(f"{large:_.2f}")        # 1_234_567.89

# Percentage
ratio = 0.4567
print(f"{ratio:.1%}")         # 45.7%
print(f"{ratio:.2%}")         # 45.67%
```

## Float Comparison Best Practices

### Don't Compare Directly
```python
# Bad - direct comparison
x = 0.1 + 0.2
if x == 0.3:  # False!
    print("Equal")

# Good - use tolerance
tolerance = 1e-10
if abs(x - 0.3) < tolerance:
    print("Approximately equal")

# Best - use math.isclose (Python 3.5+)
import math
if math.isclose(x, 0.3):
    print("Close enough")

# Custom tolerance
if math.isclose(x, 0.3, rel_tol=1e-9, abs_tol=1e-12):
    print("Close with custom tolerance")
```

### Relative vs Absolute Tolerance
```python
import math

# Absolute tolerance (good for numbers near zero)
a = 1e-10
b = 1e-11
print(math.isclose(a, b, abs_tol=1e-9))  # True
print(math.isclose(a, b, rel_tol=1e-9))  # May be False

# Relative tolerance (good for large numbers)
big_a = 1e10
big_b = 1e10 + 1
print(math.isclose(big_a, big_b, rel_tol=1e-9))  # True
print(math.isclose(big_a, big_b, abs_tol=1e-9))  # False
```

## Common Mistakes

### Mistake 1: Direct Float Comparison
```python
# Wrong
if 0.1 + 0.2 == 0.3:
    print("Equal")  # Never prints!

# Right
if abs(0.1 + 0.2 - 0.3) < 1e-10:
    print("Equal")
```

### Mistake 2: Division by Zero
```python
# Wrong - crashes
x = 10.0 / 0.0  # ZeroDivisionError

# Right - check first
if denominator != 0:
    result = numerator / denominator
else:
    print("Cannot divide by zero")
```

### Mistake 3: Assuming Decimal Precision
```python
# Wrong - expecting exact decimal results
price = 0.10
quantity = 3
total = price * quantity
print(total)  # 0.30000000000000004

# Right - use Decimal for money
from decimal import Decimal
price = Decimal('0.10')
quantity = 3
total = price * quantity
print(total)  # 0.30
```

### Mistake 4: Comparing NaN
```python
# Wrong
nan = float('nan')
if nan == nan:  # False! Always false
    print("Same")

# Right
if math.isnan(nan):
    print("Is NaN")
```

### Mistake 5: Integer Division with Floats
```python
# Wrong - expecting integer division
result = 10.0 // 3.0  # 3.0 (float, not int)

# Right - convert if needed
result = int(10.0 // 3.0)  # 3 (int)
```

## Performance Considerations

```python
import time

# Float operations are slightly slower than ints
def performance_compare():
    iterations = 10_000_000
    
    # Integer operations
    start = time.time()
    i = 0
    for _ in range(iterations):
        i += 1
    int_time = time.time() - start
    
    # Float operations
    start = time.time()
    f = 0.0
    for _ in range(iterations):
        f += 1.0
    float_time = time.time() - start
    
    print(f"Integer ops: {int_time:.3f}s")
    print(f"Float ops: {float_time:.3f}s")
    print(f"Float overhead: {(float_time/int_time - 1)*100:.1f}%")

# performance_compare()
```

## Quick Reference Table

| Operation | Syntax | Example | Result |
|-----------|--------|---------|--------|
| Float literal | `3.14` | `3.14` | `3.14` |
| Scientific | `1.5e3` | `1.5e3` | `1500.0` |
| Infinity | `float('inf')` | `float('inf')` | `inf` |
| NaN | `float('nan')` | `float('nan')` | `nan` |
| Floor | `math.floor(x)` | `math.floor(3.14)` | `3` |
| Ceil | `math.ceil(x)` | `math.ceil(3.14)` | `4` |
| Round | `round(x, n)` | `round(3.14159, 2)` | `3.14` |
| Absolute | `abs(x)` | `abs(-3.14)` | `3.14` |
| Power | `x ** y` | `2.0 ** 3.0` | `8.0` |
| Square root | `math.sqrt(x)` | `math.sqrt(16.0)` | `4.0` |

## Summary

- **float** represents real numbers (decimal points)
- **Double-precision** (64-bit) IEEE 754 format
- **Scientific notation** with `e` or `E`
- **Precision limitations** - binary representation issues
- **Never compare floats directly** - use tolerance or `math.isclose()`
- **Special values**: `inf`, `-inf`, `nan`
- **Math module** provides advanced functions
- **Decimal module** for precise decimal arithmetic
- **Fractions module** for rational numbers
- **Format with f-strings** for controlled output

## Basic Template
```python
#!/usr/bin/env python3

import math
from decimal import Decimal

# Basic float operations
def float_basics():
    """Demonstrate basic float operations"""
    
    # Declaration
    a = 3.14
    b = 2.5
    
    # Arithmetic
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    
    # Scientific notation
    print(f"1.5e3 = {1.5e3}")
    print(f"2.5e-2 = {2.5e-2}")
    
    # Special values
    print(f"inf: {float('inf')}")
    print(f"nan: {float('nan')}")

# Precision demonstration
def precision_demo():
    """Show floating-point precision issues"""
    
    print(f"0.1 + 0.2 = {0.1 + 0.2}")
    print(f"0.1 + 0.2 == 0.3? {0.1 + 0.2 == 0.3}")
    
    # Correct comparison
    if math.isclose(0.1 + 0.2, 0.3):
        print("Close enough with isclose()")
    
    # Using Decimal for precision
    d = Decimal('0.1') + Decimal('0.2')
    print(f"Decimal: {d}")

# Math functions
def math_functions():
    """Use common math functions"""
    
    x = 2.5
    
    print(f"Round: {round(x)}")
    print(f"Floor: {math.floor(x)}")
    print(f"Ceil: {math.ceil(x)}")
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"sin(90°): {math.sin(math.radians(90))}")
    print(f"π = {math.pi}")
    print(f"e = {math.e}")

# Formatting floats
def float_formatting():
    """Format float output"""
    
    x = 123.456789
    
    print(f"2 decimals: {x:.2f}")
    print(f"Scientific: {x:.2e}")
    print(f"Width 10: {x:10.2f}")
    print(f"Thousands: {1234567.89:,.2f}")
    print(f"Percentage: {0.4567:.1%}")

# Run examples
if __name__ == "__main__":
    print("=== FLOAT BASICS ===")
    float_basics()
    
    print("\n=== PRECISION DEMO ===")
    precision_demo()
    
    print("\n=== MATH FUNCTIONS ===")
    math_functions()
    
    print("\n=== FLOAT FORMATTING ===")
    float_formatting()
```

*This documentation belongs to https://github.com/InterCentury*