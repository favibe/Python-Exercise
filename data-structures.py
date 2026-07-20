#Exercise 1: List Creation using two lists
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
odd_elements = l1[1::2]     
even_elements = l2[0::2]     
l3 = []
l3.extend(odd_elements)
l3.extend(even_elements)
print(l3)  

#Exercise 2: Remove and add item in a list
list1 = [54, 44, 27, 79, 91, 41]
print("The Original list ", list1)
element = list1.pop(4)        
print("List After removing element at index 4 ", list1) 
list1.insert(2, element)     
print("List after Adding element at index 2 ", list1) 
list1.append(element)           
print("List after Adding element at last ", list1) 

#Exercise 3: Count the occurrence of each element from a list
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
count_dict = {}
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print(count_dict) 

#Exercise 4: Paired Elements from Two Lists as a Set
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
result = set(zip(first_list, second_list))
print(result)  # {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}

#Exercise 5: Set Intersection and Removal
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("First Set:", first_set)
print("Second Set:", second_set)

intersection = first_set.intersection(second_set)
print("Intersection is:", intersection)

# Remove common elements from first_set
for item in intersection:
    first_set.remove(item)

print("First Set after removing common element:", first_set)

#Exercise 10: remove duplicates from a list
sampleE_list = [87, 45, 41, 65, 94, 41, 99, 94]
print("Original list:", sampleE_list)

# Remove duplicates
unique_list = list(set(sampleE_list))
print("unique items:", unique_list)

# Convert to tuple
t = tuple(unique_list)
print("tuple:", t)

print("min:", min(t))
print("max:", max(t))
