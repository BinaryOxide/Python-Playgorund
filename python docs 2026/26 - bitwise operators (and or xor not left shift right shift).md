# 26 - Bitwise Operators (&, |, ^, ~, <<, >>)

## What are Bitwise Operators?
Bitwise operators perform operations on the binary representations of integers. They work at the bit level, manipulating individual bits (0s and 1s). These operators are essential for low-level programming, flags, permissions, and optimization.

## Binary Representation

### Understanding Binary
```python
# Python displays binary with bin()
x = 42
print(f"Decimal: {x}")
print(f"Binary: {bin(x)}")     # 0b101010
print(f"Binary (no prefix): {bin(x)[2:]}")  # 101010

# Different bit lengths
print(f"5 in binary: {bin(5)}")      # 0b101
print(f"10 in binary: {bin(10)}")    # 0b1010
print(f"255 in binary: {bin(255)}")  # 0b11111111

# Format with specific width
print(f"5: {format(5, '08b')}")   # 00000101
print(f"10: {format(10, '08b')}") # 00001010
```

### Bit Positions
```python
# Bits are numbered from right (LSB) to left (MSB)
# Example: 13 = 1101 (binary)
# Position:  3   2   1   0
# Value:     8   4   2   1

def show_bits(n, bits=8):
    """Display binary with bit positions"""
    binary = format(n, f'0{bits}b')
    print(f"Number: {n}")
    print(f"Binary: {binary}")
    print("Positions: ", end="")
    for i in range(bits):
        print(f"{bits-1-i}", end="")
    print()
    print("Values:    ", end="")
    for i in range(bits):
        print(f"{2**(bits-1-i)}", end="")
    print()

show_bits(13, 4)
show_bits(42, 8)
```

## Bitwise AND (&)

### How AND Works
```python
# AND: Returns 1 if BOTH bits are 1
# Truth table:
# 0 & 0 = 0
# 0 & 1 = 0
# 1 & 0 = 0
# 1 & 1 = 1

# Example with 4-bit numbers
a = 0b1100  # 12
b = 0b1010  # 10
result = a & b

print(f"{bin(a)} ({a})")
print(f"{bin(b)} ({b})")
print(f"{'&' * 10}")
print(f"{bin(result)} ({result})")
# 1100
# 1010
# & (AND)
# 1000 = 8
```

### Practical AND Examples
```python
# 1. Checking if a number is even
def is_even(n):
    return (n & 1) == 0

print(f"10 is even: {is_even(10)}")  # True
print(f"7 is even: {is_even(7)}")    # False

# 2. Checking if a bit is set
def is_bit_set(n, position):
    """Check if bit at 'position' is set (1)"""
    return (n & (1 << position)) != 0

num = 0b1010  # 10 in binary
print(f"Binary of {num}: {bin(num)}")
print(f"Bit 0 set? {is_bit_set(num, 0)}")  # False (0)
print(f"Bit 1 set? {is_bit_set(num, 1)}")  # True (1)
print(f"Bit 2 set? {is_bit_set(num, 2)}")  # False (0)
print(f"Bit 3 set? {is_bit_set(num, 3)}")  # True (1)

# 3. Masking (extracting specific bits)
value = 0b11011010
mask = 0b00001111  # Keep only lower 4 bits
result = value & mask
print(f"\nOriginal: {bin(value)}")
print(f"Mask:     {bin(mask)}")
print(f"Lower 4 bits: {bin(result)} ({result})")

# 4. Clearing specific bits
def clear_bits(n, mask):
    """Clear bits where mask has 1s"""
    return n & ~mask

value = 0b11111111
mask = 0b00001111  # Clear lower 4 bits
result = clear_bits(value, mask)
print(f"\nOriginal: {bin(value)}")
print(f"Clear lower 4 bits: {bin(result)} ({result})")
```

## Bitwise OR (|)

### How OR Works
```python
# OR: Returns 1 if AT LEAST ONE bit is 1
# Truth table:
# 0 | 0 = 0
# 0 | 1 = 1
# 1 | 0 = 1
# 1 | 1 = 1

a = 0b1100  # 12
b = 0b1010  # 10
result = a | b

print(f"{bin(a)} ({a})")
print(f"{bin(b)} ({b})")
print(f"{'|' * 10}")
print(f"{bin(result)} ({result})")
# 1100
# 1010
# | (OR)
# 1110 = 14
```

### Practical OR Examples
```python
# 1. Setting specific bits
def set_bit(n, position):
    """Set bit at 'position' to 1"""
    return n | (1 << position)

num = 0b1000  # 8
print(f"Original: {bin(num)} ({num})")
num = set_bit(num, 0)  # Set bit 0
print(f"Set bit 0: {bin(num)} ({num})")
num = set_bit(num, 2)  # Set bit 2
print(f"Set bit 2: {bin(num)} ({num})")

# 2. Combining flags
READ = 0b001
WRITE = 0b010
EXECUTE = 0b100

permissions = READ | WRITE  # Combine read and write
print(f"\nRead: {bin(READ)}")
print(f"Write: {bin(WRITE)}")
print(f"Read|Write: {bin(permissions)} ({permissions})")

permissions |= EXECUTE  # Add execute permission
print(f"Add execute: {bin(permissions)} ({permissions})")

# 3. Building bit patterns
def create_mask(*positions):
    """Create mask with specified bits set"""
    mask = 0
    for pos in positions:
        mask |= (1 << pos)
    return mask

mask = create_mask(0, 2, 4, 6)
print(f"\nMask with bits 0,2,4,6: {bin(mask)} ({mask})")
```

