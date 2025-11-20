import math,operator
# Some basic arithmetic operations using functions
print(sum([1, 2]))  # summation = 1 + 2 = 3
print(operator.sub(2, 1))  # subtraction = 2 - 1 = 1
print(operator.truediv(4, 2))  # division = 4 / 2 = 2.0
print(operator.mul(6, 3))  # multiplication = 6 * 3 = 18
print(pow(3, 2))  # 3^2 = 9

import random 
print(random.randrange(1,1000)) #print a random number from 1 to 1000
print(random.randint(1, 10))    # Random integer between 1 and 10
print(random.uniform(1, 10))    # Random float between 1 and 10
print(random.choice([1, 2, 3, 4]))  # Random choice from list


#maximum minimum operation using function
print(max(3,988)) # max value = 988(output)
print(min(3,300)) #minimum value = 3(output)
# Additional max and min operations with more numbers
print(max(10, 20, 30, 40, 50))  # max value = 50 (output)
print(min(10, 20, 30, 40, 50))  # minimum value = 10 (output)

#Square Root and Power Functions
print(math.sqrt(16))   # Square root of 16 → 4.0
print(math.pow(3, 4))  # 3 raised to power 4 → 81.0

#Factorial and GCD (Greatest Common Divisor)
print(math.factorial(5))   # 5! (5×4×3×2×1) → 120
print(math.gcd(36, 60))    # GCD of 36 and 60 → 12

#Rounding Functions
print(round(5.678))    # Round to nearest integer → 6
print(round(5.678, 2)) # Round to 2 decimal places → 5.68

#Exponentiation and Power
print(pow(2, 3))  # 2 raised to the power of 3 → 8

#Sorting
numbers = [4, 7, 1, 9, 12]
print(sorted(numbers))       # Sorted list → [1, 4, 7, 9, 12]
print(sorted(numbers, reverse=True))  # Descending order → [12, 9, 7, 4, 1]

# Constants
print(math.pi)  # PI = 3.141592653589793
print(math.e)   # EULER's Number = 2.718281828459045

# Trigonometric Functions (Angles in Radians)
angle = math.radians(30)  # Convert degrees to radians
print(math.sin(angle))  # Sin(30°)
print(math.cos(angle))  # Cos(30°)
print(math.tan(angle))  # Tan(30°)

# Type Conversion
print(ord('A'))   # ASCII value of 'A' → 65
print(chr(65))    # Character from ASCII → 'A'
print(hex(255))   # Convert to hexadecimal → '0xff'
print(oct(8))     # Convert to octal → '0o10'
print(bin(10))    # Convert to binary → '0b1010'