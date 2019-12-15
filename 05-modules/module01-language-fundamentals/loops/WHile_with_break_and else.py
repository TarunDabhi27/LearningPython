n = int(input("ENter a positive integer"))
i = 2
while i <= n/2:
    if n%i == 0:
        isPrime = False
        break
    i=i+1
else:
    isPrime=True

if isPrime: print("Prime")
else: print("Composite")