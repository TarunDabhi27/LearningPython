from math import  factorial

try :
    file=open("D:/Mariott/EPIC_EXECUTION/Latest_Insert/factorial.txt","w")
    for i in range(1,11):
        file.write("The factorial of {} is {}\n".format(i,factorial(i)))
except Exception as e:
    print("Unable to open file: {}".format(file))
    print("Reason : {}".format(str(e)))
else:
    print("Factorials successfully written to factorial.txt")

