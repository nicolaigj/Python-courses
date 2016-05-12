number = int(input("Please enter an integer and I'll tell you if it's a multiple of 10: "))

if number % 10 == 0:
    print("Hooray! {} is a multiple of 10.".format(number))
else: 
    print("Please try again, {} is not a multiple of 10.".format(number))