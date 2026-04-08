# 15 - Boolean Type (bool) in Python

## What are Booleans?
Boolean values represent one of two states: `True` or `False`. In Python, the `bool` type is a subclass of `int`, with `True` equal to 1 and `False` equal to 0.

## Basic Boolean Values

```python
# Boolean literals (note capitalization!)
is_true = True
is_false = False

print(is_true, type(is_true))    # True <class 'bool'>
print(is_false, type(is_false))  # False <class 'bool'>

# Case sensitive - these are wrong!
# true = True   # NameError!
# FALSE = False # NameError!
```

## Boolean from Comparisons

```python
# Comparison operators always return booleans
x = 10
y = 20

print(x == y)   # False (equal)
print(x != y)   # True (not equal)
print(x < y)    # True (less than)
print(x > y)    # False (greater than)
print(x <= y)   # True (less than or equal)
print(x >= y)   # False (greater than or equal)

# Chain comparisons
age = 25
print(18 <= age <= 65)  # True (age between 18 and 65)
print(0 < age < 18)     # False (not a minor)
```

## Boolean from Other Types (Truthiness)

### Truthy and Falsy Values
```python
# Falsy values (evaluate to False)
print(bool(None))      # False
print(bool(False))     # False
print(bool(0))         # False
print(bool(0.0))       # False
print(bool(0j))        # False
print(bool(""))        # False (empty string)
print(bool([]))        # False (empty list)
print(bool(()))        # False (empty tuple)
print(bool({}))        # False (empty dict)
print(bool(set()))     # False (empty set)
print(bool(range(0)))  # False (empty range)

# Truthy values (evaluate to True)
print(bool(True))      # True
print(bool(1))         # True
print(bool(-1))        # True
print(bool(3.14))      # True
print(bool("Hello"))   # True
print(bool([1, 2]))    # True
print(bool((1, 2)))    # True
print(bool({"a": 1}))  # True
print(bool({1, 2}))    # True
```

### Using Truthiness in Conditions
```python
# Pythonic way - check directly
name = "Alice"
if name:  # Equivalent to: if name != ""
    print(f"Hello, {name}")

# Instead of explicit comparison
if name != "":  # Less Pythonic
    print(f"Hello, {name}")

# Check if list is empty
items = []
if items:  # Equivalent to: if len(items) > 0
    print(f"Found {len(items)} items")
else:
    print("No items found")

# Check if number is non-zero
count = 5
if count:  # Equivalent to: if count != 0
    print(f"Count is {count}")
```

## Boolean Operations

### Logical Operators
```python
# and - both must be True
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# or - at least one must be True
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# not - negates the value
print(not True)         # False
print(not False)        # True
```

### Short-Circuit Evaluation
```python
# and short-circuits on first False
def expensive_check():
    print("Expensive check performed")
    return True

print(False and expensive_check())  # False (expensive_check not called)

# or short-circuits on first True
print(True or expensive_check())    # True (expensive_check not called)

# Practical example
def safe_divide(a, b):
    return b != 0 and a / b  # Division only if b != 0

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # False (no division error!)
```

### Combining Logical Operators
```python
age = 25
has_license = True
has_permit = False

# Check if can drive
can_drive = age >= 16 and (has_license or has_permit)
print(f"Can drive: {can_drive}")  # True

# Operator precedence: not > and > or
# Parentheses clarify intent
result = True or False and False
print(result)  # True (and evaluated first)

# Better with parentheses
result = True or (False and False)
print(result)  # True
```

## Boolean Functions and Methods

### Built-in Functions
```python
# bool() constructor
print(bool(42))         # True
print(bool(0))          # False
print(bool("text"))     # True
print(bool(""))         # False

# all() - True if ALL elements are truthy
print(all([True, True, True]))    # True
print(all([True, False, True]))   # False
print(all([1, 2, 3]))             # True
print(all([1, 0, 3]))             # False

# any() - True if ANY element is truthy
print(any([False, False, False])) # False
print(any([False, True, False]))  # True
print(any([0, 0, 1]))             # True
print(any([0, 0, 0]))             # False
```

