x=2
def f():
    global x
    x=3
    print(x)

print(x)

f()

print(x)