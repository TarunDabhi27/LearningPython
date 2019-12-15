if __name__ == '__main__':
    set_one = {1,2}
    set_two = {3,4}
    print(set_one.union(set_two))

    # Set Intersection
    set_one.intersection(set_two)
    print(set_one)

    set_one & set_two
    print(set_one)

    # Set Difference
    set_one = {1, 2}
    set_two = {2, 4}
    result_set = set_one.difference(set_two)
    print(result_set)

    set_one = {1, 2}
    set_two = {2, 4}
    result_set = set_one - set_two
    print(result_set)