### String Boolean Methods
```python
text = "Python123"

print(text.isalpha())     # False (contains numbers)
print(text.isdigit())     # False (contains letters)
print(text.isalnum())     # True (letters and numbers only)
print(text.islower())     # False (has capital P)
print(text.isupper())     # False
print(text.isspace())     # False
print(text.istitle())     # True (first letter capitalized)

# More string checks
print("   ".isspace())    # True
print("12345".isdigit())  # True
print("3.14".isdigit())   # False (dot not digit)
print("hello".islower())  # True
print("HELLO".isupper())  # True
```

## Boolean in Different Contexts

### Boolean in Arithmetic
```python
# bool is subclass of int
print(issubclass(bool, int))  # True
print(isinstance(True, int))  # True

# Arithmetic operations work
print(True + True)      # 2
print(True * 10)        # 10
print(False - 5)        # -5
print(True / False)     # ZeroDivisionError!

# Sum of booleans (count True values)
results = [True, False, True, True, False]
true_count = sum(results)
print(f"True count: {true_count}")  # 3

# Using as index
choices = ["No", "Yes"]
is_ready = True
print(choices[is_ready])    # "Yes"
print(choices[not is_ready]) # "No"
```

### Boolean in Bitwise Operations
```python
# Bitwise AND (&)
print(True & True)    # True
print(True & False)   # False

# Bitwise OR (|)
print(True | False)   # True
print(False | False)  # False

# Bitwise XOR (^)
print(True ^ True)    # False
print(True ^ False)   # True

# Difference: logical vs bitwise
# Use 'and', 'or', 'not' for booleans
# Use '&', '|', '^' for bitwise operations
```

## Practical Examples

### Example 1: User Authentication System
```python
class UserAuthenticator:
    """Simple authentication with boolean checks"""
    
    def __init__(self):
        self.users = {
            "alice": {"password": "alice123", "active": True, "admin": False},
            "bob": {"password": "bob456", "active": True, "admin": True},
            "charlie": {"password": "charlie789", "active": False, "admin": False}
        }
    
    def authenticate(self, username, password):
        """Check if user credentials are valid"""
        if username not in self.users:
            return False, "User not found"
        
        user = self.users[username]
        
        if not user["active"]:
            return False, "Account is deactivated"
        
        if user["password"] != password:
            return False, "Invalid password"
        
        return True, "Authentication successful"
    
    def has_admin_access(self, username):
        """Check if user has admin privileges"""
        if username in self.users:
            return self.users[username]["admin"] and self.users[username]["active"]
        return False
    
    def can_access_resource(self, username, resource_type):
        """Complex boolean logic for access control"""
        if username not in self.users:
            return False
        
        user = self.users[username]
        
        # Admin can access everything
        if user["admin"] and user["active"]:
            return True
        
        # Regular users have restrictions
        if not user["active"]:
            return False
        
        # Resource-specific logic
        if resource_type == "public":
            return True
        elif resource_type == "user_data":
            return True
        elif resource_type == "admin_only":
            return False
        
        return False

# Demo
auth = UserAuthenticator()

print("=== Authentication System ===")
print("-" * 40)

# Test authentication
test_users = [
    ("alice", "alice123"),
    ("alice", "wrong"),
    ("charlie", "charlie789"),
    ("bob", "bob456"),
    ("unknown", "pass")
]

for username, password in test_users:
    success, message = auth.authenticate(username, password)
    print(f"{username}: {message} (Success: {success})")

print("\n=== Access Control ===")
print("-" * 40)

resources = ["public", "user_data", "admin_only"]
for username in ["alice", "bob", "charlie"]:
    print(f"\nUser: {username}")
    print(f"Admin: {auth.has_admin_access(username)}")
    for resource in resources:
        can_access = auth.can_access_resource(username, resource)
        print(f"  {resource}: {'✓' if can_access else '✗'}")
```

