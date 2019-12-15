class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def set_name(self,name):
        self.name= name

    def get_name(self):
        return self.name

    def printDetails(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

if __name__ == '__main__':
    per_obj = Person("Naveen",30)
    per_obj.printDetails()
    name= per_obj.get_name()
    print(name)