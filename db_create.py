# db_create.py

import sqlite3
from config import DATABASE_PATH

# Get the connection
with sqlite3.connect(DATABASE_PATH) as connection:
	# Retrieve the cursor object
	c = connection.cursor()

	# Create the table
	c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
		   name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL,
		   status INTEGER NOT NULL)""")

	# Dummy data
	c.execute('INSERT INTO tasks (name, due_date, priority, status)'\
		   'VALUES("Finish this tutorial", "04/01/15", 10, 1)')

	c.execute('INSERT INTO tasks (name, due_date, priority, status)'\
		   'VALUES("Succeed in life", "08/01/15", 1, 1)')