## Bitwise XOR (^)

### How XOR Works
```python
# XOR: Returns 1 if bits are DIFFERENT
# Truth table:
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0

a = 0b1100  # 12
b = 0b1010  # 10
result = a ^ b

print(f"{bin(a)} ({a})")
print(f"{bin(b)} ({b})")
print(f"{'^' * 10}")
print(f"{bin(result)} ({result})")
# 1100
# 1010
# ^ (XOR)
# 0110 = 6
```

### Practical XOR Examples
```python
# 1. Toggling bits
def toggle_bit(n, position):
    """Toggle bit at 'position' (0->1, 1->0)"""
    return n ^ (1 << position)

num = 0b1010  # 10
print(f"Original: {bin(num)} ({num})")
num = toggle_bit(num, 1)
print(f"Toggle bit 1: {bin(num)} ({num})")
num = toggle_bit(num, 1)
print(f"Toggle bit 1 again: {bin(num)} ({num})")

# 2. Simple encryption (XOR cipher)
def xor_encrypt_decrypt(data, key):
    """XOR encryption/decryption (same function works for both)"""
    return data ^ key

plaintext = 12345
key = 54321
ciphertext = xor_encrypt_decrypt(plaintext, key)
decrypted = xor_encrypt_decrypt(ciphertext, key)

print(f"\nPlaintext: {plaintext}")
print(f"Key: {key}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {decrypted}")
print(f"Success: {plaintext == decrypted}")

# 3. Finding unique number (where all others appear twice)
def find_unique(numbers):
    """Find number that appears once (others appear twice)"""
    unique = 0
    for n in numbers:
        unique ^= n
    return unique

nums = [1, 2, 3, 4, 3, 2, 1]
print(f"\nNumbers: {nums}")
print(f"Unique number: {find_unique(nums)}")  # 4

# 4. Swapping without temporary variable
a = 10
b = 20
print(f"\nBefore swap: a={a}, b={b}")
a ^= b
b ^= a
a ^= b
print(f"After swap: a={a}, b={b}")
```

## Bitwise NOT (~)

### How NOT Works
```python
# NOT: Inverts all bits (1->0, 0->1)
# In Python, ~n = -n - 1 (two's complement)

x = 5  # 0b0101
result = ~x

print(f"x = {x} ({bin(x)})")
print(f"~x = {result} ({bin(result)})")
print(f"~x = -{x} - 1 = {-x - 1}")

# Demonstration with 4 bits
def show_not(n, bits=4):
    print(f"n:      {format(n, f'0{bits}b')} ({n})")
    print(f"~n:     {format(~n & ((1<<bits)-1), f'0{bits}b')} (~{n})")
    print(f"~n + 1: {format((~n + 1) & ((1<<bits)-1), f'0{bits}b')} (two's complement)")

show_not(5)
show_not(0)
show_not(-1)
```

### Practical NOT Examples
```python
# 1. Clearing specific bits
def clear_bits(n, mask):
    """Clear bits specified in mask"""
    return n & ~mask

value = 0b11111111
mask = 0b00001111
result = clear_bits(value, mask)
print(f"Original: {bin(value)}")
print(f"Clear lower 4 bits: {bin(result)} ({result})")

# 2. Getting complement within specific bit width
def get_complement(n, bits=8):
    """Get two's complement within specified bits"""
    mask = (1 << bits) - 1
    return (~n) & mask

print(f"\n5 in 8 bits: {format(5, '08b')}")
print(f"Complement: {format(get_complement(5), '08b')}")

# 3. Toggle all bits within range
def toggle_all_bits(n, bits=8):
    """Toggle all bits within specified bit width"""
    mask = (1 << bits) - 1
    return n ^ mask

num = 0b10101010
print(f"\nOriginal: {format(num, '08b')}")
print(f"Toggle all: {format(toggle_all_bits(num), '08b')}")
```

## Left Shift (<<)

### How Left Shift Works
```python
# Left shift: Shifts bits left, fills with 0 on right
# x << n = x * (2^n)

x = 5  # 0b0101
print(f"5 << 1 = {5 << 1}")  # 10 (5 * 2)
print(f"5 << 2 = {5 << 2}")  # 20 (5 * 4)
print(f"5 << 3 = {5 << 3}")  # 40 (5 * 8)

# Binary representation
def show_left_shift(n, shift):
    print(f"{n} << {shift}")
    print(f"Before: {format(n, '08b')} ({n})")
    print(f"After:  {format(n << shift, '08b')} ({n << shift})")
    print()

show_left_shift(5, 1)
show_left_shift(5, 2)
show_left_shift(5, 3)
```

### Practical Left Shift Examples
```python
# 1. Fast multiplication by powers of 2
def fast_multiply(x, y):
    """Multiply using left shifts (y must be power of 2)"""
    if y & (y - 1) != 0:  # Check if power of 2
        raise ValueError("y must be power of 2")
    shift = y.bit_length() - 1
    return x << shift

print(f"5 * 8 = {fast_multiply(5, 8)}")  # 5 << 3
print(f"10 * 4 = {fast_multiply(10, 4)}")  # 10 << 2

# 2. Building bit masks
def create_mask_up_to(position):
    """Create mask with bits 0..position set to 1"""
    return (1 << (position + 1)) - 1

print(f"Mask for bits 0-3: {bin(create_mask_up_to(3))}")
print(f"Mask for bits 0-7: {bin(create_mask_up_to(7))}")

# 3. Setting multiple bits at once
def set_bits(n, start, count):
    """Set 'count' bits starting at 'start' to 1"""
    mask = ((1 << count) - 1) << start
    return n | mask

num = 0
num = set_bits(num, 2, 3)
print(f"\nSet bits 2,3,4: {bin(num)} ({num})")

# 4. Getting specific bit field
def get_bits(n, start, count):
    """Extract 'count' bits starting at 'start'"""
    mask = ((1 << count) - 1) << start
    return (n & mask) >> start

value = 0b11011010
bits = get_bits(value, 2, 3)
print(f"\nValue: {bin(value)}")
print(f"Bits 2-4: {bin(bits)} ({bits})")
```

