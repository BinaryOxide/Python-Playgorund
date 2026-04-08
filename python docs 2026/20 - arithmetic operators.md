# 20 - Arithmetic Operators in Python

## What are Arithmetic Operators?
Arithmetic operators are used to perform mathematical operations on numeric values (integers, floats, and complex numbers). Python provides a complete set of arithmetic operators for basic and advanced calculations.

## Basic Arithmetic Operators

### Addition (+)
```python
# Integer addition
a = 10
b = 5
result = a + b
print(f"{a} + {b} = {result}")  # 10 + 5 = 15

# Float addition
x = 3.14
y = 2.86
print(f"{x} + {y} = {x + y}")  # 3.14 + 2.86 = 6.0

# String concatenation (overloaded)
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)  # Hello World

# List concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)  # [1, 2, 3, 4, 5, 6]

# Complex numbers
c1 = 3 + 4j
c2 = 1 + 2j
print(f"{c1} + {c2} = {c1 + c2}")  # (4+6j)
```

### Subtraction (-)
```python
# Integer subtraction
a = 20
b = 7
print(f"{a} - {b} = {a - b}")  # 20 - 7 = 13

# Negative result
print(f"{b} - {a} = {b - a}")  # 7 - 20 = -13

# Float subtraction
x = 10.5
y = 3.2
print(f"{x} - {y} = {x - y}")  # 10.5 - 3.2 = 7.3

# Complex numbers
c1 = 5 + 6j
c2 = 2 + 3j
print(f"{c1} - {c2} = {c1 - c2}")  # (3+3j)
```

### Multiplication (*)
```python
# Integer multiplication
a = 8
b = 7
print(f"{a} * {b} = {a * b}")  # 8 * 7 = 56

# Float multiplication
x = 3.5
y = 2.0
print(f"{x} * {y} = {x * y}")  # 3.5 * 2.0 = 7.0

# String repetition
text = "Hi"
print(text * 3)  # HiHiHi

# List repetition
items = [1, 2]
print(items * 3)  # [1, 2, 1, 2, 1, 2]

# Complex multiplication
c1 = 2 + 3j
c2 = 1 + 4j
print(f"{c1} * {c2} = {c1 * c2}")  # (-10+11j)
```

### Division (/)
```python
# Always returns float
a = 10
b = 3
print(f"{a} / {b} = {a / b}")  # 10 / 3 = 3.3333333333333335

# Integer division results in float
print(f"10 / 2 = {10 / 2}")  # 10 / 2 = 5.0 (float, not int)

# Division by zero raises error
# print(10 / 0)  # ZeroDivisionError

# Float division
x = 7.5
y = 2.5
print(f"{x} / {y} = {x / y}")  # 7.5 / 2.5 = 3.0

# Complex division
c1 = 4 + 2j
c2 = 1 + 1j
print(f"{c1} / {c2} = {c1 / c2}")  # (3-1j)
```

### Floor Division (//)
```python
# Floor division (rounds down to nearest integer)
print(f"10 // 3 = {10 // 3}")    # 3
print(f"10 // 4 = {10 // 4}")    # 2
print(f"10 // 5 = {10 // 5}")    # 2

# With negative numbers (rounds toward negative infinity)
print(f"-10 // 3 = {-10 // 3}")   # -4 (not -3!)
print(f"10 // -3 = {10 // -3}")   # -4
print(f"-10 // -3 = {-10 // -3}") # 3

# Float floor division
print(f"10.5 // 3 = {10.5 // 3}")    # 3.0
print(f"10.5 // 3.2 = {10.5 // 3.2}") # 3.0
print(f"-10.5 // 3 = {-10.5 // 3}")   # -4.0
```

