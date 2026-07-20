#Exercise 1. Arithmetic Product and Conditional Logic
def multiply_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
print(multiply_or_sum(20, 30))  # 600
print(multiply_or_sum(40, 30))  # 70

#Exercise 2. Cumulative Sum of a Range
previous_num = 0

for current_num in range(10):
    total = previous_num + current_num
    print("Current Number", current_num,
          "Previous Number", previous_num,
          "Sum:", total)

    previous_num = current_num

#Exercise 3: Remove First n Characters
def remove_chars(word, n):
    return word[n:]

print(remove_chars("pynative", 4))  # tive
print(remove_chars("pynative", 2))  # native


#Exercise 4. String Slicing and Substring Removal
text = "pynative"
print(text[::2])


#Exercise 5. Variable Swapping (The In-Place Method)
a = 5
b = 10
print(f"Before Swap: a = {a}, b = {b}")

a, b = b, a 

print(f"After Swap: a = {a}, b = {b}")


#Exercise 6: Factorial with Loop
num = 5
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")

#Exercise 7: List Add & Remove
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits.append("fig")
fruits.pop(1)
print(fruits)

#Exercise 8: String Reversal
text = "Python"
reversed_text = text[::-1]
print(f"Reversed: {reversed_text}")

#Exercise 9: Min & Max in List
nums = [45, 2, 89, 12, 7]
print(f"Largest: {max(nums)}")
print(f"Smallest: {min(nums)}")

#Exercise 10: Remove Duplicates
data = [1, 2, 2, 3, 4, 4, 4, 5]
unique_data = list(set(data))
print(f"Unique List: {unique_data}")

