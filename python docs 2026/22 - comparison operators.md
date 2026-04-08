# 22 - Comparison Operators in Python

## What are Comparison Operators?
Comparison operators (also called relational operators) are used to compare values. They return Boolean values (`True` or `False`) based on the comparison result. These operators are fundamental for decision-making in conditional statements and loops.

## Basic Comparison Operators

### Equal to (==)
```python
# Numeric comparison
print(5 == 5)      # True
print(5 == 3)      # False
print(5.0 == 5)    # True (float vs int)

# String comparison (case-sensitive)
print("hello" == "hello")    # True
print("Hello" == "hello")    # False
print("HELLO" == "hello")    # False

# Boolean comparison
print(True == True)   # True
print(True == False)  # False
print(1 == True)      # True (bool is subclass of int)
print(0 == False)     # True

# List comparison
print([1, 2, 3] == [1, 2, 3])  # True
print([1, 2, 3] == [1, 3, 2])  # False (order matters)

# Dictionary comparison
print({"a": 1, "b": 2} == {"a": 1, "b": 2})  # True
print({"a": 1, "b": 2} == {"b": 2, "a": 1})  # True (order doesn't matter)

# None comparison
print(None == None)   # True
print(None == False)  # False

# Custom objects
class Person:
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name
        return False

p1 = Person("Alice")
p2 = Person("Alice")
p3 = Person("Bob")
print(p1 == p2)  # True (if __eq__ defined)
print(p1 == p3)  # False
```

### Not Equal to (!=)
```python
# Numeric comparison
print(5 != 3)      # True
print(5 != 5)      # False
print(5.0 != 5)    # False

# String comparison
print("hello" != "world")  # True
print("hello" != "hello")  # False

# Boolean comparison
print(True != False)  # True
print(True != True)   # False

# List comparison
print([1, 2] != [1, 3])  # True
print([1, 2] != [1, 2])  # False

# With None
value = None
print(value != None)  # False
print(value != 10)    # True
```

### Greater Than (>)
```python
# Numeric comparison
print(10 > 5)     # True
print(5 > 10)     # False
print(5 > 5)      # False
print(10.5 > 10)  # True

# String comparison (lexicographical order)
print("banana" > "apple")    # True (b > a)
print("apple" > "banana")    # False
print("cat" > "cat")         # False
print("car" > "cat")         # False (r < t)

# String length doesn't matter for comparison
print("a" > "zzzz")   # False ('a' < 'z')

# List comparison (element-wise)
print([1, 2, 3] > [1, 2, 2])   # True (3 > 2)
print([1, 2, 3] > [1, 2, 3])   # False (equal)
print([1, 2, 3] > [1, 2, 4])   # False (3 < 4)

# Tuple comparison
print((1, 2) > (0, 100))  # True (1 > 0)

# Cannot compare different types
# print(10 > "5")  # TypeError in Python 3
```

### Less Than (<)
```python
# Numeric comparison
print(5 < 10)     # True
print(10 < 5)     # False
print(5 < 5)      # False
print(10 < 10.5)  # True

# String comparison
print("apple" < "banana")   # True
print("banana" < "apple")   # False
print("cat" < "cat")        # False

# List comparison
print([1, 2, 2] < [1, 2, 3])   # True
print([1, 2, 3] < [1, 2, 2])   # False

# Mixed types (Python 2 vs Python 3)
# Python 3: comparing different types raises TypeError
# print(5 < "10")  # TypeError!

# But booleans compare with numbers
print(True < 2)   # True (True is 1)
print(False < 1)  # True (False is 0)
```

### Greater Than or Equal To (>=)
```python
# Numeric comparison
print(10 >= 5)     # True
print(5 >= 10)     # False
print(5 >= 5)      # True
print(10 >= 10.0)  # True

# String comparison
print("banana" >= "apple")   # True
print("apple" >= "banana")   # False
print("cat" >= "cat")        # True

# List comparison
print([1, 2, 3] >= [1, 2, 2])   # True
print([1, 2, 3] >= [1, 2, 3])   # True
print([1, 2, 2] >= [1, 2, 3])   # False

# With different types (Python 3 raises TypeError)
# print(10 >= "5")  # TypeError!
```

