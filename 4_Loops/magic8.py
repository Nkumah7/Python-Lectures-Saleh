import random

choice = random.randint(1, 10)
name = input("Name: ")

if name:     
    question = input(f"{name} asks: ")
else:
    question = input("Question: ")

if choice == 1:
    print("Yes - definitely")
elif choice == 2:
    print("It is deecidedly so")
elif choice == 3:
    print("Without a doubt")
elif choice == 4:
    print("Reply hazy, try again.")
elif choice == 5:
    print("Ask again later")
elif choice == 6:
    print("Better not tell you now")
elif choice == 7:
    print("My sources say no")
elif choice == 8:
    print("Outlook not so good")
else:
    print("Very doubtful")
    
