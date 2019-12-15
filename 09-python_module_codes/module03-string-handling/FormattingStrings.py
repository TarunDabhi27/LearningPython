if __name__ == '__main__':
    name = "Naveen"
    company_name = "Cisco"
    print("My name is {}, and I work for {}".format(name,company_name))
    print("The {2} {1} {0}".format("fox","brown","quick"))

    # Assigning keywords
    print("The {q} {b} {f}".format(f="fox",b="brown",q="quick"))

    # String Interpolation
    print(f"My name is {name} and I work for {company_name}")