### Less Than or Equal To (<=)
```python
# Numeric comparison
print(5 <= 10)     # True
print(10 <= 5)     # False
print(5 <= 5)      # True
print(10 <= 10.0)  # True

# String comparison
print("apple" <= "banana")   # True
print("banana" <= "apple")   # False
print("cat" <= "cat")        # True

# List comparison
print([1, 2, 2] <= [1, 2, 3])   # True
print([1, 2, 3] <= [1, 2, 3])   # True
print([1, 2, 4] <= [1, 2, 3])   # False

# Chained comparisons
x = 5
print(0 <= x <= 10)   # True (0 <= 5 and 5 <= 10)
```

## Chained Comparisons

```python
# Python allows chaining comparison operators
x = 5

# Equivalent to: (1 < x) and (x < 10)
print(1 < x < 10)     # True

# Equivalent to: (x > 1) and (x < 10)
print(10 > x > 1)     # True

# Multiple chaining
print(1 < x < 10 < 20)  # True (1<5 and 5<10 and 10<20)

# With different operators
print(1 <= x <= 10)   # True
print(1 <= x < 10)    # True

# Chained comparisons with strings
word = "python"
print("a" < word < "z")  # True (lexicographical)

# Chained comparisons evaluate left to right
# But only evaluate each expression once
x = 5
print(1 < x < 10)  # x is evaluated once

# Equivalent to:
# temp = x
# 1 < temp and temp < 10

# Complex chaining
a, b, c, d = 10, 20, 30, 40
print(a < b < c < d)   # True
print(a < b > c < d)   # False (20 > 30 is False)
```

## Comparison of Different Types

### Numeric Types
```python
# int vs float
print(5 == 5.0)      # True
print(5 > 5.0)       # False
print(5 >= 5.0)      # True

# int vs complex (can compare equality only)
print(5 == 5+0j)     # True
# print(5 > 5+0j)    # TypeError!

# bool with numbers
print(True == 1)     # True
print(False == 0)    # True
print(True > 0)      # True
print(False < 1)     # True
```

### String Comparisons
```python
# Lexicographic (dictionary) order
print("apple" < "banana")     # True
print("Apple" < "apple")      # True (ASCII: A=65, a=97)
print("10" < "2")             # True (character comparison: '1' < '2')
print("abc" < "abcd")         # True (shorter string is smaller)

# Case sensitivity
print("Python" == "python")   # False
print("Python".lower() == "python".lower())  # True (case-insensitive)

# String vs number (TypeError in Python 3)
# print("5" == 5)   # False (no automatic conversion)
# print("5" > 5)    # TypeError!

# Solution: convert types
print(int("5") == 5)    # True
print("5" == str(5))    # True
```

### Sequence Comparisons
```python
# Lists compare element-wise
list1 = [1, 2, 3]
list2 = [1, 2, 4]
list3 = [1, 2, 3, 4]

print(list1 == list2)     # False
print(list1 < list2)      # True (3 < 4)
print(list1 < list3)      # True (list1 is prefix of list3)

# Tuples compare similarly
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
print(tuple1 < tuple2)    # True

# Mixed sequence types
print([1, 2] == (1, 2))   # False (different types)
# print([1, 2] < (1, 3))  # TypeError in Python 3

# Strings vs lists
print("abc" == ["a", "b", "c"])  # False (different types)
```

### Dictionary Comparisons
```python
# Dictionaries compare by key-value pairs (order doesn't matter)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}
dict3 = {"a": 1, "b": 3}

print(dict1 == dict2)     # True
print(dict1 == dict3)     # False

# Cannot use <, >, <=, >= with dictionaries
# print(dict1 < dict2)    # TypeError!

# Comparing with other types
print(dict1 == [("a", 1), ("b", 2)])  # False (different types)
```

### Set Comparisons
```python
set1 = {1, 2, 3}
set2 = {3, 2, 1}
set3 = {1, 2, 3, 4}

print(set1 == set2)       # True (order doesn't matter)
print(set1 != set3)       # True

# Subset and superset operators
print(set1 < set3)        # True (proper subset)
print(set1 <= set2)       # True (subset)
print(set3 > set1)        # True (proper superset)
print(set3 >= set2)       # True (superset)

# Not comparable with other types
# print(set1 < list1)     # TypeError!
```

