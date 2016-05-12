while True:
    pizza_topping = input("What pizza topping would you like? ")
    
    if pizza_topping.lower() == 'quit':
        break
    else:
        print("Cool, I'll add {} to your pizza".format(pizza_topping))