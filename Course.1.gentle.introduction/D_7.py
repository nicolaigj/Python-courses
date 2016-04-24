def get_user_input():
    x = input("Enter a numer: ")
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

try_finally()