# 25 - Membership Operators (in, not in)

## What are Membership Operators?
Membership operators test whether a value exists in a sequence or collection (strings, lists, tuples, dictionaries, sets, etc.). Python provides two membership operators: `in` and `not in`.

## The in Operator

### Basic Usage with Lists
```python
# Check if item exists in list
fruits = ['apple', 'banana', 'orange', 'grape']

print('apple' in fruits)    # True
print('mango' in fruits)    # False
print('orange' in fruits)   # True

# With numeric lists
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)   # True
print(10 in numbers)  # False

# With mixed types
mixed = [1, 'hello', 3.14, True]
print('hello' in mixed)  # True
print(False in mixed)    # False (True is 1, but False not present)
```

### With Strings
```python
# Substring checking
text = "Hello, World!"
print('Hello' in text)     # True
print('world' in text)     # False (case-sensitive)
print('World' in text)     # True
print('lo' in text)        # True
print('xyz' in text)       # False

# Character checking
print('H' in text)         # True
print('Z' in text)         # False

# Empty string always returns True
print('' in text)          # True
print('' in '')            # True
```

### With Tuples
```python
# Tuple membership
colors = ('red', 'green', 'blue', 'yellow')
print('green' in colors)   # True
print('purple' in colors)  # False

# With numeric tuples
coordinates = (10, 20, 30)
print(20 in coordinates)   # True
print(25 in coordinates)   # False
```

### With Dictionaries
```python
# in checks KEYS by default (not values)
person = {'name': 'Alice', 'age': 30, 'city': 'NYC'}

# Check keys
print('name' in person)     # True
print('age' in person)      # True
print('address' in person)  # False

# Check values (need to use .values())
print('Alice' in person.values())     # True
print('NYC' in person.values())       # True
print('Bob' in person.values())       # False

# Check key-value pairs
print(('name', 'Alice') in person.items())   # True
print(('name', 'Bob') in person.items())     # False
```

### With Sets
```python
# Set membership (fastest for membership testing)
numbers_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(5 in numbers_set)    # True
print(15 in numbers_set)   # False

# Sets are optimized for membership testing
import time
large_list = list(range(1000000))
large_set = set(range(1000000))

# List membership (O(n))
start = time.time()
999999 in large_list
list_time = time.time() - start

# Set membership (O(1))
start = time.time()
999999 in large_set
set_time = time.time() - start

print(f"List membership: {list_time:.6f}s")
print(f"Set membership: {set_time:.6f}s")
```

### With Ranges
```python
# Range membership (efficient in Python 3)
numbers = range(1, 1000000)
print(500 in numbers)      # True
print(1000000 in numbers)  # False

# Range checks are optimized (no iteration)
import time
large_range = range(10000000)
start = time.time()
9999999 in large_range
range_time = time.time() - start
print(f"Range check: {range_time:.6f}s")  # Very fast
```

## The not in Operator

### Basic Usage
```python
# Opposite of 'in'
fruits = ['apple', 'banana', 'orange']

print('mango' not in fruits)   # True
print('apple' not in fruits)   # False

# With strings
text = "Hello World"
print('xyz' not in text)    # True
print('Hello' not in text)  # False

# With dictionaries
person = {'name': 'Alice', 'age': 30}
print('address' not in person)  # True
print('name' not in person)     # False
```

### Practical Examples
```python
# Check if user is not in admin list
admins = ['alice', 'bob', 'charlie']
username = 'dave'

if username not in admins:
    print(f"{username} is not an admin")

# Check if domain is not allowed
allowed_domains = ['gmail.com', 'yahoo.com', 'outlook.com']
email = 'user@spam.com'
domain = email.split('@')[1]

if domain not in allowed_domains:
    print(f"Domain {domain} is not allowed")
```

## Performance Considerations

```python
import time

# Different data structures have different performance
test_value = 50000

# List membership (O(n))
my_list = list(range(100000))
start = time.time()
result = test_value in my_list
list_time = time.time() - start

# Set membership (O(1))
my_set = set(range(100000))
start = time.time()
result = test_value in my_set
set_time = time.time() - start

# Tuple membership (O(n))
my_tuple = tuple(range(100000))
start = time.time()
result = test_value in my_tuple
tuple_time = time.time() - start

print(f"List membership: {list_time:.6f}s")
print(f"Set membership: {set_time:.6f}s")
print(f"Tuple membership: {tuple_time:.6f}s")

# When to use what:
# - Use set for fast membership testing (O(1))
# - Use list/tuple for ordered data (O(n))
# - Use set when you only need to check existence
```

## Practical Examples

