import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
load_dotenv()

def connect():
    # Establishes a connection to the database.
    try:
        connection = mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        port = int(os.getenv("DB_PORT")),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_NAME"),
        )
        print("Connection established!")  # For debugging purposes only
        return connection

    except Error as err:
        print(f"Something went wrong.[Error at server.py]: {err}")

    return None  # Explicitly return None if the connection fails


def seed():
    # Check if the database exists. If not, seed it with a schema.
    try:
        connection = connect() # using the first function to connect to the database
        cursor = connection.cursor()
        # Check if the database exists
        database_name = os.getenv("DB_NAME")
        cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
        result = cursor.fetchone()

        if result:
            print(f"Database '{database_name}' already exists.")
        else:
            print(f"Database '{database_name}' does not exist. Trying to create and seed the database...")
            # Create the database
            cursor.execute(f"CREATE DATABASE {database_name}")
            connection.database = database_name  # Switch to the new database

            # Seed the database with the schema
            schema_path = "moneymaster.sql"  # Update this path if necessary
            with open(schema_path, "r") as schema_file:
                schema_sql = schema_file.read()
                for statement in schema_sql.split(";"):  # Split on ';' for individual statements
                    if statement.strip():  # Skip empty statements
                        cursor.execute(statement)

            print(f"Database '{database_name}' has been created and seeded successfully.")

        cursor.close()
        connection.close()

    except Error as err:
        print(f"Something went wrong: {err}")

