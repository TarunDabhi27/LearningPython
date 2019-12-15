import  sqlite3
if __name__ == '__main__':
    connection = sqlite3.connect("test_db.db")

    cursor = connection.cursor()
    cursor.execute("create table employee(name Text, id Integer, email Text)")
    connection.commit()
    connection.close()