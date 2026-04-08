# 06 - Escape Sequences in Python

## What are Escape Sequences?
Escape sequences are special character combinations that represent characters that cannot be typed directly or have special meaning in strings. They always start with a backslash `\` followed by one or more characters.

## Why Use Escape Sequences?

### 1. Include Special Characters in Strings
```python
# Without escape sequences - impossible
print("She said "Hello"")  # Syntax error!

# With escape sequences - works
print("She said \"Hello\"")
```

### 2. Format Text Output
```python
# Add newlines, tabs, etc.
print("Line1\nLine2\nLine3")
print("Column1\tColumn2\tColumn3")
```

### 3. Handle Paths and File Names
```python
# Windows paths need backslashes
path = "C:\\Users\\Name\\Documents"
```

## Common Escape Sequences

| Escape Sequence | Meaning | Example Output |
|----------------|---------|----------------|
| `\n` | Newline | Moves to next line |
| `\t` | Tab | Horizontal tab space |
| `\\` | Backslash | Prints one backslash |
| `\'` | Single quote | Prints ' |
| `\"` | Double quote | Prints " |
| `\r` | Carriage return | Moves to line start |
| `\b` | Backspace | Deletes previous char |
| `\f` | Form feed | Page break (rare) |
| `\v` | Vertical tab | Vertical spacing |
| `\a` | Bell/Alert | Makes beep sound |
| `\0` | Null character | Null terminator |

## Newline `\n`

```python
# Basic newline
print("Hello\nWorld")
# Output:
# Hello
# World

# Multiple newlines
print("Line1\n\nLine3")
# Output:
# Line1
# 
# Line3

# Newline in the middle
print("Start\nMiddle\nEnd")
# Output:
# Start
# Middle
# End

# Using with other text
print("Name: Alice\nAge: 25\nCity: NYC")
# Output:
# Name: Alice
# Age: 25
# City: NYC
```

## Tab `\t`

```python
# Basic tab
print("Name:\tJohn")
# Output: Name:    John

# Multiple tabs
print("A\tB\tC")
# Output: A    B    C

# Aligning columns
print("Item\t\tPrice")
print("Laptop\t\t$999")
print("Mouse\t\t$25")
print("Keyboard\t$79")
# Output:
# Item            Price
# Laptop          $999
# Mouse           $25
# Keyboard        $79

# Tabs with other text
print("1.\tFirst item")
print("2.\tSecond item")
print("10.\tTenth item")
# Output:
# 1.      First item
# 2.      Second item
# 10.     Tenth item
```

## Backslash `\\`

```python
# Single backslash
print("C:\\Users\\Name")
# Output: C:\Users\Name

# Multiple backslashes
print("Folder\\Subfolder\\file.txt")
# Output: Folder\Subfolder\file.txt

# Network path
print("\\\\server\\share\\folder")
# Output: \\server\share\folder

# Raw string alternative (no escape needed)
print(r"C:\Users\Name\Documents")
# Output: C:\Users\Name\Documents
```

## Quotes `\'` and `\"`

```python
# Single quotes inside single-quoted string
print('It\'s a beautiful day')
# Output: It's a beautiful day

# Double quotes inside double-quoted string
print("She said \"Hello\" to me")
# Output: She said "Hello" to me

# Mixing quotes without escape
print("It's a beautiful day")    # OK - double quotes outside
print('She said "Hello" to me')  # OK - single quotes outside

# Multiple quotes
print('He shouted "It\'s amazing!"')
# Output: He shouted "It's amazing!"

# Triple quotes (no escape needed)
print("""She said "It's awesome" """)
# Output: She said "It's awesome"
```

## Carriage Return `\r`

```python
# Carriage return moves cursor to start of line
print("Hello\rWorld")
# Output: World (Hello is overwritten)

# Progress indicator with \r
import time
for i in range(4):
    print(f"\rLoading {'.' * i}", end="", flush=True)
    time.sleep(0.5)
print("\rDone!     ")
# Output: Loading ... (animated) then Done!

# Updating same line
import time
for percent in range(0, 101, 20):
    print(f"\rProgress: {percent}%", end="", flush=True)
    time.sleep(0.5)
print("\rComplete!    ")
# Output: Progress: 0% -> 20% -> etc. on same line
```

## Backspace `\b`