### Modulo (%)
```python
# Remainder after division
print(f"10 % 3 = {10 % 3}")    # 1
print(f"10 % 4 = {10 % 4}")    # 2
print(f"10 % 5 = {10 % 5}")    # 0

# With negative numbers
print(f"-10 % 3 = {-10 % 3}")   # 2 (not -1!)
print(f"10 % -3 = {10 % -3}")   # -2
print(f"-10 % -3 = {-10 % -3}") # -1

# Float modulo
print(f"10.5 % 3 = {10.5 % 3}")     # 1.5
print(f"10.5 % 3.2 = {10.5 % 3.2}") # 0.9

# Check even/odd
num = 7
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")  # 7 is odd

# Check divisibility
if num % 5 == 0:
    print(f"{num} is divisible by 5")
```

### Exponentiation (**)
```python
# Power operator
print(f"2 ** 3 = {2 ** 3}")     # 8
print(f"10 ** 2 = {10 ** 2}")   # 100
print(f"5 ** 4 = {5 ** 4}")     # 625

# With floats
print(f"4 ** 0.5 = {4 ** 0.5}")  # 2.0 (square root)
print(f"8 ** (1/3) = {8 ** (1/3)}")  # 2.0 (cube root)

# Negative exponents
print(f"2 ** -2 = {2 ** -2}")    # 0.25
print(f"10 ** -1 = {10 ** -1}")  # 0.1

# Large exponents
print(f"2 ** 10 = {2 ** 10}")    # 1024
print(f"2 ** 20 = {2 ** 20}")    # 1048576
print(f"2 ** 100 = {2 ** 100}")  # Very large number

# Complex exponents
c = 2 + 1j
print(f"(2+1j) ** 2 = {c ** 2}")  # (3+4j)
```

## Operator Precedence

```python
# Precedence rules (highest to lowest):
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Unary +, -
# 4. Multiplication *, Division /, Floor //, Modulo %
# 5. Addition +, Subtraction -

# Examples
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}")  # 14 (multiplication first)

result = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result}")  # 20 (parentheses first)

result = 2 ** 3 * 4
print(f"2 ** 3 * 4 = {result}")  # 32 (exponentiation first)

result = 2 ** (3 * 4)
print(f"2 ** (3 * 4) = {result}")  # 4096

# Complex precedence
result = 10 + 2 * 3 ** 2
print(f"10 + 2 * 3 ** 2 = {result}")  # 28 (3**2=9, 2*9=18, 10+18=28)

# Using parentheses for clarity
result = 10 + (2 * (3 ** 2))
print(f"10 + (2 * (3 ** 2)) = {result}")  # 28 (same but clearer)
```

## Compound Assignment Operators

```python
# += (Addition assignment)
x = 10
x += 5  # x = x + 5
print(f"x += 5 → x = {x}")  # 15

# -= (Subtraction assignment)
x = 10
x -= 3  # x = x - 3
print(f"x -= 3 → x = {x}")  # 7

# *= (Multiplication assignment)
x = 10
x *= 2  # x = x * 2
print(f"x *= 2 → x = {x}")  # 20

# /= (Division assignment)
x = 10
x /= 3  # x = x / 3
print(f"x /= 3 → x = {x}")  # 3.3333333333333335

# //= (Floor division assignment)
x = 10
x //= 3  # x = x // 3
print(f"x //= 3 → x = {x}")  # 3

# %= (Modulo assignment)
x = 10
x %= 3  # x = x % 3
print(f"x %= 3 → x = {x}")  # 1

# **= (Exponentiation assignment)
x = 2
x **= 3  # x = x ** 3
print(f"x **= 3 → x = {x}")  # 8

# Multiple operations
x = 5
x += 3 * 2  # x = x + (3 * 2)
print(f"x += 3 * 2 → x = {x}")  # 11
```

## Unary Operators

```python
# Unary plus (+)
x = 5
print(f"+x = {+x}")  # 5

# Unary minus (-)
x = 5
print(f"-x = {-x}")  # -5

x = -5
print(f"-x = {-x}")  # 5

# With expressions
x = 3
y = -x ** 2
print(f"-x ** 2 = {y}")  # -9 (exponent before unary minus)

y = (-x) ** 2
print(f"(-x) ** 2 = {y}")  # 9
```