### Example 1: User Authentication System
```python
class AuthSystem:
    """Authentication system using membership operators"""
    
    def __init__(self):
        self.valid_users = {'alice', 'bob', 'charlie', 'diana'}
        self.blocked_users = {'hacker', 'spammer'}
        self.admin_users = {'alice', 'bob'}
        self.user_roles = {
            'alice': 'admin',
            'bob': 'admin',
            'charlie': 'user',
            'diana': 'user'
        }
    
    def authenticate(self, username, password):
        """Authenticate user"""
        if username not in self.valid_users:
            return False, "User not found"
        
        if username in self.blocked_users:
            return False, "Account blocked"
        
        # Simulate password check
        if password == f"{username}123":
            return True, "Login successful"
        
        return False, "Invalid password"
    
    def has_permission(self, username, permission):
        """Check user permissions"""
        if username not in self.valid_users:
            return False
        
        if username in self.admin_users:
            return True  # Admin has all permissions
        
        # Regular user permissions
        user_permissions = {'read', 'write'}
        return permission in user_permissions
    
    def get_user_role(self, username):
        """Get user role"""
        return self.user_roles.get(username, 'unknown')
    
    def get_users_by_role(self, role):
        """Get all users with specific role"""
        return [user for user, user_role in self.user_roles.items() 
                if user_role == role]

# Demo
auth = AuthSystem()

print("=== Authentication System ===")
print("-" * 40)

# Test authentication
test_users = [
    ('alice', 'alice123'),
    ('bob', 'wrong'),
    ('charlie', 'charlie123'),
    ('hacker', 'hacker123'),
    ('eve', 'eve123')
]

for username, password in test_users:
    success, message = auth.authenticate(username, password)
    print(f"{username}: {message}")

# Check permissions
print("\n=== Permission Check ===")
users = ['alice', 'charlie', 'eve']
for user in users:
    can_read = auth.has_permission(user, 'read')
    can_delete = auth.has_permission(user, 'delete')
    role = auth.get_user_role(user)
    print(f"{user} (Role: {role}): Read={can_read}, Delete={can_delete}")

# Get users by role
print("\n=== Users by Role ===")
for role in ['admin', 'user']:
    users = auth.get_users_by_role(role)
    print(f"{role.capitalize()}s: {', '.join(users) if users else 'None'}")
```

### Example 2: Shopping Cart with Inventory
```python
class ShoppingCart:
    """Shopping cart with inventory management"""
    
    def __init__(self):
        self.inventory = {
            'laptop': {'price': 999.99, 'stock': 5},
            'mouse': {'price': 29.99, 'stock': 20},
            'keyboard': {'price': 79.99, 'stock': 10},
            'monitor': {'price': 299.99, 'stock': 3},
            'headphones': {'price': 89.99, 'stock': 15}
        }
        self.cart = {}
        self.discount_codes = {'SAVE10', 'WELCOME20', 'FLASH50'}
        self.applied_discount = None
    
    def add_to_cart(self, item, quantity=1):
        """Add item to shopping cart"""
        if item not in self.inventory:
            return False, f"Item '{item}' not found"
        
        if self.inventory[item]['stock'] < quantity:
            return False, f"Only {self.inventory[item]['stock']} {item}(s) in stock"
        
        self.cart[item] = self.cart.get(item, 0) + quantity
        self.inventory[item]['stock'] -= quantity
        return True, f"Added {quantity}x {item} to cart"
    
    def remove_from_cart(self, item, quantity=1):
        """Remove item from cart"""
        if item not in self.cart:
            return False, f"Item '{item}' not in cart"
        
        if self.cart[item] < quantity:
            return False, f"Only {self.cart[item]} {item}(s) in cart"
        
        self.cart[item] -= quantity
        self.inventory[item]['stock'] += quantity
        
        if self.cart[item] == 0:
            del self.cart[item]
        
        return True, f"Removed {quantity}x {item} from cart"
    
    def apply_discount(self, code):
        """Apply discount code"""
        if code not in self.discount_codes:
            return False, "Invalid discount code"
        
        self.applied_discount = code
        return True, f"Discount '{code}' applied"
    
    def calculate_total(self):
        """Calculate cart total with discount"""
        total = sum(self.inventory[item]['price'] * qty 
                    for item, qty in self.cart.items())
        
        if self.applied_discount == 'SAVE10':
            total *= 0.9
        elif self.applied_discount == 'WELCOME20':
            total *= 0.8
        elif self.applied_discount == 'FLASH50':
            total *= 0.5
        
        return total
    
    def checkout(self):
        """Process checkout"""
        if not self.cart:
            return False, "Cart is empty"
        
        total = self.calculate_total()
        return True, f"Checkout successful! Total: ${total:.2f}"
    
    def get_cart_summary(self):
        """Get cart summary"""
        if not self.cart:
            return "Cart is empty"
        
        summary = []
        for item, qty in self.cart.items():
            price = self.inventory[item]['price']
            subtotal = price * qty
            summary.append(f"  {item}: {qty} x ${price:.2f} = ${subtotal:.2f}")
        
        summary.append(f"\nTotal: ${self.calculate_total():.2f}")
        if self.applied_discount:
            summary.append(f"Discount applied: {self.applied_discount}")
        
        return "\n".join(summary)

# Demo
cart = ShoppingCart()

print("=== Shopping Cart Demo ===")
print("-" * 40)

# Add items
items_to_add = [
    ('laptop', 1),
    ('mouse', 2),
    ('keyboard', 1),
    ('tablet', 1)  # Not in inventory
]

for item, qty in items_to_add:
    success, message = cart.add_to_cart(item, qty)
    print(message)

print("\n=== Cart Summary ===")
print(cart.get_cart_summary())

# Apply discount
print("\n=== Apply Discount ===")
discounts = ['SAVE10', 'INVALID', 'FLASH50']
for code in discounts:
    success, message = cart.apply_discount(code)
    print(message)
    if success:
        print(f"New total: ${cart.calculate_total():.2f}")

# Remove item
print("\n=== Remove Item ===")
success, message = cart.remove_from_cart('mouse', 1)
print(message)
print(cart.get_cart_summary())

# Checkout
print("\n=== Checkout ===")
success, message = cart.checkout()
print(message)
```

