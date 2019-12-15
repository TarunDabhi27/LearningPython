class A:
    def __init__(self):
        print("Constructor Invoked")

    def print_me(self):
        print("You called print_me() method")

class B(A):
    def __init__(self):
        A.__init__(self)
		print("B Constructor")

    def call_me(self):
        print("You called call_me")

if __name__ == '__main__':
    obj = B()
    obj.call_me()