```python
# Backspace deletes previous character
print("Hello\bWorld")
# Output: HellWorld (o is deleted)

# Multiple backspaces
print("12345\b\b\bABC")
# Output: 12ABC (345 deleted)

# Fixing typos
print("Helo\blo World")
# Output: Hello World

# Removing characters
print("Wrongggg\b\b\b Correct")
# Output: Wrong Correct
```

## Bell/Alert `\a`

```python
# Makes system beep sound (terminal dependent)
print("\a")  # May produce beep

# Alert with message
print("Warning!\a Invalid input")

# Multiple beeps
print("\a\a\a Emergency!")

# Note: May not work in all environments
# Some IDEs or terminals might ignore it
```

## Form Feed `\f` and Vertical Tab `\v`

```python
# Form feed (page break) - rarely used
print("Page 1\fPage 2")
# Output may vary by terminal

# Vertical tab
print("Line1\vLine2\vLine3")
# Output varies by terminal

# Note: These are legacy escape sequences
# Rarely used in modern Python programming
```

## Null Character `\0`

```python
# Null terminator (rare in Python)
text = "Hello\0World"
print(text)  # May print only "Hello"
print(len(text))  # Includes null character

# Used mainly for binary data or C interoperability
```

## Combining Escape Sequences

```python
# Multiple sequences together
print("Name:\tAlice\nAge:\t25\nCity:\tNYC")
# Output:
# Name:    Alice
# Age:     25
# City:    NYC

# Complex formatting
print("Item\t\tQty\tPrice\n----\t\t---\t-----\nLaptop\t\t1\t$999\nMouse\t\t2\t$50")
# Output:
# Item            Qty     Price
# ----            ---     -----
# Laptop          1       $999
# Mouse           2       $50

# Creating a box
print("┌────────┐\n│\t │\n└────────┘")
# Output:
# ┌────────┐
# │        │
# └────────┘
```

## Raw Strings (r-string)

```python
# Raw strings ignore escape sequences
print(r"C:\Users\Name\Documents")
# Output: C:\Users\Name\Documents

# Compare with regular string
print("C:\\Users\\Name\\Documents")  # Need double backslash
print(r"C:\Users\Name\Documents")     # Much cleaner

# Raw strings with quotes
print(r'She said "Hello"')
# Output: She said "Hello"

# Raw string with newline (prints as characters)
print(r"Line1\nLine2")
# Output: Line1\nLine2 (not actual newline)

# Raw strings cannot end with backslash
# print(r"C:\folder\")  # Syntax error!
print(r"C:\folder\\")   # Workaround
print("C:\\folder\\")    # Regular string
```

## Practical Examples

### Example 1: Multi-line Address
```python
# Formatting an address
name = "John Doe"
street = "123 Main Street"
city = "Springfield"
state = "IL"
zipcode = "62701"

address = f"{name}\n{street}\n{city}, {state} {zipcode}"
print(address)

# Output:
# John Doe
# 123 Main Street
# Springfield, IL 62701
```

### Example 2: Table Formatter
```python
# Creating a formatted table
print("Product\t\tPrice\t\tQuantity")
print("-" * 40)
print("Laptop\t\t$999.99\t\t5")
print("Mouse\t\t$25.50\t\t20")
print("Keyboard\t$79.99\t\t8")
print("Monitor\t\t$299.99\t\t3")

# Output:
# Product         Price           Quantity
# ----------------------------------------
# Laptop          $999.99         5
# Mouse           $25.50          20
# Keyboard        $79.99          8
# Monitor         $299.99         3
```

### Example 3: Progress Bar with \r
```python
import time

def progress_bar(total, duration=5):
    """Display a progress bar that updates in place"""
    for i in range(total + 1):
        percent = (i / total) * 100
        bar_length = 40
        filled = int(bar_length * i / total)
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"\rProgress: |{bar}| {percent:.1f}%", end="", flush=True)
        time.sleep(duration / total)
    print("\rComplete!                     ")

progress_bar(50, 2)
# Output (animated on same line):
# Progress: |████████████████████████████████████████| 100.0%
# Complete!
```

### Example 4: Text Animation
```python
import time

# Spinner animation
frames = ["-", "\\", "|", "/"]
for i in range(20):
    print(f"\rLoading {frames[i % 4]}", end="", flush=True)
    time.sleep(0.1)
print("\rDone!     ")

# Output: Animated spinner

# Countdown timer
for i in range(10, 0, -1):
    print(f"\rTime remaining: {i} seconds", end="", flush=True)
    time.sleep(1)
print("\rTime's up!            ")

# Output: Countdown on same line
```