### Example 3: Text Analyzer
```python
class TextAnalyzer:
    """Text analysis using membership operators"""
    
    def __init__(self, text):
        self.text = text
        self.vowels = set('aeiouAEIOU')
        self.consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
        self.punctuation = set('.,!?;:""\'()[]{}')
        self.stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 
                          'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are'}
    
    def count_vowels(self):
        """Count vowels in text"""
        return sum(1 for char in self.text if char in self.vowels)
    
    def count_consonants(self):
        """Count consonants in text"""
        return sum(1 for char in self.text if char in self.consonants)
    
    def count_punctuation(self):
        """Count punctuation marks"""
        return sum(1 for char in self.text if char in self.punctuation)
    
    def get_unique_words(self):
        """Get unique words from text"""
        words = self.text.lower().split()
        # Remove punctuation from words
        clean_words = []
        for word in words:
            clean_word = ''.join(c for c in word if c not in self.punctuation)
            if clean_word:
                clean_words.append(clean_word)
        return set(clean_words)
    
    def get_stop_words_used(self):
        """Get stop words present in text"""
        words = self.get_unique_words()
        return words.intersection(self.stop_words)
    
    def get_content_words(self):
        """Get non-stop words"""
        words = self.get_unique_words()
        return words - self.stop_words
    
    def contains_word(self, word):
        """Check if text contains specific word"""
        words = self.get_unique_words()
        return word.lower() in words
    
    def contains_any(self, *words):
        """Check if text contains any of the given words"""
        text_words = self.get_unique_words()
        return any(word.lower() in text_words for word in words)
    
    def contains_all(self, *words):
        """Check if text contains all given words"""
        text_words = self.get_unique_words()
        return all(word.lower() in text_words for word in words)
    
    def get_statistics(self):
        """Get text statistics"""
        words = self.text.split()
        unique_words = self.get_unique_words()
        
        return {
            'characters': len(self.text),
            'words': len(words),
            'unique_words': len(unique_words),
            'vowels': self.count_vowels(),
            'consonants': self.count_consonants(),
            'punctuation': self.count_punctuation(),
            'stop_words_used': len(self.get_stop_words_used()),
            'content_words': len(self.get_content_words())
        }

# Demo
sample_text = """
The quick brown fox jumps over the lazy dog. Python is an amazing programming language! 
Is it easy to learn? Yes, with practice and dedication, anyone can learn Python.
"""

analyzer = TextAnalyzer(sample_text)

print("=== Text Analyzer Demo ===")
print("-" * 40)
print(f"Text: {sample_text[:100]}...")
print("\n=== Statistics ===")
stats = analyzer.get_statistics()
for key, value in stats.items():
    print(f"{key.replace('_', ' ').title()}: {value}")

print("\n=== Word Analysis ===")
print(f"Unique words: {sorted(analyzer.get_unique_words())[:10]}...")
print(f"Stop words used: {analyzer.get_stop_words_used()}")
print(f"Content words (first 10): {sorted(analyzer.get_content_words())[:10]}")

print("\n=== Word Search ===")
search_words = ['python', 'java', 'programming', 'difficult']
for word in search_words:
    found = analyzer.contains_word(word)
    print(f"Contains '{word}': {found}")

print("\n=== Multiple Word Search ===")
print(f"Contains any of ['python', 'java']: {analyzer.contains_any('python', 'java')}")
print(f"Contains all of ['python', 'learn']: {analyzer.contains_all('python', 'learn')}")
print(f"Contains all of ['python', 'java']: {analyzer.contains_all('python', 'java')}")
```

