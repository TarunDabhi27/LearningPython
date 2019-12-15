
#

def f(a,b,c=2,d=3):
    print(a,b,c,d)
#f(1,2,m=9)

def f(a,b,**x):
    print(a,b)
    for k,v in x.items():
        print("The value of {} is {}".format(k,v))
f(1,2,c=2,d=3)
f(1,c=2,b=5,d=3)