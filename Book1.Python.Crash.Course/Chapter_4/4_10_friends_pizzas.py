# List of my favorite pizzas
pizzas = ['quattro stagione', 'quattro formaggi', 'salame piccante', 'margherita']
# A statement of how I like the pizzas
pizza_message = "Oh my, I think {} is my favorite pizza"
for pizza in pizzas:
    print(pizza_message.format(pizza.title()))
# End message about how I love pizzas
print("I really like pizza!")

# Creating a list for my friends pizzas
friends_pizzas = pizzas[:]

pizzas.append('napolitana')
friends_pizzas.append('pan pizza')
print(friends_pizzas)
print(pizzas)