### Example 4: Permission Checker System
```python
class PermissionChecker:
    """Advanced permission checking with membership"""
    
    def __init__(self):
        self.roles = {
            'admin': {'read', 'write', 'delete', 'execute', 'manage_users'},
            'manager': {'read', 'write', 'delete', 'approve'},
            'editor': {'read', 'write', 'edit'},
            'viewer': {'read'},
            'guest': {'read_public'}
        }
        
        self.user_roles = {
            'alice': 'admin',
            'bob': 'manager',
            'charlie': 'editor',
            'diana': 'viewer',
            'eve': 'guest'
        }
        
        self.resource_permissions = {
            '/dashboard': {'read', 'write'},
            '/admin_panel': {'manage_users', 'delete'},
            '/reports': {'read', 'approve'},
            '/settings': {'read', 'write'},
            '/public': {'read_public'}
        }
    
    def get_user_permissions(self, username):
        """Get all permissions for a user"""
        if username not in self.user_roles:
            return set()
        
        role = self.user_roles[username]
        return self.roles.get(role, set())
    
    def has_permission(self, username, permission):
        """Check if user has specific permission"""
        permissions = self.get_user_permissions(username)
        return permission in permissions
    
    def has_any_permission(self, username, *permissions):
        """Check if user has any of the given permissions"""
        user_perms = self.get_user_permissions(username)
        return any(perm in user_perms for perm in permissions)
    
    def has_all_permissions(self, username, *permissions):
        """Check if user has all given permissions"""
        user_perms = self.get_user_permissions(username)
        return all(perm in user_perms for perm in permissions)
    
    def can_access_resource(self, username, resource):
        """Check if user can access a resource"""
        if resource not in self.resource_permissions:
            return False
        
        required_perms = self.resource_permissions[resource]
        user_perms = self.get_user_permissions(username)
        
        return required_perms.issubset(user_perms)
    
    def get_accessible_resources(self, username):
        """Get all resources user can access"""
        accessible = []
        for resource, required_perms in self.resource_permissions.items():
            if required_perms.issubset(self.get_user_permissions(username)):
                accessible.append(resource)
        return accessible
    
    def get_users_with_permission(self, permission):
        """Get all users having a specific permission"""
        users = []
        for username in self.user_roles:
            if self.has_permission(username, permission):
                users.append(username)
        return users

# Demo
checker = PermissionChecker()

print("=== Permission Checker Demo ===")
print("-" * 40)

# User permissions
users = ['alice', 'bob', 'charlie', 'diana', 'eve']
for user in users:
    perms = checker.get_user_permissions(user)
    role = checker.user_roles.get(user, 'unknown')
    print(f"{user} ({role}): {', '.join(sorted(perms)) if perms else 'No permissions'}")

print("\n=== Permission Checks ===")
test_cases = [
    ('alice', 'delete'),
    ('alice', 'manage_users'),
    ('bob', 'delete'),
    ('bob', 'manage_users'),
    ('charlie', 'delete'),
    ('diana', 'write'),
    ('eve', 'read')
]

for user, perm in test_cases:
    has_perm = checker.has_permission(user, perm)
    print(f"{user} has '{perm}': {has_perm}")

print("\n=== Resource Access ===")
for user in users:
    print(f"\n{user}:")
    for resource in ['/dashboard', '/admin_panel', '/reports', '/settings', '/public']:
        can_access = checker.can_access_resource(user, resource)
        print(f"  {resource}: {'✓' if can_access else '✗'}")

print("\n=== Accessible Resources ===")
for user in users:
    accessible = checker.get_accessible_resources(user)
    print(f"{user}: {accessible if accessible else 'None'}")

print("\n=== Users with Specific Permissions ===")
permissions = ['delete', 'manage_users', 'approve', 'write']
for perm in permissions:
    users_with = checker.get_users_with_permission(perm)
    print(f"'{perm}': {users_with if users_with else 'None'}")

print("\n=== Complex Permission Checks ===")
print(f"Bob has any of ['delete', 'manage_users']: {checker.has_any_permission('bob', 'delete', 'manage_users')}")
print(f"Bob has all of ['read', 'write']: {checker.has_all_permissions('bob', 'read', 'write')}")
print(f"Charlie has all of ['read', 'write', 'edit']: {checker.has_all_permissions('charlie', 'read', 'write', 'edit')}")
```

