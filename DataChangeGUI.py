# -*- coding: utf-8 -*-
"""
Created on May 25, 2022
Create GUI for data entry in FCIN error database
@author: J. Holden
"""
# Import packages
from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox

global dbfile 
dbfile = FALSE

# build database
def opennew():
    global dbfile
    new_db_file = fd.asksaveasfilename(defaultextension=".db")
    if(new_db_file):
        dbfile = new_db_file
        conn = sqlite3.connect(dbfile)
        c = conn.cursor()
        # Create FN025_update
        c.execute("""CREATE TABLE IF NOT EXISTS FN125Updates (
            id INTEGER PRIMARY KEY,
            PRJ_CD text,
            SAM text,
            EFF text,
            SPC text,
            FISH int,
            Field2Change text,
            Value2Update int   
            ) """)

        # Do commit
        conn.commit()
        # close DB connection
        conn.close()
        dbname = dbfile.split("/")
        message_text.set("%s" % (dbname[-1]))
        query_database()
        prjcd.delete(0, END)

def openexisting():
    global dbfile
    existing_db_file = fd.askopenfilename()
    if existing_db_file:
        dbfile = existing_db_file
        conn = sqlite3.connect(dbfile)
        c = conn.cursor()
        query_database()
        dbname = dbfile.split("/")
        message_text.set("%s" % (dbname[-1]))
        c.execute("SELECT PRJ_CD FROM FN125Updates")
        myprjcd = (c.fetchall())[0]
        prjcd.delete(0, END)
        prjcd.insert(0, *myprjcd)

def show_version():
    response = messagebox.showinfo("Version", "Version: 0.0.1.9003\nCreated by J. Holden")
    
# Create application window
root = Tk()
root.title('FN2 Error Log')
root.geometry("500x500+10+10") # +10+10 indicates where it opens

# Create a Menu 
my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label = "File", menu=file_menu)
file_menu.add_command(label = "New Database", command=opennew)
file_menu.add_command(label = "Open Existing", command=openexisting)
file_menu.add_command(label = "Quit (ctrl+q)", command = root.quit)
about_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label = "Version Info", command = show_version)

# Create layout
# version_label = Label(text = "version: 0.0.1.9003", justify=RIGHT).grid(row = 4, column = 1)
message_text = StringVar()
message_text.set("Use FILE menu to select a database")

entry_frame = Frame(root).grid(row = 2, column = 0)
# message_frame = LabelFrame(root, text = "Messages").grid(column=0, row=4)
message_label = Label(textvariable = message_text).grid(row = 4, column=0)

# Entry window
frame_125 = LabelFrame(entry_frame, text = "FN125")
frame_125.grid(column = 0, row = 1, pady = 5, padx = 5)

frame_controls = LabelFrame(entry_frame, text = "Controls")
frame_controls.grid(row = 1, column = 1, pady = 1, padx = 1)

# add treeview frame
# Create Treeview Frame
tree_frame = LabelFrame(root, text = "Database records")
tree_frame.grid(row = 3, column = 0, padx = 15, pady=5, columnspan=2)

# Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")

# Pack to the screen
my_tree.pack()
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("ID", "PRJ_CD", "SAM", "EFF", "SPC", "FISH", "COLUMN", "VALUE")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=25)
my_tree.column("PRJ_CD", anchor=W, width=100)
my_tree.column("SAM", anchor=W, width=50)
my_tree.column("EFF", anchor=W, width=50)
my_tree.column("SPC", anchor=W, width=50)
my_tree.column("FISH", anchor=W, width=50)
my_tree.column("COLUMN", anchor=W, width=60)
my_tree.column("VALUE", anchor=W, width=50)

# Create Headings 
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("ID", text = "ID", anchor=W)
my_tree.heading("PRJ_CD", text="PRJ_CD", anchor=W)
my_tree.heading("SAM", text="SAM", anchor=W)
my_tree.heading("EFF", text="EFF", anchor=W)
my_tree.heading("SPC", text="SPC", anchor=W)
my_tree.heading("FISH", text="FISH", anchor=W)
my_tree.heading("COLUMN", text="COLUMN", anchor=W)
my_tree.heading("VALUE", text="VALUE", anchor=W)

# labels and entry boxes
prjcd = Entry(frame_125, width = 13)
prjcd.grid(row = 1, column = 1, padx = (0, 5))
prjcd_label = Label(frame_125, text = "PRJ_CD (ex. LWA_IA15_051)")
prjcd_label.grid(row = 1, column = 0)
prjcd.insert(0, "lwa_ia22_000")
prjcd.focus_set()

