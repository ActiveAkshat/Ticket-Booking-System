import tkinter as tk
from flights_dao import get_all_flights, get_flights_date
from sql_connection import get_sql_connection


def display_flights():
    connection = get_sql_connection()
    all_flights = get_all_flights(connection)
    connection.close()

    flights_window = tk.Tk()
    flights_window.title("List of Flights")

    # Create labels for headers
    label_flight_id = tk.Label(flights_window, text="Flight ID")
    label_flight_id.grid(row=0, column=0)
    label_flight_name = tk.Label(flights_window, text="Flight Name")
    label_flight_name.grid(row=0, column=1)
    label_source = tk.Label(flights_window, text="Source")
    label_source.grid(row=0, column=2)
    label_destination = tk.Label(flights_window, text="Destination")
    label_destination.grid(row=0, column=3)
    label_departure_time = tk.Label(flights_window, text="Departure Time")
    label_departure_time.grid(row=0, column=4)
    label_arrival_time = tk.Label(flights_window, text="Arrival Time")
    label_arrival_time.grid(row=0, column=5)
    label_fare = tk.Label(flights_window, text="Fare")
    label_fare.grid(row=0, column=6)

    row_counter = 1  # Keep track of row for data placement

    # Display flight data using labels
    for flight in all_flights:
        label_id = tk.Label(flights_window, text=flight['flight_id'])
        label_id.grid(row=row_counter, column=0)
        label_name = tk.Label(flights_window, text=flight['flight_name'])
        label_name.grid(row=row_counter, column=1)
        label_source_city = tk.Label(flights_window, text=flight['source'])
        label_source_city.grid(row=row_counter, column=2)
        label_destination_city = tk.Label(flights_window, text=flight['destination'])
        label_destination_city.grid(row=row_counter, column=3)
        label_departure_time = tk.Label(flights_window, text=flight['departure_time'])  # Assuming 'departure_time' exists in the flight dictionary
        label_departure_time.grid(row=row_counter, column=4)
        label_arrival_time = tk.Label(flights_window, text=flight['arrival_time'])  # Assuming 'arrival_time' exists in the flight dictionary
        label_arrival_time.grid(row=row_counter, column=5)
        label_fare = tk.Label(flights_window, text=flight['fare'])  # Assuming 'fare' exists in the flight dictionary
        label_fare.grid(row=row_counter, column=6)
        row_counter += 1  # Move to next row for the next flight
    flights_window.mainloop()

def display_flights_sort_by_date(date,source,destination):
    connection = get_sql_connection()
    print(connection)
    print(date)
    print(source)
    print(destination)
    all_flights = get_flights_date(date,source,destination, connection)
    connection.close()

    flights_window = tk.Tk()
    flights_window.title("List of Flights")

    # Create labels for headers
    label_flight_id = tk.Label(flights_window, text="Flight ID")
    label_flight_id.grid(row=0, column=0)
    label_flight_name = tk.Label(flights_window, text="Flight Name")
    label_flight_name.grid(row=0, column=1)
    label_source = tk.Label(flights_window, text="Source")
    label_source.grid(row=0, column=2)
    label_destination = tk.Label(flights_window, text="Destination")
    label_destination.grid(row=0, column=3)
    label_departure_time = tk.Label(flights_window, text="Departure Time")
    label_departure_time.grid(row=0, column=4)
    label_arrival_time = tk.Label(flights_window, text="Arrival Time")
    label_arrival_time.grid(row=0, column=5)
    label_fare = tk.Label(flights_window, text="Fare")
    label_fare.grid(row=0, column=6)

    row_counter = 1  # Keep track of row for data placement

    # Display flight data using labels
    for flight in all_flights:
        label_id = tk.Label(flights_window, text=flight['flight_id'])
        label_id.grid(row=row_counter, column=0)
        label_name = tk.Label(flights_window, text=flight['flight_name'])
        label_name.grid(row=row_counter, column=1)
        label_source_city = tk.Label(flights_window, text=flight['source'])
        label_source_city.grid(row=row_counter, column=2)
        label_destination_city = tk.Label(flights_window, text=flight['destination'])
        label_destination_city.grid(row=row_counter, column=3)
        label_departure_time = tk.Label(flights_window, text=flight[
            'departure_time'])  # Assuming 'departure_time' exists in the flight dictionary
        label_departure_time.grid(row=row_counter, column=4)
        label_arrival_time = tk.Label(flights_window, text=flight[
            'arrival_time'])  # Assuming 'arrival_time' exists in the flight dictionary
        label_arrival_time.grid(row=row_counter, column=5)
        label_fare = tk.Label(flights_window,
                              text=flight['fare'])  # Assuming 'fare' exists in the flight dictionary
        label_fare.grid(row=row_counter, column=6)
        row_counter += 1  # Move to next row for the next flight


    flights_window.mainloop()