## Practical Examples

### Example 1: Basic Calculator
```python
class Calculator:
    """Simple calculator with arithmetic operations"""
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    @staticmethod
    def floor_divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a // b
    
    @staticmethod
    def modulo(a, b):
        if b == 0:
            raise ValueError("Cannot modulo by zero")
        return a % b
    
    @staticmethod
    def power(a, b):
        return a ** b
    
    def calculate(self, a, b, operation):
        """Perform calculation based on operation string"""
        operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide,
            '//': self.floor_divide,
            '%': self.modulo,
            '**': self.power
        }
        
        if operation not in operations:
            raise ValueError(f"Unknown operation: {operation}")
        
        return operations[operation](a, b)

# Demo
calc = Calculator()

print("=== Calculator Demo ===")
print(f"10 + 3 = {calc.calculate(10, 3, '+')}")
print(f"10 - 3 = {calc.calculate(10, 3, '-')}")
print(f"10 * 3 = {calc.calculate(10, 3, '*')}")
print(f"10 / 3 = {calc.calculate(10, 3, '/')}")
print(f"10 // 3 = {calc.calculate(10, 3, '//')}")
print(f"10 % 3 = {calc.calculate(10, 3, '%')}")
print(f"10 ** 3 = {calc.calculate(10, 3, '**')}")
```

### Example 2: Financial Calculations
```python
class FinancialCalculator:
    """Financial calculations using arithmetic operators"""
    
    @staticmethod
    def compound_interest(principal, rate, years, compounds_per_year=12):
        """Calculate compound interest"""
        # A = P(1 + r/n)^(nt)
        rate_per_period = rate / 100 / compounds_per_year
        periods = compounds_per_year * years
        amount = principal * (1 + rate_per_period) ** periods
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
    
    @staticmethod
    def roi(initial_investment, final_value):
        """Calculate Return on Investment (ROI)"""
        if initial_investment == 0:
            return float('inf')
        return ((final_value - initial_investment) / initial_investment) * 100

# Demo
finance = FinancialCalculator()

print("=== Financial Calculator ===")
print("-" * 40)

# Compound interest
principal = 10000
rate = 5
years = 10
amount, interest = finance.compound_interest(principal, rate, years)
print(f"Compound Interest:")
print(f"  Principal: ${principal:,.2f}")
print(f"  Rate: {rate}%")
print(f"  Years: {years}")
print(f"  Final amount: ${amount:,.2f}")
print(f"  Interest earned: ${interest:,.2f}")

# Loan payment
loan_amount = 200000
annual_rate = 4.5
loan_years = 30
payment, total_paid, total_interest = finance.loan_payment(loan_amount, annual_rate, loan_years)
print(f"\nLoan Payment:")
print(f"  Loan amount: ${loan_amount:,.2f}")
print(f"  Monthly payment: ${payment:,.2f}")
print(f"  Total paid: ${total_paid:,.2f}")
print(f"  Total interest: ${total_interest:,.2f}")

# Investment growth
initial = 5000
monthly = 500
return_rate = 8
invest_years = 20
total, contributions, gain = finance.investment_growth(initial, monthly, return_rate, invest_years)
print(f"\nInvestment Growth:")
print(f"  Initial: ${initial:,.2f}")
print(f"  Monthly: ${monthly:,.2f}")
print(f"  Total contributions: ${contributions:,.2f}")
print(f"  Final value: ${total:,.2f}")
print(f"  Total gain: ${gain:,.2f}")
print(f"  ROI: {finance.roi(contributions, total):.1f}%")
```