### None Comparisons
```python
# Always use 'is' for None comparison (not ==)
value = None

# Recommended
if value is None:
    print("Value is None")

if value is not None:
    print("Value is not None")

# Works but not recommended
if value == None:
    print("Works but avoid")

# Why 'is' is better (avoids __eq__ override issues)
class BadClass:
    def __eq__(self, other):
        return True

obj = BadClass()
print(obj == None)    # True (wrong!)
print(obj is None)    # False (correct)
```

## Identity Comparison (is, is not)

```python
# 'is' compares identity (memory address)
# '==' compares value

# Small integers are cached (-5 to 256)
x = 256
y = 256
print(x is y)      # True (same object)

x = 257
y = 257
print(x is y)      # May be False (implementation dependent)

# Strings may be interned
s1 = "hello"
s2 = "hello"
print(s1 is s2)    # Often True (interned)

# But not always
s1 = "hello world"
s2 = "hello world"
print(s1 is s2)    # May be False

# For mutable objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)   # True (same values)
print(list1 is list2)   # False (different objects)

list3 = list1
print(list1 is list3)   # True (same object)

# None is a singleton
a = None
b = None
print(a is b)      # True
print(a is None)   # True

# Use 'is' for None, True, False
value = True
if value is True:    # OK, but 'if value:' is better
    pass

# Use 'is not' for negative identity
if value is not None:
    pass
```

## Comparison with Boolean Values

```python
# Direct boolean comparison
flag = True

# Not recommended (redundant)
if flag == True:
    print("Flag is True")

# Recommended (Pythonic)
if flag:
    print("Flag is True")

if not flag:
    print("Flag is False")

# Comparing with False
if flag is False:  # Works but not recommended
    pass

if not flag:       # Recommended
    pass

# Truthy/Falsy values
if 0:           # False
if 1:           # True
if "":          # False
if "text":      # True
if []:          # False
if [1, 2]:      # True
if None:        # False

# Explicit boolean conversion
if bool(value):
    pass
```

## Practical Examples

### Example 1: Age Group Classifier
```python
class AgeClassifier:
    """Classify people by age using comparison operators"""
    
    @staticmethod
    def classify(age):
        """Classify age into groups"""
        if age < 0:
            return "Invalid age"
        elif age < 13:
            return "Child"
        elif age < 20:
            return "Teenager"
        elif age < 65:
            return "Adult"
        else:
            return "Senior"
    
    @staticmethod
    def can_vote(age):
        """Check voting eligibility"""
        return age >= 18
    
    @staticmethod
    def can_drink(age, country="US"):
        """Check drinking age by country"""
        drinking_ages = {"US": 21, "UK": 18, "JP": 20}
        return age >= drinking_ages.get(country, 21)
    
    @staticmethod
    def get_life_stage(age):
        """Get detailed life stage"""
        if 0 <= age < 2:
            return "Infant"
        elif 2 <= age < 6:
            return "Early Childhood"
        elif 6 <= age < 13:
            return "Middle Childhood"
        elif 13 <= age < 18:
            return "Adolescence"
        elif 18 <= age < 40:
            return "Early Adulthood"
        elif 40 <= age < 65:
            return "Middle Adulthood"
        elif age >= 65:
            return "Late Adulthood"
        else:
            return "Unborn"

# Demo
classifier = AgeClassifier()

print("=== Age Classification Demo ===")
ages = [-5, 0, 5, 12, 15, 18, 25, 30, 40, 50, 65, 70, 100]

for age in ages:
    print(f"\nAge: {age}")
    print(f"  Category: {classifier.classify(age)}")
    print(f"  Life stage: {classifier.get_life_stage(age)}")
    print(f"  Can vote: {classifier.can_vote(age)}")
    print(f"  Can drink (US): {classifier.can_drink(age, 'US')}")
    print(f"  Can drink (UK): {classifier.can_drink(age, 'UK')}")
```

