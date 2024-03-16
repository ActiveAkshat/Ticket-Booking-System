import tkinter
import tkinter as tk
from tkcalendar import Calendar
from firebase_admin import db, credentials, initialize_app

# Initialize Firebase
cred = credentials.Certificate("my-python-project-47230-firebase-adminsdk-p4hvj-4d196bc3d4.json")
initialize_app(cred, {"databaseURL": "https://python-ticket-booking-default-rtdb.firebaseio.com/"})
database_ref = db.reference("/users")

# Create a Tkinter window
login_page = tk.Tk()
login_page.title("Login Page")

frame_login = tkinter.Frame(login_page)
frame_login.pack(padx=20, pady=10)

# Global variable to store the selected transport mode
transport_mode = None


def open_homepage():
    login_page.destroy()  # Close the login window

    def search_transport(mode):
        if mode == 1:
            print("Search for airplanes")
            # Add your logic to search for airplanes
        elif mode == 0:
            print("Search for trains")
            # Add your logic to search for trains

    def select_date():
        def set_selected_date():
            date_entry.delete(0, tk.END)
            date_entry.insert(0, cal.selection_get().strftime('%d-%m-%Y'))
            top.destroy()

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

    frame_home = tkinter.Frame(homepage)
    frame_home.pack(padx=20, pady=10)

    # Entry fields for source, destination, and date
    source_label = tk.Label(frame_home, text="Source:")
    source_label.grid(row=0, column=0, sticky="e")
    source_entry = tk.Entry(frame_home)
    source_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    source_entry.insert(0, "Source")

    destination_label = tk.Label(frame_home, text="Destination:")
    destination_label.grid(row=1, column=0, sticky="e")
    destination_entry = tk.Entry(frame_home)
    destination_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    destination_entry.insert(0, "Destination")

    date_label = tk.Label(frame_home, text="Date:")
    date_label.grid(row=2, column=0, sticky="e")
    date_entry = tk.Entry(frame_home)
    date_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    date_entry.insert(0, "DD-MM-YYYY")
    calendar_button = tk.Button(frame_home, text="📅", command=select_date)
    calendar_button.grid(row=2, column=2, padx=5, pady=5, sticky="w")

    # Load PNG images
    airplane_image = tk.PhotoImage(file="flight_logo.png")
    train_image = tk.PhotoImage(file="train_logo.png")

    # Add image buttons
    airplane_button = tk.Button(frame_home, image=airplane_image, command=set_airplane_mode)
    airplane_button.grid(row=3, column=0, padx=5, pady=5)
    train_button = tk.Button(frame_home, image=train_image, command=set_train_mode)
    train_button.grid(row=3, column=1, padx=5, pady=5)

    # Button for search
    search_button = tk.Button(frame_home, text="Search", command=lambda: search_transport(transport_mode))
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
        success_window = tk.Toplevel(login_page)
        success_window.title("Success")
        label_status.config(text="Login successful!", fg="green")

        # Open the homepage after successful login
        open_homepage()

    else:
        label_status.config(text="Invalid username or password", fg="red")


def logout():
    success_window = tk.Toplevel(login_page)
    success_window.title("Success")
    button_logout = tk.Button(login_page, text="Logout", command=logout)
    button_logout.grid(row=5, column=0, columnspan=2, pady=10)
    label_status.config(text="Logout successful!", fg="green")


# Function to handle sign up button click
def signup():
    # Create a new window for sign up
    signup_window = tk.Toplevel(login_page)
    signup_window.title("Sign Up")

    frame_signup = tkinter.Frame(signup_window)
    frame_signup.pack(padx=20, pady=10)

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
    label_new_username = tk.Label(frame_signup, text="Username:")
    label_new_username.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    entry_new_username = tk.Entry(frame_signup)
    entry_new_username.grid(row=0, column=1, padx=10, pady=10)

    label_new_password = tk.Label(frame_signup, text="Password:")
    label_new_password.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    entry_new_password = tk.Entry(frame_signup, show="*")
    entry_new_password.grid(row=1, column=1, padx=10, pady=10)

    label_confirm_password = tk.Label(frame_signup, text="Confirm Password:")
    label_confirm_password.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    entry_confirm_password = tk.Entry(frame_signup, show="*")
    entry_confirm_password.grid(row=2, column=1, padx=10, pady=10)

    button_confirm_signup = tk.Button(frame_signup, text="Sign up", command=confirm_signup)
    button_confirm_signup.grid(row=3, column=0, columnspan=2, pady=10)

    label_signup_status = tk.Label(frame_signup, text="")
    label_signup_status.grid(row=4, column=0, columnspan=2)


# Create and place widgets in the main window
label_username = tk.Label(frame_login, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry_username = tk.Entry(frame_login)
entry_username.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(frame_login, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry_password = tk.Entry(frame_login, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

button_login = tk.Button(frame_login, text="Login", command=login)
button_login.grid(row=2, column=0, columnspan=2, pady=10)

button_signup = tk.Button(frame_login, text="Sign up", command=signup)
button_signup.grid(row=3, column=0, columnspan=2, pady=10)

label_status = tk.Label(frame_login, text="")
label_status.grid(row=4, column=0, columnspan=2)

# Start the Tkinter event loop
login_page.mainloop()
