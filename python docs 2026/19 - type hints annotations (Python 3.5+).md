# 19 - Type Hints and Annotations (Python 3.5+)

## What are Type Hints?
Type hints (or type annotations) are a way to indicate the expected data types of variables, function parameters, and return values. They were introduced in Python 3.5 (PEP 484) and are **optional** - Python ignores them at runtime, but they help with documentation, IDE support, and static type checking.

## Basic Type Hints

### Variable Annotations
```python
# Basic type hints for variables
name: str = "Alice"
age: int = 25
price: float = 19.99
is_active: bool = True
items: list = [1, 2, 3]

# Without initialization (just declaration)
user_id: int
user_id = 123  # Later assignment

# Multiple variables
x: int = 10
y: int = 20
z: float = 3.14

# Python ignores type hints - these work!
name: str = 123  # No error! (but type checker would complain)
age: int = "twenty"  # No error!
```

### Function Annotations
```python
# Basic function with type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    return a + b

def calculate_average(numbers: list) -> float:
    return sum(numbers) / len(numbers)

# Multiple parameters
def create_user(name: str, age: int, email: str) -> dict:
    return {"name": name, "age": age, "email": email}

# Default values with type hints
def process_data(data: list, max_items: int = 100) -> list:
    return data[:max_items]

# No return value (returns None)
def log_message(message: str) -> None:
    print(f"[LOG] {message}")
```

## Built-in Type Hints

### Simple Types
```python
from typing import List, Dict, Tuple, Set, Optional, Union, Any

# Basic types
age: int = 25
name: str = "Alice"
price: float = 19.99
is_valid: bool = True
data: bytes = b"binary data"

# Collections (Python 3.9+ allows built-in generics)
# Python 3.9+:
numbers: list[int] = [1, 2, 3, 4, 5]
names: list[str] = ["Alice", "Bob", "Charlie"]
scores: dict[str, int] = {"Alice": 95, "Bob": 87}
point: tuple[int, int] = (10, 20)
unique_ids: set[int] = {1, 2, 3}

# Python 3.8 and earlier (need typing module):
# numbers: List[int] = [1, 2, 3, 4, 5]
# names: List[str] = ["Alice", "Bob", "Charlie"]
# scores: Dict[str, int] = {"Alice": 95, "Bob": 87}
# point: Tuple[int, int] = (10, 20)
# unique_ids: Set[int] = {1, 2, 3}
```

### Optional and Union Types
```python
from typing import Optional, Union

# Optional means value can be None
def find_user(user_id: int) -> Optional[str]:
    """Returns username or None if not found"""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

# Union means multiple possible types
def process_value(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Number: {value}"
    else:
        return f"String: {value}"

# Python 3.10+ shorthand (use | instead of Union)
# def process_value(value: int | str) -> str:
#     return f"Value: {value}"

# Optional[X] is same as Union[X, None]
def get_config(key: str) -> Optional[str]:
    config = {"host": "localhost", "port": "8080"}
    return config.get(key)
```

### Any Type
```python
from typing import Any

# Any means no type checking (like dynamic typing)
def flexible_function(data: Any) -> Any:
    return data

# Can accept and return anything
result1: Any = flexible_function(42)
result2: Any = flexible_function("hello")
result3: Any = flexible_function([1, 2, 3])

# Use sparingly - defeats purpose of type hints
```

## Advanced Type Hints

### Lists and Collections
```python
from typing import List, Dict, Tuple, Set, Sequence, Iterable, Iterator

# Nested lists
matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# List of dictionaries
users: list[dict[str, Any]] = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

# Tuple with specific types
person: tuple[str, int, float] = ("Alice", 25, 5.6)

# Tuple of variable length
tags: tuple[str, ...] = ("python", "coding", "tutorial")

# Dictionary with specific key/value types
config: dict[str, Union[int, str, bool]] = {
    "debug": True,
    "port": 8080,
    "host": "localhost"
}

# Sequence (read-only collection)
def process_sequence(items: Sequence[int]) -> int:
    return sum(items)

# Iterable (can be used in for loops)
def print_items(items: Iterable[str]) -> None:
    for item in items:
        print(item)
```

