def convert():
    num = input("Give me a number: ")
    try:
        num_float = float(num)
        if num_float.is_integer():
            num_int = int(num_float)
            print("This number is an integer.")
        else:
            print("This number is a decimal.")
    except ValueError:
        print()
convert()