### Example 5: Log Filter and Analyzer
```python
from datetime import datetime
from collections import defaultdict

class LogAnalyzer:
    """Log analysis using membership operators"""
    
    def __init__(self):
        self.logs = []
        self.log_levels = {'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'}
        self.keywords = {'error', 'failed', 'exception', 'timeout', 'crash'}
        self.sources = {'web', 'api', 'database', 'cache', 'worker'}
    
    def add_log(self, timestamp, level, source, message):
        """Add a log entry"""
        if level not in self.log_levels:
            raise ValueError(f"Invalid log level: {level}")
        
        if source not in self.sources:
            raise ValueError(f"Invalid source: {source}")
        
        self.logs.append({
            'timestamp': timestamp,
            'level': level,
            'source': source,
            'message': message
        })
    
    def filter_by_level(self, *levels):
        """Filter logs by level"""
        return [log for log in self.logs if log['level'] in levels]
    
    def filter_by_source(self, *sources):
        """Filter logs by source"""
        return [log for log in self.logs if log['source'] in sources]
    
    def filter_by_keyword(self, *keywords):
        """Filter logs containing keywords"""
        return [log for log in self.logs 
                if any(keyword in log['message'].lower() for keyword in keywords)]
    
    def filter_by_time_range(self, start_time, end_time):
        """Filter logs by time range"""
        return [log for log in self.logs 
                if start_time <= log['timestamp'] <= end_time]
    
    def get_error_logs(self):
        """Get all ERROR and CRITICAL logs"""
        return self.filter_by_level('ERROR', 'CRITICAL')
    
    def get_warning_logs(self):
        """Get all WARNING logs"""
        return self.filter_by_level('WARNING')
    
    def get_logs_containing(self, *keywords):
        """Get logs containing any of the keywords"""
        return self.filter_by_keyword(*keywords)
    
    def get_statistics(self):
        """Get log statistics"""
        stats = {
            'total': len(self.logs),
            'by_level': defaultdict(int),
            'by_source': defaultdict(int),
            'has_errors': False,
            'has_warnings': False,
            'critical_count': 0
        }
        
        for log in self.logs:
            stats['by_level'][log['level']] += 1
            stats['by_source'][log['source']] += 1
            
            if log['level'] in {'ERROR', 'CRITICAL'}:
                stats['has_errors'] = True
            if log['level'] == 'WARNING':
                stats['has_warnings'] = True
            if log['level'] == 'CRITICAL':
                stats['critical_count'] += 1
        
        return stats
    
    def get_problematic_sources(self):
        """Get sources that have errors"""
        error_logs = self.get_error_logs()
        return set(log['source'] for log in error_logs)
    
    def get_recent_errors(self, minutes=5):
        """Get errors from last N minutes"""
        from datetime import timedelta
        now = datetime.now()
        cutoff = now - timedelta(minutes=minutes)
        return [log for log in self.get_error_logs() 
                if log['timestamp'] >= cutoff]

# Demo
analyzer = LogAnalyzer()

print("=== Log Analyzer Demo ===")
print("-" * 40)

# Add sample logs
logs_data = [
    (datetime(2024, 1, 15, 10, 30, 0), 'INFO', 'web', 'User login successful'),
    (datetime(2024, 1, 15, 10, 31, 0), 'INFO', 'api', 'API request processed'),
    (datetime(2024, 1, 15, 10, 32, 0), 'WARNING', 'database', 'Slow query detected'),
    (datetime(2024, 1, 15, 10, 33, 0), 'ERROR', 'database', 'Connection failed'),
    (datetime(2024, 1, 15, 10, 34, 0), 'INFO', 'cache', 'Cache hit'),
    (datetime(2024, 1, 15, 10, 35, 0), 'ERROR', 'api', 'API timeout error'),
    (datetime(2024, 1, 15, 10, 36, 0), 'CRITICAL', 'database', 'Database crash'),
    (datetime(2024, 1, 15, 10, 37, 0), 'INFO', 'worker', 'Task completed'),
    (datetime(2024, 1, 15, 10, 38, 0), 'WARNING', 'web', 'Slow response time')
]

for timestamp, level, source, message in logs_data:
    analyzer.add_log(timestamp, level, source, message)

# Statistics
stats = analyzer.get_statistics()
print("\n=== Statistics ===")
print(f"Total logs: {stats['total']}")
print(f"By level: {dict(stats['by_level'])}")
print(f"By source: {dict(stats['by_source'])}")
print(f"Has errors: {stats['has_errors']}")
print(f"Has warnings: {stats['has_warnings']}")
print(f"Critical count: {stats['critical_count']}")

# Filter examples
print("\n=== Filter Examples ===")
print(f"ERROR logs: {len(analyzer.get_error_logs())}")
print(f"WARNING logs: {len(analyzer.get_warning_logs())}")

# Filter by source
db_logs = analyzer.filter_by_source('database')
print(f"Database logs: {len(db_logs)}")

# Filter by keyword
error_logs = analyzer.filter_by_keyword('error', 'failed', 'crash')
print(f"Logs with error keywords: {len(error_logs)}")
for log in error_logs:
    print(f"  {log['timestamp']}: {log['message']}")

# Problematic sources
problem_sources = analyzer.get_problematic_sources()
print(f"\nProblematic sources: {problem_sources}")

# Complex filtering
print("\n=== Complex Filter ===")
critical_db = [log for log in analyzer.logs 
               if log['level'] in {'ERROR', 'CRITICAL'} 
               and log['source'] in {'database', 'api'}
               and 'fail' in log['message'].lower()]

print(f"Critical DB/API failures: {len(critical_db)}")
for log in critical_db:
    print(f"  {log['timestamp']}: [{log['level']}] {log['source']} - {log['message']}")
```