### Type Aliases
```python
from typing import List, Dict, Tuple, Union

# Create aliases for complex types
UserId = int
UserName = str
UserInfo = Dict[str, Union[str, int]]

# Use aliases
def get_user_info(user_id: UserId) -> UserInfo:
    return {"id": user_id, "name": "Alice", "age": 25}

# More complex alias
Point = Tuple[float, float]
Rectangle = Tuple[Point, Point]  # (top-left, bottom-right)

def area(rect: Rectangle) -> float:
    (x1, y1), (x2, y2) = rect
    return abs(x2 - x1) * abs(y2 - y1)

# Generic alias
from typing import TypeVar, Generic

T = TypeVar('T')
Stack = List[T]

def push(stack: Stack[T], item: T) -> None:
    stack.append(item)
```

### Callable Types
```python
from typing import Callable

# Function that takes two ints and returns int
operation: Callable[[int, int], int] = lambda x, y: x + y

def apply_operation(x: int, y: int, func: Callable[[int, int], int]) -> int:
    return func(x, y)

# Function with no arguments, returns str
def get_message() -> str:
    return "Hello"

message_func: Callable[[], str] = get_message

# Function that takes a string and returns nothing
def log(message: str) -> None:
    print(message)

logger: Callable[[str], None] = log

# Complex callback
def process_data(data: list[int], 
                callback: Callable[[list[int]], int]) -> int:
    return callback(data)
```

### Type Variables and Generics
```python
from typing import TypeVar, Generic, List

# Simple type variable
T = TypeVar('T')

def first_element(items: List[T]) -> T:
    return items[0] if items else None

# Generic class
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()
    
    def peek(self) -> T:
        return self._items[-1]

# Usage
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
value: int = int_stack.pop()

str_stack = Stack[str]()
str_stack.push("hello")
text: str = str_stack.pop()

# Multiple type variables
K = TypeVar('K')
V = TypeVar('V')

class Pair(Generic[K, V]):
    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value
```

### Literal Types
```python
from typing import Literal

# Function that only accepts specific values
def set_status(status: Literal['active', 'inactive', 'pending']) -> None:
    print(f"Status set to: {status}")

set_status('active')    # OK
set_status('pending')   # OK
# set_status('unknown') # Type checker error

# Multiple literal values
def http_method(method: Literal['GET', 'POST', 'PUT', 'DELETE']) -> str:
    return f"Using {method} method"

# Literal with numbers
def set_priority(priority: Literal[1, 2, 3, 4, 5]) -> None:
    print(f"Priority: {priority}")
```

### TypedDict
```python
from typing import TypedDict, Optional

# Define dictionary structure
class User(TypedDict):
    name: str
    age: int
    email: str
    phone: Optional[str]

# Use typed dict
def create_user(user: User) -> None:
    print(f"Creating user: {user['name']}, {user['age']}")

# Valid usage
alice: User = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com",
    "phone": None
}

# Type checker would catch missing keys
# bob: User = {
#     "name": "Bob",
#     "age": 30
#     # Missing email - error!
# }

# Total=False makes all keys optional
class PartialUser(TypedDict, total=False):
    name: str
    age: int
    email: str

def update_user(user_id: int, updates: PartialUser) -> None:
    print(f"Updating user {user_id}: {updates}")
```

## Practical Examples

### Example 1: Data Validation with Type Hints
```python
from typing import List, Dict, Optional, Union, Any
from datetime import datetime

class DataValidator:
    """Validate data using type hints"""
    
    @staticmethod
    def validate_type(value: Any, expected_type: type) -> bool:
        """Check if value matches expected type"""
        return isinstance(value, expected_type)
    
    @staticmethod
    def validate_user(user: Dict[str, Any]) -> List[str]:
        """Validate user dictionary using type hints"""
        errors = []
        
        # Expected types for each field
        type_map = {
            'name': str,
            'age': int,
            'email': str,
            'scores': list,
            'is_active': bool,
            'created_at': datetime
        }
        
        for field, expected_type in type_map.items():
            if field not in user:
                errors.append(f"Missing field: {field}")
            elif not isinstance(user[field], expected_type):
                errors.append(
                    f"Field '{field}' should be {expected_type.__name__}, "
                    f"got {type(user[field]).__name__}"
                )
        
        # Additional validation
        if 'age' in user and user['age'] not in range(0, 151):
            errors.append("Age must be between 0 and 150")
        
        if 'email' in user and '@' not in user['email']:
            errors.append("Invalid email format")
        
        return errors

# Example usage
valid_user = {
    'name': 'Alice',
    'age': 25,
    'email': 'alice@example.com',
    'scores': [85, 92, 88],
    'is_active': True,
    'created_at': datetime.now()
}

invalid_user = {
    'name': 'Bob',
    'age': 'thirty',  # Wrong type
    'email': 'invalid',
    'is_active': 'yes'  # Wrong type
    # Missing scores and created_at
}

validator = DataValidator()
print("Valid user errors:", validator.validate_user(valid_user))
print("Invalid user errors:", validator.validate_user(invalid_user))
```