### Example 5: File Path Handling
```python
import os

# Windows paths
windows_path = "C:\\Users\\Name\\Documents\\file.txt"
print(f"Windows: {windows_path}")

# Using raw string (cleaner)
windows_path_raw = r"C:\Users\Name\Documents\file.txt"
print(f"Raw: {windows_path_raw}")

# Convert to correct OS format
unix_path = windows_path.replace("\\", "/")
print(f"Unix: {unix_path}")

# Using os.path
correct_path = os.path.join("C:", "Users", "Name", "Documents", "file.txt")
print(f"os.path: {correct_path}")

# Output:
# Windows: C:\Users\Name\Documents\file.txt
# Raw: C:\Users\Name\Documents\file.txt
# Unix: C:/Users/Name/Documents/file.txt
# os.path: C:Users\Name\Documents\file.txt
```

### Example 6: Menu System with Box Drawing
```python
# Creating a menu with box characters
print("╔" + "═" * 30 + "╗")
print("║" + " " * 30 + "║")
print("║" + "     MAIN MENU".center(30) + "║")
print("║" + " " * 30 + "║")
print("║" + "  1. Start Game".ljust(30) + "║")
print("║" + "  2. Load Game".ljust(30) + "║")
print("║" + "  3. Settings".ljust(30) + "║")
print("║" + "  4. Exit".ljust(30) + "║")
print("║" + " " * 30 + "║")
print("╚" + "═" * 30 + "╝")

# Output:
# ╔══════════════════════════════╗
# ║                              ║
# ║          MAIN MENU           ║
# ║                              ║
# ║  1. Start Game               ║
# ║  2. Load Game                ║
# ║  3. Settings                 ║
# ║  4. Exit                     ║
# ║                              ║
# ╚══════════════════════════════╝
```

### Example 7: CSV Data Generation
```python
# Creating CSV data with escape sequences
data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "Los Angeles"],
    ["Charlie", "35", "Chicago"]
]

# Write to CSV format
with open("output.csv", "w") as f:
    for row in data:
        # Join with commas, add newline
        line = ",".join(row) + "\n"
        f.write(line)
        print(line, end="")

# Output:
# Name,Age,City
# Alice,25,New York
# Bob,30,Los Angeles
# Charlie,35,Chicago
```

### Example 8: Quote Escaping in JSON-like String
```python
# Building a JSON string manually
name = "Alice"
message = 'She said "Hello"'
age = 25

# Using escape sequences
json_string = f'{{"name": "{name}", "message": "{message}", "age": {age}}}'
print(json_string)

# Handling quotes inside
text = 'He shouted "It\'s amazing!"'
json_string2 = f'{{"text": "{text}"}}'
print(json_string2)

# Output:
# {"name": "Alice", "message": "She said \"Hello\"", "age": 25}
# {"text": "He shouted \"It's amazing!\""}
```

## Escape Sequences in Different Contexts

### In f-strings
```python
name = "Alice"
print(f"Hello\n{name}")  # Newline works
print(f"Name:\t{name}")   # Tab works
print(f"{{name}}")        # Escape braces with double braces
# Output: {name}
```

### In .format() strings
```python
print("Line1\nLine2")  # Newline
print("{{brackets}}".format())  # Escape braces
# Output: {brackets}
```

### In Regular Expressions
```python
import re

# In regex, backslash has special meaning
pattern = r"\d+"  # Raw string for regex
text = "123 abc"
match = re.search(pattern, text)
print(match.group())  # Output: 123

# Without raw string (need double escape)
pattern = "\\d+"
match = re.search(pattern, text)
print(match.group())  # Output: 123
```

## Common Mistakes

### Mistake 1: Forgetting to Escape Backslashes
```python
# Wrong
path = "C:\Users\Name"  # \U and \N are escape sequences!
# Output: SyntaxError or weird characters

# Right
path = "C:\\Users\\Name"
path = r"C:\Users\Name"
```

### Mistake 2: Mixing Quotes Incorrectly
```python
# Wrong
text = 'It's Python'  # Syntax error

# Right
text = "It's Python"
text = 'It\'s Python'
```