### Example 6: Tag Management System
```python
class TagManager:
    """Tag management using membership operators"""
    
    def __init__(self):
        self.items = {}
        self.tag_index = defaultdict(set)
        self.all_tags = set()
    
    def add_item(self, item_id, name, tags):
        """Add item with tags"""
        if item_id in self.items:
            print(f"Item {item_id} already exists")
            return False
        
        tags_set = set(tags)
        self.items[item_id] = {
            'name': name,
            'tags': tags_set
        }
        
        for tag in tags_set:
            self.tag_index[tag].add(item_id)
            self.all_tags.add(tag)
        
        return True
    
    def update_tags(self, item_id, tags):
        """Update item tags"""
        if item_id not in self.items:
            return False
        
        old_tags = self.items[item_id]['tags']
        new_tags = set(tags)
        
        # Remove from old tags
        for tag in old_tags - new_tags:
            self.tag_index[tag].discard(item_id)
            if not self.tag_index[tag]:
                del self.tag_index[tag]
                self.all_tags.discard(tag)
        
        # Add to new tags
        for tag in new_tags - old_tags:
            self.tag_index[tag].add(item_id)
            self.all_tags.add(tag)
        
        self.items[item_id]['tags'] = new_tags
        return True
    
    def get_items_by_tag(self, tag):
        """Get all items with a specific tag"""
        if tag not in self.all_tags:
            return []
        return [self.items[item_id] for item_id in self.tag_index[tag]]
    
    def get_items_by_tags(self, tags, require_all=False):
        """Get items with any or all of the given tags"""
        if require_all:
            # Items that have ALL the tags
            result_items = None
            for tag in tags:
                if tag not in self.tag_index:
                    return []
                tag_items = self.tag_index[tag]
                if result_items is None:
                    result_items = tag_items
                else:
                    result_items &= tag_items
                if not result_items:
                    return []
            return [self.items[item_id] for item_id in result_items]
        else:
            # Items that have ANY of the tags
            result_items = set()
            for tag in tags:
                if tag in self.tag_index:
                    result_items.update(self.tag_index[tag])
            return [self.items[item_id] for item_id in result_items]
    
    def get_items_without_tag(self, tag):
        """Get items that don't have a specific tag"""
        if tag not in self.all_tags:
            return list(self.items.values())
        
        items_with_tag = self.tag_index[tag]
        return [item for item_id, item in self.items.items() 
                if item_id not in items_with_tag]
    
    def get_related_tags(self, tag):
        """Get tags that appear with the given tag"""
        if tag not in self.all_tags:
            return set()
        
        related = set()
        for item_id in self.tag_index[tag]:
            related.update(self.items[item_id]['tags'])
        related.discard(tag)
        return related
    
    def get_tag_statistics(self):
        """Get statistics about tags"""
        return {
            'total_tags': len(self.all_tags),
            'total_items': len(self.items),
            'tags_per_item': sum(len(item['tags']) for item in self.items.values()) / len(self.items) if self.items else 0,
            'most_used_tag': max(self.tag_index.items(), key=lambda x: len(x[1]))[0] if self.tag_index else None,
            'least_used_tag': min(self.tag_index.items(), key=lambda x: len(x[1]))[0] if self.tag_index else None
        }

# Demo
manager = TagManager()

print("=== Tag Manager Demo ===")
print("-" * 40)

# Add items
items_data = [
    (1, "Python Tutorial", {"python", "programming", "beginner"}),
    (2, "Advanced Python", {"python", "programming", "advanced"}),
    (3, "Data Science Guide", {"python", "data", "machine-learning"}),
    (4, "Web Development", {"javascript", "html", "css"}),
    (5, "Flask Framework", {"python", "web", "framework"}),
    (6, "Django Tutorial", {"python", "web", "framework", "beginner"})
]

for item_id, name, tags in items_data:
    manager.add_item(item_id, name, tags)
    print(f"Added: {name}")

print("\n=== Tag Statistics ===")
stats = manager.get_tag_statistics()
for key, value in stats.items():
    print(f"{key.replace('_', ' ').title()}: {value}")

print(f"\nAll tags: {sorted(manager.all_tags)}")

print("\n=== Get Items by Tag ===")
test_tags = ['python', 'web', 'beginner']
for tag in test_tags:
    items = manager.get_items_by_tag(tag)
    print(f"'{tag}': {[item['name'] for item in items]}")

print("\n=== Get Items by Multiple Tags ===")
print("Items with ANY of ['python', 'web']:")
items = manager.get_items_by_tags(['python', 'web'], require_all=False)
for item in items:
    print(f"  - {item['name']} ({', '.join(item['tags'])})")

print("\nItems with ALL of ['python', 'web']:")
items = manager.get_items_by_tags(['python', 'web'], require_all=True)
for item in items:
    print(f"  - {item['name']} ({', '.join(item['tags'])})")

print("\n=== Items Without Tag ===")
items = manager.get_items_without_tag('beginner')
print(f"Items without 'beginner' tag: {[item['name'] for item in items]}")

print("\n=== Related Tags ===")
for tag in ['python', 'web']:
    related = manager.get_related_tags(tag)
    print(f"Tags related to '{tag}': {sorted(related)}")

print("\n=== Update Tags ===")
manager.update_tags(1, {"python", "programming", "intermediate"})
item = manager.items[1]
print(f"Updated Python Tutorial tags: {item['tags']}")

print("\n=== Final Tag Statistics ===")
stats = manager.get_tag_statistics()
for key, value in stats.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
```

