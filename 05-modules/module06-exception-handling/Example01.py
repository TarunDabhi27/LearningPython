if __name__ == '__main__':
    try:
        numerator = int(input("Enter numerator"))
        denominator = int(input("Enter denominator"))
        result = numerator/denominator
        print("Result= ",result)
    except ZeroDivisionError:
        print("Number cannot be divisible by '0'")
    except ValueError:
        print("Please enter number")

    print("Other statements executing")