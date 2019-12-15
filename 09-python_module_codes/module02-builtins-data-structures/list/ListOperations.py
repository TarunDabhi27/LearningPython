if __name__ == '__main__':
    number_list = [1, 2, 3, 4, 5]
    minimum_value = min(number_list)
    maximum_value = max(number_list)

    print("Minimum value: ",minimum_value)
    print("Maximum value: ",maximum_value)
    number_list.reverse()
    print("Reversed list: ",number_list)

    number_list.sort()
    print("Sorted list: ",number_list)