## Membership with Custom Classes

```python
class Course:
    """Course class with custom membership behavior"""
    
    def __init__(self, name, students):
        self.name = name
        self.students = students
    
    def __contains__(self, student):
        """Customize 'in' operator behavior"""
        return student in self.students
    
    def __iter__(self):
        """Make course iterable"""
        return iter(self.students)

# Custom class with __contains__
class Playlist:
    def __init__(self):
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
    
    def __contains__(self, song):
        """Check if song is in playlist"""
        return any(song.lower() in s.lower() for s in self.songs)

# Demo
print("\n=== Custom Class Membership ===")

# Course example
course = Course("Python 101", ["Alice", "Bob", "Charlie"])
print(f"'Alice' in course: {'Alice' in course}")  # True
print(f"'Dave' in course: {'Dave' in course}")    # False

# Iteration works automatically
print(f"Students: {', '.join(course)}")

# Playlist example
playlist = Playlist()
playlist.add_song("Shape of You")
playlist.add_song("Blinding Lights")
playlist.add_song("Rolling in the Deep")

print(f"'shape' in playlist: {'shape' in playlist}")  # True (case-insensitive)
print(f"'hello' in playlist: {'hello' in playlist}")  # False
```

## Common Mistakes

### Mistake 1: Using in with Dictionaries Incorrectly
```python
# Wrong - checking values instead of keys
person = {'name': 'Alice', 'age': 30}
if 'Alice' in person:  # False (checks keys, not values)
    print("Found")

# Right - check keys
if 'name' in person:  # True
    print("Key exists")

# Right - check values
if 'Alice' in person.values():  # True
    print("Value exists")
```

### Mistake 2: Case Sensitivity
```python
# Wrong - case-sensitive by default
text = "Hello World"
if "hello" in text:  # False (case mismatch)
    print("Found")

# Right - convert to same case
if "hello" in text.lower():  # True
    print("Found")
```

### Mistake 3: Using in with None
```python
# Wrong - None is not iterable
value = None
# if 5 in value:  # TypeError!

# Right - check for None first
if value is not None and 5 in value:
    print("Found")
```

### Mistake 4: String vs Substring Confusion
```python
# This works but might not be what you want
words = ['cat', 'dog', 'bird']
if 'cat' in words:  # True (exact match)
    print("Found cat")

# But for strings, 'in' checks substrings
text = "The cat sat"
if 'cat' in text:  # True (substring)
    print("Found cat")
```

### Mistake 5: Performance with Large Lists
```python
# Wrong - slow for large lists
large_list = list(range(1000000))
if 999999 in large_list:  # O(n) - slow
    print("Found")

# Right - use set for fast membership
large_set = set(range(1000000))
if 999999 in large_set:  # O(1) - fast
    print("Found")
```

## Performance Comparison

