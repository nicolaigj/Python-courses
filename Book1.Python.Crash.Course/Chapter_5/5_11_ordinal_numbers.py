ordinal_numbers = [i for i in range(1,10)]
for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print("{}st".format(ordinal_number))
    elif ordinal_number == 2:
        print("{}nd".format(ordinal_number))
    elif ordinal_number == 3:
        print("{}rd".format(ordinal_number))
    else:
        print("{}th".format(ordinal_number))