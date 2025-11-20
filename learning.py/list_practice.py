#List  = [] ordered and changeable. Duplicates OK
#Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#Tuple = () ordered and unchangeable. Duplicates OK. FASTER

data_list = list(range(2,102))
print("list,")
print(data_list)
total_sum = sum(data_list)
print("sum of all elements: ", total_sum)
average = total_sum / len(data_list)
print("list average:", average)
max_min_average = max(data_list) / min(data_list)
print("average of maximum and minimum:", max_min_average)
print("maxmimum value:", max(data_list))
print("minimum valure:", min(data_list))

list_of_even_num = [x for x in data_list if x % 2 == 0]
print("even numbers:", list_of_even_num)

list_of_odd_num = [x for x in data_list if x % 2 != 0]
print("list of odd numbers:", list_of_odd_num)

data_list.append("coconut")
print(data_list)# now the list is a mixed list 
data_list.remove("coconut")
print(data_list)

#add something at the specific index 
data_list.insert(30," mango")
print(data_list)

#data_list.sort()
print(data_list)
#data_list.reverse()










































