def get_result(name, mark):
    result = None
    if mark > 75:
        result = "{} has got Dist. with {} marks.".format(name, mark)
    elif mark > 35:
        result = "{} is passed with {} marks.".format(name, mark)
    else :
        result = "{} is failed with {} marks.".format(name, mark)
    
    return result
 
 
def main():
    name = input("Enter student name : ")
    mark = int(input("Enter students mark : "))
    
    result = get_result(name, mark)
    print(result)
           
if __name__ == '__main__':
    main()
    