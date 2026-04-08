# 23 - Logical Operators (and, or, not)

## What are Logical Operators?
Logical operators are used to combine conditional statements. They allow you to create complex boolean logic by combining multiple conditions. Python provides three logical operators: `and`, `or`, and `not`.

## The and Operator

### Basic Usage
```python
# and returns True only if both operands are True
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# With comparisons
age = 25
has_license = True
print(age >= 18 and has_license)  # True

# Multiple conditions
score = 85
attendance = 90
print(score >= 80 and attendance >= 75)  # True

# With different data types (truthiness)
print(5 and 10)      # 10 (returns last truthy value)
print(0 and 10)      # 0 (returns first falsy value)
print("" and "text") # "" (empty string is falsy)
```

### Short-Circuit Evaluation
```python
# and stops at first False value
def expensive_check():
    print("Expensive check performed")
    return True

print(False and expensive_check())  # False (expensive_check not called)
print(True and expensive_check())   # Expensive check performed, then True

# Practical example
def safe_divide(a, b):
    return b != 0 and a / b  # Division only if b != 0

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # False (no division error!)

# Multiple conditions with short-circuit
x = 5
result = x > 0 and x < 10 and x != 5
print(result)  # False (stops at x != 5)
```

### Combining Multiple Conditions
```python
# Multiple and conditions
age = 25
citizen = True
has_id = True
can_vote = age >= 18 and citizen and has_id
print(f"Can vote: {can_vote}")  # True

# With parentheses for clarity
is_eligible = (age >= 18) and (citizen) and (has_id)

# All conditions must be True
conditions = [True, True, True]
result = all(conditions)  # Same as multiple and
print(result)  # True
```

## The or Operator

### Basic Usage
```python
# or returns True if at least one operand is True
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# With comparisons
age = 16
has_permission = True
print(age >= 18 or has_permission)  # True

# Multiple options
payment_method = "credit"
print(payment_method == "cash" or payment_method == "credit" or payment_method == "debit")  # True

# With different data types (truthiness)
print(0 or 10)      # 10 (returns first truthy value)
print(5 or 10)      # 5 (returns first truthy)
print("" or "text") # "text"
```

### Short-Circuit Evaluation
```python
# or stops at first True value
def expensive_check():
    print("Expensive check performed")
    return True

print(True or expensive_check())   # True (expensive_check not called)
print(False or expensive_check())  # Expensive check performed, then True

# Default values pattern
def get_name(user):
    return user.get("name") or "Anonymous"

print(get_name({"name": "Alice"}))  # Alice
print(get_name({}))                  # Anonymous

# Lazy evaluation
def get_data():
    print("Fetching data...")
    return [1, 2, 3]

cached_data = None
data = cached_data or get_data()  # get_data called because cached_data is falsy
print(data)  # [1, 2, 3]
```

### Providing Default Values
```python
# Common pattern for defaults
def greet(name=None):
    name = name or "Guest"
    print(f"Hello, {name}!")

greet("Alice")   # Hello, Alice!
greet()          # Hello, Guest!
greet("")        # Hello, Guest! (empty string is falsy)

# With multiple options
config = {
    "host": "localhost",
    "port": None
}

host = config.get("host") or "127.0.0.1"
port = config.get("port") or 8080
print(f"{host}:{port}")  # localhost:8080

# First non-falsy value
value = None or "" or 0 or 42 or "default"
print(value)  # 42
```

## The not Operator

### Basic Usage
```python
# not inverts the boolean value
print(not True)     # False
print(not False)    # True

# With comparisons
age = 25
print(not age < 18)  # True (age is not less than 18)

# With truthiness
print(not 0)        # True (0 is falsy)
print(not 5)        # False (5 is truthy)
print(not "")       # True (empty string is falsy)
print(not "text")   # False

# Inverting conditions
is_raining = False
if not is_raining:
    print("Let's go outside!")
```

### Double Negation
```python
# Double not (!!) converts to boolean
value = 42
print(not not value)   # True (converts to bool)
print(not not 0)       # False
print(not not "hello") # True

# Equivalent to bool()
print(bool(value))     # True

# But not not is rarely used in practice
```

## Combining Logical Operators

### Operator Precedence
```python
# Precedence: not > and > or
# not evaluated first, then and, then or

# Without parentheses
result = True or False and False
print(result)  # True (and evaluated first: False and False = False, then True or False)

# With parentheses (clear)
result = True or (False and False)
print(result)  # True

# Complex example
x = 5
y = 10
z = 15

result = x > 0 and y > 5 or z < 10
# Evaluated as: (x > 0 and y > 5) or z < 10
print(result)  # True

# Use parentheses for clarity
result = (x > 0 and y > 5) or (z < 10)
print(result)  # True
```

