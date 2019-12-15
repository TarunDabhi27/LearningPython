word = input("Enter a word:")
if word.isalnum():
    print("Alphanumeric")
    if word.isalpha():
        print("Alphabetic")
        if word.isupper(): print("Uppercase")
        elif word.islower(): print("Lowercase")
        elif word.istitle(): print("Titlecase")
    elif word.isnumeric(): print("Numeric")
elif word.isspace(): print("Whitespace")