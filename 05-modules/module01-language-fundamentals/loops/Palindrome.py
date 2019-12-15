n= int(input("Enter an integer"))
num=n
reverse=0
while n>0:
    digit = n%10
    reverse = reverse * 10 + digit
    n //= 10

if num==reverse: print("The number is a palindrome")
else: print("The number is not a palindrome")