names = ["Jo", "Vanessa", "Fredrick", "Shanice", "Rachel"]

# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])

# For Loop
# Syntax
# for <temporary variable> in <collection>:
#     <code to execute>
# name = rachel
# for name in names:
#     print(name)
# for name in names:
#     name += " Saleh"
#     print(name)
# for name in names: print(name)

# For Loops: Using Range
# Syntax
# for <temporary variable> in <list of length of number>:
#     <execute code on temporary variable>

# for i in range(100):
#     print("I, Vanessa will read my Python books and do my assignments", i+1)

# for _ in range(6):
#     print("Meow")

# While Loop
# while <conditional statement>:
#     <execute code>

# count = 0
# while count < 5:
#     print("Meow")
#     count += 1
# Meow
# Meow
# Meow
# Meow
# Meow

# i = 5
# while i != 0:
#     print("Woof")
#     i -= 1

# While Loops: Lists
# index = 0

# while index < len(names):
#     print(names[index])
#     index += 1

# Infinite Loops
# nums = [2, 4, 6, 7, 9]

# for num in nums:
#     nums.append(7)

# Loop Control: Break

# for name in names:
#     print(name)
#     if name == "Shanice":
#         break
# print("End Search")

# Loop Control: Continue
# ages = [17, 19, 20, 30, 40, 30, 7, 30, 24, 60]

# for age in ages:
#     if age == 30:
#         continue
#     print(age)

# Nested Loops
# bio = [
#     ["Jo", 100],
#     ["Vanessa", 20],
#     ["Fredrick", 30],
#     ["Shanice", 24],
#     ["Rachel", 28]
# ]

# for info in bio:
#     for data in info:
#         print(data)

# List Comprehensions
# full_names = []

# for name in names:
#     full_names.append(name + " Saleh")
    
# print(full_names)
# Syntax
# new_list = [<code to execute> for <element> in <collection>]
# full_names = [name + " Saleh" for name in names]
# print(full_names)

# List Comprehension Using Conditionals
# odd_nums = [num for num in range(100) if num % 2 != 0]
# print(odd_nums)

even_odd = [f"Even: {num}" if num % 2 == 0 else f"Odd: {num}" for num in range(100)]
print(even_odd)