### Example 2: Form Validator
```python
import re

class FormValidator:
    """Form validation using boolean logic"""
    
    @staticmethod
    def is_valid_email(email):
        """Check if email format is valid"""
        if not email:
            return False
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def is_strong_password(password):
        """Check password strength"""
        if len(password) < 8:
            return False
        if not any(c.isupper() for c in password):
            return False
        if not any(c.islower() for c in password):
            return False
        if not any(c.isdigit() for c in password):
            return False
        if not any(c in "!@#$%^&*" for c in password):
            return False
        return True
    
    @staticmethod
    def is_valid_age(age):
        """Check if age is valid"""
        try:
            age = int(age)
            return 0 <= age <= 150
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def is_valid_phone(phone):
        """Check phone number format"""
        if not phone:
            return False
        # Remove non-digits
        digits = re.sub(r'\D', '', phone)
        return len(digits) == 10
    
    def validate_form(self, data):
        """Validate complete form"""
        errors = []
        
        # Name validation
        name = data.get('name', '')
        if not name:
            errors.append("Name is required")
        elif len(name) < 2:
            errors.append("Name must be at least 2 characters")
        
        # Email validation
        email = data.get('email', '')
        if not self.is_valid_email(email):
            errors.append("Valid email is required")
        
        # Age validation
        age = data.get('age', '')
        if not self.is_valid_age(age):
            errors.append("Valid age (0-150) is required")
        
        # Password validation
        password = data.get('password', '')
        if not self.is_strong_password(password):
            errors.append("Password must be 8+ chars with uppercase, lowercase, number, special")
        
        # Phone validation (optional)
        phone = data.get('phone', '')
        if phone and not self.is_valid_phone(phone):
            errors.append("Phone number must be 10 digits")
        
        # Terms agreement
        agree = data.get('agree_terms', False)
        if not agree:
            errors.append("You must agree to the terms")
        
        is_valid = len(errors) == 0
        return is_valid, errors

# Demo
validator = FormValidator()

print("=== Form Validation ===")
print("-" * 50)

test_data = {
    'name': 'Alice Wonderland',
    'email': 'alice@example.com',
    'age': 25,
    'password': 'SecurePass123!',
    'phone': '555-123-4567',
    'agree_terms': True
}

is_valid, errors = validator.validate_form(test_data)
print(f"Form valid: {is_valid}")
if errors:
    print("Errors:")
    for error in errors:
        print(f"  • {error}")

print("\n=== Individual Validations ===")
print("-" * 50)

test_values = [
    ("email", "invalid-email", validator.is_valid_email),
    ("email", "valid@email.com", validator.is_valid_email),
    ("password", "weak", validator.is_strong_password),
    ("password", "StrongP@ss123", validator.is_strong_password),
    ("age", "25", validator.is_valid_age),
    ("age", "-5", validator.is_valid_age),
    ("age", "200", validator.is_valid_age),
    ("phone", "5551234567", validator.is_valid_phone),
    ("phone", "555-123-4567", validator.is_valid_phone),
]

for name, value, func in test_values:
    result = func(value)
    print(f"{name:10} '{value:20}' → {result}")
```

### Example 3: Permission System
```python
class PermissionSystem:
    """Advanced permission system using boolean logic"""
    
    def __init__(self):
        self.permissions = {
            'read': 1 << 0,    # 1
            'write': 1 << 1,   # 2
            'execute': 1 << 2, # 4
            'delete': 1 << 3,  # 8
            'admin': 1 << 4,   # 16
        }
    
    def has_permission(self, user_permissions, permission):
        """Check if user has specific permission"""
        mask = self.permissions.get(permission, 0)
        return (user_permissions & mask) == mask
    
    def add_permission(self, user_permissions, permission):
        """Add permission to user"""
        mask = self.permissions.get(permission, 0)
        return user_permissions | mask
    
    def remove_permission(self, user_permissions, permission):
        """Remove permission from user"""
        mask = self.permissions.get(permission, 0)
        return user_permissions & ~mask
    
    def get_permissions_list(self, user_permissions):
        """Get list of permissions as strings"""
        return [p for p, mask in self.permissions.items() 
                if self.has_permission(user_permissions, p)]
    
    def can_access_file(self, user_permissions, file_permissions, operation):
        """Check if user can perform operation on file"""
        # Admin has all permissions
        if self.has_permission(user_permissions, 'admin'):
            return True
        
        # Check specific operation permission
        if not self.has_permission(user_permissions, operation):
            return False
        
        # Check file permissions
        return self.has_permission(file_permissions, operation)

# Demo
ps = PermissionSystem()

print("=== Permission System ===")
print("-" * 50)

# Create users with different permission levels
users = {
    'guest': 0,
    'reader': ps.add_permission(0, 'read'),
    'writer': ps.add_permission(ps.add_permission(0, 'read'), 'write'),
    'admin': ps.add_permission(ps.add_permission(0, 'read'), 'admin')
}

# Add execute permission to writer
users['writer'] = ps.add_permission(users['writer'], 'execute')

for user, perms in users.items():
    print(f"\nUser: {user}")
    print(f"  Permissions: {ps.get_permissions_list(perms)}")
    print(f"  Can read? {ps.has_permission(perms, 'read')}")
    print(f"  Can write? {ps.has_permission(perms, 'write')}")
    print(f"  Can execute? {ps.has_permission(perms, 'execute')}")
    print(f"  Can delete? {ps.has_permission(perms, 'delete')}")

# File access example
print("\n=== File Access Control ===")
print("-" * 50)

file_perms = ps.add_permission(ps.add_permission(0, 'read'), 'write')
file_name = "document.txt"

print(f"File: {file_name}")
print(f"File permissions: {ps.get_permissions_list(file_perms)}")

for user, user_perms in users.items():
    print(f"\nUser: {user}")
    for op in ['read', 'write', 'delete']:
        can_access = ps.can_access_file(user_perms, file_perms, op)
        print(f"  Can {op}: {'✓' if can_access else '✗'}")
```

