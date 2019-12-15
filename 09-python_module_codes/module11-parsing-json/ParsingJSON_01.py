import json
if __name__ == '__main__':
    employee_json_str = '{"id":1,"name":"Naveen","technical_skills":["Java","Python"]}'
    employee_json = json.loads(employee_json_str)
    print(employee_json["technical_skills"][0])
    print(employee_json["name"])