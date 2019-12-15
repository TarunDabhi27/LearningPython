'''
Created on Dec 7, 2019

@author: tarun.dabhi
'''



def main():
    
    metrix = [["C", "C++"], ["Java", "Scala"]]
    for row in metrix:
        result = ""
        for el in row:
            result = result + "-" + el
        print(result)
    
    
if __name__ == '__main__':
    main()
    