### Example 4: Feature Flag System
```python
class FeatureFlags:
    """Feature flag management using booleans"""
    
    def __init__(self):
        self.flags = {
            'new_ui': False,
            'beta_features': False,
            'analytics': True,
            'debug_mode': False,
            'experimental_api': False,
        }
    
    def is_enabled(self, feature):
        """Check if feature is enabled"""
        return self.flags.get(feature, False)
    
    def enable(self, feature):
        """Enable a feature"""
        if feature in self.flags:
            self.flags[feature] = True
            return True
        return False
    
    def disable(self, feature):
        """Disable a feature"""
        if feature in self.flags:
            self.flags[feature] = False
            return True
        return False
    
    def get_enabled_features(self):
        """Get list of enabled features"""
        return [f for f, enabled in self.flags.items() if enabled]
    
    def can_use_feature(self, user_tier, feature):
        """Check if user can use feature based on tier"""
        if not self.is_enabled(feature):
            return False
        
        # Tier-based access rules
        tier_access = {
            'new_ui': ['premium', 'enterprise'],
            'beta_features': ['enterprise'],
            'analytics': ['free', 'premium', 'enterprise'],
            'debug_mode': ['developer'],
            'experimental_api': ['enterprise']
        }
        
        allowed_tiers = tier_access.get(feature, [])
        return user_tier in allowed_tiers

# Demo
flags = FeatureFlags()

print("=== Feature Flags System ===")
print("-" * 50)

print("Initial features:")
print(f"Enabled: {flags.get_enabled_features()}")

# Enable features
flags.enable('new_ui')
flags.enable('beta_features')

print("\nAfter enabling features:")
print(f"Enabled: {flags.get_enabled_features()}")

print(f"\nFeature status:")
for feature in flags.flags:
    print(f"  {feature:20} → {flags.is_enabled(feature)}")

print("\n=== User Access ===")
print("-" * 50)

users = [
    ('free_user', 'free'),
    ('premium_user', 'premium'),
    ('enterprise_user', 'enterprise'),
    ('developer', 'developer')
]

for user, tier in users:
    print(f"\nUser: {user} (Tier: {tier})")
    for feature in flags.flags:
        can_use = flags.can_use_feature(tier, feature)
        if flags.is_enabled(feature):
            print(f"  {feature:20} → {'✓' if can_use else '✗'} (available: {can_use})")
        else:
            print(f"  {feature:20} → ✗ (disabled)")
```