## Right Shift (>>)

### How Right Shift Works
```python
# Right shift: Shifts bits right, fills with sign bit (for negative)
# x >> n = x // (2^n) (floor division)

x = 20
print(f"20 >> 1 = {20 >> 1}")  # 10 (20 // 2)
print(f"20 >> 2 = {20 >> 2}")  # 5 (20 // 4)
print(f"20 >> 3 = {20 >> 3}")  # 2 (20 // 8)

# Binary representation
def show_right_shift(n, shift):
    print(f"{n} >> {shift}")
    print(f"Before: {format(n, '08b')} ({n})")
    print(f"After:  {format(n >> shift, '08b')} ({n >> shift})")
    print()

show_right_shift(20, 1)
show_right_shift(20, 2)
show_right_shift(20, 3)

# With negative numbers (arithmetic shift)
print(f"-20 >> 1 = {-20 >> 1}")  # -10 (preserves sign)
print(f"-20 >> 2 = {-20 >> 2}")  # -5
```

### Practical Right Shift Examples
```python
# 1. Fast division by powers of 2
def fast_divide(x, y):
    """Divide using right shifts (y must be power of 2)"""
    if y & (y - 1) != 0:  # Check if power of 2
        raise ValueError("y must be power of 2")
    shift = y.bit_length() - 1
    return x >> shift

print(f"100 / 4 = {fast_divide(100, 4)}")  # 100 >> 2
print(f"64 / 8 = {fast_divide(64, 8)}")    # 64 >> 3

# 2. Extracting individual bytes from integer
def get_byte(n, byte_index):
    """Extract byte from integer (0 = LSB, 1 = next, etc.)"""
    return (n >> (byte_index * 8)) & 0xFF

value = 0x12345678
print(f"\nValue: {hex(value)}")
for i in range(4):
    byte = get_byte(value, i)
    print(f"Byte {i}: {hex(byte)}")

# 3. Checking if number is power of 2
def is_power_of_two(n):
    """Check if n is power of 2"""
    return n > 0 and (n & (n - 1)) == 0

print(f"\nIs 16 power of 2? {is_power_of_two(16)}")
print(f"Is 18 power of 2? {is_power_of_two(18)}")

# 4. Getting highest set bit position
def highest_bit_position(n):
    """Get position of highest set bit (0-indexed)"""
    if n == 0:
        return -1
    return n.bit_length() - 1

print(f"\nHighest bit in 42: {highest_bit_position(42)}")
print(f"42 in binary: {bin(42)}")
```

## Bitwise Operator Precedence

```python
# Precedence (from highest to lowest):
# ~ (bitwise NOT)
# <<, >> (shifts)
# & (AND)
# ^ (XOR)
# | (OR)

# Examples
a = 10  # 0b1010
b = 4   # 0b0100
c = 2   # 0b0010

result1 = a & b | c
result2 = a & (b | c)
print(f"a & b | c = {result1}")
print(f"a & (b | c) = {result2}")

result3 = a << 1 & b
result4 = a << (1 & b)
print(f"\na << 1 & b = {result3}")
print(f"a << (1 & b) = {result4}")

# Use parentheses for clarity
result = ((a & b) | c) << 1
print(f"\n((a & b) | c) << 1 = {result}")
```

## Practical Examples

### Example 1: Permission System with Bit Flags
```python
class PermissionSystem:
    """Bit flag permission system"""
    
    # Permission bits
    READ = 1 << 0      # 1
    WRITE = 1 << 1     # 2
    EXECUTE = 1 << 2   # 4
    DELETE = 1 << 3    # 8
    ADMIN = 1 << 4     # 16
    
    PERMISSION_NAMES = {
        READ: "READ",
        WRITE: "WRITE",
        EXECUTE: "EXECUTE",
        DELETE: "DELETE",
        ADMIN: "ADMIN"
    }
    
    def __init__(self, permissions=0):
        self.permissions = permissions
    
    def add(self, *perms):
        """Add permissions"""
        for perm in perms:
            self.permissions |= perm
        return self
    
    def remove(self, *perms):
        """Remove permissions"""
        for perm in perms:
            self.permissions &= ~perm
        return self
    
    def has(self, perm):
        """Check if has permission"""
        return (self.permissions & perm) == perm
    
    def has_any(self, *perms):
        """Check if has any of the permissions"""
        mask = 0
        for perm in perms:
            mask |= perm
        return (self.permissions & mask) != 0
    
    def has_all(self, *perms):
        """Check if has all permissions"""
        mask = 0
        for perm in perms:
            mask |= perm
        return (self.permissions & mask) == mask
    
    def toggle(self, perm):
        """Toggle permission"""
        self.permissions ^= perm
        return self
    
    def list_permissions(self):
        """List all granted permissions"""
        granted = []
        for perm, name in self.PERMISSION_NAMES.items():
            if self.has(perm):
                granted.append(name)
        return granted
    
    def __str__(self):
        perms = self.list_permissions()
        return f"Permissions({', '.join(perms) if perms else 'None'})"

# Demo
print("=== Permission System Demo ===")
print("-" * 40)

# Create user permissions
user = PermissionSystem()
print(f"Initial: {user}")

# Add permissions
user.add(PermissionSystem.READ, PermissionSystem.WRITE)
print(f"After adding READ, WRITE: {user}")

# Check permissions
print(f"Has READ? {user.has(PermissionSystem.READ)}")
print(f"Has EXECUTE? {user.has(PermissionSystem.EXECUTE)}")
print(f"Has any (READ, EXECUTE)? {user.has_any(PermissionSystem.READ, PermissionSystem.EXECUTE)}")
print(f"Has all (READ, WRITE)? {user.has_all(PermissionSystem.READ, PermissionSystem.WRITE)}")

# Toggle permission
user.toggle(PermissionSystem.EXECUTE)
print(f"After toggling EXECUTE: {user}")

# Remove permission
user.remove(PermissionSystem.WRITE)
print(f"After removing WRITE: {user}")

# Multiple users
print("\n=== Multiple Users ===")
users = {
    "admin": PermissionSystem().add(PermissionSystem.ADMIN),
    "editor": PermissionSystem().add(PermissionSystem.READ, PermissionSystem.WRITE),
    "viewer": PermissionSystem().add(PermissionSystem.READ),
    "guest": PermissionSystem()
}

for name, perms in users.items():
    print(f"{name}: {perms}")
```