### Example 3: Geometry Calculator
```python
import math

class GeometryCalculator:
    """Geometry calculations using arithmetic operators"""
    
    @staticmethod
    def circle_area(radius):
        """Calculate area of circle: πr²"""
        return math.pi * radius ** 2
    
    @staticmethod
    def circle_circumference(radius):
        """Calculate circumference: 2πr"""
        return 2 * math.pi * radius
    
    @staticmethod
    def rectangle_area(length, width):
        """Calculate area of rectangle: l × w"""
        return length * width
    
    @staticmethod
    def rectangle_perimeter(length, width):
        """Calculate perimeter: 2(l + w)"""
        return 2 * (length + width)
    
    @staticmethod
    def triangle_area(base, height):
        """Calculate area of triangle: ½ × base × height"""
        return (base * height) / 2
    
    @staticmethod
    def triangle_perimeter(side1, side2, side3):
        """Calculate perimeter: a + b + c"""
        return side1 + side2 + side3
    
    @staticmethod
    def sphere_volume(radius):
        """Calculate sphere volume: ⁴⁄₃πr³"""
        return (4/3) * math.pi * radius ** 3
    
    @staticmethod
    def sphere_surface_area(radius):
        """Calculate sphere surface area: 4πr²"""
        return 4 * math.pi * radius ** 2
    
    @staticmethod
    def cylinder_volume(radius, height):
        """Calculate cylinder volume: πr²h"""
        return math.pi * radius ** 2 * height
    
    @staticmethod
    def pythagorean_theorem(a, b):
        """Calculate hypotenuse: √(a² + b²)"""
        return math.sqrt(a ** 2 + b ** 2)
    
    @staticmethod
    def distance_2d(x1, y1, x2, y2):
        """Calculate distance between two points: √((x2-x1)² + (y2-y1)²)"""
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Demo
geo = GeometryCalculator()

print("=== Geometry Calculator ===")
print("-" * 40)

# Circle
radius = 5
print(f"Circle (r={radius}):")
print(f"  Area: {geo.circle_area(radius):.2f}")
print(f"  Circumference: {geo.circle_circumference(radius):.2f}")

# Rectangle
length, width = 10, 6
print(f"\nRectangle ({length}×{width}):")
print(f"  Area: {geo.rectangle_area(length, width)}")
print(f"  Perimeter: {geo.rectangle_perimeter(length, width)}")

# Triangle
base, height = 8, 5
print(f"\nTriangle (base={base}, height={height}):")
print(f"  Area: {geo.triangle_area(base, height)}")

# 3D shapes
radius = 3
print(f"\nSphere (r={radius}):")
print(f"  Volume: {geo.sphere_volume(radius):.2f}")
print(f"  Surface area: {geo.sphere_surface_area(radius):.2f}")

# Pythagorean theorem
a, b = 3, 4
print(f"\nPythagorean Theorem ({a}, {b}):")
print(f"  Hypotenuse: {geo.pythagorean_theorem(a, b)}")

# Distance
x1, y1, x2, y2 = 0, 0, 3, 4
print(f"\nDistance between ({x1},{y1}) and ({x2},{y2}):")
print(f"  Distance: {geo.distance_2d(x1, y1, x2, y2)}")
```

