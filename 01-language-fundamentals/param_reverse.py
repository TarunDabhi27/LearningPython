'''
Created on Dec 7, 2019

@author: tarun.dabhi
'''

def print_emp_details(name, age, salary):
    print("Name = {}, Age = {}, Salary = {}".format(name, age, salary))

def main():
    print_emp_details(salary=50000, age=25, name="Tarun")

if __name__ == '__main__':
    main()