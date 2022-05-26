# Data Change Log Database GUI
Author: Jeremy Holden
Email: jeremy.holden@ontario.ca
version: 0.0.1.9001
version date: May 26, 2022

# Objective
Create a lightweight sqlite data base with a tkinter GUI that is used to record required data changes to FN2 files. Changes are recorded in the data base and then in R a `rows_update()` applies the changes to the data. 

# Issues and Features
1. Current template only for FN125 - consider implementation for other tables
2. Add treeview
3. Add text box explaining *flen* will be converted to *FLEN*
4. Add "last entry box"