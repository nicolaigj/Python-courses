# List of my favorite pizzas
pizzas = ['quattro stagione', 'quattro formaggi', 'salame piccante', 'margherita']
# A statement of how I like the pizzas
pizza_message = "Oh my, I think {} is my favorite pizza"
for pizza in pizzas:
    print(pizza_message.format(pizza.title()))
# End message about how I love pizzas
print("I really like pizza!")
