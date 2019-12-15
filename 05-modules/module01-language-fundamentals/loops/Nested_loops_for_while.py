lim = int(input("ENter the limit"))
for n in range(2,lim+1):
    i=2
    while i<= n/2:
        if n%i == 0:
            break
        i=i+1
    else:
        print(n)