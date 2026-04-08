# 18 - Constants and Naming Conventions in Python

## What are Constants?
Constants are values that should not change during program execution. Unlike C++ which has a `const` keyword, Python doesn't have true constants. Instead, Python uses **naming conventions** to indicate that a variable should be treated as a constant.

## Constants in Python (By Convention)

### Basic Constant Naming
```python
# Constants are written in UPPER_CASE with underscores
MAX_USERS = 100
PI = 3.14159
APP_NAME = "MyApplication"
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

# These are not true constants - they can still be modified!
# MAX_USERS = 200  # This works! (but violates convention)

print(MAX_USERS)  # 100
print(PI)         # 3.14159
```

### Why Python Has No True Constants
```python
# Python doesn't have a 'const' keyword like C++
# const int MAX = 100;  // C++ - cannot change

# In Python, constants are just variables by convention
MAX_SIZE = 100
MAX_SIZE = 200  # Allowed! (but bad practice)

# Workarounds exist but aren't perfect
class Constants:
    MAX_SIZE = 100

Constants.MAX_SIZE = 200  # Still can change!

# Using property for read-only
class ReadOnlyConstants:
    def __init__(self):
        self._max_size = 100
    
    @property
    def MAX_SIZE(self):
        return self._max_size

const = ReadOnlyConstants()
# const.MAX_SIZE = 200  # AttributeError: can't set attribute
print(const.MAX_SIZE)  # 100
```

## Python Naming Conventions (PEP 8)

### Variables (snake_case)
```python
# Variables use snake_case: lowercase with underscores
user_name = "Alice"
total_score = 95
max_retries = 3
is_active = True
items_list = [1, 2, 3]

# Good examples
first_name = "Bob"
last_name = "Smith"
age = 25
email_address = "bob@example.com"

# Bad examples (avoid)
firstName = "Bob"      # camelCase - not Pythonic
FirstName = "Bob"      # PascalCase - used for classes
firstname = "Bob"      # Unclear word boundary
```

### Constants (UPPER_CASE)
```python
# Constants use UPPER_CASE with underscores
MAX_CONNECTIONS = 100
DEFAULT_PORT = 8080
API_KEY = "abc123"
DEBUG_MODE = False

# Group related constants
class MathConstants:
    PI = 3.14159
    E = 2.71828
    GOLDEN_RATIO = 1.61803

class AppConstants:
    VERSION = "1.0.0"
    APP_NAME = "MyApp"
    COMPANY_NAME = "MyCompany"

# Module-level constants
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
ALLOWED_EXTENSIONS = {'.txt', '.pdf', '.doc'}
```

### Classes (PascalCase)
```python
# Class names use PascalCase: Capitalized words without underscores
class UserAccount:
    pass

class DataProcessor:
    pass

class HTTPServer:
    pass

class BankAccountManager:
    pass

# Examples
class Customer:
    pass

class ShoppingCart:
    pass

class EmailValidator:
    pass

# Acronyms can stay uppercase
class HTTPSConnection:
    pass

class XMLParser:
    pass
```

### Functions and Methods (snake_case)
```python
# Functions use snake_case
def calculate_total():
    pass

def get_user_name():
    pass

def process_data():
    pass

def send_email_notification():
    pass

# Methods (same as functions)
class User:
    def get_full_name(self):
        pass
    
    def update_email(self):
        pass

# Private methods (leading underscore)
class Processor:
    def _internal_helper(self):
        pass
    
    def public_method(self):
        pass
```

### Private Variables and Methods (Leading Underscore)
```python
# Single leading underscore: "protected" / internal use
class BankAccount:
    def __init__(self):
        self._balance = 0      # Internal use
        self._transaction_log = []
    
    def _calculate_interest(self):  # Internal method
        pass
    
    def deposit(self, amount):
        self._balance += amount
        self._transaction_log.append(f"Deposited {amount}")

# Still accessible but convention says "don't use"
account = BankAccount()
print(account._balance)  # Works but violates convention
```

### Name Mangling (Double Leading Underscore)
```python
# Double leading underscore: name mangling (prevents accidental override)
class Parent:
    def __init__(self):
        self.__private_value = 10  # Becomes _Parent__private_value
    
    def __private_method(self):    # Becomes _Parent__private_method
        return "Private"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__private_value = 20  # Different! _Child__private_value
    
    def __private_method(self):    # Different! _Child__private_method
        return "Child Private"

obj = Child()
# print(obj.__private_value)  # AttributeError
print(obj._Parent__private_value)  # 10 (not recommended)
print(obj._Child__private_value)   # 20
```

