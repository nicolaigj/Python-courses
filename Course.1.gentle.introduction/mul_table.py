def process_input(raw_input):
    try:
        processed_input = int(raw_input)
    except ValueError:
        raise ValueError("The input is not an integer")
    if(processed_input <= 0):
        raise ValueError("All dimensions must be greater than zero")
    return processed_input

def create_multiplication_table(width, heigth):
    output = ""
    num_chars = len(str(width*heigth)) + 1
    for a in range(1,heigth+1):
        for b in range(1,width+1):
            product = a*b
            product_str = str(product)
            product_str = product_str.rjust(num_chars, ' ')
            output += product_str
        output += '\n\n'
    return output

def get_user_input():
    values = []
    for prompt in ('Width', 'Height'):
        raw_input = input(prompt + ': ')
        prossesed_input = process_input(raw_input)
        values.append(prossesed_input)
    return values
        

def main():
    success = False
    try:
        width, height = get_user_input()
        success = True
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("\nGoodbye!")
    if(success):
        output = create_multiplication_table(width, height)
        print('\n\n' + output + '\n\n')
    
    
if __name__ == '__main__':
    main()