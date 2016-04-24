def get_user_input():
    x = input("Enter a number: ")
    x = int(x)
    return x 

def try_exept():
    try:
        x = get_user_input()
        print(x)
    except:
        print("Err")
    print("Exiting try_exept")

def try_exept_finally():
    try:
        x = get_user_input()
        print(x)
    except:
        print("Err")
    finally:
        print("Finally")
    print("Exiting try_exept_finally")

def try_finally():
    try:
        x = get_user_input()
        print(x)
    finally:
        print("Finally")
    print("Exiting try_finally")

def multiple_excepts():
    try:
        x = get_user_input()
        print(x)
    except Except:
        print("Tits")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    
    
multiple_excepts()