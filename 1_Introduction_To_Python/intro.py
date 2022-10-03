# name = "Jo"
# Printing my name
# print(name, "Nkumah", 4, True, False)

# Strings
# print("This is a string")
# print('This is also a string')

# Variable
# A variable is used to store data for reuse
firstname = "Jo"
# snake case - python convention
first_name = "Joseph"
last_name = "Nkumah"
# camel case
firstName = "Joseph"

# Do not name variable like this
# 1. Do not start a variable with a number
# 2. Do not name a variable with a Python inbuilt function
# 3. Don not start a variable with special characters(.,!#*)
# 4. Do not name a variable as a string

# print("First Name:", first_name)

# Errors
# Syntax error
# print("This will cause a syntax error')

# print("This will be a name error")

# Numbers
# Integer/int - 1 2 3 4 5 10 100 1000 1000000
# Float - 0.5 5.3 7.88 10.45

# age = 100
# avg_score = 80.6
# height = 181.9

# print("Age:", age)
# print("Average Score:", avg_score)
# print("Height:", height)
# print(100)

# Calculations
# BODMAS - bracket off division multiplication addition subtraction
# PEMDAS - parenthesis exponent multiplication division addition subtraction - Python follows this
# print(400 - 80 + 2)
# print(20 * 5)

# x = 20
# y = 10

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y) # remainder is modulo
# print(x ** y)

# print(25 * 68 + 13 / 28)

# first_name = "Vanessa"
# print(first_name)

# tea_price = 150
# num_of_friends = 5

# total_cost = tea_price * num_of_friends
# print("Old Price:", total_cost)

# Updating the price
# tea_price = 200
# num_of_friends = 5
# total_cost = tea_price * num_of_friends
# print("New Price:", total_cost)

# print("Joseph" + " " + "Nkumah")
first_name = "Joseph"
last_name = "Nkumah"
age = 100
# print(type(age))
# print(type(first_name))
# Casting
# Method of converting a number datatype to a string datatype or vice versa
# print(first_name + last_name + " is " + str(age) + " years old")
# print(f"{first_name} {last_name} is {age} years old")

# += sign
# age = 20
# print(f"Vanessa is currently {age} years old")
# # Updated age
# # age = age + 5
# age += 5
# print(f"Vanessa will be {age} years old in 5 years time")

# adventure = "I had a great time at Paris"
# adventure += " #explore"
# adventure += " #viral"
# print(adventure)

# age -= 5
# print(f"Vanessa's current age is {age}")

# Multi-line Strings
# famous_quote = """Jack of all trades is master of none kdsnipsjfp'welkf'esnfljnsbefkdsnljvdbwnlmds;lcvmlksdvnlksdvbvjv
# ndsjnfdlkvnldml;s,f'ls,fl,f,kdsmfkemf
# dkmfdksfnkerm"""
# famous_quote = '''Jack of all trades is master of none kdsnipsjfp'welkf'esnfljnsbefkdsnljvdbwnlmds;lcvmlksdvnlksdvbvjv
# ndsjnfdlkvnldml;s,f'ls,fl,f,kdsmfkemf
# dkmfdksfnkerm'''
# famous_quote = "Jack of all trades is master of none kdsnipsjfp'welkf'esnfljnsbefkdsnljvdbwnlmds;lcvmlksdvnlksdvbvjv\
# ndsjnfdlkvnldml;s,f'ls,fl,f,kdsmfkemfkdncdsjckdsmcl;dsmc;ldskc'dcdls'c,dlckds'ckpdsjclkdsjcl/dkc;ldmcsl;scmslmdsdkcmd\
# dkmfdksfnkerm"

# print(famous_quote) 

# User Input
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
age = int(input("What is your age? "))
age -= 5
print(type(age))
print(f"{first_name} {last_name} will be {age} years old")