### Truth Tables
```python
# AND truth table
print("AND Truth Table:")
print(f"True  and True  = {True and True}")
print(f"True  and False = {True and False}")
print(f"False and True  = {False and True}")
print(f"False and False = {False and False}")

# OR truth table
print("\nOR Truth Table:")
print(f"True  or True  = {True or True}")
print(f"True  or False = {True or False}")
print(f"False or True  = {False or True}")
print(f"False or False = {False or False}")

# NOT truth table
print("\nNOT Truth Table:")
print(f"not True  = {not True}")
print(f"not False = {not False}")
```

## De Morgan's Laws
```python
# De Morgan's Laws:
# not (A and B) == (not A) or (not B)
# not (A or B) == (not A) and (not B)

# Example 1
A = True
B = False

left = not (A and B)
right = (not A) or (not B)
print(f"not (A and B) = {left}")
print(f"(not A) or (not B) = {right}")
print(f"Equal: {left == right}")

# Example 2
A = False
B = False

left = not (A or B)
right = (not A) and (not B)
print(f"\nnot (A or B) = {left}")
print(f"(not A) and (not B) = {right}")
print(f"Equal: {left == right}")

# Practical application
def is_valid_age(age):
    # Instead of:
    if not (age >= 0 and age <= 150):
        return False
    
    # Use De Morgan's:
    if age < 0 or age > 150:
        return False
    return True
```

## Practical Examples

### Example 1: User Authentication System
```python
class AuthenticationSystem:
    """User authentication with logical operators"""
    
    def __init__(self):
        self.users = {
            "alice": {"password": "alice123", "active": True, "admin": False},
            "bob": {"password": "bob456", "active": True, "admin": True},
            "charlie": {"password": "charlie789", "active": False, "admin": False}
        }
    
    def authenticate(self, username, password):
        """Authenticate user with multiple conditions"""
        # Check if user exists
        if username not in self.users:
            return False, "User not found"
        
        user = self.users[username]
        
        # All conditions must be true for successful login
        is_valid = (user["password"] == password and 
                   user["active"] == True)
        
        if is_valid:
            return True, "Login successful"
        else:
            # Check specific failure reasons
            if user["password"] != password:
                return False, "Invalid password"
            elif not user["active"]:
                return False, "Account deactivated"
            else:
                return False, "Login failed"
    
    def has_access(self, username, resource):
        """Check if user has access to resource"""
        if username not in self.users:
            return False
        
        user = self.users[username]
        
        # Admin has access to everything
        if user["admin"] and user["active"]:
            return True
        
        # Regular users have limited access
        if not user["active"]:
            return False
        
        # Resource-specific access
        public_resources = ["home", "about", "contact"]
        user_resources = ["profile", "settings", "dashboard"]
        
        has_access = (resource in public_resources or 
                     (resource in user_resources and user["active"]))
        
        return has_access
    
    def can_reset_password(self, username, email_verified, security_question_answered):
        """Check if user can reset password"""
        if username not in self.users:
            return False
        
        user = self.users[username]
        
        # Must be active AND (email verified OR security question answered)
        can_reset = (user["active"] and 
                    (email_verified or security_question_answered))
        
        return can_reset

# Demo
auth = AuthenticationSystem()

print("=== Authentication System Demo ===")
print("-" * 40)

# Test authentication
test_cases = [
    ("alice", "alice123"),
    ("alice", "wrong"),
    ("bob", "bob456"),
    ("charlie", "charlie789"),
    ("dave", "pass")
]

for username, password in test_cases:
    success, message = auth.authenticate(username, password)
    print(f"{username}: {message} (Success: {success})")

# Test access control
print("\n=== Access Control ===")
users = ["alice", "bob", "charlie"]
resources = ["home", "profile", "admin_panel"]

for user in users:
    print(f"\nUser: {user}")
    for resource in resources:
        has_access = auth.has_access(user, resource)
        print(f"  {resource}: {'✓' if has_access else '✗'}")

# Test password reset
print("\n=== Password Reset ===")
print(f"Alice (active, email verified): {auth.can_reset_password('alice', True, False)}")
print(f"Alice (active, security answered): {auth.can_reset_password('alice', False, True)}")
print(f"Alice (inactive): {auth.can_reset_password('alice', True, True)}")
print(f"Charlie (inactive): {auth.can_reset_password('charlie', True, False)}")
```

