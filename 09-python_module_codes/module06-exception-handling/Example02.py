if __name__ == '__main__':
    try:
        numerator = int(input("Enter numerator"))
        denominator = int(input("Enter denominator"))
        result = numerator/denominator
        print("Result= ",result)
    except (ZeroDivisionError, ValueError):
        print("Oops! unable to calculate")