### Example 2: Repository Pattern with Generics
```python
from typing import TypeVar, Generic, List, Optional, Dict, Any
from abc import ABC, abstractmethod

T = TypeVar('T')
ID = TypeVar('ID')

class Repository(Generic[T, ID], ABC):
    """Generic repository interface"""
    
    @abstractmethod
    def get(self, id: ID) -> Optional[T]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[T]:
        pass
    
    @abstractmethod
    def add(self, entity: T) -> T:
        pass
    
    @abstractmethod
    def update(self, id: ID, entity: T) -> Optional[T]:
        pass
    
    @abstractmethod
    def delete(self, id: ID) -> bool:
        pass

class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
    
    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, email={self.email})"

class InMemoryUserRepository(Repository[User, int]):
    """In-memory implementation of user repository"""
    
    def __init__(self):
        self._storage: Dict[int, User] = {}
        self._next_id = 1
    
    def get(self, id: int) -> Optional[User]:
        return self._storage.get(id)
    
    def get_all(self) -> List[User]:
        return list(self._storage.values())
    
    def add(self, user: User) -> User:
        if user.id == 0:
            user.id = self._next_id
            self._next_id += 1
        self._storage[user.id] = user
        return user
    
    def update(self, id: int, user: User) -> Optional[User]:
        if id in self._storage:
            user.id = id
            self._storage[id] = user
            return user
        return None
    
    def delete(self, id: int) -> bool:
        if id in self._storage:
            del self._storage[id]
            return True
        return False

# Usage
repo: Repository[User, int] = InMemoryUserRepository()

# Add users
alice = User(0, "Alice", "alice@example.com")
bob = User(0, "Bob", "bob@example.com")

repo.add(alice)
repo.add(bob)

print("All users:", repo.get_all())
print("Get user 1:", repo.get(1))

# Update user
updated_alice = User(1, "Alice Smith", "alice.smith@example.com")
repo.update(1, updated_alice)
print("After update:", repo.get(1))

# Delete user
repo.delete(2)
print("After deletion:", repo.get_all())
```

### Example 3: API Client with Type Hints
```python
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass
import json
from datetime import datetime

@dataclass
class Product:
    """Product data model"""
    id: int
    name: str
    price: float
    category: str
    in_stock: bool
    tags: List[str]
    created_at: datetime

@dataclass
class Order:
    """Order data model"""
    id: int
    user_id: int
    products: List[Product]
    total: float
    status: str
    created_at: datetime

class APIClient:
    """API client with type hints"""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url
        self.api_key = api_key
        self._session: Dict[str, Any] = {}
    
    def get_product(self, product_id: int) -> Optional[Product]:
        """Fetch product by ID"""
        # Simulate API call
        if product_id == 1:
            return Product(
                id=1,
                name="Laptop",
                price=999.99,
                category="Electronics",
                in_stock=True,
                tags=["computer", "portable"],
                created_at=datetime.now()
            )
        return None
    
    def get_products(self, 
                    category: Optional[str] = None,
                    in_stock_only: bool = False,
                    limit: int = 10) -> List[Product]:
        """Get products with filters"""
        products = [
            Product(1, "Laptop", 999.99, "Electronics", True, ["computer"], datetime.now()),
            Product(2, "Mouse", 29.99, "Electronics", True, ["accessory"], datetime.now()),
            Product(3, "Keyboard", 79.99, "Electronics", False, ["accessory"], datetime.now()),
            Product(4, "Book", 19.99, "Books", True, ["reading"], datetime.now()),
        ]
        
        # Apply filters
        if category:
            products = [p for p in products if p.category == category]
        
        if in_stock_only:
            products = [p for p in products if p.in_stock]
        
        return products[:limit]
    
    def create_order(self, user_id: int, product_ids: List[int]) -> Order:
        """Create new order"""
        products = []
        total = 0.0
        
        for pid in product_ids:
            product = self.get_product(pid)
            if product:
                products.append(product)
                total += product.price
        
        return Order(
            id=hash(f"{user_id}{datetime.now()}"),
            user_id=user_id,
            products=products,
            total=total,
            status="pending",
            created_at=datetime.now()
        )
    
    def process_response(self, response: Union[str, bytes, dict]) -> Dict[str, Any]:
        """Process API response with union type"""
        if isinstance(response, str):
            return json.loads(response)
        elif isinstance(response, bytes):
            return json.loads(response.decode('utf-8'))
        elif isinstance(response, dict):
            return response
        else:
            raise TypeError(f"Unsupported response type: {type(response)}")

# Usage
client = APIClient("https://api.example.com", api_key="test-key")

# Get single product
product = client.get_product(1)
if product:
    print(f"Product: {product.name} - ${product.price}")

# Get filtered products
electronics = client.get_products(category="Electronics", in_stock_only=True)
print(f"\nIn-stock electronics: {len(electronics)}")
for p in electronics:
    print(f"  - {p.name}")

# Create order
order = client.create_order(123, [1, 2])
print(f"\nOrder #{order.id}: ${order.total}")
print(f"Products: {', '.join(p.name for p in order.products)}")
```

