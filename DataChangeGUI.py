# -*- coding: utf-8 -*-
"""
Created on May 25, 2022
Create GUI for data entry in FCIN error database
@author: jeremy
"""
# Import packages
from tkinter import *
#import tkinter.font as font
#from tkinter import filedialog
import sqlite3
from tkinter import ttk

# build database
conn = sqlite3.connect('update_data.db')
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


# Create application window
root = Tk()
root.title('FN2 Error Log')
root.iconbitmap("fishicon2.ico")
root.geometry("600x500+10+10")


# Create layout
frame_125 = LabelFrame(root, text = "FN125")
frame_125.grid(row=1, column = 0, pady = 10, padx = 10)

frame_controls = LabelFrame(root, text = "Controls")
frame_controls.grid(row = 2, column = 0, pady = 5, padx = 5)

# add treeview frame
# Create Treeview Frame
tree_frame = Frame(root)
tree_frame.grid(row = 3, padx = 5, pady=5)

# Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)
# Create Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
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
prjcd = Entry(frame_125, width = 15)
prjcd.grid(row = 1, column = 1)
prjcd_label = Label(frame_125, text = "PRJ_CD (ex. LWA_IA15_051)")
prjcd_label.grid(row = 1, column = 0)
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
    conn = sqlite3.connect("update_data.db")
    c = conn.cursor()
    c.execute("SELECT * FROM FN125Updates")
    records = c.fetchall()
    print(records)
    for record in records:
        my_tree.insert(parent="", index = record[0],  values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]))

# Clear, submit and exit buttons
## define command functions
def clear_contents():
    sam.delete(0, END)
    eff.delete(0, END)
    spc.delete(0, END)
    fish.delete(0,END)
    tabfield.delete(0, END)
    updateval.delete(0, END)
    prjcd.focus_set()

def submit():
    # Create db connection
    conn = sqlite3.connect('update_data.db')
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

# Create clear contents button
# Create submit button
submit_btn = Button(frame_controls, text = "Add Record", command = submit) 
submit_btn.grid(row = 1, column = 0, pady = 5, padx = 5)
#submit_btn['font'] = font.Font(size = 18)

clear_btn = Button(frame_controls, text = "Clear Contents", command = clear_contents)
clear_btn.grid(row = 1, column = 2, pady = 5, padx = 5)

# Create exit button
exit_btn = Button(frame_controls, text = "End Program", command = root.destroy)
exit_btn.grid(row = 1, column = 3, pady = 5, padx = 5)
#exit_btn['font'] = font.Font(size = 14)

# for testing
# query_database()

# Runs the window
root.mainloop()
