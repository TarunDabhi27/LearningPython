'''
Created on Dec 8, 2019

@author: tarun.dabhi
'''
def main():
    emp_list = [
            {"1":{"p_detail":["Naveen"], "skills": ["C", "C++", "Python"]}},
            {"2":{"p_detail":["Tarun"], "skills": ["C", "Python"]}},
            {"3":{"p_detail":["Rohit"], "skills": ["C", "Scala"]}},
            {"4":{"p_detail":["Ravi"], "skills": ["C++", "Python"]}},
            {"5":{"p_detail":["Sanjay"], "skills": ["C", "C++"]}},
        ]

    id = input("Enter id")
    for emp in emp_list:
        emp_detail = emp.get(id)
        if emp_detail == None:
            continue
        else:
            skills = emp_detail.get("skills")
            if skills.count("Python") >= 1:
                print(emp_detail.get("p_detail")[0])
            else:
                print("No Python skill")

if __name__ == '__main__':
    main()