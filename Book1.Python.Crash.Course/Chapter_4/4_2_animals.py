# A list of animals
animals = ['cat', 'dog', 'lion', 'sea urchin', 'kakadoo']
# My opinion about the animal aptness to be a pet
message = "I think {} would make a good pet."
# Loop to print all animals
for animal in animals:
    print(message.format(animal.title()))
    
print("Any of these animals would make a good pet!")