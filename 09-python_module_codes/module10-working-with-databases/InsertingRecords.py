import  sqlite3
if __name__ == '__main__':
    connection = sqlite3.connect("test_db.db")
    cursor = connection.cursor()
    query_one = "insert into employee values('Naveen',1,'info@npntraining.com')"
    cursor.execute(query_one)

    query_two = """insert into employee values (? , ?, ?)"""
    cursor.execute(query_two,('Praveen',2,'praveen@company.com'))

    connection.commit()
    connection.close()