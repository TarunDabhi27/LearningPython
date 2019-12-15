'''
Created on Dec 7, 2019

@author: tarun.dabhi
'''

axis_data = {"x_axis": [1,2,3,14,15,6], "y_axis": [10,50,30,20,10]}

def get_max(key):
    return max(axis_data.get(key, [0]))

def main():
    
    key = input("Enter Key : ")
    max_val = get_max(key)
    print("Max value of {} is {}".format(key, max_val))
    
    
if __name__ == '__main__':
    main()