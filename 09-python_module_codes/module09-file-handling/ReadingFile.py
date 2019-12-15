if __name__ == '__main__':
    file = open("./data-file.txt")
    # Similar to cat command
    # print(file.read())

    for line in file.read():
        print(line)
