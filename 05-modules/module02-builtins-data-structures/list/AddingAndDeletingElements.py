if __name__ == '__main__':
    list_one = [1,2,3,4]
    list_two = [6,7]
    # Appending elements
    list_one.append(5)
    print(list_one)
    list_one.extend(list_two)
    print(list_one)

    # Deleting Elements
    list_three = [1,2,3,4]
    del(list_three[0])
    del (list_three[0:1])
    print(list_three)

    # remove : Used to delete specific element
    list_three.remove(3)
    print(list_three)

    # Using pop() to Delete elements
    list_four = [1, 3, 5, 7]
    print(list_four.pop(1))

    # Delete last element
    print(list_four.pop())

    # Clearing all elements
    print(list_four.clear()) # Similar to del L[:]