### Example 2: Loan Approval System
```python
class LoanApproval:
    """Loan approval system using logical operators"""
    
    def __init__(self):
        self.min_credit_score = 650
        self.min_income = 30000
        self.max_debt_ratio = 0.4
        self.min_employment_years = 2
    
    def check_credit(self, credit_score):
        """Check credit score condition"""
        return credit_score >= self.min_credit_score
    
    def check_income(self, income):
        """Check income condition"""
        return income >= self.min_income
    
    def check_debt_ratio(self, debt_ratio):
        """Check debt ratio condition"""
        return debt_ratio <= self.max_debt_ratio
    
    def check_employment(self, years):
        """Check employment condition"""
        return years >= self.min_employment_years
    
    def approve_loan(self, credit_score, income, debt_ratio, employment_years, 
                     has_collateral=False, is_veteran=False):
        """Comprehensive loan approval logic"""
        
        # Basic requirements (all must be true)
        meets_basic = (self.check_credit(credit_score) and
                      self.check_income(income) and
                      self.check_debt_ratio(debt_ratio) and
                      self.check_employment(employment_years))
        
        # Special programs (at least one)
        special_program = has_collateral or is_veteran
        
        # Fast track for excellent candidates
        excellent = (credit_score >= 750 and 
                    income >= 50000 and 
                    debt_ratio <= 0.3 and 
                    employment_years >= 5)
        
        # Final decision
        approved = excellent or (meets_basic and special_program)
        
        # Determine reason
        if approved:
            if excellent:
                reason = "Excellent candidate - fast track approved"
            else:
                reason = "Approved with special program"
        else:
            reasons = []
            if not self.check_credit(credit_score):
                reasons.append(f"Credit score too low ({credit_score} < {self.min_credit_score})")
            if not self.check_income(income):
                reasons.append(f"Income too low (${income} < ${self.min_income})")
            if not self.check_debt_ratio(debt_ratio):
                reasons.append(f"Debt ratio too high ({debt_ratio:.1%} > {self.max_debt_ratio:.0%})")
            if not self.check_employment(employment_years):
                reasons.append(f"Employment too short ({employment_years} < {self.min_employment_years})")
            if not special_program and not meets_basic:
                reasons.append("No special program qualified")
            reason = " | ".join(reasons)
        
        return approved, reason

# Demo
loan = LoanApproval()

print("=== Loan Approval System Demo ===")
print("-" * 40)

applications = [
    # Excellent candidate
    {"credit": 780, "income": 75000, "debt": 0.25, "years": 8, "collateral": False, "veteran": False},
    # Meets basic with collateral
    {"credit": 680, "income": 45000, "debt": 0.35, "years": 3, "collateral": True, "veteran": False},
    # Meets basic with veteran
    {"credit": 670, "income": 40000, "debt": 0.38, "years": 4, "collateral": False, "veteran": True},
    # Meets basic but no special program
    {"credit": 660, "income": 35000, "debt": 0.39, "years": 2, "collateral": False, "veteran": False},
    # Low credit score
    {"credit": 600, "income": 50000, "debt": 0.30, "years": 5, "collateral": True, "veteran": False},
    # Low income
    {"credit": 700, "income": 25000, "debt": 0.30, "years": 4, "collateral": False, "veteran": True},
    # High debt ratio
    {"credit": 700, "income": 50000, "debt": 0.50, "years": 4, "collateral": True, "veteran": False}
]

for i, app in enumerate(applications, 1):
    approved, reason = loan.approve_loan(
        app["credit"], app["income"], app["debt"], app["years"],
        app["collateral"], app["veteran"]
    )
    
    print(f"\nApplication {i}:")
    print(f"  Credit: {app['credit']}, Income: ${app['income']}, Debt: {app['debt']:.0%}")
    print(f"  Years: {app['years']}, Collateral: {app['collateral']}, Veteran: {app['veteran']}")
    print(f"  Result: {'APPROVED' if approved else 'REJECTED'}")
    print(f"  Reason: {reason}")
```

