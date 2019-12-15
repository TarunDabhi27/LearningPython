filename=input("Enter filename:")

try :
    file=open(filename)
    contents=list(file.read())
    for line in contents: print(line,end='')
except Exception as e:
    print("Unable to open file: {}".format(filename))
    print("Reason : {}".format(str(e)))