#Carolina Rodriguez
#CSD-310
#Module 7 Assignment

import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read database credentials from environment variables
db_user = os.getenv("USER")
db_password = os.getenv("PASSWORD")
db_host = os.getenv("HOST")
db_database = os.getenv("DATABASE")

# Database configuration
config = {
    "user": db_user,
    "password": db_password,
    "host": db_host,
    "database": db_database,
    "raise_on_warnings": True
}

try:
    # Connect to MySQL
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\nDatabase user {} connected to MySQL on host {} with database {}\n".format(
        db_user, db_host, db_database
    ))
    input("\nPress any key to continue...")

    # All studios
    print("=== Studio Table ===")
    cursor.execute("SELECT * FROM studio")
    for studio in cursor.fetchall():
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

     #All genres
    print("=== Genre Table ===")
    cursor.execute("SELECT * FROM genre")
    for genre in cursor.fetchall():
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

    #Movies under 2 hours
    print("=== Films Under 2 Hours ===")
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    for film_name in cursor.fetchall():
        print("Film Name: {}\nRuntime: {} minutes\n".format(film_name[0], film_name[1]))

    #Films grouped by film_director
    print("=== Films By Director ===")
    cursor.execute("SELECT film_director, film_name FROM film ORDER BY film_director")
    film = cursor.fetchall()

    current_director = None
    for film_director, film_name in film:
        if film_director != current_director:
            print("\nDirector:", film_director)
            current_director = film_director
        print("   Film:", film_name)

  

except mysql.connector.Error as err:
    # Handle database errors
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")
    else:
        print(err)

finally:
    # Close connection
        db.close()
        print("\nConnection closed.")