### Example 4: Function Overloading with Type Hints
```python
from typing import overload, Union, List, Dict, Any

class DataProcessor:
    """Function overloading using @overload"""
    
    @overload
    def process(self, data: str) -> str:
        """Process string data"""
        ...
    
    @overload
    def process(self, data: int) -> int:
        """Process integer data"""
        ...
    
    @overload
    def process(self, data: List[int]) -> List[int]:
        """Process list of integers"""
        ...
    
    def process(self, data: Union[str, int, List[int]]) -> Union[str, int, List[int]]:
        """Actual implementation"""
        if isinstance(data, str):
            return data.upper()
        elif isinstance(data, int):
            return data * 2
        elif isinstance(data, list):
            return [x * 2 for x in data]
        else:
            raise TypeError(f"Unsupported type: {type(data)}")
    
    @overload
    def calculate(self, a: int, b: int) -> int:
        ...
    
    @overload
    def calculate(self, a: float, b: float) -> float:
        ...
    
    @overload
    def calculate(self, a: str, b: str) -> str:
        ...
    
    def calculate(self, a: Union[int, float, str], 
                  b: Union[int, float, str]) -> Union[int, float, str]:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            raise TypeError("Incompatible types")

# Usage
processor = DataProcessor()

# String processing
result1: str = processor.process("hello")
print(f"String result: {result1}")

# Integer processing
result2: int = processor.process(42)
print(f"Integer result: {result2}")

# List processing
result3: List[int] = processor.process([1, 2, 3])
print(f"List result: {result3}")

# Calculate with different types
print(f"Int addition: {processor.calculate(5, 3)}")
print(f"Float addition: {processor.calculate(3.14, 2.86)}")
print(f"String concatenation: {processor.calculate('Hello', ' World')}")
```

