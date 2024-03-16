#!/usr/bin/python3
"""
 script that takes in arguments and displays all values
 in the states table of hbtn_0e_0_usa where name matches
 the argument. But this time, write one that is safe from MySQL injections!
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        database = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
        )
        cursor = database.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))
        states = cursor.fetchall()
        for state in states:
            print(state)
        cursor.close()
        database.close()
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