### Example 5: Decision Making System
```python
class DecisionEngine:
    """Complex decision making with boolean logic"""
    
    @staticmethod
    def should_approve_loan(credit_score, income, debt_ratio, employment_years, has_collateral):
        """Loan approval decision based on multiple factors"""
        
        # Basic requirements
        has_min_credit = credit_score >= 650
        has_min_income = income >= 30000
        has_acceptable_debt = debt_ratio <= 0.4
        has_stable_job = employment_years >= 2
        
        # Fast approval (exceptional cases)
        fast_approve = (credit_score >= 750 and income >= 50000 and 
                       debt_ratio <= 0.3 and employment_years >= 3)
        
        # Fast reject (obvious no)
        fast_reject = (credit_score < 550 or income < 20000 or 
                      debt_ratio > 0.6)
        
        # Conditional approval with collateral
        collateral_approve = (has_collateral and has_min_credit and 
                            has_min_income and debt_ratio <= 0.5)
        
        # Normal approval
        normal_approve = (has_min_credit and has_min_income and 
                         has_acceptable_debt and has_stable_job)
        
        return fast_approve or collateral_approve or (normal_approve and not fast_reject)
    
    @staticmethod
    def should_send_promotion(customer):
        """Marketing promotion decision"""
        
        conditions = [
            customer.get('is_active', False),
            customer.get('purchase_frequency', 0) >= 3,
            customer.get('avg_order_value', 0) >= 50,
            not customer.get('unsubscribed', False),
            customer.get('loyalty_points', 0) >= 100
        ]
        
        # Different promotion tiers
        if all(conditions[:3]) and conditions[3]:
            return "premium_promo"
        elif sum(conditions) >= 3:
            return "standard_promo"
        elif conditions[0] and not conditions[4]:
            return "reactivation_promo"
        else:
            return None
    
    @staticmethod
    def can_access_system(user):
        """Multi-factor system access decision"""
        
        checks = {
            'has_valid_credentials': user.get('password_valid', False),
            'is_account_active': user.get('active', False),
            'is_ip_whitelisted': user.get('ip_whitelisted', False),
            'has_2fa_enabled': user.get('two_factor', False),
            'is_trusted_device': user.get('trusted_device', False),
            'location_verified': user.get('location_verified', False)
        }
        
        # High security path (requires 2FA or trusted device)
        high_security = (checks['has_valid_credentials'] and 
                        checks['is_account_active'] and
                        (checks['has_2fa_enabled'] or checks['is_trusted_device']))
        
        # Low security path (requires whitelist or location)
        low_security = (checks['has_valid_credentials'] and 
                       checks['is_account_active'] and
                       (checks['is_ip_whitelisted'] or checks['location_verified']))
        
        return high_security or low_security

# Demo
engine = DecisionEngine()

print("=== Loan Approval System ===")
print("-" * 50)

loan_applications = [
    {"credit": 720, "income": 60000, "debt": 0.25, "years": 5, "collateral": False},
    {"credit": 680, "income": 35000, "debt": 0.35, "years": 3, "collateral": False},
    {"credit": 620, "income": 25000, "debt": 0.45, "years": 1, "collateral": False},
    {"credit": 580, "income": 45000, "debt": 0.30, "years": 4, "collateral": True},
    {"credit": 520, "income": 18000, "debt": 0.50, "years": 1, "collateral": False},
]

for i, app in enumerate(loan_applications, 1):
    decision = engine.should_approve_loan(
        app["credit"], app["income"], app["debt"], 
        app["years"], app["collateral"]
    )
    print(f"Application {i}: {'APPROVED' if decision else 'REJECTED'}")
    print(f"  Credit: {app['credit']}, Income: ${app['income']}, Debt: {app['debt']:.0%}")

print("\n=== Promotion System ===")
print("-" * 50)

customers = [
    {"is_active": True, "purchase_frequency": 5, "avg_order_value": 75, 
     "unsubscribed": False, "loyalty_points": 150},
    {"is_active": True, "purchase_frequency": 2, "avg_order_value": 40, 
     "unsubscribed": False, "loyalty_points": 50},
    {"is_active": True, "purchase_frequency": 1, "avg_order_value": 30, 
     "unsubscribed": False, "loyalty_points": 80},
    {"is_active": False, "purchase_frequency": 0, "avg_order_value": 0, 
     "unsubscribed": False, "loyalty_points": 200},
]

for i, customer in enumerate(customers, 1):
    promo = engine.should_send_promotion(customer)
    print(f"Customer {i}: {promo or 'No promotion'}")

print("\n=== System Access Control ===")
print("-" * 50)

users = [
    {"password_valid": True, "active": True, "ip_whitelisted": True, 
     "two_factor": False, "trusted_device": False, "location_verified": False},
    {"password_valid": True, "active": True, "ip_whitelisted": False, 
     "two_factor": True, "trusted_device": False, "location_verified": False},
    {"password_valid": True, "active": True, "ip_whitelisted": False, 
     "two_factor": False, "trusted_device": True, "location_verified": True},
    {"password_valid": True, "active": False, "ip_whitelisted": True, 
     "two_factor": False, "trusted_device": False, "location_verified": False},
    {"password_valid": False, "active": True, "ip_whitelisted": True, 
     "two_factor": False, "trusted_device": False, "location_verified": False},
]

for i, user in enumerate(users, 1):
    access = engine.can_access_system(user)
    print(f"User {i}: {'GRANTED' if access else 'DENIED'}")
```

