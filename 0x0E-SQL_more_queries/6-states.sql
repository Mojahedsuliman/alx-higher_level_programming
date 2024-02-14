-- This script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

echo "CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;"
USE hbtn_0d_usa;
echo "CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);"