### Special Methods (Dunder Methods)
```python
# Double leading and trailing underscores: "magic" methods
class MyClass:
    def __init__(self):      # Constructor
        pass
    
    def __str__(self):       # String representation
        return "MyClass"
    
    def __len__(self):       # Length
        return 10
    
    def __add__(self, other): # Addition
        return self
    
    def __eq__(self, other):  # Equality
        return True

# Avoid creating your own dunder names
# __my_method__  # Reserved for Python
```

## Comprehensive Naming Examples

### Module-Level Names
```python
# module: user_processor.py

# Module constants
DEFAULT_USER_ROLE = "guest"
MAX_USERNAME_LENGTH = 50
VALID_EMAIL_DOMAIN = "@example.com"

# Module variables (avoid when possible)
_global_cache = {}  # Internal use

# Functions
def validate_username(username):
    """Check if username is valid"""
    return len(username) <= MAX_USERNAME_LENGTH

def _internal_helper(data):  # Internal function
    return data.upper()

# Classes
class UserProcessor:
    def __init__(self):
        self._users = []      # Internal attribute
    
    def add_user(self, user):
        self._users.append(user)
    
    def _validate(self):      # Internal method
        return True

# Main execution
if __name__ == "__main__":
    main()
```

### Class Attributes and Methods
```python
class DatabaseConnection:
    # Class constants
    DEFAULT_TIMEOUT = 30
    MAX_RETRIES = 3
    SUPPORTED_DB_TYPES = ['mysql', 'postgresql', 'sqlite']
    
    # Class variable (shared across instances)
    connection_count = 0
    
    def __init__(self, db_type, host, port):
        # Instance variables (snake_case)
        self.db_type = db_type
        self.host = host
        self.port = port
        self._is_connected = False  # Internal
        self.__connection_id = None # Name mangled
        
        DatabaseConnection.connection_count += 1
    
    # Public method
    def connect(self):
        self._internal_connect()
        self._is_connected = True
    
    # Internal method
    def _internal_connect(self):
        pass
    
    # Private method (name mangled)
    def __create_connection(self):
        pass
    
    # Property (looks like attribute)
    @property
    def is_connected(self):
        return self._is_connected
    
    # Class method
    @classmethod
    def get_connection_count(cls):
        return cls.connection_count
    
    # Static method
    @staticmethod
    def validate_db_type(db_type):
        return db_type in DatabaseConnection.SUPPORTED_DB_TYPES
```

## Anti-Patterns and Bad Naming

### What to Avoid
```python
# Avoid - single letters (except trivial loops)
x = 10          # What is x?
y = process()   # What does y represent?
for i in range(10):  # OK for simple loop
    pass

# Avoid - using 'l', 'O', 'I' (look like numbers)
l = 10   # Looks like 1
O = 20   # Looks like 0
I = 30   # Looks like 1

# Avoid - vague names
data = get_info()
temp = calculate()
stuff = process_things()

# Avoid - Hungarian notation (type in name)
strName = "Alice"
intAge = 25
lstItems = [1, 2, 3]

# Avoid - mixed case in constants
MaxSize = 100      # Use MAX_SIZE
DefaultValue = 10  # Use DEFAULT_VALUE

# Avoid - trailing underscores (except to avoid keywords)
class_ = MyClass  # OK to avoid keyword
name_ = "Alice"   # Unnecessary

# Avoid - double leading and trailing (reserved)
__my_method__  # Don't create these

# Avoid - using built-in names
list = [1, 2, 3]   # Overwrites built-in
dict = {"a": 1}    # Overwrites built-in
str = "hello"      # Overwrites built-in
```

## Practical Examples

