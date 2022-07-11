# Data Change Log Database GUI
Author: Jeremy Holden  
Email: jeremy.holden@ontario.ca  
version: 0.0.1.9002  
version date: May 30, 2022  

# Objective
Create a lightweight sqlite data base with a tkinter GUI that is used to record required data changes to FN2 files. Changes are recorded in the data base and then in R a `rows_update()` applies the changes to the data along with additional cleaning and standardization routines. Changes are recorded in the database and will later be merged using R along with additional cleaning and standardization routines as the data are migrated to a long term storage system. In this manner, raw data can remain unchanged while creating a documented, reproducible pipeline of data changes. 

![graphic user interface](gui_pic.png)

# Usage
The script (executable if created) should be moved to an existing project directory. On load, a new sqlite database will be created in the working directory. In sucessive loads the GUI will connect to the existing database and load the data to the spreadsheet view section of the GUI. You can move between entry boxes using "TAB". New records are added to the database via the "Submit" button (on click or with "ENTER" when highlighted). Currently, errors can only be deleted and not edited (at least not from this GUI - see DBBrowser software to interact with update_data.db if required). To delete a record, highlight the record in the spreadsheet window that is intended to be deleted and then click "Delete".  

## Running from terminal
```
python DataChangeGUI.py
```
## Executable
An executable can be created using *auto-py-to-exe*.
```
auto-py-to-exe
```


# Issues and Features
1. Current template only for FN125 - consider implementation for other tables
2. Add additional checks for field constraints (eg. `entry` in "flen", "tlen", ...))