### Example 6: Game Logic with Booleans
```python
class GameCharacter:
    """Game character with boolean states"""
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 50
        self.is_alive = True
        self.is_poisoned = False
        self.is_stunned = False
        self.has_shield = False
        self.is_invisible = False
    
    def take_damage(self, damage):
        """Apply damage with various modifiers"""
        if not self.is_alive:
            return False
        
        # Shield blocks 50% damage
        if self.has_shield:
            damage = damage // 2
        
        self.health -= damage
        
        if self.health <= 0:
            self.is_alive = False
            self.health = 0
        
        return self.is_alive
    
    def heal(self, amount):
        """Heal character"""
        if self.is_alive:
            self.health = min(100, self.health + amount)
    
    def can_cast_spell(self, mana_cost):
        """Check if spell can be cast"""
        return (self.is_alive and 
                not self.is_stunned and 
                self.mana >= mana_cost)
    
    def cast_spell(self, mana_cost):
        """Cast a spell"""
        if self.can_cast_spell(mana_cost):
            self.mana -= mana_cost
            return True
        return False
    
    def can_attack(self):
        """Check if can attack"""
        return self.is_alive and not self.is_stunned
    
    def update_status(self):
        """Update status effects"""
        if self.is_poisoned:
            self.take_damage(5)
        
        # Auto-heal if not in combat
        if self.is_alive and self.health < 100:
            self.heal(2)
    
    def get_status(self):
        """Get character status as booleans"""
        return {
            'alive': self.is_alive,
            'poisoned': self.is_poisoned,
            'stunned': self.is_stunned,
            'shielded': self.has_shield,
            'invisible': self.is_invisible,
            'can_act': self.can_attack() and not self.is_stunned
        }

class CombatSystem:
    """Combat system using boolean logic"""
    
    @staticmethod
    def can_attack(attacker, target):
        """Determine if attack is possible"""
        return (attacker.can_attack() and 
                target.is_alive and 
                not target.is_invisible)
    
    @staticmethod
    def calculate_damage(attacker, target, base_damage):
        """Calculate final damage with modifiers"""
        # Critical hit (20% chance)
        import random
        is_critical = random.random() < 0.2
        
        damage = base_damage * (2 if is_critical else 1)
        
        # Target shield reduces damage
        if target.has_shield:
            damage = damage // 2
        
        return int(damage), is_critical
    
    @staticmethod
    def get_combat_status(characters):
        """Get overall combat status"""
        any_alive = any(c.is_alive for c in characters)
        all_dead = all(not c.is_alive for c in characters)
        any_poisoned = any(c.is_poisoned for c in characters)
        any_stunned = any(c.is_stunned for c in characters)
        
        return {
            'combat_ongoing': any_alive and not all_dead,
            'any_alive': any_alive,
            'all_dead': all_dead,
            'any_poisoned': any_poisoned,
            'any_stunned': any_stunned
        }

# Demo
print("=== Game Combat System ===")
print("-" * 50)

# Create characters
hero = GameCharacter("Hero")
villain = GameCharacter("Villain")

# Apply status effects
villain.is_poisoned = True
hero.has_shield = True

print(f"{hero.name}: Health={hero.health}, Mana={hero.mana}")
print(f"{villain.name}: Health={villain.health}, Mana={villain.mana}")

print("\n=== Combat Round ===")
print("-" * 30)

combat = CombatSystem()

# Hero attacks
if combat.can_attack(hero, villain):
    damage, is_critical = combat.calculate_damage(hero, villain, 25)
    print(f"{hero.name} attacks for {damage} damage {'(CRITICAL!)' if is_critical else ''}")
    villain.take_damage(damage)

# Villain attacks
if combat.can_attack(villain, hero):
    damage, is_critical = combat.calculate_damage(villain, hero, 20)
    print(f"{villain.name} attacks for {damage} damage {'(CRITICAL!)' if is_critical else ''}")
    hero.take_damage(damage)

# Update status effects
hero.update_status()
villain.update_status()

print("\n=== Combat Status ===")
print("-" * 30)

status = combat.get_combat_status([hero, villain])
for key, value in status.items():
    print(f"{key}: {value}")

print(f"\n{hero.name}: Health={hero.health}, Alive={hero.is_alive}")
print(f"{villain.name}: Health={villain.health}, Alive={villain.is_alive}")

print("\n=== Hero Status Details ===")
for status, value in hero.get_status().items():
    print(f"{status}: {value}")
```

