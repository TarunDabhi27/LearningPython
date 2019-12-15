def sum(a,b=100,*x):
    s=a+b
    for i in x: s+=i
    print(s)

sum(5)
sum(5,8)
sum(5,8,12)