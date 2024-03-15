#!/usr/bin/python3
"""
Script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    if len(sys.argv) == 4:
        try:
            db = MySQLdb.connect(host="localhost", 
                port=3306,
                user=username, 
                passwd=password, 
                db=database)
            cursor = db.cursor()

            query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
            cursor.execute(query, (state_name,))

            states = cursor.fetchall()
            for state in states:
                print(state)

            cursor.close()
            db.close()

        except MySQLdb.Error as e:
            print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
            sys.exit(1)
