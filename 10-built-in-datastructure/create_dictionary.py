'''
Created on Dec 7, 2019

@author: tarun.dabhi
'''

my_dict ={}

def add_el_to_dict():
    
    key = input("Enter key : ")
    value = input("Enter Value : ")

    if(my_dict.get(key) == None):
        my_dict[key] = [value]
    else :
        values = my_dict.get(key)
        values.append(value)
        
    coninue = input("Press Y for Continue, N for exit : ")
    
    if coninue == "Y":
        add_el_to_dict()
    else :
        return

def main():
    
    add_el_to_dict()
    print(my_dict)

if __name__ == '__main__':
    main()