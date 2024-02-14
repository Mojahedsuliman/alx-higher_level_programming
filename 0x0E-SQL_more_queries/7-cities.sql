-- This part of script will create the database hbtn_0d_usa if not exists
echo "CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;"

-- This part of script will create the table cities if not exists
echo "CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);"
