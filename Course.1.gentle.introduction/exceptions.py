def get_user_input():
    x = input("Enter a number: ")
    x = int(x)
    return x 

def answer_multiple_excepts():
    try:
        x = get_user_input()
        print(x)
    except Exception:
        print("ValueError")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    
    
    
answer_multiple_excepts()