```python
import time

# Different data structures performance
test_size = 100000
test_value = test_size - 1

# List membership (O(n))
my_list = list(range(test_size))
start = time.time()
result = test_value in my_list
list_time = time.time() - start

# Set membership (O(1))
my_set = set(range(test_size))
start = time.time()
result = test_value in my_set
set_time = time.time() - start

# Tuple membership (O(n))
my_tuple = tuple(range(test_size))
start = time.time()
result = test_value in my_tuple
tuple_time = time.time() - start

# Range membership (O(1) optimized)
my_range = range(test_size)
start = time.time()
result = test_value in my_range
range_time = time.time() - start

print(f"\n=== Performance for {test_size} elements ===")
print(f"List:  {list_time:.6f}s (O(n))")
print(f"Tuple: {tuple_time:.6f}s (O(n))")
print(f"Set:   {set_time:.6f}s (O(1))")
print(f"Range: {range_time:.6f}s (O(1) optimized)")
```

## Quick Reference Table

| Collection | in Operator Behavior | Example | Time Complexity |
|------------|---------------------|---------|-----------------|
| list | Checks for element | `5 in [1,2,3,4,5]` | O(n) |
| tuple | Checks for element | `5 in (1,2,3,4,5)` | O(n) |
| set | Checks for element | `5 in {1,2,3,4,5}` | O(1) |
| dict | Checks keys | `'name' in {'name':'Alice'}` | O(1) |
| str | Checks substring | `'lo' in 'hello'` | O(n) |
| range | Checks value in range | `5 in range(10)` | O(1) |

## Summary

- **`in`** checks if a value exists in a collection
- **`not in`** checks if a value does NOT exist
- **Strings**: checks for substrings
- **Dictionaries**: checks keys (not values)
- **Sets**: fastest membership testing (O(1))
- **Lists/Tuples**: slower membership (O(n))
- **Ranges**: optimized membership checking
- **Custom classes** can implement `__contains__`
- **Case sensitivity** matters for strings
- **Use `in` for readability** over manual loops

## Basic Template
```python
#!/usr/bin/env python3

def list_membership():
    """Demonstrate list membership"""
    fruits = ['apple', 'banana', 'orange', 'grape']
    
    print(f"Fruits: {fruits}")
    print(f"'apple' in fruits: {'apple' in fruits}")
    print(f"'mango' in fruits: {'mango' in fruits}")
    print(f"'grape' not in fruits: {'grape' not in fruits}")

def string_membership():
    """Demonstrate string membership"""
    text = "Hello, World!"
    
    print(f"\nText: '{text}'")
    print(f"'Hello' in text: {'Hello' in text}")
    print(f"'world' in text: {'world' in text} (case-sensitive)")
    print(f"'world' in text.lower(): {'world' in text.lower()}")
    print(f"'xyz' not in text: {'xyz' not in text}")

def dict_membership():
    """Demonstrate dictionary membership"""
    person = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
    
    print(f"\nPerson: {person}")
    print(f"'name' in person: {'name' in person} (checks keys)")
    print(f"'Alice' in person: {'Alice' in person} (False - checks keys)")
    print(f"'Alice' in person.values(): {'Alice' in person.values()}")
    print(f"('name', 'Alice') in person.items(): {('name', 'Alice') in person.items()}")

def set_membership():
    """Demonstrate set membership (fastest)"""
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    
    print(f"\nNumbers: {numbers}")
    print(f"5 in numbers: {5 in numbers}")
    print(f"15 in numbers: {15 in numbers}")
    
    # Set operations with membership
    evens = {2, 4, 6, 8, 10}
    print(f"Evens subset: {evens.issubset(numbers)}")
    print(f"All evens in numbers: {all(n in numbers for n in evens)}")

def custom_membership():
    """Custom class with __contains__"""
    
    class Team:
        def __init__(self, name, members):
            self.name = name
            self.members = members
        
        def __contains__(self, member):
            return member in self.members
    
    team = Team("Developers", ["Alice", "Bob", "Charlie"])
    
    print(f"\nTeam: {team.name}")
    print(f"Members: {team.members}")
    print(f"'Bob' in team: {'Bob' in team}")
    print(f"'Dave' in team: {'Dave' in team}")

def practical_example():
    """Practical membership example"""
    
    # Validate user input
    valid_commands = {'start', 'stop', 'pause', 'resume', 'exit'}
    
    def process_command(cmd):
        if cmd in valid_commands:
            print(f"Executing: {cmd}")
        else:
            print(f"Invalid command: {cmd}")
    
    print("\n=== Command Processor ===")
    test_commands = ['start', 'stop', 'jump', 'exit']
    for cmd in test_commands:
        process_command(cmd)

if __name__ == "__main__":
    print("=== MEMBERSHIP OPERATORS ===\n")
    list_membership()
    string_membership()
    dict_membership()
    set_membership()
    custom_membership()
    practical_example()
```

*This documentation belongs to https://github.com/InterCentury*