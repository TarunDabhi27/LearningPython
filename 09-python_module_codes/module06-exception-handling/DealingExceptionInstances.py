if __name__ == '__main__':
    try:
        result = 1/0
    except ZeroDivisionError as ex:
        print("Details: ",ex)