### Example 2: Color Manipulation (RGB)
```python
class Color:
    """RGB color manipulation with bitwise operations"""
    
    def __init__(self, color=0x000000):
        self.color = color
    
    @classmethod
    def from_rgb(cls, r, g, b):
        """Create color from RGB values (0-255)"""
        color = (r << 16) | (g << 8) | b
        return cls(color)
    
    def get_red(self):
        """Extract red component"""
        return (self.color >> 16) & 0xFF
    
    def get_green(self):
        """Extract green component"""
        return (self.color >> 8) & 0xFF
    
    def get_blue(self):
        """Extract blue component"""
        return self.color & 0xFF
    
    def set_red(self, r):
        """Set red component"""
        self.color = (self.color & 0x00FFFF) | (r << 16)
        return self
    
    def set_green(self, g):
        """Set green component"""
        self.color = (self.color & 0xFF00FF) | (g << 8)
        return self
    
    def set_blue(self, b):
        """Set blue component"""
        self.color = (self.color & 0xFFFF00) | b
        return self
    
    def invert(self):
        """Invert all colors (negative)"""
        self.color ^= 0xFFFFFF
        return self
    
    def grayscale(self):
        """Convert to grayscale"""
        r, g, b = self.get_red(), self.get_green(), self.get_blue()
        gray = (r + g + b) // 3
        self.color = (gray << 16) | (gray << 8) | gray
        return self
    
    def brighten(self, amount):
        """Brighten color by adding to each component"""
        r = min(255, self.get_red() + amount)
        g = min(255, self.get_green() + amount)
        b = min(255, self.get_blue() + amount)
        self.color = (r << 16) | (g << 8) | b
        return self
    
    def darken(self, amount):
        """Darken color by subtracting from each component"""
        r = max(0, self.get_red() - amount)
        g = max(0, self.get_green() - amount)
        b = max(0, self.get_blue() - amount)
        self.color = (r << 16) | (g << 8) | b
        return self
    
    def __str__(self):
        return f"#{self.color:06X} (RGB: {self.get_red()},{self.get_green()},{self.get_blue()})"

# Demo
print("=== Color Manipulation Demo ===")
print("-" * 40)

# Create colors
red = Color.from_rgb(255, 0, 0)
green = Color.from_rgb(0, 255, 0)
blue = Color.from_rgb(0, 0, 255)
white = Color.from_rgb(255, 255, 255)
black = Color.from_rgb(0, 0, 0)

print(f"Red: {red}")
print(f"Green: {green}")
print(f"Blue: {blue}")
print(f"White: {white}")
print(f"Black: {black}")

# Color operations
print("\n=== Color Operations ===")
purple = Color.from_rgb(128, 0, 128)
print(f"Original: {purple}")
purple.brighten(50)
print(f"Brighten 50: {purple}")
purple.darken(100)
print(f"Darken 100: {purple}")
purple.invert()
print(f"Inverted: {purple}")

# Grayscale
color = Color.from_rgb(100, 150, 200)
print(f"\nOriginal: {color}")
color.grayscale()
print(f"Grayscale: {color}")

# Component manipulation
color = Color.from_rgb(100, 100, 100)
print(f"\nOriginal: {color}")
color.set_red(255)
print(f"Set red to 255: {color}")
color.set_green(0)
print(f"Set green to 0: {color}")
color.set_blue(128)
print(f"Set blue to 128: {color}")
```