### Example 4: Statistics Calculator
```python
class StatisticsCalculator:
    """Statistical calculations using arithmetic operators"""
    
    @staticmethod
    def mean(numbers):
        """Calculate mean: sum(numbers) / n"""
        if not numbers:
            return None
        return sum(numbers) / len(numbers)
    
    @staticmethod
    def median(numbers):
        """Calculate median (middle value)"""
        if not numbers:
            return None
        
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        mid = n // 2
        
        if n % 2 == 0:
            # Even number of elements
            return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
        else:
            # Odd number of elements
            return sorted_numbers[mid]
    
    @staticmethod
    def mode(numbers):
        """Calculate mode (most frequent value)"""
        if not numbers:
            return None
        
        frequency = {}
        for num in numbers:
            frequency[num] = frequency.get(num, 0) + 1
        
        max_freq = max(frequency.values())
        modes = [num for num, freq in frequency.items() if freq == max_freq]
        
        return modes if len(modes) > 1 else modes[0]
    
    @staticmethod
    def variance(numbers, sample=True):
        """Calculate variance"""
        if len(numbers) < 2:
            return None
        
        mean_val = StatisticsCalculator.mean(numbers)
        squared_diffs = [(x - mean_val) ** 2 for x in numbers]
        
        if sample:
            return sum(squared_diffs) / (len(numbers) - 1)
        else:
            return sum(squared_diffs) / len(numbers)
    
    @staticmethod
    def std_dev(numbers, sample=True):
        """Calculate standard deviation"""
        variance = StatisticsCalculator.variance(numbers, sample)
        if variance is None:
            return None
        return variance ** 0.5  # Square root
    
    @staticmethod
    def range(numbers):
        """Calculate range: max - min"""
        if not numbers:
            return None
        return max(numbers) - min(numbers)
    
    @staticmethod
    def sum_of_squares(numbers):
        """Calculate sum of squares: Σ(x²)"""
        return sum(x ** 2 for x in numbers)
    
    @staticmethod
    def z_score(value, mean, std_dev):
        """Calculate z-score: (x - μ) / σ"""
        if std_dev == 0:
            return None
        return (value - mean) / std_dev

# Demo
stats = StatisticsCalculator()

# Sample data
data = [12, 15, 14, 10, 12, 18, 16, 14, 12, 15]

print("=== Statistics Calculator ===")
print(f"Data: {data}")
print("-" * 40)

print(f"Mean: {stats.mean(data):.2f}")
print(f"Median: {stats.median(data)}")
print(f"Mode: {stats.mode(data)}")
print(f"Range: {stats.range(data)}")
print(f"Variance (sample): {stats.variance(data):.2f}")
print(f"Std Dev (sample): {stats.std_dev(data):.2f}")
print(f"Sum of squares: {stats.sum_of_squares(data)}")

# Z-scores
mean_val = stats.mean(data)
std_val = stats.std_dev(data)
print(f"\nZ-scores:")
for value in data[:5]:  # First 5 values
    z = stats.z_score(value, mean_val, std_val)
    print(f"  {value} → {z:.2f}")

# Additional statistics
print(f"\nAdditional Calculations:")
print(f"Sum: {sum(data)}")
print(f"Min: {min(data)}")
print(f"Max: {max(data)}")
print(f"Count: {len(data)}")
```

### Example 5: Unit Converter
```python
class UnitConverter:
    """Unit conversion using arithmetic operators"""
    
    # Length conversions
    @staticmethod
    def km_to_miles(km):
        return km * 0.621371
    
    @staticmethod
    def miles_to_km(miles):
        return miles * 1.60934
    
    @staticmethod
    def meters_to_feet(meters):
        return meters * 3.28084
    
    @staticmethod
    def feet_to_meters(feet):
        return feet * 0.3048
    
    @staticmethod
    def cm_to_inches(cm):
        return cm * 0.393701
    
    @staticmethod
    def inches_to_cm(inches):
        return inches * 2.54
    
    # Temperature conversions
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15
    
    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15
    
    # Weight conversions
    @staticmethod
    def kg_to_pounds(kg):
        return kg * 2.20462
    
    @staticmethod
    def pounds_to_kg(pounds):
        return pounds * 0.453592
    
    @staticmethod
    def grams_to_ounces(grams):
        return grams * 0.035274
    
    @staticmethod
    def ounces_to_grams(ounces):
        return ounces * 28.3495
    
    # Area conversions
    @staticmethod
    def sq_meters_to_sq_feet(sq_meters):
        return sq_meters * 10.7639
    
    @staticmethod
    def sq_feet_to_sq_meters(sq_feet):
        return sq_feet * 0.092903
    
    # Volume conversions
    @staticmethod
    def liters_to_gallons(liters):
        return liters * 0.264172
    
    @staticmethod
    def gallons_to_liters(gallons):
        return gallons * 3.78541
    
    # Speed conversions
    @staticmethod
    def kmh_to_mph(kmh):
        return kmh * 0.621371
    
    @staticmethod
    def mph_to_kmh(mph):
        return mph * 1.60934

# Demo
converter = UnitConverter()

print("=== Unit Converter Demo ===")
print("-" * 40)

# Length
km = 10
print(f"Length:")
print(f"  {km} km = {converter.km_to_miles(km):.2f} miles")
print(f"  {km} miles = {converter.miles_to_km(km):.2f} km")

# Temperature
celsius = 25
print(f"\nTemperature:")
print(f"  {celsius}°C = {converter.celsius_to_fahrenheit(celsius):.1f}°F")
print(f"  {celsius}°C = {converter.celsius_to_kelvin(celsius):.2f}K")

fahrenheit = 77
print(f"  {fahrenheit}°F = {converter.fahrenheit_to_celsius(fahrenheit):.1f}°C")

# Weight
kg = 70
print(f"\nWeight:")
print(f"  {kg} kg = {converter.kg_to_pounds(kg):.2f} lbs")
print(f"  {kg} lbs = {converter.pounds_to_kg(kg):.2f} kg")

# Area
sq_m = 100
print(f"\nArea:")
print(f"  {sq_m} m² = {converter.sq_meters_to_sq_feet(sq_m):.2f} ft²")

# Volume
liters = 5
print(f"\nVolume:")
print(f"  {liters} L = {converter.liters_to_gallons(liters):.2f} gallons")

# Speed
kmh = 100
print(f"\nSpeed:")
print(f"  {kmh} km/h = {converter.kmh_to_mph(kmh):.2f} mph")
```

