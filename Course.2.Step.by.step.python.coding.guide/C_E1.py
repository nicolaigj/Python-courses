raw_input = int(input("How far would you like to travel in miles? "))
miles = int(raw_input)
if miles < 3:
    method_of_transport = 'walk'
elif miles < 100:
    method_of_transport = 'drive'
else:
    method_of_transport = 'fly'

print("I would suggest you {} to your destination".format(method_of_transport))