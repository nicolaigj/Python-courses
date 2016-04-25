# List of places I want to visit
places = ['london', 'bologna', 'new york', 'perth', 'budapest', 'san fransisco']
# Print unsorted
print(places)
# Print sorted
print(sorted(places))
# Print unsorted to show that the list is not changed
print(places)
# Print the list sorted and in reverse 
print(sorted(places, reverse=True))
# Print unsorted to show that the list is not changed
print(places)
# Reverce the list
places.reverse()
# Print reversed list
print(places)
# Reverse the list again
places.reverse()
# Print reversed list, now in the original state
print(places)
# Sort the list and print it 
places.sort()
print(places)
# Sort the list, reverse it and print it 
places.sort(reverse=True)
print(places)
# Intentional IndexError
print(places[6])
