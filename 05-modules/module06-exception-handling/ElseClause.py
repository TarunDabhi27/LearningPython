if __name__ == '__main__':
    try:
        numerator = int(input("Enter numerator"))
        denominator = int(input("Enter denominator"))
        result = numerator/denominator
    except:
        print("Oops! unable to calculate")
    else:
        print("{}/{}={}".format(numerator,denominator,int(result)))