### Example 3: IP Address Manipulation
```python
class IPAddress:
    """IP address manipulation with bitwise operations"""
    
    def __init__(self, ip_int=0):
        self.ip_int = ip_int
    
    @classmethod
    def from_string(cls, ip_str):
        """Create from dotted decimal string"""
        parts = ip_str.split('.')
        if len(parts) != 4:
            raise ValueError("Invalid IP address")
        
        ip_int = 0
        for part in parts:
            ip_int = (ip_int << 8) | int(part)
        return cls(ip_int)
    
    def to_string(self):
        """Convert to dotted decimal string"""
        parts = []
        ip = self.ip_int
        for _ in range(4):
            parts.append(str(ip & 0xFF))
            ip >>= 8
        return '.'.join(reversed(parts))
    
    def get_octet(self, index):
        """Get octet (0-3, 0=first)")
        shift = (3 - index) * 8
        return (self.ip_int >> shift) & 0xFF
    
    def set_octet(self, index, value):
        """Set octet (0-3, 0=first)")
        shift = (3 - index) * 8
        mask = 0xFF << shift
        self.ip_int = (self.ip_int & ~mask) | (value << shift)
        return self
    
    def get_network(self, subnet_mask):
        """Get network address"""
        return IPAddress(self.ip_int & subnet_mask.ip_int)
    
    def get_broadcast(self, subnet_mask):
        """Get broadcast address"""
        return IPAddress(self.ip_int | (~subnet_mask.ip_int & 0xFFFFFFFF))
    
    def is_in_subnet(self, network, subnet_mask):
        """Check if IP is in subnet"""
        return (self.ip_int & subnet_mask.ip_int) == network.ip_int
    
    def __and__(self, other):
        """Bitwise AND operator"""
        return IPAddress(self.ip_int & other.ip_int)
    
    def __or__(self, other):
        """Bitwise OR operator"""
        return IPAddress(self.ip_int | other.ip_int)
    
    def __invert__(self):
        """Bitwise NOT operator"""
        return IPAddress(~self.ip_int & 0xFFFFFFFF)
    
    def __str__(self):
        return self.to_string()

class SubnetMask:
    """Subnet mask helper"""
    
    @staticmethod
    def from_cidr(cidr):
        """Create subnet mask from CIDR notation (/24)"""
        if not 0 <= cidr <= 32:
            raise ValueError("CIDR must be between 0 and 32")
        mask_int = (0xFFFFFFFF << (32 - cidr)) & 0xFFFFFFFF
        return IPAddress(mask_int)
    
    @staticmethod
    def to_cidr(mask):
        """Convert subnet mask to CIDR notation"""
        return bin(mask.ip_int).count('1')

# Demo
print("=== IP Address Manipulation Demo ===")
print("-" * 40)

# Create IP addresses
ip1 = IPAddress.from_string("192.168.1.100")
ip2 = IPAddress.from_string("10.0.0.1")
print(f"IP1: {ip1}")
print(f"IP2: {ip2}")

# Octet manipulation
print(f"\nOctets of {ip1}:")
for i in range(4):
    print(f"  Octet {i}: {ip1.get_octet(i)}")

ip1.set_octet(3, 50)
print(f"\nAfter setting last octet to 50: {ip1}")

# Subnet calculations
print("\n=== Subnet Calculations ===")
network_ip = IPAddress.from_string("192.168.1.0")
subnet_mask = SubnetMask.from_cidr(24)
broadcast = network_ip.get_broadcast(subnet_mask)

print(f"Network: {network_ip}")
print(f"Subnet Mask: {subnet_mask} (CIDR: /{SubnetMask.to_cidr(subnet_mask)})")
print(f"Broadcast: {broadcast}")
print(f"Usable range: {network_ip} - {broadcast}")
print(f"Total hosts: {2**(32-SubnetMask.to_cidr(subnet_mask)) - 2}")

# Check if IP is in subnet
test_ip = IPAddress.from_string("192.168.1.50")
is_in = test_ip.is_in_subnet(network_ip, subnet_mask)
print(f"\nIs {test_ip} in subnet? {is_in}")

test_ip2 = IPAddress.from_string("192.168.2.50")
is_in2 = test_ip2.is_in_subnet(network_ip, subnet_mask)
print(f"Is {test_ip2} in subnet? {is_in2}")

# Bitwise operations on IPs
print("\n=== Bitwise Operations ===")
print(f"IP1: {ip1} ({bin(ip1.ip_int)})")
print(f"IP2: {ip2} ({bin(ip2.ip_int)})")
print(f"IP1 & IP2: {ip1 & ip2}")
print(f"IP1 | IP2: {ip1 | ip2}")
print(f"~IP1: {~ip1}")
```