### Example 1: Configuration Module
```python
# config.py - Application configuration constants

import os
from pathlib import Path

# Application metadata
APP_NAME = "DataProcessor"
VERSION = "2.1.0"
COMPANY = "DataCorp"
COPYRIGHT = f"Copyright © 2024 {COMPANY}"

# File system constants
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
TEMP_DIR = BASE_DIR / "temp"

# Create directories if they don't exist
for directory in [DATA_DIR, LOG_DIR, TEMP_DIR]:
    directory.mkdir(exist_ok=True)

# File size limits (in bytes)
MAX_UPLOAD_SIZE = 50 * 1024 * 1024  # 50 MB
MAX_LOG_SIZE = 10 * 1024 * 1024     # 10 MB
MAX_CACHE_SIZE = 100 * 1024 * 1024  # 100 MB

# Network constants
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 8080
API_TIMEOUT = 30  # seconds
MAX_RETRIES = 3
RETRY_DELAY = 1   # seconds

# Database constants
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "myapp")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

# Application settings
DEBUG_MODE = os.getenv("DEBUG", "False").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
TIMEZONE = "UTC"
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# User roles
ROLE_ADMIN = "admin"
ROLE_USER = "user"
ROLE_GUEST = "guest"
ROLE_MODERATOR = "moderator"

# HTTP status codes (constants)
HTTP_OK = 200
HTTP_CREATED = 201
HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_INTERNAL_ERROR = 500

# Validation constants
EMAIL_MAX_LENGTH = 254
USERNAME_MIN_LENGTH = 3
USERNAME_MAX_LENGTH = 50
PASSWORD_MIN_LENGTH = 8

# Regular expression patterns (constants)
EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PHONE_PATTERN = r'^\+?1?\d{9,15}$'
ZIPCODE_PATTERN = r'^\d{5}(-\d{4})?$'

def get_config_summary():
    """Return summary of current configuration"""
    return {
        "app_name": APP_NAME,
        "version": VERSION,
        "debug": DEBUG_MODE,
        "data_dir": str(DATA_DIR),
        "db_host": DB_HOST,
        "db_port": DB_PORT,
    }

# Usage example
if __name__ == "__main__":
    print(f"{APP_NAME} v{VERSION}")
    print(f"Data directory: {DATA_DIR}")
    print(f"Debug mode: {DEBUG_MODE}")
    print(f"API timeout: {API_TIMEOUT}s")
```

### Example 2: Enums for Constants (Python 3.4+)
```python
from enum import Enum, auto, IntEnum
from typing import List

# Using Enum for related constants
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    
    def __str__(self):
        return self.name.lower()

class Status(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"

# Auto-assigned values
class Priority(Enum):
    LOW = auto()      # 1
    MEDIUM = auto()   # 2
    HIGH = auto()     # 3
    CRITICAL = auto() # 4

# IntEnum for integer constants
class OrderStatus(IntEnum):
    NEW = 1
    PAID = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELLED = 5

# Practical example
class DatabaseErrorCode(IntEnum):
    SUCCESS = 0
    CONNECTION_FAILED = 1001
    QUERY_FAILED = 1002
    DUPLICATE_KEY = 1003
    FOREIGN_KEY_ERROR = 1004
    TIMEOUT = 1005

# Using enum in a class
class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, name: str, priority: Priority):
        self.tasks.append({
            'name': name,
            'priority': priority,
            'status': Status.PENDING
        })
    
    def process_tasks(self):
        for task in self.tasks:
            if task['status'] == Status.PENDING:
                task['status'] = Status.PROCESSING
                # Process task
                task['status'] = Status.COMPLETED
    
    def get_tasks_by_status(self, status: Status) -> List[dict]:
        return [t for t in self.tasks if t['status'] == status]

# Demo
print("=== Enum Constants Demo ===")
print(f"Color.RED: {Color.RED}")
print(f"Color.RED.value: {Color.RED.value}")
print(f"Color.RED.name: {Color.RED.name}")

# Enum iteration
print("\nAll colors:")
for color in Color:
    print(f"  {color}: {color.value}")

# Enum in use
manager = TaskManager()
manager.add_task("Write code", Priority.HIGH)
manager.add_task("Test code", Priority.MEDIUM)
manager.add_task("Deploy", Priority.CRITICAL)

print("\nTasks by status:")
for task in manager.tasks:
    print(f"  {task['name']}: {task['priority'].name} priority, {task['status'].value}")

# Compare enums
if manager.tasks[0]['priority'] == Priority.HIGH:
    print("\nHigh priority task found!")

# IntEnum usage
error = DatabaseErrorCode.CONNECTION_FAILED
print(f"\nError code: {error}, value: {error.value}")
```

