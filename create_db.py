"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
from datetime import datetime
import os
import inspect
import sqlite3
from faker import Faker

def main():
    global db_path
    db_path = os.path.join(get_script_dir(), 'social_network.db')
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body
conn = sqlite3.connect('social_network.db')

c = conn.cursor()
#creating a table
people_table_query = """"
    CREATE TABLE IF NOT EXISTS people
            (id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
            city TEXT NOT NULL
            provice TEXT NOT NULL
            bio TEXT NOT NULL
            age INTEGER,
            email TEXT NOT NULL ,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL);
            """
            
#executing the code 
c.execute(people_table_query)

#commiting the code 
conn.commit()

#closing the connection 
conn.close()


def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
fake = Faker()
for i in range(200):
    name = fake.name()
    address = fake.street_address()
    city = fake.city()
    province = fake.administrative_unit()
    bio = fake.text(max_nb_chars=200)
    age = fake.random_int(min=1, max=100)
    email = fake.email()
    created_at = datetime.now()
    updated_at = datetime.now()

    # insert the fake person into the people table
c.execute("INSERT INTO people (name, bio , age, email, address, province, city, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)", (name, bio , age, email, created_at, updated_at, city, province))
conn.commit()
conn.close()
    

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
   main()