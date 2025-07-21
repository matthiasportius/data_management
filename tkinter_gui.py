import tkinter as tk
from tkinter import ttk

from tkinter_frames import ZipFrame, PdfFrame



root = tk.Tk()
root.title("Data Manager")
nb = ttk.Notebook(root)

# for resizing the window:
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# generates frame for zipping files:
ZipFrame(nb)

# generates frame for merging pdf files:
PdfFrame(nb)


root.mainloop()



# some NOTES

# justify = center/left/right possible with labels etc. (with single line anchor='n' option is better)
# many widgets have options: borderwith = int and relief = "flat"/"raised"/"sunken"/"solid"/"ridge"/"groove"

# using variables in widgets of Tkinter only possible with instance of StringVar class (not arbitrary Python variables)
# label2 = ttk.Label(mainframe, textvariable="Initial")
# result = tk.StringVar()
# label["textvariable"] = result
# result.set("New")

# widget can be positioned in corners using anchor = n for north or e, s, w, ne, ... 
# grid can be used with columspan=2 / rowspan=4

# testv = tk.BooleanVar()
# check = ttk.Checkbutton(mainframe, text="Test this?", variable=testv, onvalue=True, offvalue=False) # default of onvalue=1 and offvalue = 0
# read more on that on how to initialize testv variable + starting value and how to read it
# maybe with testv = BooleanVar(value=False (is also default))



# # disallow menubar tearoff:
# root.option_add('*tearOff', False)  # or FALSE?
# menubar:
# win = tk.Toplevel(root) 
# menubar = tk.Menu(win)
# win['menu'] = menubar
#     # make menubar child of other window (root or mainframe) to not have 2nd window
# menu_file = tk.Menu(menubar)
# menu_edit = tk.Menu(menubar)
# menubar.add_cascade(menu=menu_file, label='File')
# menubar.add_cascade(menu=menu_edit, label='Edit')
# def newFile():
#     pass
# def openFile():
#     pass
# def closeFile():
#     pass
# menu_file.add_command(label='New', command=newFile)
# menu_file.add_command(label='Open...', command=openFile)
# menu_file.add_command(label='Close', command=closeFile)