## Boolean Operators Precedence

```python
# Precedence: not > and > or
# Use parentheses for clarity

# Without parentheses (not clear)
result = True or False and False
print(result)  # True (and evaluated first)

# With parentheses (clear)
result = True or (False and False)
print(result)  # True

# Another example
result = not True and False or True
print(result)  # True

# Equivalent with parentheses
result = ((not True) and False) or True
print(result)  # True

# Best practice: use parentheses
is_valid = (age >= 18) and (has_license or has_permit)
```

## Common Mistakes

### Mistake 1: Assignment vs Comparison
```python
# Wrong - assignment instead of comparison
x = 10
if x = 5:  # SyntaxError!
    print("x is 5")

# Right
if x == 5:
    print("x is 5")

# Python 3.8+ walrus operator (assignment expression)
if (x := 5) == 5:  # Assigns x=5 then compares
    print("x is 5")
```

### Mistake 2: Using 'is' instead of '=='
```python
# Wrong - 'is' checks identity, not equality
x = True
y = True
print(x is y)  # True (cached, but unreliable)

x = 1 == 1  # True
y = 2 == 2  # True
print(x is y)  # Usually True (cached)

# Wrong for comparing values
if x is True:  # Works but not recommended
    print("True")

# Right - use == for value comparison
if x == True:
    print("True")

# Best - just use the boolean directly
if x:
    print("True")
```

### Mistake 3: Forgetting Truthiness
```python
# Wrong - explicit comparison when not needed
name = "Alice"
if name != "":
    print(f"Hello, {name}")

# Right - use truthiness
if name:
    print(f"Hello, {name}")

# Wrong - checking empty list
items = []
if len(items) > 0:
    print("Has items")

# Right
if items:
    print("Has items")
```

### Mistake 4: Confusing 'and'/'or' with '&'/'|'
```python
# Wrong - bitwise operators with booleans
x = True
y = False
print(x & y)   # False (works but not intended)
print(x | y)   # True (works but not intended)

# Right - logical operators for booleans
print(x and y)  # False
print(x or y)   # True

# Use & and | for bitwise operations on integers
flags = 0b1010
mask = 0b1100
print(flags & mask)  # 0b1000
```

### Mistake 5: Misunderstanding Short-Circuit
```python
# Wrong - relying on side effects
def get_data():
    print("Getting data...")
    return []

data = get_data() or default_data  # get_data always called
print(data)  # [] (empty list is falsy, so default used)

# Right - explicit check
data = get_data()
if not data:
    data = default_data
```

## Boolean Best Practices

### ✅ Do This
```python
# Use truthiness for emptiness checks
if my_list:
    process(my_list)

# Use explicit booleans for flags
is_active = True
has_permission = False

# Use descriptive variable names
is_valid = True
can_proceed = False
should_update = True

# Use parentheses for complex conditions
if (age >= 18) and (has_license or has_permit):
    can_drive = True

# Use all() and any() for collections
if all(conditions):
    proceed()

if any(errors):
    handle_errors()

# Return booleans directly
def is_even(n):
    return n % 2 == 0  # Returns bool directly
```

### ❌ Avoid This
```python
# Avoid - unnecessary if-else for booleans
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# Avoid - comparing to True/False
if is_valid == True:  # Just use 'if is_valid'
    do_something()

# Avoid - using 'is' for value comparison
if flag is True:  # Use '== True' or just 'if flag'
    do_something()

# Avoid - overly complex conditions
if (x == True and y == False) or (x == False and y == True):
    # Use: if x != y
    pass
```

## Quick Reference Table

