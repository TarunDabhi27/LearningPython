if __name__ == '__main__':
    number_list = [10,2,3,4,5,10,10,10]

    print(2 in number_list)

    # Couting occurence
    print(number_list.count(10))

    # Locating elements
    print(number_list.index(10))

    print(number_list.index(2,1,len(number_list)-1))