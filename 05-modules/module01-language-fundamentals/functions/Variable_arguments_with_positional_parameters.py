def sum(a,b,*x):
    s=a+b
    for i in x: s+=i
    print(s)

sum(2,3)
sum(2,3,5,3,5,3)
#sum()

#def sum(a,b,*x):
#   s=a+b
#    for i in x: s+=i
#    print(s)..we cannot provide positional parameters after varaiable arguments
    
