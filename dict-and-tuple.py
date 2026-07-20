#Exercise 1: Basic Dictionary Operations
student = {"name": "Alice", "age": 20, "grade": "B"}
student["city"] = "New York"
student["age"] = 21
print(student) 
print("Name:", student["name"])  # Name: Alice

#Exercise 2: Dictionary Operations
car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}
car.pop("color")
print(car)
print(car.items())
print("brand" in car)
print("color" in car)

#Exercise 3: Dictionary from Two Lists
keys = ["name", "age", "city"]
values = ["Bob", 25, "London"]
result = dict(zip(keys, values))
print(result)

#Exercise 4: Initialize Dictionary with Default Values
keys = ["math", "science", "english", "history"]
default = 0
scores = dict.fromkeys(keys, default)
print(scores)

#Exercise 9: Rename a Key of Dictionary
employee = {"fname": "John", "age": 30, "dept": "Engineering"}
employee["first_name"] = employee.pop("fname")
print(employee)



#Exercise 1: Basic Tuple Operations
fruits = ("apple", "banana", "cherry", "date")

print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("Length:", len(fruits))

#Exercise 2: The Trailing Comma
t = (50,)

print(t)
print(type(t))

#Exercise 3: Tuple Repetition
colors = ("red", "green")
repeated = colors * 3
print(repeated)

#Exercise 4: Tuple Reversal
items = (1, 2, 3, 4, 5)
reversed_items = items[::-1]
print(reversed_items) 

#Exercise 5: Type Casting
my_list = [10, 20, 30, 40, 50]
my_tuple = tuple(my_list)
print(my_tuple)      
print(type(my_tuple))

#Exercise 10: Counting
votes = ("yes", "no", "yes", "yes", "no", "yes")
yes_count = votes.count("yes")
no_count = votes.count("no")
print("yes appears", yes_count, "times")  
print("no appears", no_count, "times")    
