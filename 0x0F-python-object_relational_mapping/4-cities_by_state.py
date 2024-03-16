#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
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
        cursor.execute("SELECT cities.id, cities.name, states.name FROM cities")
        cities = cursor.fetchall()
        for city in cities:
            print(city)
        cursor.close()
        database.close()
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
