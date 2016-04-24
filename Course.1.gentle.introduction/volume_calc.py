def process_input(raw_input):
    try:
        value = float(raw_input)
    except ValueError:
        raise ValueError ("%s is not a number" % raw_input)
    if value <= 0:
        raise ValueError("All dimensions must be greater than zero")
    return value

def get_dimensions_from_user(*names):
    output_values = []
    for name in names:
        raw_input = input(name + ": ")
        prosessed_input = process_input(raw_input)
        output_values.append(prosessed_input)
    return output_values

def main():
    print("This program will calculate the volume of a rectangular box given its length, \
    width and height.\n")
    try:
        length, width, height = get_dimensions_from_user('Length', 'Width', 'Height')
        volume = length * width * height
        print("The volume of the box is %.2f." % volume)
    except ValueError as e:
        print(e)
    except KeyboardInterrupt:
        print("\nGoodbye.")

if __name__ == "__main__":
    main()