### Example 3: Input Validator
```python
class InputValidator:
    """Validate user input using logical operators"""
    
    @staticmethod
    def is_valid_email(email):
        """Validate email format"""
        if not email or not isinstance(email, str):
            return False
        
        has_at = '@' in email
        has_dot = '.' in email.split('@')[-1] if '@' in email else False
        no_spaces = ' ' not in email
        valid_length = 5 <= len(email) <= 100
        
        return has_at and has_dot and no_spaces and valid_length
    
    @staticmethod
    def is_strong_password(password):
        """Check password strength"""
        if not password or len(password) < 8:
            return False
        
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
        
        # At least 3 of 4 criteria
        criteria_met = sum([has_upper, has_lower, has_digit, has_special])
        
        return criteria_met >= 3
    
    @staticmethod
    def is_valid_age(age):
        """Validate age"""
        try:
            age = int(age)
            return 0 <= age <= 150
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def is_valid_phone(phone):
        """Validate phone number"""
        if not phone:
            return False
        
        # Remove non-digits
        digits = ''.join(c for c in phone if c.isdigit())
        
        valid_length = len(digits) == 10
        starts_valid = digits[0] in '23456789'  # US numbers don't start with 0 or 1
        
        return valid_length and starts_valid
    
    @staticmethod
    def validate_registration(username, email, password, age, phone, agree_terms):
        """Complete registration validation"""
        errors = []
        
        # Username validation
        if not username or len(username) < 3:
            errors.append("Username must be at least 3 characters")
        elif len(username) > 20:
            errors.append("Username cannot exceed 20 characters")
        elif not username.isalnum():
            errors.append("Username can only contain letters and numbers")
        
        # Email validation
        if not InputValidator.is_valid_email(email):
            errors.append("Invalid email format")
        
        # Password validation
        if not InputValidator.is_strong_password(password):
            errors.append("Password is not strong enough")
        
        # Age validation
        if not InputValidator.is_valid_age(age):
            errors.append("Invalid age (must be 0-150)")
        
        # Phone validation (optional)
        if phone and not InputValidator.is_valid_phone(phone):
            errors.append("Invalid phone number format")
        
        # Terms agreement
        if not agree_terms:
            errors.append("You must agree to the terms")
        
        is_valid = len(errors) == 0
        
        return is_valid, errors

# Demo
validator = InputValidator()

print("=== Input Validation Demo ===")
print("-" * 40)

# Test email validation
emails = [
    "user@example.com",
    "invalid",
    "user@",
    "@example.com",
    "user@domain",
    "user@domain.c",
    "user name@example.com"
]

print("Email Validation:")
for email in emails:
    is_valid = validator.is_valid_email(email)
    print(f"  '{email:25}' → {'✓' if is_valid else '✗'}")

# Test password strength
print("\nPassword Strength:")
passwords = [
    "weak",
    "WeakPwd",
    "WeakPwd1",
    "Str0ng!",
    "VeryStr0ngP@ss",
    "12345678",
    "password123"
]

for pwd in passwords:
    is_strong = validator.is_strong_password(pwd)
    print(f"  '{pwd:20}' → {'Strong' if is_strong else 'Weak'}")

# Test registration
print("\nRegistration Validation:")
registrations = [
    {
        "username": "alice123",
        "email": "alice@example.com",
        "password": "Alice123!",
        "age": 25,
        "phone": "555-123-4567",
        "agree_terms": True
    },
    {
        "username": "a",
        "email": "invalid",
        "password": "weak",
        "age": 200,
        "phone": "123",
        "agree_terms": False
    }
]

for reg in registrations:
    is_valid, errors = validator.validate_registration(
        reg["username"], reg["email"], reg["password"],
        reg["age"], reg["phone"], reg["agree_terms"]
    )
    
    print(f"\nRegistration: {reg['username']}")
    print(f"  Valid: {is_valid}")
    if errors:
        print("  Errors:")
        for error in errors:
            print(f"    - {error}")
```