### Example 2: Grade Calculator with Comparisons
```python
class GradeCalculator:
    """Calculate letter grades using comparison operators"""
    
    @staticmethod
    def calculate_grade(score):
        """Calculate letter grade based on score"""
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    
    @staticmethod
    def calculate_gpa(score):
        """Calculate GPA (4.0 scale)"""
        if score >= 90:
            return 4.0
        elif score >= 80:
            return 3.0
        elif score >= 70:
            return 2.0
        elif score >= 60:
            return 1.0
        else:
            return 0.0
    
    @staticmethod
    def get_grade_points(grade):
        """Get grade points for letter grade"""
        grade_points = {
            "A": 4.0, "A-": 3.7,
            "B+": 3.3, "B": 3.0, "B-": 2.7,
            "C+": 2.3, "C": 2.0, "C-": 1.7,
            "D+": 1.3, "D": 1.0, "D-": 0.7,
            "F": 0.0
        }
        return grade_points.get(grade, 0.0)
    
    @staticmethod
    def is_passing(score, passing_grade=60):
        """Check if score is passing"""
        return score >= passing_grade
    
    @staticmethod
    def is_honors(score):
        """Check if score qualifies for honors"""
        return score >= 85
    
    @staticmethod
    def get_class_standing(gpa):
        """Get academic standing based on GPA"""
        if gpa >= 3.5:
            return "Dean's List"
        elif gpa >= 3.0:
            return "Good Standing"
        elif gpa >= 2.0:
            return "Academic Warning"
        else:
            return "Academic Probation"

# Demo
calculator = GradeCalculator()

print("=== Grade Calculator Demo ===")
scores = [95, 87, 72, 68, 55, 91, 84, 76, 63, 48]

for score in scores:
    grade = calculator.calculate_grade(score)
    gpa = calculator.calculate_gpa(score)
    standing = calculator.get_class_standing(gpa)
    
    print(f"\nScore: {score}")
    print(f"  Grade: {grade}")
    print(f"  GPA: {gpa:.1f}")
    print(f"  Passing: {calculator.is_passing(score)}")
    print(f"  Honors: {calculator.is_honors(score)}")
    print(f"  Standing: {standing}")

# Class statistics
print("\n=== Class Statistics ===")
print(f"Average score: {sum(scores)/len(scores):.1f}")
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")
print(f"Passing rate: {sum(1 for s in scores if s >= 60)/len(scores)*100:.1f}%")
print(f"Honors rate: {sum(1 for s in scores if s >= 85)/len(scores)*100:.1f}%")
```

### Example 3: Password Strength Checker
```python
class PasswordStrength:
    """Check password strength using comparison operators"""
    
    @staticmethod
    def check_length(password):
        """Check password length"""
        length = len(password)
        if length < 8:
            return 0, "Too short"
        elif length < 12:
            return 1, "Weak"
        elif length < 16:
            return 2, "Good"
        else:
            return 3, "Excellent"
    
    @staticmethod
    def check_complexity(password):
        """Check password complexity"""
        score = 0
        
        # Check for lowercase
        if any(c.islower() for c in password):
            score += 1
        
        # Check for uppercase
        if any(c.isupper() for c in password):
            score += 1
        
        # Check for digits
        if any(c.isdigit() for c in password):
            score += 1
        
        # Check for special characters
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        if any(c in special_chars for c in password):
            score += 1
        
        return score
    
    @staticmethod
    def get_strength(password):
        """Get overall password strength"""
        length_score, length_desc = PasswordStrength.check_length(password)
        complexity_score = PasswordStrength.check_complexity(password)
        
        total_score = length_score + complexity_score
        
        if total_score <= 2:
            return "Very Weak", total_score
        elif total_score <= 4:
            return "Weak", total_score
        elif total_score <= 6:
            return "Moderate", total_score
        elif total_score <= 8:
            return "Strong", total_score
        else:
            return "Very Strong", total_score
    
    @staticmethod
    def get_feedback(password):
        """Provide improvement feedback"""
        feedback = []
        
        if len(password) < 8:
            feedback.append("Use at least 8 characters")
        
        if not any(c.islower() for c in password):
            feedback.append("Add lowercase letters")
        
        if not any(c.isupper() for c in password):
            feedback.append("Add uppercase letters")
        
        if not any(c.isdigit() for c in password):
            feedback.append("Add numbers")
        
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        if not any(c in special_chars for c in password):
            feedback.append("Add special characters")
        
        return feedback

# Demo
checker = PasswordStrength()

print("=== Password Strength Checker ===")
print("-" * 40)

passwords = [
    "weak",
    "password123",
    "Password123",
    "Str0ngP@ss",
    "VeryStr0ngP@ssw0rd!",
    "aB1!",
    "ThisIsAStrongPassword123!"
]

for pwd in passwords:
    strength, score = checker.get_strength(pwd)
    length_score, length_desc = checker.check_length(pwd)
    complexity = checker.check_complexity(pwd)
    feedback = checker.get_feedback(pwd)
    
    print(f"\nPassword: {pwd}")
    print(f"  Strength: {strength} (Score: {score})")
    print(f"  Length: {len(pwd)} chars - {length_desc}")
    print(f"  Complexity score: {complexity}/4")
    if feedback:
        print("  Improvements needed:")
        for fb in feedback:
            print(f"    - {fb}")
```

