import tkinter as tk
from firebase_admin import db, credentials, initialize_app
from tkcalendar import Calendar

from backend.list_of_flights import display_flights
from backend.list_of_trains import display_trains
from backend.trains_dao import get_all_trains
from flights_dao import get_all_flights, get_flights_date
from sql_connection import get_sql_connection

# Initialize Firebase
cred = credentials.Certificate("my-python-project-47230-firebase-adminsdk-p4hvj-4d196bc3d4.json")
initialize_app(cred, {"databaseURL": "https://my-python-project-47230-default-rtdb.asia-southeast1.firebasedatabase.app/"})
database_ref = db.reference("/users")

# Create a Tkinter window
window = tk.Tk()
window.title("Login Page")


def open_homepage():
    window.destroy()  # Close the login window
    # Global variable to store the selected transport mode
    transport_mode = None

    def search_transport(mode):
        global transport_mode
        if transport_mode == 1:
            print("Search for airplanes")
            # Add your logic to search for airplanes
            display_flights()

        elif transport_mode == 0:
            print("Search for trains")
            # Add your logic to search for trains
        display_trains()

    def select_date():
        def set_selected_date():
            date_entry.delete(0, tk.END)
            date_entry.insert(0, cal.selection_get().strftime('%d-%m-%Y'))
            top.destroy()

            get_flights_date(date_entry)

        top = tk.Toplevel(homepage)
        cal = Calendar(top, selectmode='day')
        cal.pack()
        select_button = tk.Button(top, text="Select", command=set_selected_date)
        select_button.pack()

    def set_airplane_mode():
        global transport_mode
        transport_mode = 1

    def set_train_mode():
        global transport_mode
        transport_mode = 0

    # Create and run the homepage window
    homepage = tk.Tk()
    homepage.title("Airline and Train Ticket Booking System")

    # Entry fields for source, destination, and date
    source_label = tk.Label(homepage, text="Source:")
    source_label.grid(row=0, column=0, sticky="e")
    source_entry = tk.Entry(homepage)
    source_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    source_entry.insert(0, "Source")

    destination_label = tk.Label(homepage, text="Destination:")
    destination_label.grid(row=1, column=0, sticky="e")
    destination_entry = tk.Entry(homepage)
    destination_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    destination_entry.insert(0, "Destination")

    date_label = tk.Label(homepage, text="Date:")
    date_label.grid(row=2, column=0, sticky="e")
    date_entry = tk.Entry(homepage)
    date_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    date_entry.insert(0, "DD-MM-YYYY")
    calendar_button = tk.Button(homepage, text="📅", command=select_date)
    calendar_button.grid(row=2, column=2, padx=5, pady=5, sticky="w")

    # Load PNG images
    airplane_image = tk.PhotoImage(file="../flight_logo.png")
    train_image = tk.PhotoImage(file="../train_logo.png")

    # Add image buttons
    airplane_button = tk.Button(homepage, image=airplane_image, command=set_airplane_mode)
    airplane_button.grid(row=3, column=0, padx=5, pady=5)
    train_button = tk.Button(homepage, image=train_image, command=set_train_mode)
    train_button.grid(row=3, column=1, padx=5, pady=5)

    # Button for search
    search_button = tk.Button(homepage, text="Search", command=lambda: [search_transport(transport_mode), display_trains()])
    search_button.grid(row=4, columnspan=2, padx=5, pady=5)

    # Run the Tkinter event loop
    homepage.mainloop()


# Function to handle login button click
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Check login credentials against the database
    user_data = database_ref.child(username).get()

    if user_data and user_data.get("password") == password:
        success_window = tk.Toplevel(window)
        success_window.title("Success")
        label_status.config(text="Login successful!", fg="green")

        # Open the homepage after successful login
        open_homepage()

    else:
        label_status.config(text="Invalid username or password", fg="red")



def logout():
    success_window = tk.Toplevel(window)
    success_window.title("Success")
    button_logout = tk.Button(window, text="Logout", command=logout)
    button_logout.grid(row=5, column=0, columnspan=2, pady=10)
    label_status.config(text="Logout successful!", fg="green")


# Function to handle sign up button click
def signup():
    # Create a new window for sign up
    signup_window = tk.Toplevel(window)
    signup_window.title("Sign Up")

    # Function to handle sign up confirmation button click
    def confirm_signup():
        new_username = entry_new_username.get()
        new_password = entry_new_password.get()
        confirm_password = entry_confirm_password.get()

        if new_password == confirm_password:
            # Store the new user in the database
            database_ref.child(new_username).set({"password": new_password})
            label_status.config(text="Registration successful!", fg="green")
            signup_window.destroy()
        else:
            label_signup_status.config(text="Passwords do not match", fg="red")

    # Create and place widgets in the sign-up window
    label_new_username = tk.Label(signup_window, text="New Username:")
    label_new_username.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    entry_new_username = tk.Entry(signup_window)
    entry_new_username.grid(row=0, column=1, padx=10, pady=10)

    label_new_password = tk.Label(signup_window, text="New Password:")
    label_new_password.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    entry_new_password = tk.Entry(signup_window, show="*")
    entry_new_password.grid(row=1, column=1, padx=10, pady=10)

    label_confirm_password = tk.Label(signup_window, text="Confirm Password:")
    label_confirm_password.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    entry_confirm_password = tk.Entry(signup_window, show="*")
    entry_confirm_password.grid(row=2, column=1, padx=10, pady=10)

    button_confirm_signup = tk.Button(signup_window, text="Sign up", command=confirm_signup)
    button_confirm_signup.grid(row=3, column=0, columnspan=2, pady=10)

    label_signup_status = tk.Label(signup_window, text="")
    label_signup_status.grid(row=4, column=0, columnspan=2)


# Create and place widgets in the main window
label_username = tk.Label(window, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry_username = tk.Entry(window)
entry_username.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(window, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry_password = tk.Entry(window, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

button_login = tk.Button(window, text="Login", command=login)
button_login.grid(row=2, column=0, columnspan=2, pady=10)

button_signup = tk.Button(window, text="Sign up", command=signup)
button_signup.grid(row=3, column=0, columnspan=2, pady=10)

label_status = tk.Label(window, text="")
label_status.grid(row=4, column=0, columnspan=2)

# Start the Tkinter event loop
window.mainloop()