### Example 4: Search Filter System
```python
class SearchFilter:
    """Search and filter system using logical operators"""
    
    def __init__(self, items):
        self.items = items
    
    def filter_by(self, **criteria):
        """Filter items by multiple criteria"""
        results = self.items
        
        for key, value in criteria.items():
            if value is not None:  # Only filter if value provided
                results = [item for item in results if item.get(key) == value]
        
        return results
    
    def search(self, query=None, category=None, min_price=None, max_price=None, 
               in_stock=None, min_rating=None):
        """Advanced search with multiple conditions"""
        results = self.items
        
        if query:
            results = [item for item in results if 
                      query.lower() in item['name'].lower() or 
                      query.lower() in item.get('description', '').lower()]
        
        if category:
            results = [item for item in results if item['category'] == category]
        
        if min_price is not None and max_price is not None:
            results = [item for item in results if 
                      min_price <= item['price'] <= max_price]
        elif min_price is not None:
            results = [item for item in results if item['price'] >= min_price]
        elif max_price is not None:
            results = [item for item in results if item['price'] <= max_price]
        
        if in_stock is not None:
            results = [item for item in results if item['in_stock'] == in_stock]
        
        if min_rating is not None:
            results = [item for item in results if item['rating'] >= min_rating]
        
        return results
    
    def advanced_search(self, **filters):
        """Flexible search with any combination of filters"""
        results = self.items
        
        for filter_name, filter_value in filters.items():
            if filter_value is not None:
                if filter_name == 'price_range':
                    min_p, max_p = filter_value
                    results = [item for item in results if 
                              min_p <= item['price'] <= max_p]
                elif filter_name == 'text_search':
                    results = [item for item in results if
                              any(filter_value.lower() in str(value).lower() 
                                  for value in item.values())]
                elif filter_name == 'multiple_categories':
                    results = [item for item in results if
                              item['category'] in filter_value]
                elif callable(filter_value):
                    results = [item for item in results if filter_value(item)]
                else:
                    results = [item for item in results if 
                              item.get(filter_name) == filter_value]
        
        return results

# Sample data
products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999.99, 
     "in_stock": True, "rating": 4.5, "description": "High-performance laptop"},
    {"id": 2, "name": "Mouse", "category": "Electronics", "price": 29.99, 
     "in_stock": True, "rating": 4.2, "description": "Wireless mouse"},
    {"id": 3, "name": "Keyboard", "category": "Electronics", "price": 79.99, 
     "in_stock": False, "rating": 4.0, "description": "Mechanical keyboard"},
    {"id": 4, "name": "Monitor", "category": "Electronics", "price": 299.99, 
     "in_stock": True, "rating": 4.7, "description": "4K Monitor"},
    {"id": 5, "name": "Book", "category": "Books", "price": 19.99, 
     "in_stock": True, "rating": 4.8, "description": "Python Programming"},
    {"id": 6, "name": "Desk", "category": "Furniture", "price": 199.99, 
     "in_stock": True, "rating": 4.3, "description": "Standing desk"},
    {"id": 7, "name": "Chair", "category": "Furniture", "price": 149.99, 
     "in_stock": False, "rating": 4.1, "description": "Ergonomic chair"}
]

# Demo
search = SearchFilter(products)

print("=== Search Filter Demo ===")
print("-" * 40)

# Basic search
print("Basic Search:")
results = search.search(query="laptop")
print(f"  Search 'laptop': {len(results)} results")

results = search.search(category="Electronics", in_stock=True)
print(f"  Electronics in stock: {len(results)} results")

results = search.search(min_price=100, max_price=500)
print(f"  Price $100-$500: {len(results)} results")

results = search.search(min_rating=4.5, in_stock=True)
print(f"  Rating >=4.5 and in stock: {len(results)} results")

# Combined search
print("\nCombined Search:")
results = search.search(
    category="Electronics",
    min_price=50,
    max_price=500,
    in_stock=True,
    min_rating=4.0
)
print(f"  Electronics $50-$500, in stock, rating>=4.0: {len(results)} results")
for item in results:
    print(f"    - {item['name']}: ${item['price']} (Rating: {item['rating']})")

# Advanced search
print("\nAdvanced Search:")
results = search.advanced_search(
    category="Electronics",
    in_stock=True,
    price_range=(50, 300)
)
print(f"  Electronics in stock $50-$300: {len(results)} results")

# Custom filter function
results = search.advanced_search(
    custom_filter=lambda x: x['price'] < 100 and x['rating'] > 4.0
)
print(f"\n  Price < $100 and rating > 4.0: {len(results)} results")
for item in results:
    print(f"    - {item['name']}: ${item['price']} (Rating: {item['rating']})")

# Multiple categories
results = search.advanced_search(
    multiple_categories=["Electronics", "Books"],
    in_stock=True
)
print(f"\n  Electronics or Books, in stock: {len(results)} results")
```