### Example 6: Complex Number Operations
```python
class ComplexMath:
    """Complex number operations using arithmetic operators"""
    
    @staticmethod
    def add(z1, z2):
        """Add two complex numbers"""
        return z1 + z2
    
    @staticmethod
    def subtract(z1, z2):
        """Subtract two complex numbers"""
        return z1 - z2
    
    @staticmethod
    def multiply(z1, z2):
        """Multiply two complex numbers"""
        return z1 * z2
    
    @staticmethod
    def divide(z1, z2):
        """Divide two complex numbers"""
        if z2 == 0:
            raise ValueError("Cannot divide by zero")
        return z1 / z2
    
    @staticmethod
    def power(z, n):
        """Raise complex number to integer power"""
        return z ** n
    
    @staticmethod
    def magnitude(z):
        """Calculate magnitude (absolute value)"""
        return abs(z)
    
    @staticmethod
    def conjugate(z):
        """Return complex conjugate"""
        return z.conjugate()
    
    @staticmethod
    def real_part(z):
        """Extract real part"""
        return z.real
    
    @staticmethod
    def imag_part(z):
        """Extract imaginary part"""
        return z.imag
    
    @staticmethod
    def polar_to_rectangular(r, theta):
        """Convert polar coordinates to rectangular"""
        import math
        return complex(r * math.cos(theta), r * math.sin(theta))
    
    @staticmethod
    def quadratic_roots(a, b, c):
        """Solve quadratic equation: ax² + bx + c = 0"""
        import math
        
        # Calculate discriminant
        d = b ** 2 - 4 * a * c
        
        if d >= 0:
            # Real roots
            root1 = (-b + math.sqrt(d)) / (2 * a)
            root2 = (-b - math.sqrt(d)) / (2 * a)
            return root1, root2
        else:
            # Complex roots
            real_part = -b / (2 * a)
            imag_part = math.sqrt(-d) / (2 * a)
            root1 = complex(real_part, imag_part)
            root2 = complex(real_part, -imag_part)
            return root1, root2

# Demo
cm = ComplexMath()

print("=== Complex Number Operations ===")
print("-" * 40)

# Create complex numbers
z1 = 3 + 4j
z2 = 1 - 2j

print(f"z1 = {z1}")
print(f"z2 = {z2}")
print(f"z1 + z2 = {cm.add(z1, z2)}")
print(f"z1 - z2 = {cm.subtract(z1, z2)}")
print(f"z1 * z2 = {cm.multiply(z1, z2)}")
print(f"z1 / z2 = {cm.divide(z1, z2):.2f}")
print(f"z1 ** 2 = {cm.power(z1, 2)}")

print(f"\nProperties of {z1}:")
print(f"  Magnitude: {cm.magnitude(z1):.2f}")
print(f"  Conjugate: {cm.conjugate(z1)}")
print(f"  Real part: {cm.real_part(z1)}")
print(f"  Imag part: {cm.imag_part(z1)}")

# Polar to rectangular
import math
r = 5
theta = math.radians(53.13)
z3 = cm.polar_to_rectangular(r, theta)
print(f"\nPolar ({r:.1f}∠{math.degrees(theta):.1f}°) = Rectangular {z3:.2f}")

# Quadratic equation
print(f"\nQuadratic Equation Solver:")
a, b, c = 1, -5, 6
roots = cm.quadratic_roots(a, b, c)
print(f"  {a}x² + {b}x + {c} = 0")
print(f"  Roots: {roots[0]}, {roots[1]}")

a, b, c = 1, 2, 5
roots = cm.quadratic_roots(a, b, c)
print(f"\n  {a}x² + {b}x + {c} = 0")
print(f"  Roots: {roots[0]:.2f}, {roots[1]:.2f}")
```