### Example 3: Named Constants for Magic Numbers
```python
# Bad - magic numbers
def calculate_circle_area(radius):
    return 3.14159 * radius * radius  # What's 3.14159?

def calculate_temperature(celsius):
    return celsius * 1.8 + 32  # What are 1.8 and 32?

# Good - named constants
import math

class CircleMath:
    PI = math.pi
    TAU = 2 * math.pi
    RADIUS_TO_DIAMETER = 2
    RADIUS_TO_CIRCUMFERENCE = 2 * PI

def calculate_circle_area(radius):
    return CircleMath.PI * radius ** 2

def calculate_temperature(celsius):
    CELSIUS_TO_FAHRENHEIT_MULTIPLIER = 9/5
    FAHRENHEIT_OFFSET = 32
    return celsius * CELSIUS_TO_FAHRENHEIT_MULTIPLIER + FAHRENHEIT_OFFSET

# More examples
class PhysicsConstants:
    SPEED_OF_LIGHT = 299792458  # m/s
    GRAVITATIONAL_CONSTANT = 6.67430e-11  # m³/kg/s²
    PLANCK_CONSTANT = 6.62607015e-34  # J·s
    ELECTRON_MASS = 9.1093837e-31  # kg
    PROTON_MASS = 1.6726219e-27  # kg

class FinancialConstants:
    VAT_RATE = 0.20  # 20%
    INTEREST_DAYS_PER_YEAR = 365
    DEFAULT_CREDIT_SCORE = 650
    MAX_LOAN_TO_VALUE = 0.80

class TimeConstants:
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    DAYS_PER_WEEK = 7
    DAYS_PER_YEAR = 365
    MONTHS_PER_YEAR = 12

# Usage
def seconds_to_days(seconds):
    return seconds / (TimeConstants.SECONDS_PER_MINUTE * 
                     TimeConstants.MINUTES_PER_HOUR * 
                     TimeConstants.HOURS_PER_DAY)

def calculate_interest(principal, rate, years):
    return principal * rate * years

def calculate_vat(amount):
    return amount * FinancialConstants.VAT_RATE
```

### Example 4: Constants in Classes
```python
class DataProcessor:
    """Data processor with class-level constants"""
    
    # Class constants
    DEFAULT_BUFFER_SIZE = 4096
    MAX_FILE_SIZE = 100 * 1024 * 1024  # 100 MB
    SUPPORTED_FORMATS = {'csv', 'json', 'xml'}
    
    # Processing constants
    CHUNK_SIZE = 1024
    ENCODING = 'utf-8'
    
    # Error codes
    ERR_SUCCESS = 0
    ERR_FILE_NOT_FOUND = 1
    ERR_INVALID_FORMAT = 2
    ERR_SIZE_EXCEEDED = 3
    
    def __init__(self, buffer_size=None):
        self.buffer_size = buffer_size or self.DEFAULT_BUFFER_SIZE
    
    def process_file(self, filepath, format_type):
        if format_type not in self.SUPPORTED_FORMATS:
            return self.ERR_INVALID_FORMAT
        
        file_size = self._get_file_size(filepath)
        if file_size > self.MAX_FILE_SIZE:
            return self.ERR_SIZE_EXCEEDED
        
        # Process file
        return self.ERR_SUCCESS
    
    @classmethod
    def get_constants(cls):
        """Return all class constants"""
        return {
            'DEFAULT_BUFFER_SIZE': cls.DEFAULT_BUFFER_SIZE,
            'MAX_FILE_SIZE': cls.MAX_FILE_SIZE,
            'SUPPORTED_FORMATS': cls.SUPPORTED_FORMATS,
            'CHUNK_SIZE': cls.CHUNK_SIZE,
            'ENCODING': cls.ENCODING
        }

class DatabaseConfig:
    """Database configuration constants"""
    
    # Connection defaults
    DEFAULT_HOST = "localhost"
    DEFAULT_PORT = 5432
    DEFAULT_TIMEOUT = 30
    MAX_POOL_SIZE = 20
    
    # Query limits
    MAX_ROWS = 1000
    DEFAULT_LIMIT = 100
    MAX_QUERY_LENGTH = 10000
    
    # Data types mapping
    TYPE_MAPPING = {
        'int': 'INTEGER',
        'str': 'VARCHAR(255)',
        'float': 'REAL',
        'bool': 'BOOLEAN',
        'datetime': 'TIMESTAMP'
    }
    
    def __init__(self, host=None, port=None):
        self.host = host or self.DEFAULT_HOST
        self.port = port or self.DEFAULT_PORT
    
    def get_connection_string(self):
        return f"postgresql://{self.host}:{self.port}"
    
    @staticmethod
    def get_sql_type(python_type):
        return DatabaseConfig.TYPE_MAPPING.get(python_type, 'TEXT')

# Usage
print("=== Class Constants Demo ===")
print(f"Supported formats: {DataProcessor.SUPPORTED_FORMATS}")
print(f"Max file size: {DataProcessor.MAX_FILE_SIZE / (1024*1024)} MB")
print(f"Constants: {DataProcessor.get_constants()}")

config = DatabaseConfig()
print(f"\nDatabase config: {config.get_connection_string()}")
print(f"SQL type for 'int': {DatabaseConfig.get_sql_type('int')}")
```

