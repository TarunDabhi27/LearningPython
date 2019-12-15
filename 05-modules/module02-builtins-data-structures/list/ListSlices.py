if __name__ == '__main__':
    number_list = [10, 2, 3, 4, 5, 10, 10, 10]
    sliced_list = number_list[1:3]
    print(sliced_list)

    number_list[0:3] = [100,22,33]
    print(number_list)