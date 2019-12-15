import  sqlite3
if __name__ == '__main__':
    connection = sqlite3.connect("test_db.db")
    query = "select * from employee"
    cursor = connection.cursor()
    cursor.execute(query)

    for record in cursor.fetchall():
        print(record)