| Concept | Syntax | Example | Result |
|---------|--------|---------|---------|
| True literal | `True` | `True` | `True` |
| False literal | `False` | `False` | `False` |
| Logical AND | `a and b` | `True and False` | `False` |
| Logical OR | `a or b` | `True or False` | `True` |
| Logical NOT | `not a` | `not True` | `False` |
| Equality | `a == b` | `5 == 5` | `True` |
| Inequality | `a != b` | `5 != 3` | `True` |
| Greater than | `a > b` | `5 > 3` | `True` |
| Less than | `a < b` | `5 < 3` | `False` |
| Truth check | `if x:` | `if name:` | Checks truthiness |
| Bool constructor | `bool(x)` | `bool(42)` | `True` |
| All true? | `all(iterable)` | `all([True, True])` | `True` |
| Any true? | `any(iterable)` | `any([False, True])` | `True` |

## Summary

- **bool** represents `True` or `False` (capitalized!)
- **Subclass of int**: `True` == 1, `False` == 0
- **Comparison operators** always return booleans
- **Truthiness**: Many values are truthy/falsy
- **Logical operators**: `and`, `or`, `not` (short-circuit)
- **Bitwise operators**: `&`, `|`, `^` (use for integers)
- **`all()` and `any()`** for iterable boolean checks
- **String methods** like `isdigit()`, `isalpha()` return booleans
- **Use truthiness** for emptiness/non-zero checks
- **Avoid explicit comparisons** to `True`/`False` when possible

## Basic Template
```python
#!/usr/bin/env python3

# Boolean basics
def boolean_basics():
    """Demonstrate basic boolean operations"""
    
    # Boolean literals
    true_val = True
    false_val = False
    print(f"True: {true_val}, type: {type(true_val)}")
    print(f"False: {false_val}, type: {type(false_val)}")
    
    # Comparison operators
    x, y = 10, 20
    print(f"{x} == {y}: {x == y}")
    print(f"{x} != {y}: {x != y}")
    print(f"{x} < {y}: {x < y}")
    print(f"{x} > {y}: {x > y}")
    print(f"{x} <= {y}: {x <= y}")
    print(f"{x} >= {y}: {x >= y}")

# Truthiness
def truthiness_demo():
    """Demonstrate truthy and falsy values"""
    
    falsy_values = [None, False, 0, 0.0, "", [], (), {}, set()]
    
    print("Falsy values:")
    for value in falsy_values:
        print(f"  bool({value}) = {bool(value)}")
    
    truthy_values = [True, 1, -1, 3.14, "Hello", [1, 2], (1,), {"a": 1}]
    
    print("\nTruthy values:")
    for value in truthy_values:
        print(f"  bool({value}) = {bool(value)}")

# Logical operators
def logical_operators():
    """Demonstrate and, or, not"""
    
    print("Truth table for 'and':")
    for a in [True, False]:
        for b in [True, False]:
            print(f"  {a} and {b} = {a and b}")
    
    print("\nTruth table for 'or':")
    for a in [True, False]:
        for b in [True, False]:
            print(f"  {a} or {b} = {a or b}")
    
    print("\nTruth table for 'not':")
    for a in [True, False]:
        print(f"  not {a} = {not a}")

# Practical usage
def practical_booleans():
    """Practical boolean usage examples"""
    
    # Check if value is valid
    def is_valid_name(name):
        return bool(name and name.strip())
    
    # Check if number is in range
    def in_range(n, low, high):
        return low <= n <= high
    
    # Check if any condition met
    def can_proceed(checks):
        return all(checks)  # All must be True
    
    # Test functions
    print(f"is_valid_name('Alice'): {is_valid_name('Alice')}")
    print(f"is_valid_name(''): {is_valid_name('')}")
    print(f"in_range(5, 1, 10): {in_range(5, 1, 10)}")
    print(f"in_range(15, 1, 10): {in_range(15, 1, 10)}")
    print(f"can_proceed([True, True, True]): {can_proceed([True, True, True])}")
    print(f"can_proceed([True, False, True]): {can_proceed([True, False, True])}")

# Run examples
if __name__ == "__main__":
    print("=== BOOLEAN BASICS ===")
    boolean_basics()
    
    print("\n=== TRUTHINESS DEMO ===")
    truthiness_demo()
    
    print("\n=== LOGICAL OPERATORS ===")
    logical_operators()
    
    print("\n=== PRACTICAL BOOLEANS ===")
    practical_booleans()
```

*This documentation belongs to https://github.com/InterCentury*