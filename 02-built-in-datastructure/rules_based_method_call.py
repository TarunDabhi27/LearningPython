'''
Created on Dec 7, 2019

@author: tarun.dabhi
'''

def get_method(rule_id):
    
    my_rule_dictonaty = {"r1": m1,"r2": m2, "r3": m3}
    return my_rule_dictonaty[rule_id]
    
def main():
    
    entered_rule = input("Please enter the rule r1, r2 or r3 : ")
    fn = get_method(entered_rule)
    fn()

def m1():
    print("This is the method for rule 1 ")


def m2():
    print("This is the method for rule 2 ")
    

def m3():
    print("This is the method for rule 3 ")
    
if __name__ == '__main__':
    main()