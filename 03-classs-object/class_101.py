'''
Created on Dec 7, 2019

@author: tarun.dabhi
'''


class Employee:
    company_name = "CISCO"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor")
      
    def show_details(self):
        print("name "+ self.name)
        print("age "+ self.age)  
        
        
    def get_name(self):
        return self.name
        
    def __del__(self):
        print("Deleted")
        
    @staticmethod
    def get_company_name():
        return Employee.company_name
        
        
if __name__ == '__main__':
    obj = Employee("Tarun", "22")
    obj.show_details()
    print(Employee.get_company_name())
    print(obj.get_name())
    del(obj)