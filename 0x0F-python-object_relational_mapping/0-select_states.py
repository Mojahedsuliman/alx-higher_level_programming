#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        try:
            database = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database,
            )
            cursor = database.cursor()
            cursor.execute("SELECT * FROM states ORDER BY id ASC")
            states = cursor.fetchall()
            for state in states:
                print(state)
            cursor.close()
            database.close()
        except MySQLdb.Error as e:
            print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
            sys.exit(1)
