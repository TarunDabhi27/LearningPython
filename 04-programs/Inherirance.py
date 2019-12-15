'''
Created on Dec 8, 2019

@author: tarun.dabhi
'''

class A:
    
    def __init__(self):
        print("Constructor A Invoked")
        
    def print_me(self):
        print("Print Me has been called from class A")
        
class B(A):
    
    def __init__(self):
        A.__init__(self)
        print("Constructor B Invoked")
        
    def call_me(self):
        print("Call Me has been called from class B")


if __name__ == '__main__':
    obj = B()
    obj.call_me()
    obj.print_me()