### Example 5: Permission System
```python
class PermissionSystem:
    """Advanced permission system using logical operators"""
    
    def __init__(self):
        self.permissions = {
            'read': 1 << 0,    # 1
            'write': 1 << 1,   # 2
            'delete': 1 << 2,  # 4
            'execute': 1 << 3, # 8
            'admin': 1 << 4    # 16
        }
    
    def has_permission(self, user_permissions, permission):
        """Check if user has specific permission"""
        mask = self.permissions.get(permission, 0)
        return (user_permissions & mask) == mask
    
    def has_any(self, user_permissions, *permissions):
        """Check if user has any of the permissions"""
        return any(self.has_permission(user_permissions, p) for p in permissions)
    
    def has_all(self, user_permissions, *permissions):
        """Check if user has all of the permissions"""
        return all(self.has_permission(user_permissions, p) for p in permissions)
    
    def can_access_resource(self, user_permissions, resource_type, operation):
        """Check access based on resource type and operation"""
        
        # Admin has all access
        if self.has_permission(user_permissions, 'admin'):
            return True, "Admin access"
        
        # Public resources
        if resource_type == 'public':
            return True, "Public resource"
        
        # Protected resources
        if resource_type == 'protected':
            if operation == 'read':
                has_access = self.has_permission(user_permissions, 'read')
                return has_access, "Read access" if has_access else "No read permission"
            elif operation == 'write':
                has_access = self.has_permission(user_permissions, 'write')
                return has_access, "Write access" if has_access else "No write permission"
        
        # Private resources
        if resource_type == 'private':
            required = self.has_all(user_permissions, 'read', 'write')
            return required, "Full access" if required else "Insufficient permissions"
        
        return False, "Unknown resource type"
    
    def get_user_role_description(self, user_permissions):
        """Describe user's role based on permissions"""
        if self.has_permission(user_permissions, 'admin'):
            return "Administrator (full access)"
        elif self.has_all(user_permissions, 'read', 'write', 'delete'):
            return "Manager (read, write, delete)"
        elif self.has_all(user_permissions, 'read', 'write'):
            return "Editor (read, write)"
        elif self.has_permission(user_permissions, 'read'):
            return "Viewer (read only)"
        else:
            return "No access"
    
    def can_perform_operation(self, user_permissions, operation, context=None):
        """Context-aware permission checking"""
        
        # Admin bypass
        if self.has_permission(user_permissions, 'admin'):
            return True, "Admin override"
        
        # Basic operation checks
        if operation == 'view':
            if self.has_permission(user_permissions, 'read'):
                return True, "Has read permission"
            return False, "Missing read permission"
        
        elif operation == 'edit':
            if self.has_all(user_permissions, 'read', 'write'):
                return True, "Has read+write permissions"
            return False, "Missing write permission"
        
        elif operation == 'create':
            if self.has_permission(user_permissions, 'write'):
                return True, "Has write permission"
            return False, "Missing write permission"
        
        elif operation == 'delete':
            if self.has_permission(user_permissions, 'delete'):
                return True, "Has delete permission"
            # Delete requires admin or specific delete permission
            return False, "Missing delete permission"
        
        elif operation == 'execute':
            if self.has_permission(user_permissions, 'execute'):
                return True, "Has execute permission"
            return False, "Missing execute permission"
        
        return False, "Unknown operation"

# Demo
ps = PermissionSystem()

print("=== Permission System Demo ===")
print("-" * 40)

# Define user permissions
users = {
    "Guest": 0,
    "Viewer": ps.permissions['read'],
    "Editor": ps.permissions['read'] | ps.permissions['write'],
    "Manager": ps.permissions['read'] | ps.permissions['write'] | ps.permissions['delete'],
    "Admin": ps.permissions['admin']
}

# Display user roles
print("User Roles:")
for user, perms in users.items():
    role = ps.get_user_role_description(perms)
    print(f"  {user}: {role}")

# Check specific permissions
print("\n=== Permission Checks ===")
for user, perms in users.items():
    print(f"\n{user}:")
    print(f"  Has read: {ps.has_permission(perms, 'read')}")
    print(f"  Has write: {ps.has_permission(perms, 'write')}")
    print(f"  Has delete: {ps.has_permission(perms, 'delete')}")
    print(f"  Has any (read/write): {ps.has_any(perms, 'read', 'write')}")
    print(f"  Has all (read/write): {ps.has_all(perms, 'read', 'write')}")

# Resource access
print("\n=== Resource Access ===")
resources = [
    ("public", "read"),
    ("protected", "read"),
    ("protected", "write"),
    ("private", "read"),
    ("private", "write")
]

for user, perms in users.items():
    print(f"\n{user}:")
    for resource_type, operation in resources:
        can_access, reason = ps.can_access_resource(perms, resource_type, operation)
        print(f"  {resource_type}/{operation}: {'✓' if can_access else '✗'} - {reason}")

# Operation permissions
print("\n=== Operation Permissions ===")
operations = ['view', 'edit', 'create', 'delete', 'execute']

for user, perms in users.items():
    print(f"\n{user}:")
    for operation in operations:
        can_perform, reason = ps.can_perform_operation(perms, operation)
        print(f"  {operation}: {'✓' if can_perform else '✗'} - {reason}")
```

