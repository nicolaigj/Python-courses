cubes = [value**3 for value in range(1,11)]
for cube in cubes:
    print(cube)

# Print the first three elements
print("The first three elements are:")
for cube in cubes[:3]:
    print(cube)

# Print the three middle items
print("The three middle items are:")
for cube in cubes[int((len(cubes)/2-1)):int((len(cubes)/2+2))]:
    print(cube)
# Print the last items
print("The three last items are:")
for cube in cubes[-3:]:
    print(cube)