### Example 5: Type Hints for Data Classes
```python
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

@dataclass
class Address:
    """Address data class with type hints"""
    street: str
    city: str
    state: str
    zip_code: str
    country: str = "USA"
    
    def full_address(self) -> str:
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}, {self.country}"

@dataclass
class User:
    """User data class with validation"""
    id: int
    username: str
    email: str
    role: UserRole
    created_at: datetime = field(default_factory=datetime.now)
    is_active: bool = True
    address: Optional[Address] = None
    tags: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate after initialization"""
        if not self.username or len(self.username) < 3:
            raise ValueError("Username must be at least 3 characters")
        
        if '@' not in self.email:
            raise ValueError("Invalid email format")
    
    def get_display_name(self) -> str:
        """Get display name based on role"""
        if self.role == UserRole.ADMIN:
            return f"{self.username} (Admin)"
        return self.username
    
    def has_tag(self, tag: str) -> bool:
        """Check if user has specific tag"""
        return tag in self.tags

@dataclass
class UserRepository:
    """Repository for user operations"""
    _users: Dict[int, User] = field(default_factory=dict)
    
    def add_user(self, user: User) -> None:
        """Add user to repository"""
        if user.id in self._users:
            raise ValueError(f"User with id {user.id} already exists")
        self._users[user.id] = user
    
    def get_user(self, user_id: int) -> Optional[User]:
        """Get user by ID"""
        return self._users.get(user_id)
    
    def get_active_users(self) -> List[User]:
        """Get all active users"""
        return [u for u in self._users.values() if u.is_active]
    
    def find_by_tag(self, tag: str) -> List[User]:
        """Find users with specific tag"""
        return [u for u in self._users.values() if u.has_tag(tag)]
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get repository statistics"""
        users = list(self._users.values())
        if not users:
            return {"total": 0, "active": 0, "roles": {}}
        
        roles = {}
        for role in UserRole:
            count = sum(1 for u in users if u.role == role)
            if count > 0:
                roles[role.value] = count
        
        return {
            "total": len(users),
            "active": sum(1 for u in users if u.is_active),
            "roles": roles,
            "avg_tag_count": sum(len(u.tags) for u in users) / len(users)
        }

# Usage
# Create address
address = Address(
    street="123 Main St",
    city="Boston",
    state="MA",
    zip_code="02101"
)

# Create users
alice = User(
    id=1,
    username="alice_wonder",
    email="alice@example.com",
    role=UserRole.ADMIN,
    address=address,
    tags=["python", "developer", "admin"]
)

bob = User(
    id=2,
    username="bob_builder",
    email="bob@example.com",
    role=UserRole.USER,
    tags=["python", "beginner"]
)

charlie = User(
    id=3,
    username="charlie",
    email="charlie@example.com",
    role=UserRole.USER,
    is_active=False
)

# Repository operations
repo = UserRepository()
repo.add_user(alice)
repo.add_user(bob)
repo.add_user(charlie)

print("=== User Information ===")
print(f"Alice: {alice.get_display_name()}")
print(f"Alice's address: {alice.address.full_address() if alice.address else 'None'}")

print("\n=== Repository Statistics ===")
stats = repo.get_statistics()
for key, value in stats.items():
    print(f"  {key}: {value}")

print("\n=== Users with 'python' tag ===")
python_users = repo.find_by_tag("python")
for user in python_users:
    print(f"  - {user.username}")
```

### Example 6: Type Hints with Context Managers
```python
from typing import ContextManager, Optional, Any, Generator
from contextlib import contextmanager
import sqlite3
from datetime import datetime

class DatabaseConnection:
    """Database connection with type hints"""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._connection: Optional[sqlite3.Connection] = None
    
    def __enter__(self) -> 'DatabaseConnection':
        """Enter context manager"""
        self._connection = sqlite3.connect(self.db_path)
        return self
    
    def __exit__(self, exc_type: Optional[type], 
                 exc_val: Optional[Exception], 
                 exc_tb: Optional[Any]) -> None:
        """Exit context manager"""
        if self._connection:
            if exc_type is None:
                self._connection.commit()
            else:
                self._connection.rollback()
            self._connection.close()
            self._connection = None
    
    def execute(self, query: str, params: tuple = ()) -> list:
        """Execute query and return results"""
        if not self._connection:
            raise RuntimeError("Not connected to database")
        
        cursor = self._connection.cursor()
        cursor.execute(query, params)
        
        if query.strip().upper().startswith('SELECT'):
            return cursor.fetchall()
        return []
    
    @property
    def is_connected(self) -> bool:
        """Check if connected"""
        return self._connection is not None

@contextmanager
def timed_operation(name: str) -> Generator[None, None, None]:
    """Context manager for timing operations"""
    print(f"Starting: {name}")
    start = datetime.now()
    try:
        yield
    finally:
        end = datetime.now()
        duration = (end - start).total_seconds()
        print(f"Completed: {name} in {duration:.3f}s")

class DataExporter:
    """Export data with type hints"""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
    
    def export_users(self) -> list:
        """Export all users"""
        with DatabaseConnection(self.db_path) as db:
            result = db.execute("SELECT id, name, email FROM users")
            return [{"id": row[0], "name": row[1], "email": row[2]} for row in result]
    
    def export_orders(self, user_id: Optional[int] = None) -> list:
        """Export orders with optional filter"""
        with DatabaseConnection(self.db_path) as db:
            if user_id:
                query = "SELECT id, user_id, total FROM orders WHERE user_id = ?"
                params = (user_id,)
            else:
                query = "SELECT id, user_id, total FROM orders"
                params = ()
            
            result = db.execute(query, params)
            return [{"id": row[0], "user_id": row[1], "total": row[2]} for row in result]
    
    def create_backup(self, backup_path: str) -> bool:
        """Create database backup"""
        import shutil
        try:
            with timed_operation(f"Backup to {backup_path}"):
                shutil.copy2(self.db_path, backup_path)
            return True
        except Exception as e:
            print(f"Backup failed: {e}")
            return False

# Usage
print("=== Context Managers with Type Hints ===")

# Create a temporary database (simulated)
import tempfile
import os

def setup_test_db() -> str:
    """Create test database"""
    fd, path = tempfile.mkstemp(suffix='.db')
    os.close(fd)
    
    with DatabaseConnection(path) as db:
        db.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
        
        db.execute("""
            CREATE TABLE orders (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                total REAL
            )
        """)
        
        # Insert test data
        db.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
        db.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Bob", "bob@example.com"))
        db.execute("INSERT INTO orders (user_id, total) VALUES (?, ?)", (1, 99.99))
        db.execute("INSERT INTO orders (user_id, total) VALUES (?, ?)", (1, 49.99))
        db.execute("INSERT INTO orders (user_id, total) VALUES (?, ?)", (2, 29.99))
    
    return path

# Use the database
db_path = setup_test_db()
exporter = DataExporter(db_path)

# Export data with timing
with timed_operation("Export users"):
    users = exporter.export_users()
    print(f"Exported {len(users)} users")
    for user in users:
        print(f"  - {user['name']} ({user['email']})")

with timed_operation("Export Alice's orders"):
    orders = exporter.export_orders(user_id=1)
    print(f"Alice has {len(orders)} orders")
    for order in orders:
        print(f"  - Order #{order['id']}: ${order['total']}")

# Cleanup
os.unlink(db_path)
```

