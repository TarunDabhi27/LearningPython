

def decorator_function(any_func):
    def wrapper_function():
        print("################")
        any_func()
    return wrapper_function

@decorator_function
def func1():
    print("This is function 01")

@decorator_function
def func2():
    print("This is function 022")


if __name__ == '__main__':
    #fn = decorator_function(func1)
    #fn()
    func1()
    func2()

