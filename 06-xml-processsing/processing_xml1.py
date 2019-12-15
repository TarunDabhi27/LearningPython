from xml.dom import minidom

if __name__ == '__main__':
    
    document = minidom.parse("input.xml")
    staffs = document.getElementsByTagName("staff")
    
    for staff in staffs:
        sid = staff.getAttribute("id")
        nickname = staff.getElementsByTagName("nickname")[0].firstChild.data
        salary = staff.getElementsByTagName("salary")[0].firstChild.data
        print("Staff Name : {}".format(sid))
        print("NickName : {}".format(nickname))
        print("Salary : {}".format(salary))
        print()