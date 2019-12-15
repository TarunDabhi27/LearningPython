filename=input("Enter filename:")

try :
    file=open(filename)
    for line in file: print(line,end='')
except Exception as e:
    print("Unable to open file: {}".format(filename))
    print("Reason : {}".format(str(e)))
