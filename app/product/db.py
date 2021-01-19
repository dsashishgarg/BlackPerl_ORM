import sqlite3
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY, product_name text, product_price real)"
cursor.execute(create_table)

connection.commit()

connection.close()
