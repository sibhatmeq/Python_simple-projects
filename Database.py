from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Databse  in python Tkinter")
root.geometry("500x500")

# Database 672499548

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')
# create cursor
c = conn.cursor()


# # create table
# c.execute("""CREATE TABLE addresses(
#     first_name text,
#     last_name text,
#     addressm text,
#     city text,
#     state text,
#     zipcode integer
# )""")
# create edit fun to update a record

def edit():
    editor = Tk()
    editor.title("update a record")
    editor.geometry("400x600")
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()
    # query the database

    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
    # loop through results
    for record in records:
        



    print_records = ""
    for record in records:
        print_records += str(record[0]) + "  " + str(record[1]) + " " + " \t" + str(record[6]) + "\n"

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)


    # Create text box labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))

    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)

    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)

    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)

    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)

    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)
    # create save button
    save_btn = Button(editor, text="Save Records", command=edit)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)


def delete():
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()
    # Delete a record
    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())
    conn.commit()
    conn.close()


# create submit function for databases
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()
    # insert into a table
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    conn.commit()

    # close connection
    conn.close()

    # clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


#  create query fun
def query():
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()
    # query the database
    c.execute("SELECT * , oid FROM addresses")
    records = c.fetchall()
    # print(records)
    # Loop through results
    print_records = ""
    for record in records:
        print_records += str(record[0]) + "  " +  str(record[1]) + " " + " \t" + str(record[6]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    conn.commit()

    # close connection
    conn.close()


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)


# Create text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Delete ID ")
delete_box_label.grid(row=9, column=0)


# Create Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Create query button
query_btn = Button(root, text="show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a delete button

delete_btn = Button(root, text="Delete Records", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
# Create a update button

edit_btn = Button(root, text="Update Records", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=141)


conn.commit()

# close connection
conn.close()

root.mainloop()