## Operator Overloading

```python
class Vector:
    """2D vector with operator overloading"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Vector addition: + operator"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        """Vector subtraction: - operator"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        """Scalar multiplication: * operator"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __rmul__(self, scalar):
        """Right scalar multiplication"""
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        """Scalar division: / operator"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x / scalar, self.y / scalar)
        return NotImplemented
    
    def __neg__(self):
        """Unary negation: - operator"""
        return Vector(-self.x, -self.y)
    
    def __abs__(self):
        """Magnitude: abs() function"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Demo operator overloading
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print("=== Operator Overloading Demo ===")
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"2 * v1 = {2 * v1}")
print(f"v1 / 2 = {v1 / 2}")
print(f"-v1 = {-v1}")
print(f"|v1| = {abs(v1):.2f}")
```

## Common Mistakes

### Mistake 1: Integer Division Confusion
```python
# Wrong - expecting integer result
result = 10 / 3
print(result)  # 3.3333333333333335 (float)

# Right - use // for integer division
result = 10 // 3
print(result)  # 3
```

### Mistake 2: Modulo with Negative Numbers
```python
# Wrong - expecting positive remainder
result = -10 % 3
print(result)  # 2 (not -1!)

# Right - understand behavior
# Python: a % b = a - (a // b) * b
print(-10 // 3)  # -4
print(-10 - (-4 * 3))  # 2

# For positive remainder, use:
def positive_modulo(a, b):
    return ((a % b) + b) % b

print(positive_modulo(-10, 3))  # 2 (still)
```

### Mistake 3: Floating-Point Precision
```python
# Wrong - expecting exact result
result = 0.1 + 0.2
print(result == 0.3)  # False!

# Right - use tolerance
tolerance = 1e-10
print(abs(result - 0.3) < tolerance)  # True

# Or use Decimal
from decimal import Decimal
result = Decimal('0.1') + Decimal('0.2')
print(result == Decimal('0.3'))  # True
```

### Mistake 4: Division by Zero
```python
# Wrong - crashes
# result = 10 / 0  # ZeroDivisionError

# Right - check first
def safe_divide(a, b):
    if b == 0:
        return None
    return a / b

result = safe_divide(10, 0)
if result is None:
    print("Cannot divide by zero")
```

### Mistake 5: Operator Precedence
```python
# Wrong - incorrect order
result = 10 + 5 * 2
print(result)  # 20 (not 30)

# Right - use parentheses
result = (10 + 5) * 2
print(result)  # 30
```

## Performance Considerations