### Example 5: Configuration Pattern with Property Constants
```python
class AppConfig:
    """Read-only configuration using properties"""
    
    def __init__(self):
        self._app_name = "MyApp"
        self._version = "1.0.0"
        self._debug = False
        self._max_users = 100
        self._api_key = "default-key-123"
    
    @property
    def APP_NAME(self):
        """Read-only app name"""
        return self._app_name
    
    @property
    def VERSION(self):
        """Read-only version"""
        return self._version
    
    @property
    def DEBUG(self):
        """Read-only debug flag"""
        return self._debug
    
    @property
    def MAX_USERS(self):
        """Read-only max users"""
        return self._max_users
    
    @property
    def API_KEY(self):
        """Read-only API key"""
        return self._api_key
    
    # Setters only for values that can change
    def set_debug(self, value):
        """Allow debug mode to be changed"""
        if isinstance(value, bool):
            self._debug = value
    
    def set_api_key(self, key):
        """Allow API key to be changed"""
        if key and isinstance(key, str):
            self._api_key = key

# Immutable constants using namedtuple
from collections import namedtuple

Constants = namedtuple('Constants', [
    'APP_NAME',
    'VERSION',
    'COMPANY',
    'COPYRIGHT'
])

APP_CONSTANTS = Constants(
    APP_NAME="DataProcessor",
    VERSION="2.0.0",
    COMPANY="DataCorp",
    COPYRIGHT="© 2024 DataCorp"
)

# APP_CONSTANTS.APP_NAME = "NewName"  # AttributeError!

# Using dataclass with frozen=True
from dataclasses import dataclass

@dataclass(frozen=True)
class FrozenConfig:
    """Immutable configuration"""
    APP_NAME: str
    VERSION: str
    MAX_USERS: int
    DEBUG: bool = False
    TIMEOUT: int = 30

config = FrozenConfig(
    APP_NAME="MyApp",
    VERSION="1.0.0",
    MAX_USERS=100
)

# config.MAX_USERS = 200  # dataclasses.FrozenInstanceError

print("=== Immutable Configurations ===")
print(f"App: {APP_CONSTANTS.APP_NAME}")
print(f"Version: {APP_CONSTANTS.VERSION}")
print(f"Config: {config}")
```

### Example 6: Real-World Application Structure
```python
# settings.py - Application settings with constants

import os
from enum import Enum
from pathlib import Path
from typing import Dict, Any

# Environment detection
ENVIRONMENT = os.getenv("ENVIRONMENT", "development").lower()
IS_PRODUCTION = ENVIRONMENT == "production"
IS_DEVELOPMENT = ENVIRONMENT == "development"
IS_TESTING = ENVIRONMENT == "testing"

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
SRC_DIR = PROJECT_ROOT / "src"
TESTS_DIR = PROJECT_ROOT / "tests"
DATA_DIR = PROJECT_ROOT / "data"
LOGS_DIR = PROJECT_ROOT / "logs"
CACHE_DIR = PROJECT_ROOT / "cache"

# Ensure directories exist
for dir_path in [DATA_DIR, LOGS_DIR, CACHE_DIR]:
    dir_path.mkdir(exist_ok=True)

# Application constants
class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class HttpStatus(IntEnum):
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    INTERNAL_ERROR = 500

class UserRole(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"
    GUEST = "guest"

# Configuration by environment
class Config:
    """Base configuration"""
    APP_NAME = "MyApplication"
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    
    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # API
    API_PREFIX = "/api/v1"
    API_TITLE = "MyApp API"
    API_VERSION = "1.0.0"
    
    # Pagination
    DEFAULT_PAGE_SIZE = 20
    MAX_PAGE_SIZE = 100
    
    # Rate limiting
    RATELIMIT_DEFAULT = "100/hour"
    RATELIMIT_STORAGE_URL = "memory://"
    
    # File uploads
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
    ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.pdf'}

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URL", "sqlite:///dev.db")
    RATELIMIT_ENABLED = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    RATELIMIT_ENABLED = True
    
    # Stricter security
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    RATELIMIT_ENABLED = False
    WTF_CSRF_ENABLED = False

# Select configuration based on environment
config_map: Dict[str, Any] = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}

CurrentConfig = config_map.get(ENVIRONMENT, DevelopmentConfig)

# Helper functions
def get_config() -> Any:
    """Get current configuration"""
    return CurrentConfig

def is_debug() -> bool:
    """Check if debug mode is enabled"""
    return CurrentConfig.DEBUG

def is_production() -> bool:
    """Check if running in production"""
    return ENVIRONMENT == "production"

# Usage example
if __name__ == "__main__":
    print("=== Application Configuration ===")
    print(f"Environment: {ENVIRONMENT}")
    print(f"Production: {IS_PRODUCTION}")
    print(f"Debug mode: {CurrentConfig.DEBUG}")
    print(f"App name: {CurrentConfig.APP_NAME}")
    print(f"API prefix: {CurrentConfig.API_PREFIX}")
    print(f"Database URI: {CurrentConfig.SQLALCHEMY_DATABASE_URI}")
    
    print("\n=== User Roles ===")
    for role in UserRole:
        print(f"  {role.value}: {role.name}")
    
    print("\n=== HTTP Status Codes ===")
    for status in HttpStatus:
        print(f"  {status.value}: {status.name}")
```

