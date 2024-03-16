import tkinter
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
from tkinter import messagebox
from docx2pdf import convert


# Define global variables
source = ""
destination = ""
date = ""
trainName = ""
fare = 0

# Global variable to store the number of passengers
passenger_count = 0


def fetch_details():
    global source, destination, date, trainName, fare

    try:
        # Importing details from another Python file
        from train_details import source, destination, date, trainName, fare
    except ImportError:
        # For testing purposes, defining variables manually
        source = "TestSource"
        destination = "TestDestination"
        date = "15-03-2024"
        trainName = "TestTrain"
        fare = 1000


def clear_item():
    passName_entry.delete(0, tkinter.END)
    age_entry.delete(0, tkinter.END)
    age_entry.insert(0, "1")
    gender_entry.set("")


ticket_list = []


def add_item():
    global passenger_count
    Pname = passName_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    Pclass = class_entry.get()
    ticket_item = [Pname, age, gender, Pclass]

    tree.insert('', 0, values=ticket_item)
    clear_item()
    ticket_list.append(ticket_item)
    passenger_count += 1  # Increment passenger count when an item is added


def new_ticket():
    global passenger_count
    name_entry.delete(0, tkinter.END)
    trainID_entry.delete(0, tkinter.END)
    class_entry.delete(0, tkinter.END)
    clear_item()
    tree.delete(*tree.get_children())
    ticket_list.clear()
    passenger_count = 0


def generate_ticket():
    fetch_details()

    doc = DocxTemplate("train_ticket_template.docx")
    name = name_entry.get()
    trainID = trainID_entry.get()

    # Initialize seat number
    seat_number = 20

    # Iterate over each ticket item and assign seat number
    for ticket_item in ticket_list:
        ticket_item.append(seat_number)
        seat_number += 1

    subtotal = fare * passenger_count
    platformFee = (fare * 0.01) * passenger_count
    total = subtotal + platformFee

    doc.render({"fname": name,
                "trainID": trainID,
                "source": source,
                "destination": destination,
                "date": date,
                "trainName": trainName,
                "ticket_list": ticket_list,
                "subtotal": subtotal,
                "platformFee": platformFee,
                "total": total
                })

    doc_name = "Ticket_" + name + datetime.datetime.now().strftime("%d-%m-%Y-%H%M%S") + ".docx"
    doc.save(doc_name)

    # Convert generated docx ticket to pdf and save into the "Tickets" folder
    generate_pdf(doc_name)

    messagebox.showinfo("Ticket Booked", "Ticket Booked Successfully")

    new_ticket()


def generate_pdf(docx_file_path):
    try:
        # Convert docx to pdf and specify the output folder
        convert(docx_file_path)
        print("PDF generated successfully.")
    except Exception as e:
        print("Error generating PDF:", e)


bookingPage = tkinter.Tk()
bookingPage.title("Ticket Booking Form")

frame = tkinter.Frame(bookingPage)
frame.pack(padx=20, pady=10)

name_label = tkinter.Label(frame, text="Name")
name_label.grid(row=0, column=0)
trainID_label = tkinter.Label(frame, text="Train No.")
trainID_label.grid(row=0, column=1)
class_label = tkinter.Label(frame, text="Class")
class_label.grid(row=0, column=2)

name_entry = tkinter.Entry(frame)
name_entry.grid(row=1, column=0)
trainID_entry = tkinter.Entry(frame)
trainID_entry.grid(row=1, column=1)
class_entry = tkinter.Entry(frame)
class_entry.grid(row=1, column=2)

passName_label = tkinter.Label(frame, text="Passenger Name")
passName_label.grid(row=2, column=0)
age_label = tkinter.Label(frame, text="Age")
age_label.grid(row=2, column=1)
gender_label = tkinter.Label(frame, text="Gender")
gender_label.grid(row=2, column=2)

passName_entry = tkinter.Entry(frame)
passName_entry.grid(row=3, column=0)
age_entry = tkinter.Spinbox(frame, from_=1, to=100, increment=1)
age_entry.grid(row=3, column=1)

gender_entry = tkinter.StringVar()
gender_drop_down = ttk.Combobox(frame, textvariable=gender_entry)
gender_drop_down['values'] = ('Male', 'Female')
gender_drop_down.grid(row=3, column=2)
add_item_button = tkinter.Button(frame, text="Add passenger", command=add_item)
add_item_button.grid(row=4, column=2, pady=5)

columns = ('Name', 'Age', 'Gender', 'Class')
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading('Name', text='Name')
tree.heading('Age', text='Age')
tree.heading('Gender', text='Gender')
tree.heading('Class', text='Class')

tree.grid(row=5, column=0, columnspan=3, padx=20, pady=10)

save_ticket_button = tkinter.Button(frame, text="Confirm Booking", command=generate_ticket)
save_ticket_button.grid(row=6, column=0, columnspan=3, sticky="news", padx=20, pady=5)
new_ticket_button = tkinter.Button(frame, text="Clear All", command=new_ticket)
new_ticket_button.grid(row=7, column=0, columnspan=3, sticky="news", padx=20, pady=5)

bookingPage.mainloop()
