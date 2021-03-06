glossary = {
    'if': "A conditional check, used to check if a condition is True or False.",
    'del': "A statement that deletes an item from a list or dictionary.",
    'for': "A loop that runs through all items of a list, tuple or dictionary",
    'def': "Keyword to define a function.",
    'else': "Used with the if-statement to run code of not the if check is True.",
    'elif': "Used after an if statement to run another conditional check before the else-block.",
    'in': "Defines the set that the for loop should iterate over."
}

for word, meaning in glossary.items():
    print("{}: {}".format(word,meaning))