### Example 4: Packing and Unpacking Data
```python
class DataPacker:
    """Pack multiple values into single integer using bitwise ops"""
    
    @staticmethod
    def pack_4_bytes(b1, b2, b3, b4):
        """Pack 4 bytes into 32-bit integer"""
        return (b1 << 24) | (b2 << 16) | (b3 << 8) | b4
    
    @staticmethod
    def unpack_4_bytes(packed):
        """Unpack 32-bit integer into 4 bytes"""
        b1 = (packed >> 24) & 0xFF
        b2 = (packed >> 16) & 0xFF
        b3 = (packed >> 8) & 0xFF
        b4 = packed & 0xFF
        return b1, b2, b3, b4
    
    @staticmethod
    def pack_rgb565(r, g, b):
        """Pack RGB to 16-bit (5 bits R, 6 bits G, 5 bits B)"""
        return ((r & 0x1F) << 11) | ((g & 0x3F) << 5) | (b & 0x1F)
    
    @staticmethod
    def unpack_rgb565(packed):
        """Unpack 16-bit to RGB (5-6-5)"""
        r = (packed >> 11) & 0x1F
        g = (packed >> 5) & 0x3F
        b = packed & 0x1F
        # Scale to 0-255
        r = (r * 255) // 31
        g = (g * 255) // 63
        b = (b * 255) // 31
        return r, g, b
    
    @staticmethod
    def pack_coordinates(x, y, bits_x=12, bits_y=12):
        """Pack two coordinates into single integer"""
        return (x << bits_y) | y
    
    @staticmethod
    def unpack_coordinates(packed, bits_x=12, bits_y=12):
        """Unpack integer into two coordinates"""
        mask_y = (1 << bits_y) - 1
        y = packed & mask_y
        x = packed >> bits_y
        return x, y

# Demo
print("=== Data Packing Demo ===")
print("-" * 40)

# Pack 4 bytes
print("4-Byte Packing:")
b1, b2, b3, b4 = 0x12, 0x34, 0x56, 0x78
packed = DataPacker.pack_4_bytes(b1, b2, b3, b4)
print(f"Bytes: {hex(b1)}, {hex(b2)}, {hex(b3)}, {hex(b4)}")
print(f"Packed: {hex(packed)}")
unpacked = DataPacker.unpack_4_bytes(packed)
print(f"Unpacked: {hex(unpacked[0])}, {hex(unpacked[1])}, {hex(unpacked[2])}, {hex(unpacked[3])}")

# RGB565 packing
print("\nRGB565 Packing:")
r, g, b = 128, 200, 50
packed_rgb = DataPacker.pack_rgb565(r, g, b)
print(f"RGB: ({r}, {g}, {b})")
print(f"Packed RGB565: {hex(packed_rgb)}")
ur, ug, ub = DataPacker.unpack_rgb565(packed_rgb)
print(f"Unpacked RGB: ({ur}, {ug}, {ub})")

# Coordinate packing
print("\nCoordinate Packing:")
x, y = 1234, 5678
packed_xy = DataPacker.pack_coordinates(x, y, 12, 12)
print(f"Coordinates: ({x}, {y})")
print(f"Packed: {packed_xy}")
ux, uy = DataPacker.unpack_coordinates(packed_xy, 12, 12)
print(f"Unpacked: ({ux}, {uy})")

# Memory efficiency demonstration
print("\nMemory Efficiency:")
print(f"Two 12-bit coordinates: 24 bits total")
print(f"Packed into single integer: {packed_xy.bit_length()} bits")
```

### Example 5: Bit Array Implementation
```python
class BitArray:
    """Space-efficient array of bits using bitwise operations"""
    
    def __init__(self, size):
        self.size = size
        # Each integer holds 64 bits (on 64-bit systems)
        self.array_size = (size + 63) // 64
        self.data = [0] * self.array_size
    
    def _get_index(self, position):
        """Get array index and bit position"""
        if not 0 <= position < self.size:
            raise IndexError("Position out of range")
        return position // 64, position % 64
    
    def set(self, position):
        """Set bit at position to 1"""
        idx, bit = self._get_index(position)
        self.data[idx] |= (1 << bit)
    
    def clear(self, position):
        """Set bit at position to 0"""
        idx, bit = self._get_index(position)
        self.data[idx] &= ~(1 << bit)
    
    def toggle(self, position):
        """Toggle bit at position"""
        idx, bit = self._get_index(position)
        self.data[idx] ^= (1 << bit)
    
    def get(self, position):
        """Get bit at position"""
        idx, bit = self._get_index(position)
        return (self.data[idx] >> bit) & 1
    
    def set_range(self, start, end, value=1):
        """Set range of bits to value (0 or 1)"""
        for i in range(start, end):
            if value:
                self.set(i)
            else:
                self.clear(i)
    
    def count_ones(self):
        """Count number of 1 bits"""
        count = 0
        for word in self.data:
            count += bin(word).count('1')
        return count
    
    def count_zeros(self):
        """Count number of 0 bits"""
        return self.size - self.count_ones()
    
    def to_string(self):
        """Convert to binary string"""
        result = []
        for word in reversed(self.data):
            result.append(format(word, '064b'))
        return ''.join(result)[-self.size:]
    
    def __and__(self, other):
        """Bitwise AND of two BitArrays"""
        if self.size != other.size:
            raise ValueError("BitArrays must have same size")
        result = BitArray(self.size)
        for i in range(self.array_size):
            result.data[i] = self.data[i] & other.data[i]
        return result
    
    def __or__(self, other):
        """Bitwise OR of two BitArrays"""
        if self.size != other.size:
            raise ValueError("BitArrays must have same size")
        result = BitArray(self.size)
        for i in range(self.array_size):
            result.data[i] = self.data[i] | other.data[i]
        return result
    
    def __xor__(self, other):
        """Bitwise XOR of two BitArrays"""
        if self.size != other.size:
            raise ValueError("BitArrays must have same size")
        result = BitArray(self.size)
        for i in range(self.array_size):
            result.data[i] = self.data[i] ^ other.data[i]
        return result
    
    def __invert__(self):
        """Bitwise NOT of BitArray"""
        result = BitArray(self.size)
        for i in range(self.array_size):
            result.data[i] = ~self.data[i] & ((1 << 64) - 1)
        return result

# Demo
print("=== BitArray Demo ===")
print("-" * 40)

# Create bit array
ba = BitArray(20)
print(f"Size: {ba.size} bits")
print(f"Initial: {ba.to_string()}")

# Set bits
ba.set(0)
ba.set(5)
ba.set(10)
ba.set(15)
ba.set(19)
print(f"After setting bits: {ba.to_string()}")
print(f"Ones: {ba.count_ones()}, Zeros: {ba.count_zeros()}")

# Clear bit
ba.clear(10)
print(f"After clearing bit 10: {ba.to_string()}")

# Toggle bits
ba.toggle(5)
ba.toggle(15)
print(f"After toggling bits 5 and 15: {ba.to_string()}")

# Set range
ba2 = BitArray(20)
ba2.set_range(2, 18, 1)
print(f"\nBitArray 2: {ba2.to_string()}")

# Bitwise operations
print(f"\nBitArray 1: {ba.to_string()}")
print(f"BitArray 2: {ba2.to_string()}")
print(f"AND: {(ba & ba2).to_string()}")
print(f"OR:  {(ba | ba2).to_string()}")
print(f"XOR: {(ba ^ ba2).to_string()}")
print(f"NOT (BA1): {(~ba).to_string()[:20]}")
```