### Example 6: Game Logic System
```python
class GameLogic:
    """Game mechanics using logical operators"""
    
    def __init__(self):
        self.player = {
            'health': 100,
            'mana': 50,
            'level': 1,
            'has_shield': False,
            'is_poisoned': False,
            'is_stunned': False,
            'is_invisible': False
        }
    
    def can_cast_spell(self, spell_cost):
        """Check if player can cast spell"""
        return (self.player['health'] > 0 and 
                self.player['mana'] >= spell_cost and 
                not self.player['is_stunned'])
    
    def can_attack(self):
        """Check if player can attack"""
        return (self.player['health'] > 0 and 
                not self.player['is_stunned'] and 
                not self.player['is_invisible'])
    
    def take_damage(self, damage):
        """Apply damage with modifiers"""
        if self.player['has_shield']:
            damage = damage // 2
        
        self.player['health'] -= damage
        
        if self.player['health'] <= 0:
            self.player['health'] = 0
            return False  # Player died
        return True  # Player alive
    
    def update_status(self):
        """Apply status effects"""
        if self.player['is_poisoned']:
            self.player['health'] -= 5
        
        # Auto-heal if not in combat and not poisoned
        if not self.player['is_poisoned'] and self.player['health'] < 100:
            self.player['health'] = min(100, self.player['health'] + 2)
        
        # Regenerate mana
        if not self.player['is_stunned']:
            self.player['mana'] = min(50, self.player['mana'] + 1)
    
    def check_victory_conditions(self, enemy_health, boss_fight=False):
        """Check various victory conditions"""
        player_alive = self.player['health'] > 0
        enemy_dead = enemy_health <= 0
        
        if boss_fight:
            # Boss fight requires special conditions
            special_condition = (self.player['level'] >= 5 or 
                                self.player['has_shield'])
            return player_alive and enemy_dead and special_condition
        else:
            return player_alive and enemy_dead
    
    def can_use_item(self, item_type):
        """Check if player can use specific item"""
        if self.player['health'] <= 0:
            return False
        
        if item_type == 'health_potion':
            return self.player['health'] < 100 and not self.player['is_poisoned']
        
        elif item_type == 'mana_potion':
            return self.player['mana'] < 50 and not self.player['is_stunned']
        
        elif item_type == 'antidote':
            return self.player['is_poisoned']
        
        elif item_type == 'shield':
            return not self.player['has_shield']
        
        return False
    
    def get_combat_status(self):
        """Get comprehensive combat status"""
        return {
            'can_act': self.can_attack() or self.can_cast_spell(0),
            'is_critical': self.player['health'] < 30,
            'needs_healing': self.player['health'] < 50,
            'can_use_health': self.can_use_item('health_potion'),
            'can_use_mana': self.can_use_item('mana_potion'),
            'status_effects': {
                'poisoned': self.player['is_poisoned'],
                'stunned': self.player['is_stunned'],
                'shielded': self.player['has_shield'],
                'invisible': self.player['is_invisible']
            }
        }

# Demo
game = GameLogic()

print("=== Game Logic Demo ===")
print("-" * 40)

print("Initial Player Status:")
print(f"  Health: {game.player['health']}")
print(f"  Mana: {game.player['mana']}")
print(f"  Can attack: {game.can_attack()}")
print(f"  Can cast spell (20 mana): {game.can_cast_spell(20)}")

# Apply status effects
print("\n=== Applying Status Effects ===")
game.player['is_poisoned'] = True
game.player['has_shield'] = True
print(f"Poisoned: {game.player['is_poisoned']}, Shielded: {game.player['has_shield']}")

# Check item usage
print("\n=== Item Usage ===")
items = ['health_potion', 'mana_potion', 'antidote', 'shield']
for item in items:
    can_use = game.can_use_item(item)
    print(f"  Can use {item}: {can_use}")

# Combat simulation
print("\n=== Combat Simulation ===")
enemy_health = 50
round_num = 1

while game.player['health'] > 0 and enemy_health > 0:
    print(f"\nRound {round_num}:")
    print(f"  Player: Health={game.player['health']}, Mana={game.player['mana']}")
    print(f"  Enemy: Health={enemy_health}")
    
    # Check if can attack
    if game.can_attack():
        damage = 15
        enemy_health -= damage
        print(f"  Player attacks for {damage} damage!")
    
    # Enemy attacks
    if enemy_health > 0:
        game.take_damage(10)
        print(f"  Enemy attacks for 10 damage!")
    
    # Update status effects
    game.update_status()
    
    # Show status
    status = game.get_combat_status()
    print(f"  Status: Critical={status['is_critical']}, Needs healing={status['needs_healing']}")
    
    round_num += 1
    
    if round_num > 10:  # Safety limit
        break

# Check victory
victory = game.check_victory_conditions(enemy_health, boss_fight=False)
print(f"\nCombat Result: {'VICTORY!' if victory else 'DEFEAT...'}")
print(f"Final Player Health: {game.player['health']}")
print(f"Final Enemy Health: {enemy_health}")

# Final status
print("\nFinal Combat Status:")
status = game.get_combat_status()
for key, value in status.items():
    if key != 'status_effects':
        print(f"  {key}: {value}")
print("  Status Effects:")
for effect, active in status['status_effects'].items():
    print(f"    {effect}: {active}")
```

## Truth Table Reference

| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

## Short-Circuit Behavior

```python
# and short-circuits on first False
print("and short-circuit:")
def false_func():
    print("  false_func called")
    return False

def true_func():
    print("  true_func called")
    return True

result = false_func() and true_func()  # true_func NOT called
print(f"  Result: {result}")

# or short-circuits on first True
print("\nor short-circuit:")
result = true_func() or false_func()  # false_func NOT called
print(f"  Result: {result}")
```

## Common Mistakes

### Mistake 1: Using Bitwise Operators Instead of Logical
```python
# Wrong - bitwise operators
x = 5
y = 10
if x & y:  # Bitwise AND, not logical
    print("Both true")

# Right - logical operators
if x and y:  # Logical AND
    print("Both truthy")
```

