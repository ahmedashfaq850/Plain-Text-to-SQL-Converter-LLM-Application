import sqlite3

## Create a connection to the database
connection = sqlite3.connect('employees.db')

## Create a cursor object
cursor = connection.cursor()

## Create a table
table_info = """
CREATE TABLE employees (
    NAME VARCHAR(50),
    AGE INT,
    POSITION VARCHAR(50),
    SALARY INT
);
"""

## Execute the query
cursor.execute(table_info)

## Insert Some Records
cursor.execute("INSERT INTO employees VALUES ('Bilal Siddique', 28, 'Cloud Engineer', 500000)")
cursor.execute("INSERT INTO employees VALUES ('Zuhad Zahid', 32, 'WordPress Developer', 5000)")
cursor.execute("INSERT INTO employees VALUES ('Muhammad Hasan', 26, 'Ceo', 5000000)")
cursor.execute("INSERT INTO employees VALUES ('Ahmed Ashfaq', 28, 'Software Engineer', 700000)")

## Display
data = cursor.execute("SELECT * FROM employees")

for record in data:
    print(record)
    
    
connection.commit()
connection.close()