### Example 6: Error Detection (CRC)
```python
class CRC:
    """CRC (Cyclic Redundancy Check) using bitwise operations"""
    
    @staticmethod
    def crc8(data, polynomial=0x07):
        """Calculate 8-bit CRC"""
        crc = 0
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 0x80:
                    crc = (crc << 1) ^ polynomial
                else:
                    crc <<= 1
                crc &= 0xFF
        return crc
    
    @staticmethod
    def crc16(data, polynomial=0x8005):
        """Calculate 16-bit CRC (CRC-16-IBM)"""
        crc = 0xFFFF
        for byte in data:
            crc ^= (byte << 8)
            for _ in range(8):
                if crc & 0x8000:
                    crc = (crc << 1) ^ polynomial
                else:
                    crc <<= 1
                crc &= 0xFFFF
        return crc
    
    @staticmethod
    def crc32(data):
        """Calculate 32-bit CRC (CRC-32)"""
        crc = 0xFFFFFFFF
        polynomial = 0xEDB88320
        
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 1:
                    crc = (crc >> 1) ^ polynomial
                else:
                    crc >>= 1
        return crc ^ 0xFFFFFFFF
    
    @staticmethod
    def verify_crc8(data, expected_crc, polynomial=0x07):
        """Verify 8-bit CRC"""
        return CRC.crc8(data, polynomial) == expected_crc

# Demo
print("=== CRC Error Detection Demo ===")
print("-" * 40)

# Test data
test_data = b"Hello, World!"
test_data2 = b"Hello, World?"  # Different by one character

# Calculate CRCs
crc8_1 = CRC.crc8(test_data)
crc8_2 = CRC.crc8(test_data2)

print(f"Data 1: {test_data}")
print(f"Data 2: {test_data2}")
print(f"\nCRC-8 of data1: 0x{crc8_1:02X}")
print(f"CRC-8 of data2: 0x{crc8_2:02X}")
print(f"CRCs match? {crc8_1 == crc8_2}")

# CRC-16
crc16_1 = CRC.crc16(test_data)
crc16_2 = CRC.crc16(test_data2)
print(f"\nCRC-16 of data1: 0x{crc16_1:04X}")
print(f"CRC-16 of data2: 0x{crc16_2:04X}")
print(f"CRCs match? {crc16_1 == crc16_2}")

# CRC-32
crc32_1 = CRC.crc32(test_data)
crc32_2 = CRC.crc32(test_data2)
print(f"\nCRC-32 of data1: 0x{crc32_1:08X}")
print(f"CRC-32 of data2: 0x{crc32_2:08X}")
print(f"CRCs match? {crc32_1 == crc32_2}")

# Verification
print("\n=== Verification ===")
crc = CRC.crc8(test_data)
valid = CRC.verify_crc8(test_data, crc)
print(f"Data: {test_data}")
print(f"CRC: 0x{crc:02X}")
print(f"Verification: {'PASSED' if valid else 'FAILED'}")

# Corrupt data
corrupted = bytearray(test_data)
corrupted[5] ^= 0xFF  # Flip bits
valid2 = CRC.verify_crc8(corrupted, crc)
print(f"\nCorrupted data: {corrupted}")
print(f"Verification: {'PASSED' if valid2 else 'FAILED'}")
```

## Common Mistakes

### Mistake 1: Confusing Bitwise with Logical Operators
```python
# Wrong - using bitwise instead of logical
x = 5
y = 10
if x & y:  # Bitwise AND, not logical
    print("Both non-zero")

# Right - use 'and' for logical
if x and y:
    print("Both non-zero")
```

### Mistake 2: Sign Extension in Right Shift
```python
# Right shift on negative numbers preserves sign
x = -8
print(f"{-8 >> 1} = {-8 >> 1}")  # -4 (not 0x7FFFFFFC)

# For unsigned behavior, mask after shift
def unsigned_rshift(n, shift, bits=32):
    mask = (1 << bits) - 1
    return (n >> shift) & mask

print(f"Unsigned -8 >> 1: {unsigned_rshift(-8, 1)}")
```

### Mistake 3: Assuming Bit Length
```python
# Python integers have unlimited bits
x = 1
print(f"~1 = {~1}")  # -2 (not 0xFFFFFFFE in 32-bit)

# Mask to specific bit width
def mask_bits(n, bits=32):
    return n & ((1 << bits) - 1)

print(f"~1 (8-bit): {mask_bits(~1, 8)}")  # 254
```

### Mistake 4: Operator Precedence
```python
# Wrong - unexpected precedence
x = 5
y = 3
result = x << 1 + y  # x << (1 + y), not (x << 1) + y
print(result)  # 5 << 4 = 80

# Right - use parentheses
result = (x << 1) + y
print(result)  # 10 + 3 = 13
```

## Performance Comparison

