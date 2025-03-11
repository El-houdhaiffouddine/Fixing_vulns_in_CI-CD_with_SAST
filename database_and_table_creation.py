# Please run this Python file to create the Flask database and users table before running the Flask app

from database import create_database, create_users_table

#Creation of the database
create_database()

#Creation of the users table
create_users_table()