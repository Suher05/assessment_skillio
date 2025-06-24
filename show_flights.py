import psycopg2
from tabulate import tabulate
from config import get_db_config

def insert_flight(flight_number, departure_time, arrival_time, departure_airport, destination_airport, airline):
    try:
        config = get_db_config()
        connection = psycopg2.connect(**config)
        cursor = connection.cursor()

        # Check if the flight already exists

        cursor.execute("SELECT * FROM flights WHERE flight_number = %s;", (flight_number,))
        existing = cursor.fetchone()

        if existing:
            print(f"Flight {flight_number} already exists. Skipping insert.")
        else:
            query = """
                INSERT INTO flights (flight_number, departure_time, arrival_time, departure_airport, destination_airport, airline)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (flight_number, departure_time, arrival_time, departure_airport, destination_airport, airline))
            connection.commit()
            print(f"Flight {flight_number} inserted successfully.")

    except Exception as e:
        print("Error inserting flight:", e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def show_flights():
    try:
        config = get_db_config()
        connection = psycopg2.connect(**config)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM flights ORDER BY departure_time;")
        rows = cursor.fetchall()

        headers = ["ID", "Flight", "Departure", "Arrival", "From", "To", "Airline"]
        print("\nAll flights (sorted by departure time):\n")
        print(tabulate(rows, headers=headers, tablefmt="grid"))

    except Exception as e:
        print("Error fetching flights:", e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