sam = Entry(frame_125, width = 5)
sam.grid(row = 2, column = 1)
sam_label = Label(frame_125, text = "SAM")
sam_label.grid(row = 2, column = 0)

eff = Entry(frame_125, width = 5)
eff.grid(row = 3, column = 1)
eff_label = Label(frame_125, text = "EFF (ex. 038)")
eff_label.grid(row = 3, column = 0)

spc = Entry(frame_125, width = 5)
spc.grid(row = 4, column = 1)
spc_label = Label(frame_125, text = "SPC (ex. 081)")
spc_label.grid(row = 4, column = 0)

fish = Entry(frame_125, width = 5)
fish.grid(row = 5, column = 1)
fish_label = Label(frame_125, text = "FISH")
fish_label.grid(row = 5, column = 0)

tabfield = Entry(frame_125, width = 5)
tabfield.grid(row = 6, column = 1)
tabfield_label = Label(frame_125, text = "Field to replace (ex. FLEN)")
tabfield_label.grid(row = 6, column = 0)

updateval = Entry(frame_125, width = 5)
updateval.grid(row = 7, column = 1)
updateval_label = Label(frame_125, text = "Corrected value")
updateval_label.grid(row = 7, column = 0)

# populate the tree view with data
def query_database():
    for record in my_tree.get_children():
	    my_tree.delete(record)
        
    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    c.execute("SELECT * FROM FN125Updates")
    records = c.fetchall()
    records.sort(reverse=True)
    
    # counter required for proper indexing
    i=0
    for record in records:
        my_tree.insert("", index=i,  values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]))
        i+=1

# Clear, submit and exit buttons
## define command functions
# clean contents will empty the entry boxes
def clear_contents():
    sam.delete(0, END)
    eff.delete(0, END)
    spc.delete(0, END)
    fish.delete(0,END)
    tabfield.delete(0, END)
    updateval.delete(0, END)
    prjcd.focus_set()
    message_text.set(" ")

# submit writes the new data to the db
def submit(event = None):
    # Create db connection
    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    c.execute("INSERT INTO FN125Updates (PRJ_CD, SAM, EFF, SPC, FISH, Field2Change, Value2Update) VALUES (:PRJ_CD, :SAM, :EFF, :SPC, :FISH, :Field2Change, :Value2Update)",
        {
            'PRJ_CD': prjcd.get().upper(),
            'SAM': sam.get(),
            'EFF': eff.get().zfill(3),
            'SPC': spc.get().zfill(3),
            'FISH': fish.get(),
            'Field2Change': tabfield.get().upper(),
            'Value2Update': updateval.get()   
        }              
    )
    # Close cursor
    conn.commit()
    conn.close()
    clear_contents()
    query_database()
    message_text.set("New record was added to database")

# this will delete a record from the database and update treeview
def delete_record():
    # retrieves the index where treeview is focused
    selected = my_tree.focus()
    
    # retrieves the input values of selected
    values = my_tree.item(selected, 'values')
    
    # gets the index and deletes it from the tree view
    x = my_tree.selection()[0]
    my_tree.delete(x)
    
    # delete the record from the data
    conn = sqlite3.connect(dbfile)
    
    c = conn.cursor()
    c.execute("DELETE from FN125Updates WHERE ID=" + values[0])

    conn.commit()
    conn.close()
    clear_contents()
    
    # update treeview
    query_database()
    
    # provide confirmation message
    message_text.set("Record was successfully deleted")


# Create submit button
submit_btn = Button(frame_controls, text = "Add Record", command = submit) 
submit_btn.grid(row = 1, column = 0, pady = 5, padx = 5)
submit_btn.bind('<Return>', submit)

# Create clear contents button
clear_btn = Button(frame_controls, text = "Clear Form", command = clear_contents)
clear_btn.grid(row = 2, column = 0, pady = 5, padx = 5)

# delete a record button
delete_btn = Button(frame_controls, text = "Delete Record", command = delete_record)
delete_btn.grid(row = 3, column=0, pady=5, padx=5)

# Create exit button
# exit_btn = Button(frame_controls, text = "End Program", command = root.destroy)
# exit_btn.grid(row = 4, column = 0, pady = 5, padx = 5)

# bind ctrl+q to quick exit
def end_app(event):
    root.destroy()
root.bind("<Control-q>", end_app)

# required to fill treeview on start up
# query_database()

# Runs the window
root.mainloop()

# end