```python
import time

# Integer vs float operations
iterations = 10_000_000

# Integer addition
start = time.time()
x = 0
for i in range(iterations):
    x += 1
int_time = time.time() - start

# Float addition
start = time.time()
y = 0.0
for i in range(iterations):
    y += 1.0
float_time = time.time() - start

print(f"Integer addition: {int_time:.3f}s")
print(f"Float addition: {float_time:.3f}s")

# Exponentiation methods
x = 2
y = 10

# Using ** operator
start = time.time()
for i in range(iterations):
    result = x ** y
pow_time = time.time() - start

# Using pow() function
start = time.time()
for i in range(iterations):
    result = pow(x, y)
pow_func_time = time.time() - start

print(f"x ** y: {pow_time:.3f}s")
print(f"pow(x, y): {pow_func_time:.3f}s")
```

## Quick Reference Table

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3.333...` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulo | `10 % 3` | `1` |
| `**` | Exponentiation | `10 ** 3` | `1000` |
| `+=` | Add and assign | `x += 3` | `x = x + 3` |
| `-=` | Subtract and assign | `x -= 3` | `x = x - 3` |
| `*=` | Multiply and assign | `x *= 3` | `x = x * 3` |
| `/=` | Divide and assign | `x /= 3` | `x = x / 3` |
| `//=` | Floor divide and assign | `x //= 3` | `x = x // 3` |
| `%=` | Modulo and assign | `x %= 3` | `x = x % 3` |
| `**=` | Power and assign | `x **= 3` | `x = x ** 3` |

## Summary

- **Addition (+)** - Adds numbers, concatenates strings/lists
- **Subtraction (-)** - Subtracts numbers
- **Multiplication (*)** - Multiplies numbers, repeats sequences
- **Division (/)** - Always returns float
- **Floor Division (//)** - Integer division (rounds down)
- **Modulo (%)** - Returns remainder
- **Exponentiation (**)** - Raises to power
- **Compound assignments** - Combine operation with assignment
- **Operator precedence** - PEMDAS rules (use parentheses)
- **Division by zero** - Raises ZeroDivisionError
- **Floating-point precision** - Be careful with comparisons
- **Operator overloading** - Custom behavior for user classes

## Basic Template
```python
#!/usr/bin/env python3

def arithmetic_demo():
    """Demonstrate basic arithmetic operators"""
    
    a = 10
    b = 3
    
    print(f"a = {a}, b = {b}")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")
    print(f"a // b = {a // b}")
    print(f"a % b = {a % b}")
    print(f"a ** b = {a ** b}")

def compound_assignments():
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
    
    x **= 3
    print(f"x **= 3 → {x}")

def precedence_demo():
    """Demonstrate operator precedence"""
    
    print("Without parentheses:")
    print(f"  2 + 3 * 4 = {2 + 3 * 4}")
    print(f"  10 - 3 * 2 = {10 - 3 * 2}")
    print(f"  2 ** 3 * 2 = {2 ** 3 * 2}")
    
    print("\nWith parentheses:")
    print(f"  (2 + 3) * 4 = {(2 + 3) * 4}")
    print(f"  10 - (3 * 2) = {10 - (3 * 2)}")
    print(f"  2 ** (3 * 2) = {2 ** (3 * 2)}")

def practical_math():
    """Practical mathematical calculations"""
    
    # Calculate circle area
    radius = 5
    area = 3.14159 * radius ** 2
    print(f"\nCircle area (r={radius}): {area:.2f}")
    
    # Calculate average
    scores = [85, 90, 78, 92, 88]
    average = sum(scores) / len(scores)
    print(f"Average score: {average:.1f}")
    
    # Check if number is even
    num = 7
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
    
    # Calculate percentage
    part = 45
    whole = 200
    percentage = (part / whole) * 100
    print(f"{part} is {percentage:.1f}% of {whole}")

if __name__ == "__main__":
    print("=== ARITHMETIC OPERATORS ===\n")
    arithmetic_demo()
    
    print("\n=== COMPOUND ASSIGNMENTS ===\n")
    compound_assignments()
    
    print("\n=== OPERATOR PRECEDENCE ===\n")
    precedence_demo()
    
    print("\n=== PRACTICAL MATH ===\n")
    practical_math()
```

*This documentation belongs to https://github.com/InterCentury*