
#List  = [] ordered and changeable. Duplicates OK
#Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#Tuple = () ordered and unchangeable. Duplicates OK. FASTER


friends = ["maruf","siahan","alvi"]
#indexes      0       1       2

print(friends)
#print or access a specific elements from the list
print(friends[0])
print(friends[1])
print(friends[2])
#reverse printing 


print("reverse printing...")
#reverse printint starts from -1 (not 0)
print(friends[-1])
print(friends[-2])
print(friends[-3])


numbers = list(range(1, 10))  # [1, 2, 3, 4, 5]
print(numbers)

fruit_list = ["banana","mango","apple","strawberry"]
#appending element:
fruit_list.append("juice")
print(fruit_list)
#insertinf element:
fruit_list.insert(3,"earth")
print(fruit_list)
#Removing elements
fruit_list.remove("banana")
print(fruit_list)
#concatenating lists
combined = fruit_list+["grape" + "kiwi"]
print (combined)
#repeated list 
repeated_list = [1,2,3] * 6