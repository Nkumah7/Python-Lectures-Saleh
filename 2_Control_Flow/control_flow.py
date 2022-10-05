# Relational Operators: 
# 1. Equals - ==
# 2. Not equals - !=

# print(1 == 1)
# print(5 != 6)
# print(8.9 == 9)
# print(10 == "10")

# print(10 - 5 == (5 ** 2)/5)
# print(40 + (100/10) != 100 - 60)

# bool_one = 10 != 17
# bool_two = 4 * 5 != 20
# bool_three = 6 * 6 == 36

# print(bool_one, bool_two, bool_three)

# If statement
# if (condition is met):
#     execute code
# is_raining = False
# if is_raining:
#     print("Bring your umbrella")

# if 10 ** 3 == (1000000 - (10**3)):
#     print("These numbers are confusing me!")

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))

# if num1 == num2:
#     print("Vanessa needs to read her Python notes!")

# Relational Operators II
# 1. greater than - >
# 2. greater than or equal to - >=
# 3. less than - <
# 4. less than or equal to - <=

vanessa_age = 20
friend_age = (vanessa_age ** 2) /  20

# if vanessa_age > friend_age:
#     print("Vanessa is older than her friend")

# if vanessa_age >= friend_age:
#     print("Vanessa is older than her friend")

# Boolean Operators (logical operators)
# 1. and - all statements must be True for condition to met
# 2. or - One statement must be True for condition to be met
# 3. not - Opposite of the condition 

# and
# print((5 + 5 == 10) and (100/10 == 10))
# print((0.5 > (1/2)) and (7.5 > 4))
# print((100 - 50 <= 70) and (-20 * -10 < -5))

# or
# print(-4<-5)
# print(True or -4 < -5)
# print(2**3 == 9 or False)

# not
# print(not True == False)
# print(not False == False)

# print(not(4*2 >=10) and (3 * 3 == 9))
# print(not((7 ** 2 == 49) and (30/2 == 7+8)))

vanessa_age += 5
friend_age -= 5

# if vanessa_age >= friend_age:
#     print("Vanessa is getting old")

# if not friend_age <= 20:
#     print("Your friend is young")
    
# if not(not vanessa_age >= friend_age or friend_age <= 20):
#     print("All these ages are confusing me")

# If-Else
# if (statement):
#     execute code if condition is met
# else:
#     execute code if condition is not met


# if vanessa_age <= friend_age:
#     print("Vanessa is getting old")
# else:
#     print("Vanessa is looking younger by the day")

# gender = "Female"

# if not(vanessa_age >= 18 and gender == "Female"):
#     print("You are allowed in the club")
# else:
#     print("Go home, you are too young")

# If-Else If
# if (statement):
#     execute code if statement 1 is True
# elif (statement):
#     execute code if statement 1 is False and statement 2 is True
# elif (statement):
#     execute code if statement 1 and statement 2 are False and statement 3 is True
# else:
#     execute code if all statements are False

# score = int(input("Biology Score: "))

# if score >= 90 and score <= 100:
#     print("A")
# elif score >= 80 and score < 90:
#     print("B")
# elif score >= 70 and score < 80:
#     print("C")
# elif score >= 60 and score < 70:
#     print("D")
# else:
#     print("F")

# if 90 <= score and score <= 100:
#     print("A")
# elif 80 <= score and score < 90:
#     print("B")
# elif 70 <= score and score < 80:
#     print("C")
# elif 60 <= score and score < 70:
#     print("D")
# else:
#     print("F")

# if 90 <= score <= 100:
#     print("A")
# elif 80 <= score < 90:
#     print("B")
# elif 70 <= score < 80:
#     print("C")
# elif 60 <= score < 70:
#     print("D")
# else:
#     print("F")

# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# ternary operators
print("Even" if num % 2 == 0 else "Odd")
