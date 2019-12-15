'''
Created on Dec 7, 2019

@author: tarun.dabhi
'''
class BestClubMembers:
    
    member_count = 0
    
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        BestClubMembers.member_count += 1
    
    def __str__(self):
        return "First Name : {}".format(self.f_name)
        
    @staticmethod
    def get_count():
        return BestClubMembers.member_count

if __name__ == '__main__':
    
    
    while True:
        f_name = input("Enter first name")
        l_name = input("Enter last name")
        
        if BestClubMembers.get_count() == 5:
            print("Not allowed")
            exit()
        else:
            obj = BestClubMembers(f_name, l_name)
            print(obj)
        