```python
import time

# Multiplication vs left shift
iterations = 10_000_000

# Using multiplication
start = time.time()
for i in range(iterations):
    result = i * 2
mult_time = time.time() - start

# Using left shift
start = time.time()
for i in range(iterations):
    result = i << 1
shift_time = time.time() - start

print(f"Multiplication: {mult_time:.3f}s")
print(f"Left shift: {shift_time:.3f}s")
print(f"Shift is {mult_time/shift_time:.2f}x faster")

# Division vs right shift
start = time.time()
for i in range(iterations):
    result = i // 2
div_time = time.time() - start

start = time.time()
for i in range(iterations):
    result = i >> 1
rshift_time = time.time() - start

print(f"\nDivision: {div_time:.3f}s")
print(f"Right shift: {rshift_time:.3f}s")
print(f"Shift is {div_time/rshift_time:.2f}x faster")
```

## Quick Reference Table

| Operator | Name | Example | Result |
|----------|------|---------|---------|
| `&` | AND | `0b1100 & 0b1010` | `0b1000` (8) |
| `\|` | OR | `0b1100 \| 0b1010` | `0b1110` (14) |
| `^` | XOR | `0b1100 ^ 0b1010` | `0b0110` (6) |
| `~` | NOT | `~0b1010` | `-0b1011` (-11) |
| `<<` | Left shift | `0b1010 << 1` | `0b10100` (20) |
| `>>` | Right shift | `0b1010 >> 1` | `0b101` (5) |

## Summary

- **`&` (AND)** - Both bits 1 → 1 (used for masking, clearing bits)
- **`|` (OR)** - At least one bit 1 → 1 (used for setting bits)
- **`^` (XOR)** - Bits different → 1 (used for toggling, encryption)
- **`~` (NOT)** - Inverts all bits (used for complement)
- **`<<` (Left shift)** - Multiply by power of 2 (fast multiplication)
- **`>>` (Right shift)** - Divide by power of 2 (fast division)
- **Bitwise operators work on integers** at binary level
- **Python integers have unlimited precision** (no overflow)
- **Use masks** to limit to specific bit widths
- **Permissions/flags** are common use cases
- **Faster than arithmetic** for powers of 2
- **Precedence**: `~` > `<<`/`>>` > `&` > `^` > `|`

## Basic Template
```python
#!/usr/bin/env python3

def bitwise_basics():
    """Demonstrate basic bitwise operations"""
    
    a = 0b1100  # 12
    b = 0b1010  # 10
    
    print(f"a = {bin(a)} ({a})")
    print(f"b = {bin(b)} ({b})")
    print(f"a & b = {bin(a & b)} ({a & b})")
    print(f"a | b = {bin(a | b)} ({a | b})")
    print(f"a ^ b = {bin(a ^ b)} ({a ^ b})")
    print(f"~a = {bin(~a & 0xFF)} ({~a})")
    print(f"a << 1 = {bin(a << 1)} ({a << 1})")
    print(f"a >> 1 = {bin(a >> 1)} ({a >> 1})")

def bit_flags():
    """Use bitwise operators for flags"""
    
    # Define flags
    FLAG_A = 1 << 0  # 1
    FLAG_B = 1 << 1  # 2
    FLAG_C = 1 << 2  # 4
    FLAG_D = 1 << 3  # 8
    
    # Set flags
    flags = 0
    flags |= FLAG_A
    flags |= FLAG_C
    print(f"Flags set: {bin(flags)}")
    
    # Check flags
    print(f"Has FLAG_A: {(flags & FLAG_A) != 0}")
    print(f"Has FLAG_B: {(flags & FLAG_B) != 0}")
    
    # Toggle flag
    flags ^= FLAG_B
    print(f"After toggle FLAG_B: {bin(flags)}")
    
    # Clear flag
    flags &= ~FLAG_A
    print(f"After clear FLAG_A: {bin(flags)}")

def bit_masking():
    """Extract and manipulate bits with masks"""
    
    value = 0b11011010
    
    # Extract lower 4 bits
    lower = value & 0b00001111
    print(f"Lower 4 bits of {bin(value)}: {bin(lower)}")
    
    # Extract upper 4 bits
    upper = (value >> 4) & 0b00001111
    print(f"Upper 4 bits: {bin(upper)}")
    
    # Set specific bits
    mask = 0b00110000
    result = value | mask
    print(f"Set bits: {bin(value)} | {bin(mask)} = {bin(result)}")

def fast_math():
    """Use shifts for fast multiplication/division"""
    
    x = 10
    
    # Multiply by powers of 2
    print(f"{x} * 2 = {x << 1}")
    print(f"{x} * 4 = {x << 2}")
    print(f"{x} * 8 = {x << 3}")
    
    # Divide by powers of 2
    print(f"{x} / 2 = {x >> 1}")
    print(f"{x} / 4 = {x >> 2}")
    print(f"{x} / 8 = {x >> 3}")

def parity_check():
    """Check parity (odd/even) with bitwise"""
    
    def is_even(n):
        return (n & 1) == 0
    
    def is_odd(n):
        return (n & 1) == 1
    
    numbers = [1, 2, 3, 4, 5, 10, 11]
    for n in numbers:
        print(f"{n}: even={is_even(n)}, odd={is_odd(n)}")

if __name__ == "__main__":
    print("=== BITWISE BASICS ===")
    bitwise_basics()
    
    print("\n=== BIT FLAGS ===")
    bit_flags()
    
    print("\n=== BIT MASKING ===")
    bit_masking()
    
    print("\n=== FAST MATH ===")
    fast_math()
    
    print("\n=== PARITY CHECK ===")
    parity_check()
```

*This documentation belongs to https://github.com/InterCentury*