class A:
    def __init__(self):
        print("Constructor")

    def __del__(self):
        print("Destructor")

if __name__ == '__main__':
    obj = A()
    del(obj)