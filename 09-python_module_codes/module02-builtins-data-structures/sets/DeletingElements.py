if __name__ == '__main__':
    set_one = set([1, 2, 3, 4])

    # It will produce a KeyError if element not found
    # set_one.remove(44)
    # print(set_one)

    set_one.discard(44)
    print(set_one)