### Example 4: Date Comparison Utility
```python
from datetime import datetime, date, timedelta

class DateComparator:
    """Compare dates and times using comparison operators"""
    
    @staticmethod
    def compare_dates(date1, date2):
        """Compare two dates"""
        if date1 < date2:
            return f"{date1} is earlier than {date2}"
        elif date1 > date2:
            return f"{date1} is later than {date2}"
        else:
            return f"{date1} is the same as {date2}"
    
    @staticmethod
    def is_weekend(date_obj):
        """Check if date is weekend"""
        return date_obj.weekday() >= 5  # 5=Saturday, 6=Sunday
    
    @staticmethod
    def is_weekday(date_obj):
        """Check if date is weekday"""
        return date_obj.weekday() < 5
    
    @staticmethod
    def is_future(date_obj):
        """Check if date is in future"""
        return date_obj > date.today()
    
    @staticmethod
    def is_past(date_obj):
        """Check if date is in past"""
        return date_obj < date.today()
    
    @staticmethod
    def is_today(date_obj):
        """Check if date is today"""
        return date_obj == date.today()
    
    @staticmethod
    def days_until(date_obj):
        """Calculate days until date"""
        if date_obj >= date.today():
            return (date_obj - date.today()).days
        else:
            return -((date.today() - date_obj).days)
    
    @staticmethod
    def is_between(date_obj, start_date, end_date):
        """Check if date is between two dates"""
        return start_date <= date_obj <= end_date

# Demo
comparator = DateComparator()

print("=== Date Comparison Demo ===")
print("-" * 40)

# Create dates
today = date.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
next_week = today + timedelta(days=7)
last_week = today - timedelta(days=7)
weekend = today
while weekend.weekday() < 5:
    weekend += timedelta(days=1)

dates = [yesterday, today, tomorrow, next_week, last_week, weekend]

print(f"Today is: {today}")
print("\nDate Comparisons:")
for d in dates:
    print(f"\nDate: {d} ({d.strftime('%A')})")
    print(f"  Compared to today: {comparator.compare_dates(d, today)}")
    print(f"  Is weekend? {comparator.is_weekend(d)}")
    print(f"  Is weekday? {comparator.is_weekday(d)}")
    print(f"  Is future? {comparator.is_future(d)}")
    print(f"  Is past? {comparator.is_past(d)}")
    print(f"  Is today? {comparator.is_today(d)}")
    print(f"  Days from today: {comparator.days_until(d)}")

# Date range check
print("\n=== Date Range Check ===")
start_date = today - timedelta(days=5)
end_date = today + timedelta(days=5)
test_dates = [today - timedelta(days=10), today - timedelta(days=2), 
              today, today + timedelta(days=3), today + timedelta(days=10)]

print(f"Range: {start_date} to {end_date}")
for test in test_dates:
    is_between = comparator.is_between(test, start_date, end_date)
    print(f"{test}: {'Within range' if is_between else 'Outside range'}")
```

