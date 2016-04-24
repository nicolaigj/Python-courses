def get_user_input():
    try:
        x = input("Enter a number: ")
        x = int(x)
        return x
    except ValueError:
        raise Exception("%s is not a number" % x)
    except KeyboardInterrupt:
        print("\nGoodbye")
        raise

def answer_multiple_excepts():
    try:
        x = get_user_input()
        print(x)
    except Exception:
        print("ValueError")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    
def exception_objects():
    try:
        x = get_user_input()
        print(x)
    except Exception as e:
        print(e)
    except KeyboardInterrupt as k:
        print(k)
    print("Exiting exception")
    
exception_objects()