if __name__ == '__main__':
    dictionary_elements = {"apple":"red","grapes":"green"}
    print(dictionary_elements["apple"])
    print(dictionary_elements.get("apple"))

    # Adding elemnts
    dictionary_elements["grapes"] = "purple"
    dictionary_elements["mango"] = "yellow"

    # Accessing Dictionaries
    for key in dictionary_elements:
        print(dictionary_elements[key])

    # Iterating throgh the key,value pairs of a dictionary
    for (k,v) in dictionary_elements.items():
        print("Key= ",k," Value= ",v)


    del(dictionary_elements["mango"])
    print("----Deleting elements----")
    for key in dictionary_elements:
        print(dictionary_elements[key])

    print(dictionary_elements.popitem())
    for key in dictionary_elements:
        print(dictionary_elements[key])