## Type Checkers and Tools

### mypy - Static Type Checker
```bash
# Install mypy
pip install mypy

# Run type checking
mypy myfile.py

# With strict mode
mypy --strict myfile.py

# Ignore missing imports
mypy --ignore-missing-imports myfile.py
```

```python
# example.py
def add(a: int, b: int) -> int:
    return a + b

# mypy will catch this
# result: str = add(5, 3)  # Error: Incompatible type

# Run: mypy example.py
```

### Pyright (Microsoft)
```bash
# Install pyright
npm install -g pyright

# Run
pyright myfile.py
```

### Type Checking in IDEs
```python
# VSCode with Pylance extension provides real-time type checking
# PyCharm has built-in type checking

def process(value: int) -> str:
    return str(value)

# IDE will show warning if used incorrectly
# result: int = process("hello")  # Warning shown in editor
```

## Common Mistakes

### Mistake 1: Assuming Type Hints Enforce Types
```python
# Wrong - thinking Python enforces types
def add(a: int, b: int) -> int:
    return a + b

result = add("5", "3")  # No error! Returns "53"
print(result)  # "53"

# Type hints are just hints - Python ignores them
```

### Mistake 2: Inconsistent Type Annotations
```python
# Wrong - inconsistent
def process(data: list) -> str:
    return data  # Returns list, not str

# Right - match return type
def process(data: list) -> list:
    return data
```

### Mistake 3: Over-annotating Simple Code
```python
# Wrong - too verbose for simple code
x: int = 5
y: int = 10
result: int = x + y

# Right - type hints optional for obvious cases
x = 5
y = 10
result = x + y
```

### Mistake 4: Using Built-in Types as Annotations
```python
# Wrong - using built-in as annotation
def process(items: list) -> list:
    return items

# Better - specify element type
def process(items: list[int]) -> list[int]:
    return items

# Even better with Python 3.9+
def process(items: list[int]) -> list[int]:
    return items
```

## Best Practices

### ✅ Do This
```python
# Use type hints for public APIs
def calculate_total(items: list[float]) -> float:
    return sum(items)

# Use Optional for values that can be None
def find_user(user_id: int) -> Optional[dict]:
    return users.get(user_id)

# Use Union for multiple possible types
def process(value: Union[int, str]) -> str:
    return str(value)

# Use TypeVar for generic functions
T = TypeVar('T')
def first(items: list[T]) -> T:
    return items[0]

# Use type aliases for complex types
UserId = int
UserDict = dict[str, Union[str, int]]

# Use dataclasses for structured data
@dataclass
class Point:
    x: float
    y: float

# Keep type hints consistent with actual usage
def add(a: int, b: int) -> int:
    return a + b  # Actually returns int
```

