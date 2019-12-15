import  sqlite3
if __name__ == '__main__':
    connection = sqlite3.connect("test_db.db")
    query = "select * from employee"
    cursor = connection.cursor()
    cursor.execute(query)

    while True:
        records = cursor.fetchmany(2)
        if len(records) == 0: break
        for record in records:
            print(record)