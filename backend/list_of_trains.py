import tkinter as tk
from trains_dao import get_all_trains
from sql_connection import get_sql_connection

def display_trains():
    connection = get_sql_connection()
    all_trains = get_all_trains(connection)
    connection.close()

    trains_window = tk.Tk()
    trains_window.title("List of Trains")

    trains_list = tk.Text(trains_window, height=10, width=50)
    trains_list.pack()

    for train in all_trains:
        trains_list.insert(tk.END, f"{train['train_id']} - {train['train_name']} - {train['source']} to {train['destination']}\n")

    trains_window.mainloop()
