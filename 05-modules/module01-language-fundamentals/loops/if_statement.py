name = input("Enter your name")
age= int(input("Enter your age: "))
if age >= 18 : print("Hi {}! You can vote!".format(name))
if age <18 : print("Sorry {}! You can't vote !".format(name))