### Example 5: Product Price Comparator
```python
class Product:
    """Product with price comparison capabilities"""
    
    def __init__(self, name, price, rating=0, in_stock=True):
        self.name = name
        self.price = price
        self.rating = rating
        self.in_stock = in_stock
    
    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return False
    
    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Product):
            return self.price <= other.price
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Product):
            return self.price > other.price
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, Product):
            return self.price >= other.price
        return NotImplemented
    
    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

class PriceComparator:
    """Compare products and prices"""
    
    @staticmethod
    def find_best_price(products):
        """Find product with best (lowest) price"""
        if not products:
            return None
        return min(products)
    
    @staticmethod
    def find_highest_price(products):
        """Find product with highest price"""
        if not products:
            return None
        return max(products)
    
    @staticmethod
    def filter_by_price_range(products, min_price, max_price):
        """Filter products by price range"""
        return [p for p in products if min_price <= p.price <= max_price]
    
    @staticmethod
    def filter_by_rating(products, min_rating):
        """Filter products by minimum rating"""
        return [p for p in products if p.rating >= min_rating]
    
    @staticmethod
    def get_price_tier(price):
        """Categorize price into tiers"""
        if price < 10:
            return "Budget"
        elif price < 50:
            return "Affordable"
        elif price < 100:
            return "Mid-range"
        elif price < 500:
            return "Premium"
        else:
            return "Luxury"
    
    @staticmethod
    def compare_products(product1, product2):
        """Compare two products"""
        if product1.price < product2.price:
            return f"{product1.name} is cheaper than {product2.name}"
        elif product1.price > product2.price:
            return f"{product1.name} is more expensive than {product2.name}"
        else:
            return f"{product1.name} and {product2.name} have the same price"

# Demo
print("=== Product Price Comparator Demo ===")
print("-" * 40)

# Create products
products = [
    Product("Laptop", 999.99, 4.5, True),
    Product("Mouse", 29.99, 4.2, True),
    Product("Keyboard", 79.99, 4.0, True),
    Product("Monitor", 299.99, 4.7, True),
    Product("USB Cable", 9.99, 3.8, True),
    Product("Desk", 199.99, 4.3, True),
    Product("Chair", 149.99, 4.1, True),
    Product("Headphones", 89.99, 4.4, True)
]

print("All Products:")
for p in products:
    print(f"  {p} (Rating: {p.rating})")

# Find best and worst prices
best = PriceComparator.find_best_price(products)
highest = PriceComparator.find_highest_price(products)
print(f"\nBest price: {best}")
print(f"Highest price: {highest}")

# Price range filter
print("\n=== Price Range Filter ===")
ranges = [(0, 50), (50, 100), (100, 200), (200, 500), (500, 1000)]
for min_p, max_p in ranges:
    filtered = PriceComparator.filter_by_price_range(products, min_p, max_p)
    print(f"${min_p}-${max_p}: {len(filtered)} products")

# Rating filter
print("\n=== Rating Filter ===")
min_ratings = [3.5, 4.0, 4.5]
for rating in min_ratings:
    filtered = PriceComparator.filter_by_rating(products, rating)
    print(f"Rating >= {rating}: {len(filtered)} products")

# Price tiers
print("\n=== Price Tiers ===")
for product in products:
    tier = PriceComparator.get_price_tier(product.price)
    print(f"{product.name:15} ${product.price:7.2f} → {tier}")

# Product comparison
print("\n=== Product Comparisons ===")
print(PriceComparator.compare_products(products[0], products[1]))
print(PriceComparator.compare_products(products[1], products[2]))
print(PriceComparator.compare_products(products[3], products[3]))

# Sorting products by price
print("\n=== Products Sorted by Price ===")
sorted_products = sorted(products)
for i, p in enumerate(sorted_products, 1):
    print(f"{i}. {p}")
```

