

def decorator_function(any_function):
    def wrapper_function(arg1,arg2):
        if arg2 == 0:
            print("Cannot divide number by zero")
            return 0
        else:
            any_function(arg1,arg2)
    return wrapper_function

# @decorator_function
def divide(num1,num2):
    print(num1/num2)


if __name__ == '__main__':
    # fn = decorator_function(divide)
    # result = fn(2,2)
    # print(result)
   divide(2,2)