## Naming Conventions Quick Reference

| Type | Convention | Example |
|------|------------|---------|
| Variable | snake_case | `user_name`, `total_count` |
| Constant | UPPER_CASE | `MAX_USERS`, `API_KEY` |
| Class | PascalCase | `UserAccount`, `DataProcessor` |
| Function | snake_case | `calculate_total()`, `get_name()` |
| Method | snake_case | `get_value()`, `set_value()` |
| Private method | _leading_underscore | `_internal_helper()` |
| Private variable | _leading_underscore | `_cache`, `_temp` |
| Name mangled | __double_leading | `__private_var` |
| Dunder method | __double_leading_and_trailing__ | `__init__`, `__str__` |
| Module | snake_case | `user_processor.py` |
| Package | lowercase | `mypackage` |

## Summary

- **No true constants** in Python (only by convention)
- **UPPER_CASE** for constants: `MAX_SIZE = 100`
- **snake_case** for variables/functions: `user_name`, `calculate_total()`
- **PascalCase** for classes: `UserAccount`, `DataProcessor`
- **Leading underscore** for internal/private: `_internal_method()`
- **Double underscore** for name mangling: `__private_attr`
- **Avoid magic numbers** - use named constants
- **Use Enums** for related constants (Python 3.4+)
- **Be consistent** - follow PEP 8 throughout project
- **Use descriptive names** - make code self-documenting

## Basic Template
```python
#!/usr/bin/env python3
"""
Module docstring describing purpose.
"""

# Module constants
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
API_VERSION = "v1"

# Module variables (avoid when possible)
_module_cache = {}  # Internal use

# Enums for related constants
from enum import Enum, auto

class Status(Enum):
    PENDING = auto()
    PROCESSING = auto()
    COMPLETED = auto()
    FAILED = auto()

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

# Classes (PascalCase)
class DataProcessor:
    """Class docstring"""
    
    # Class constants (UPPER_CASE)
    DEFAULT_BUFFER = 4096
    SUPPORTED_FORMATS = {'json', 'xml'}
    
    def __init__(self, name):
        # Instance variables (snake_case)
        self.name = name
        self._internal_cache = {}  # Internal
        self.__private_attr = None  # Name mangled
    
    # Public methods (snake_case)
    def process_data(self, data):
        """Process the given data"""
        result = self._internal_calculate(data)
        return result
    
    # Internal method (leading underscore)
    def _internal_calculate(self, data):
        """Internal calculation (not part of public API)"""
        return len(data)
    
    # Property (looks like attribute)
    @property
    def is_ready(self):
        """Check if processor is ready"""
        return self._internal_cache is not None

# Functions (snake_case)
def calculate_total(items):
    """Calculate total of items"""
    total = 0
    for item in items:
        total += item
    return total

def _helper_function():
    """Internal helper (not exported)"""
    pass

# Main execution
if __name__ == "__main__":
    # Main program logic
    processor = DataProcessor("Main")
    result = processor.process_data([1, 2, 3])
    print(f"Result: {result}")
```

*This documentation belongs to https://github.com/InterCentury*