### Example 6: Range Validator
```python
class RangeValidator:
    """Validate values within ranges using comparison operators"""
    
    @staticmethod
    def in_range(value, min_val, max_val):
        """Check if value is within range [min, max]"""
        return min_val <= value <= max_val
    
    @staticmethod
    def in_exclusive_range(value, min_val, max_val):
        """Check if value is within range (min, max) exclusive"""
        return min_val < value < max_val
    
    @staticmethod
    def in_closed_range(value, min_val, max_val):
        """Check if value is within range [min, max] inclusive"""
        return min_val <= value <= max_val
    
    @staticmethod
    def validate_numeric(value, min_val=None, max_val=None):
        """Validate numeric value with optional bounds"""
        if min_val is not None and value < min_val:
            return False, f"Value {value} is below minimum {min_val}"
        if max_val is not None and value > max_val:
            return False, f"Value {value} exceeds maximum {max_val}"
        return True, "Valid"
    
    @staticmethod
    def get_range_category(value, ranges):
        """Categorize value based on ranges"""
        for name, (min_val, max_val) in ranges.items():
            if min_val <= value <= max_val:
                return name
        return "Out of range"
    
    @staticmethod
    def clamp(value, min_val, max_val):
        """Clamp value to range [min, max]"""
        if value < min_val:
            return min_val
        if value > max_val:
            return max_val
        return value
    
    @staticmethod
    def is_overlap(range1, range2):
        """Check if two ranges overlap"""
        min1, max1 = range1
        min2, max2 = range2
        return max(min1, min2) <= min(max1, max2)

# Demo
validator = RangeValidator()

print("=== Range Validator Demo ===")
print("-" * 40)

# Test numeric validation
test_values = [-10, 0, 15, 25, 30, 50, 75, 100, 150]
min_val, max_val = 0, 100

print(f"Validating values between {min_val} and {max_val}:")
for value in test_values:
    is_valid, message = validator.validate_numeric(value, min_val, max_val)
    print(f"  {value:3}: {'✓' if is_valid else '✗'} - {message}")

# Range categories
print("\n=== Range Categories ===")
temperature_ranges = {
    "Freezing": (-50, 0),
    "Cold": (0, 32),
    "Cool": (32, 60),
    "Warm": (60, 80),
    "Hot": (80, 100),
    "Extreme": (100, 150)
}

temperatures = [-10, 0, 25, 45, 70, 85, 95, 110]
for temp in temperatures:
    category = validator.get_range_category(temp, temperature_ranges)
    print(f"{temp}°F: {category}")

# Clamping values
print("\n=== Clamping Values ===")
values = [-50, -10, 0, 25, 50, 75, 100, 150, 200]
min_bound, max_bound = 0, 100
print(f"Clamping to range [{min_bound}, {max_bound}]:")
for value in values:
    clamped = validator.clamp(value, min_bound, max_bound)
    print(f"  {value:3} → {clamped:3}")

# Range overlap checking
print("\n=== Range Overlap Check ===")
ranges = [
    (0, 10),
    (5, 15),
    (20, 30),
    (25, 35),
    (40, 50)
]

for i in range(len(ranges)):
    for j in range(i + 1, len(ranges)):
        overlap = validator.is_overlap(ranges[i], ranges[j])
        if overlap:
            print(f"Range {ranges[i]} overlaps with {ranges[j]}")
```

## Common Mistakes

### Mistake 1: Using = instead of ==
```python
# Wrong - assignment instead of comparison
x = 5
if x = 10:  # SyntaxError!
    print("x is 10")

# Right
if x == 10:
    print("x is 10")
```

### Mistake 2: Chaining Comparisons Incorrectly
```python
# Wrong - doesn't work as expected
x = 5
if 1 < x > 10:  # Equivalent to 1 < x and x > 10
    print("This won't print")

# Right - be explicit
if 1 < x < 10:
    print("x between 1 and 10")
```

### Mistake 3: Comparing Different Types
```python
# Wrong - comparing different types
# print(10 < "5")  # TypeError in Python 3

# Right - convert to same type
print(10 < int("5"))   # False
print(str(10) < "5")   # False (string comparison)
```

### Mistake 4: Floating-Point Comparison
```python
# Wrong - direct float comparison
result = 0.1 + 0.2
if result == 0.3:  # False!
    print("Equal")

# Right - use tolerance
tolerance = 1e-10
if abs(result - 0.3) < tolerance:
    print("Equal")

# Or use math.isclose
import math
if math.isclose(result, 0.3):
    print("Equal")
```

### Mistake 5: Using 'is' for Value Comparison
```python
# Wrong - using 'is' for value comparison
a = [1, 2, 3]
b = [1, 2, 3]
if a is b:  # False (different objects)
    print("Same list")

# Right - use == for value comparison
if a == b:  # True
    print("Same values")

# Right - use 'is' for None, True, False
if a is None:
    pass
```

### Mistake 6: String Comparison with Numbers
```python
# Wrong - comparing strings with numbers
age = "25"
# if age > 18:  # TypeError!

# Right - convert to number first
if int(age) > 18:
    print("Adult")
```

## Operator Precedence

```python
# Comparison operators have lower precedence than arithmetic
result = 5 + 3 > 7  # (5 + 3) > 7
print(result)  # True

result = 10 - 2 * 3 < 5  # 10 - (2*3) < 5
print(result)  # False (4 < 5)

# Chained comparisons have special handling
x = 5
print(1 < x < 10)  # True
print(1 < x and x < 10)  # Same but less efficient

# Comparisons can be combined with logical operators
age = 25
has_license = True
can_drive = age >= 16 and has_license
print(can_drive)  # True
```

## Performance Considerations

