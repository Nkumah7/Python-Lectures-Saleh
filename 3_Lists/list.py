ages = [20, 19, 17, 24]

names = ["Vanessa", "Jo", "Shanice", "Divine"]

different_datatypes = ["Vanessa", 7, True, False, 9.3, ["Jo", 5, 10.5]]

empty_list = []
# print(empty_list)
# print(ages)
# print(names)

# list_name.method().

# append - Used to add an element to the end of the list
# print("Old list: ", names)
names.append("Rachel")
# print("New list: ", names)

# print("Old ages: ", ages)
ages.append(21)
ages.append(23)
# print("New ages: ", ages)

# Remove
# list_name.remove(element)
# print("Old datatypes: ", different_datatypes)
# different_datatypes.remove(False)
# different_datatypes.remove(9.3)
# print("New datatypes: ", different_datatypes)

shopping_basket = []

# Growing a List: Append

# shopping_basket.append("Sugar")
# shopping_basket.append("Soap")
# shopping_basket.append("Toothbrush")
# print(shopping_basket)

# Growing a List: Plus(+)
# stuff = ["Sugar", "Soap", "Toothbrush"]
# shopping_basket = shopping_basket + ["Sugar"]
# shopping_basket += stuff
# print(shopping_basket)

# shoe_sizes = [40]

# shoe_sizes.append(41)
# shoe_sizes.append(42)
# shoe_sizes.append(44)

# print(shoe_sizes)

# sizes = [41, 42, 44]
# shoe_sizes += sizes
# print(shoe_sizes)

# Accessing a List: Positive index
# print(names[0])
# print(names[1])
# print(names[4])

# Accessing a List: Negative index
# print(names[-1])
# print(names[-3])
# print(names[-5])

# Modifying List Elements
# makeup_kit = ["Lip gloss", "Foundation", "Concealer", "Lip stick"]
# print("Old Makeup Kit: ", makeup_kit)
# makeup_kit[0] = "Powder"
# makeup_kit[-2] = "Eye Pencil"
# print("New Makeup Kit: ", makeup_kit)

# Two-Dimensional (2D) Lists
bio = ["Dan", 24]

friends_bio = [
    ["Vanessa", 20], 
    ["Jo", 18], 
    ["Shanice", 14], 
    ["Divine", 15],
    ["Rachel", 23]
    ]

# print("Old friends bio: ", friends_bio)
friends_bio.append(["Fredrick", 18])
# print("New friends bio: ", friends_bio)

# Accessing 2D Lists
# print(friends_bio[0])
# print(friends_bio[-3])
# print(friends_bio[0][0])
# print(friends_bio[-3][-1])
# print(friends_bio[1][-1])

# Modifying 2D Lists
# friends_bio[2] = ["Michael", 16]
# friends_bio[2][-1] = 17
# print(friends_bio)

# Working with Lists
# Example syntax
# list.method(input)

# Example syntax for a built-in function
# builtinfunction(input)

# insert
# vanessa_games = ["Red Dead Redemption", "Detroit: Be Human", "Call of Duty"]
# print("Old games: ", vanessa_games)
# vanessa_games.insert(1, "DMC")
# print("New games: ", vanessa_games)

# pop
# anime = ["Made in Abyss", "Naruto", "Bleach", "One Piece", "Attack on Titan", "Dragon Ball Z"]
# print("Old Anime: ", anime)
# removed_item = anime.pop()
# print("New Anime: ", anime)
# print(removed_item)

# anime.pop(3)
# print("New new anime: ", anime)

# Consecutive Lists: Range
# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# num_list = range(10)
# print(list(num_list))

# range(starting point, ending point)
# num_list2 = range(10, 51)
# print(list(num_list2))

# range(starting point, ending point, increment)
# num_list3 = range(0, 101, 10)
# print(list(num_list3))

# num_list4 = range(101, 0, -10)
# print(list(num_list4))

# Len
# print(len(names))

# Slicing Lists I - Positive Index
# Syntax
# list[start:end]
# Start - first element we want to include
# End - The end index is not inclusive. So you have to add 1 to extract the end index
# ex if end is 5 that means you have to add 1 to 5 which gives you 6 for extraction
# print(names[1:4])

# Slicing Lists I - Negative Index
# print(names[-5:-2])

# Slicing Lists II
# print(names[0:3])
# print(names[:3])
# print(names[2:])

# Counting in a List
# num = [3, 5, 6, 7, 3, 7, 8, 7, 9, 10, 7]
# num_of_7 = num.count(7)
# print(num_of_7)

# Sorting Lists I
# names.sort()
# names.sort(reverse=True)
# print(names)

# Sorting Lists II
# names_sorted = sorted(names)
# print(names_sorted)
# print(names)