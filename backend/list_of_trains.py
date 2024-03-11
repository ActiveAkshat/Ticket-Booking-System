import tkinter as tk
from trains_dao import get_all_trains
from sql_connection import get_sql_connection


def display_trains():
    connection = get_sql_connection()
    all_trains = get_all_trains(connection)
    connection.close()

    trains_window = tk.Tk()
    trains_window.title("List of Trains")

    # Create labels for headers
    label_train_id = tk.Label(trains_window, text="Train ID")
    label_train_id.grid(row=0, column=0)
    label_train_name = tk.Label(trains_window, text="Train Name")
    label_train_name.grid(row=0, column=1)
    label_source = tk.Label(trains_window, text="Source")
    label_source.grid(row=0, column=2)
    label_destination = tk.Label(trains_window, text="Destination")
    label_destination.grid(row=0, column=3)
    label_departure_time = tk.Label(trains_window, text="Departure Time")
    label_departure_time.grid(row=0, column=4)
    label_arrival_time = tk.Label(trains_window, text="Arrival Time")
    label_arrival_time.grid(row=0, column=5)
    label_fare = tk.Label(trains_window, text="Fare")
    label_fare.grid(row=0, column=6)

    row_counter = 1  # Keep track of row for data placement

    # Display train data using labels
    for train in all_trains:
        label_id = tk.Label(trains_window, text=train['train_id'])
        label_id.grid(row=row_counter, column=0)
        label_name = tk.Label(trains_window, text=train['train_name'])
        label_name.grid(row=row_counter, column=1)
        label_source_city = tk.Label(trains_window, text=train['source'])
        label_source_city.grid(row=row_counter, column=2)
        label_destination_city = tk.Label(trains_window, text=train['destination'])
        label_destination_city.grid(row=row_counter, column=3)
        label_departure_time = tk.Label(trains_window, text=train['departure_time'])  # Assuming 'departure_time' exists in the train dictionary
        label_departure_time.grid(row=row_counter, column=4)
        label_arrival_time = tk.Label(trains_window, text=train['arrival_time'])  # Assuming 'arrival_time' exists in the train dictionary
        label_arrival_time.grid(row=row_counter, column=5)
        label_fare = tk.Label(trains_window, text=train['fare'])  # Assuming 'fare' exists in the train dictionary
        label_fare.grid(row=row_counter, column=6)
        row_counter += 1  # Move to next row for the next train

    trains_window.mainloop()
