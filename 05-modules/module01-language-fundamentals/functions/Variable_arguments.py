#The special * prefix is used to denote that we are dealing with a variable arguments

def sum(*x):
    s=0
    for i in x: s+=i
    print(s)

sum(2,3)
sum(2,3,5,3,5,3)
sum()