### Mistake 3: Assuming Raw Strings End with Backslash
```python
# Wrong
path = r"C:\folder\"  # Syntax error

# Right
path = r"C:\folder\\"
path = "C:\\folder\\"
```

### Mistake 4: Forgetting \r Overwrites
```python
# Wrong - expecting both lines
print("Hello\rWorld")  # Only "World" shows

# Right - add newline
print("Hello\r\nWorld")  # Both show
```

### Mistake 5: Using \n in input()
```python
# Wrong - input doesn't interpret escape sequences
text = input("Enter text with \\n: ")
print(text)  # Prints literally, not as newline

# Right - manually replace
text = input("Enter text: ").replace("\\n", "\n")
print(text)
```

## Best Practices

### ✅ Do This
```python
# Use raw strings for Windows paths
path = r"C:\Users\Name\Documents"

# Use triple quotes for multi-line strings
message = """Line 1
Line 2
Line 3"""

# Use \n for newlines in formatted output
print(f"Name: {name}\nAge: {age}")

# Use \r for updating same line
print(f"\rProgress: {percent}%", end="", flush=True)

# Use double quotes to avoid escaping single quotes
text = "It's easy"  # No escape needed

# Use .replace() for dynamic escape sequences
user_input = user_input.replace("\\n", "\n")
```

### ❌ Avoid This
```python
# Avoid - double escaping when not needed
path = "C:\\\\Users\\\\Name"  # Too many backslashes

# Avoid - manual line breaks with \n when triple quotes work
text = "Line1\nLine2\nLine3"  # Hard to read

# Avoid - mixing quotes unnecessarily
text = 'She said \"Hello\"'  # Use double quotes outside

# Avoid - assuming \r works everywhere
# Some terminals don't support carriage return well

# Avoid - invisible escape sequences in user-facing strings
print("Value:\x00")  # Null character may cause issues
```

## Platform Differences

```python
import os

# Different newline characters by platform
# Windows: \r\n
# Linux/Mac: \n
# Old Mac: \r

# Python handles it automatically
with open("file.txt", "w") as f:
    f.write("Line1\nLine2")  # Python converts \n to platform default

# Explicit platform newline
import platform
if platform.system() == "Windows":
    newline = "\r\n"
else:
    newline = "\n"

# Using os.linesep (platform-specific newline)
import os
print(f"Line1{os.linesep}Line2")
```

## Quick Reference Table

| Sequence | Name | Common Use |
|----------|------|-------------|
| `\n` | Newline | Line breaks |
| `\t` | Tab | Column alignment |
| `\\` | Backslash | File paths |
| `\'` | Single quote | Strings with quotes |
| `\"` | Double quote | Strings with quotes |
| `\r` | Carriage return | Progress bars |
| `\b` | Backspace | Simple animations |
| `\a` | Bell | Alerts |
| `r""` | Raw string | Paths, regex |

## Summary

- **Escape sequences** start with backslash `\`
- **`\n`** creates newlines for multi-line output
- **`\t`** creates tabs for column alignment
- **`\\`** prints a single backslash (for paths)
- **`\'`** and **`\"`** include quotes in strings
- **`\r`** returns cursor to line start (progress bars)
- **Raw strings** (`r""`) ignore escape sequences
- **Triple quotes** are better for multi-line strings
- **Platform differences** affect newline characters
- Use **`\r` with `end=""` and `flush=True`** for updating lines

## Basic Template
```python
#!/usr/bin/env python3

# Basic escape sequences
print("Hello\nWorld")  # Newline
print("Name:\tAlice")   # Tab
print("Path: C:\\Users\\Name")  # Backslash

# Quotes in strings
print("She said \"Hello\"")
print('It\'s Python')

# Multi-line string (preferred method)
message = """This is line 1
This is line 2
This is line 3"""
print(message)

# Progress indicator with carriage return
import time
for i in range(101):
    if i % 10 == 0:
        print(f"\rProgress: {i}%", end="", flush=True)
    time.sleep(0.01)
print("\rComplete!     ")

# Raw strings for paths
windows_path = r"C:\Users\Name\Documents"
print(windows_path)

# Table formatting
print("Item\t\tPrice\t\tStock")
print("Laptop\t\t$999\t\t5")
print("Mouse\t\t$25\t\t20")
```

*This documentation belongs to https://github.com/InterCentury*