import sqlite3


if __name__ == '__main__':
    connection = sqlite3.connect("test_db")
    print("DB connection successful")
    
    cursor = connection.cursor()
#     query = "create table employee(name Text, id INT )"
#     query = "insert into employee values('Tarun',27)"
#     query = "insert into employee values('Rohit',23)"
#     query = "insert into employee values('Navin',21)"

    query = "select id, name from employee"

    cursor.execute(query)
#     records = cursor.fetchone()
    records = cursor.fetchall()
    print(records)
    
    connection.commit()
    connection.close()