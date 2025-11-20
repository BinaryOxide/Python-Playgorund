# List-related built-in functions in Python using lucky_numbers

# Example list of lucky numbers
lucky_numbers = [7, 3, 8, 21, 13, 42, 17]

# 1. len() - Returns the number of items in the list
print("Number of lucky numbers:", len(lucky_numbers))  # Output: 7

# 2. sorted() - Returns a new sorted list
print("Sorted lucky numbers:", sorted(lucky_numbers))  # Output: [3, 7, 8, 13, 17, 21, 42]

# 3. reversed() - Returns a reverse iterator of the list
print("Reversed lucky numbers:", list(reversed(lucky_numbers)))  # Output: [17, 42, 13, 21, 8, 3, 7]

# 4. sum() - Returns the sum of all elements in the list
print("Sum of lucky numbers:", sum(lucky_numbers))  # Output: 111

# 5. min() - Returns the smallest element in the list
print("Smallest lucky number:", min(lucky_numbers))  # Output: 3

# 6. max() - Returns the largest element in the list
print("Largest lucky number:", max(lucky_numbers))  # Output: 42

# 7. all() - Returns True if all elements in the list are true (or if the list is empty)
print("Are all lucky numbers true?", all(lucky_numbers))  # Output: True

# 8. any() - Returns True if at least one element in the list is true
print("Is any lucky number true?", any(lucky_numbers))  # Output: True

# 9. enumerate() - Adds a counter to the list and returns it as an enumerate object
print("Enumerated lucky numbers:")
for index, value in enumerate(lucky_numbers):
    print(f"Index: {index}, Lucky Number: {value}")
# Output :
# Index: 0, Lucky Number: 7 <-----------------<\_/>-----------------> <\>
# Index: 1, Lucky Number: 3 <-----------------<\_/>-----------------> <\>
# Index: 2, Lucky Number: 8 <-----------------<\_/>-----------------> <\>
# Index: 3, Lucky Number: 2 <-----------------<\_/>-----------------> <\>
# Index: 4, Lucky Number: 1 <-----------------<\_/>-----------------> <\>
# Index: 5, Lucky Number: 4 <-----------------<\_/>-----------------> <\>
# Index: 6, Lucky Number: 1 <-----------------<\_/>-----------------> <\>
# 10. zip() - Combines multiple lists into a single iterable of tuples
lucky_colors = ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Orange', 'Pink']
print("Zipped lucky numbers and colors:", list(zip(lucky_numbers, lucky_colors)))
# Output: [(7, 'Red'), (3, 'Green'), (8, 'Blue'), (21, 'Yellow'), (13, 'Purple'), (42, 'Orange'), (17, 'Pink')]

# 11. map() - Applies a function to all items in the list
squared_numbers = map(lambda x: x ** 2, lucky_numbers)
print("Squared lucky numbers:", list(squared_numbers))  # Output: [49, 9, 64, 441, 169, 1764, 289]

# 12. filter() - Filters elements in the list based on a condition                                                
even_lucky_numbers = filter(lambda x: x % 2 == 0, lucky_numbers)                                      
print("Even lucky numbers:", list(even_lucky_numbers))  # Output: [8, 42                                            
# 13. list() - Converts an iterable (e.g., tuple, string) into a list                                                 
lucky_tuple = (7, 3, 8, 21, 13, 42, 17)                                                         
print("Converted tuple to list:", list(lucky_tuple))  # Output: [7, 3, 8, 21, 13, 42, 17]               