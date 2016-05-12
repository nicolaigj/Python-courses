age = int(input("What is you age and I'll tell you the ticket price: "))

if age < 3:
    print("Your ticket is free! Enjoy")
elif age < 12:
    print("Your ticket costs 10$")
else:
    print("Your ticket costs 15$")