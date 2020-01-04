

x=5

def print_local():
    x=10
    print("Local x : ", x)
    # globals() is a function used to access global variable 
    # Syntex is globals()["<<variable_name>>"] for ex below code
    print("Global x : ", globals()["x"])



print_local()