### Mistake 2: Misunderstanding Operator Precedence
```python
# Wrong - incorrect order
x = True
y = False
z = False
result = x or y and z  # and evaluated first
print(result)  # True

# Right - use parentheses
result = (x or y) and z
print(result)  # False
```

### Mistake 3: Using 'and' for Default Values
```python
# Wrong - and doesn't work for defaults
name = input("Name: ") or "Guest"  # This works with 'or'
# name = input("Name: ") and "Guest"  # This doesn't work as expected

# Right - use 'or' for defaults
name = input("Name: ") or "Guest"
```

### Mistake 4: Forgetting Parentheses in Complex Conditions
```python
# Wrong - unclear precedence
age = 25
has_license = True
has_permit = False
can_drive = age >= 16 and has_license or has_permit  # Ambiguous

# Right - explicit parentheses
can_drive = (age >= 16) and (has_license or has_permit)
```

## Best Practices

### ✅ Do This
```python
# Use parentheses for clarity
if (age >= 18) and (has_license or has_permit):
    can_drive = True

# Use 'or' for defaults
name = user_input or "Default"

# Use 'and' for safe operations
result = denominator != 0 and numerator / denominator

# Use De Morgan's laws for readability
if not (age >= 0 and age <= 150):
    # vs
if age < 0 or age > 150:
    pass

# Use all() for multiple and conditions
if all([condition1, condition2, condition3]):
    pass

# Use any() for multiple or conditions
if any([condition1, condition2, condition3]):
    pass
```

### ❌ Avoid This
```python
# Avoid - overly complex conditions
if condition1 and condition2 or condition3 and not condition4:
    pass

# Avoid - using 'and' for flow control
x and expensive_operation()  # Confusing

# Avoid - unnecessary parentheses for simple conditions
if ((age >= 18) and (has_license)):  # Too many parentheses
    pass

# Avoid - mixing 'and' and 'or' without parentheses
if a and b or c and d:
    pass
```

## Quick Reference Table

| Operator | Description | Example | Result |
|----------|-------------|---------|---------|
| `and` | True if both are true | `True and False` | `False` |
| `or` | True if at least one is true | `True or False` | `True` |
| `not` | Inverts boolean value | `not True` | `False` |

## Summary

- **`and`**: Returns True only if both operands are True
- **`or`**: Returns True if at least one operand is True
- **`not`**: Inverts boolean value
- **Short-circuit evaluation**: Stops when result is determined
- **Precedence**: `not` > `and` > `or`
- **Use parentheses** for complex conditions
- **Use `all()`** for multiple `and` conditions
- **Use `any()`** for multiple `or` conditions
- **Use `or` for defaults** (e.g., `value or default`)
- **Use `and` for safe operations** (e.g., `b != 0 and a/b`)

## Basic Template
```python
#!/usr/bin/env python3

def and_demo():
    """Demonstrate and operator"""
    print("=== AND Operator ===")
    age = 25
    has_license = True
    
    if age >= 18 and has_license:
        print("Can drive")
    
    # Short-circuit example
    def expensive():
        print("Expensive check")
        return True
    
    result = False and expensive()  # expensive not called
    print(f"Result: {result}")

def or_demo():
    """Demonstrate or operator"""
    print("\n=== OR Operator ===")
    payment = "cash"
    
    if payment == "cash" or payment == "credit":
        print("Payment accepted")
    
    # Default value pattern
    name = input("Enter name: ") or "Guest"
    print(f"Hello, {name}")

def not_demo():
    """Demonstrate not operator"""
    print("\n=== NOT Operator ===")
    is_raining = False
    
    if not is_raining:
        print("Good weather!")
    
    # Double negative (converts to bool)
    value = 42
    print(f"not not {value} = {not not value}")

def combined_logic():
    """Combine logical operators"""
    print("\n=== Combined Logic ===")
    x = 5
    y = 10
    z = 15
    
    # Complex condition
    if (x > 0 and y > 0) or (z > 0):
        print("At least one condition true")
    
    # De Morgan's laws
    a = True
    b = False
    print(f"not (a and b) = {not (a and b)}")
    print(f"(not a) or (not b) = {(not a) or (not b)}")

def practical_usage():
    """Practical examples"""
    print("\n=== Practical Usage ===")
    
    # Safe division
    def safe_divide(a, b):
        return b != 0 and a / b
    
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")
    
    # Validation
    def validate(age, name):
        return age >= 0 and name and len(name) > 0
    
    print(f"Valid (25, 'Alice'): {validate(25, 'Alice')}")
    print(f"Valid (-5, 'Bob'): {validate(-5, 'Bob')}")
    print(f"Valid (30, ''): {validate(30, '')}")

if __name__ == "__main__":
    and_demo()
    or_demo()
    not_demo()
    combined_logic()
    practical_usage()
```

*This documentation belongs to https://github.com/InterCentury*