### ❌ Avoid This
```python
# Avoid - lying about return type
def get_name() -> str:
    return 123  # Returns int, not str

# Avoid - over-annotating internal variables
def process():
    x: int = 5  # Unnecessary
    y: int = 10  # Unnecessary
    return x + y

# Avoid - using Any when specific type known
def process(data: Any) -> Any:  # Too vague
    return data

# Avoid - ignoring type hints in complex code
def process(data):  # Missing type hints
    return data

# Avoid - using type hints as documentation only
# Use them consistently or don't use them at all
```

## Quick Reference Table

| Syntax | Meaning | Example |
|--------|---------|---------|
| `var: type` | Variable annotation | `name: str = "Alice"` |
| `func(param: type) -> type` | Function annotation | `def add(a: int) -> int` |
| `list[T]` | List of T type | `numbers: list[int]` |
| `dict[K, V]` | Dictionary mapping | `scores: dict[str, int]` |
| `tuple[T, ...]` | Tuple of T type | `tags: tuple[str, ...]` |
| `Optional[T]` | T or None | `Optional[str]` |
| `Union[T, U]` | T or U | `Union[int, str]` |
| `Any` | Any type | `data: Any` |
| `TypeVar('T')` | Generic type | `T = TypeVar('T')` |
| `Callable[[P], R]` | Function type | `Callable[[int], str]` |
| `Literal[vals]` | Specific values | `Literal['a', 'b']` |
| `TypedDict` | Dict structure | `class User(TypedDict)` |

## Summary

- **Type hints are optional** - Python ignores them at runtime
- **PEP 484** introduced type hints in Python 3.5
- **Better documentation** - self-documenting code
- **IDE support** - autocomplete, refactoring, error detection
- **Static checking** - use mypy, pyright, or PyCharm
- **No runtime cost** - hints removed before execution
- **Gradual typing** - add hints incrementally
- **Generic types** - use TypeVar for reusable code
- **Union and Optional** - handle multiple or nullable types
- **TypedDict** - structure dictionaries
- **Literal types** - restrict to specific values

## Basic Template
```python
#!/usr/bin/env python3
"""
Module with type hints example.
"""

from typing import List, Dict, Optional, Union, Any
from dataclasses import dataclass
from enum import Enum

# Type aliases
UserId = int
UserName = str
UserData = Dict[str, Union[str, int, bool]]

# Enums
class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

# Data classes
@dataclass
class User:
    """User data class"""
    id: int
    name: str
    email: str
    role: UserRole
    is_active: bool = True
    
    def get_display_name(self) -> str:
        """Get formatted display name"""
        if self.role == UserRole.ADMIN:
            return f"{self.name} (Admin)"
        return self.name

# Functions with type hints
def create_user(name: str, email: str, role: UserRole = UserRole.USER) -> User:
    """Create a new user"""
    import uuid
    return User(
        id=hash(f"{name}{email}"),
        name=name,
        email=email,
        role=role
    )

def find_user(users: List[User], user_id: int) -> Optional[User]:
    """Find user by ID"""
    for user in users:
        if user.id == user_id:
            return user
    return None

def get_active_users(users: List[User]) -> List[User]:
    """Get all active users"""
    return [u for u in users if u.is_active]

def process_user_data(data: Any) -> Dict[str, Any]:
    """Process arbitrary user data"""
    if isinstance(data, User):
        return {"id": data.id, "name": data.name}
    elif isinstance(data, dict):
        return {"id": data.get("id"), "name": data.get("name")}
    else:
        return {"error": f"Unsupported type: {type(data)}"}

# Generic function
T = TypeVar('T')

def first_element(items: List[T]) -> Optional[T]:
    """Return first element of list"""
    return items[0] if items else None

# Main execution
def main() -> None:
    """Main function"""
    # Create users
    alice = create_user("Alice", "alice@example.com", UserRole.ADMIN)
    bob = create_user("Bob", "bob@example.com")
    
    users: List[User] = [alice, bob]
    
    # Find user
    found = find_user(users, alice.id)
    if found:
        print(f"Found: {found.get_display_name()}")
    
    # Active users
    active = get_active_users(users)
    print(f"Active users: {len(active)}")
    
    # Process data
    result = process_user_data(alice)
    print(f"Processed: {result}")

if __name__ == "__main__":
    main()
```

*This documentation belongs to https://github.com/InterCentury*