```python
import time

# Chained comparisons vs individual comparisons
iterations = 10_000_000
x = 5

# Chained comparison
start = time.time()
for _ in range(iterations):
    result = 1 < x < 10
chained_time = time.time() - start

# Individual comparisons
start = time.time()
for _ in range(iterations):
    result = 1 < x and x < 10
individual_time = time.time() - start

print(f"Chained comparison: {chained_time:.3f}s")
print(f"Individual comparison: {individual_time:.3f}s")
print(f"Chained is {'faster' if chained_time < individual_time else 'slower'}")

# Chained is often slightly faster (evaluates x only once)
```

## Quick Reference Table

| Operator | Name | Example | Result |
|----------|------|---------|---------|
| `==` | Equal | `5 == 5` | `True` |
| `!=` | Not equal | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `3 <= 5` | `True` |
| `is` | Identity | `x is None` | `True/False` |
| `is not` | Negative identity | `x is not None` | `True/False` |

## Summary

- **Comparison operators** return Boolean values (`True`/`False`)
- **`==`** checks value equality, **`is`** checks identity
- **Chained comparisons** like `a < b < c` are valid and efficient
- **Different types** may not be comparable (TypeError in Python 3)
- **Strings** compare lexicographically (dictionary order)
- **Lists/tuples** compare element-wise
- **Dictionaries** compare key-value pairs (equality only)
- **Sets** support subset/superset operators (`<`, `<=`, `>`, `>=`)
- **Float comparisons** need tolerance due to precision
- **`None`** should be compared with `is` not `==`
- **Boolean expressions** short-circuit for efficiency

## Basic Template
```python
#!/usr/bin/env python3

def comparison_basics():
    """Demonstrate basic comparison operators"""
    
    x = 10
    y = 20
    
    print(f"x = {x}, y = {y}")
    print(f"x == y: {x == y}")
    print(f"x != y: {x != y}")
    print(f"x > y: {x > y}")
    print(f"x < y: {x < y}")
    print(f"x >= y: {x >= y}")
    print(f"x <= y: {x <= y}")

def chained_comparisons():
    """Demonstrate chained comparisons"""
    
    x = 5
    
    print(f"x = {x}")
    print(f"1 < x < 10: {1 < x < 10}")
    print(f"0 < x < 5: {0 < x < 5}")
    print(f"x == 5 < 10: {x == 5 < 10}")
    print(f"1 <= x <= 10: {1 <= x <= 10}")

def string_comparison():
    """Demonstrate string comparisons"""
    
    str1 = "apple"
    str2 = "banana"
    str3 = "Apple"
    
    print(f"'{str1}' == '{str2}': {str1 == str2}")
    print(f"'{str1}' < '{str2}': {str1 < str2}")
    print(f"'{str1}' > '{str3}': {str1 > str3} (case-sensitive)")
    print(f"'{str1.lower()}' == '{str3.lower()}': {str1.lower() == str3.lower()}")

def identity_comparison():
    """Demonstrate identity vs equality"""
    
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = list1
    
    print(f"list1 == list2: {list1 == list2}")  # True (same values)
    print(f"list1 is list2: {list1 is list2}")  # False (different objects)
    print(f"list1 is list3: {list1 is list3}")  # True (same object)
    
    # Use 'is' for None
    value = None
    print(f"value is None: {value is None}")
    print(f"value is not None: {value is not None}")

def practical_comparison():
    """Practical comparison examples"""
    
    # Age verification
    age = 25
    if age >= 18:
        print(f"Age {age}: Adult")
    else:
        print(f"Age {age}: Minor")
    
    # Score grading
    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"Score {score}: Grade {grade}")
    
    # Range check
    temperature = 72
    if 68 <= temperature <= 77:
        print(f"Temperature {temperature}°F: Comfortable")
    else:
        print(f"Temperature {temperature}°F: Not comfortable")

if __name__ == "__main__":
    print("=== BASIC COMPARISONS ===")
    comparison_basics()
    
    print("\n=== CHAINED COMPARISONS ===")
    chained_comparisons()
    
    print("\n=== STRING COMPARISONS ===")
    string_comparison()
    
    print("\n=== IDENTITY COMPARISONS ===")
    identity_comparison()
    
    print("\n=== PRACTICAL COMPARISONS ===")
    practical_comparison()
```

*This documentation belongs to https://github.com/InterCentury*