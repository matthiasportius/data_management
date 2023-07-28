import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from to_zip import compress_data, add_to_zip



root = tk.Tk()
nb = ttk.Notebook(root)

# for resizing the window:
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


class ZipFrame:
    def __init__(self):
        self.mainframe = ttk.Frame(nb, padding= (45, 30, 45, 15))
        self.mainframe.grid(column=0, row=0)        
        self.populate_frame(self.mainframe)
        self.label_response = ttk.Label(self.mainframe, text="")
        self.label_response.grid(column=0, row=3, columnspan=3, pady=(10,0))


    def populate_frame(self, mainframe):
        nb.add(mainframe, text="Zip Data")
        nb.grid(column=0, row=0)

        label_zip = ttk.Label(mainframe, text="Select the folder you want to zip.", width=35, anchor=tk.W)  
        label_zip.grid(column=0, row=0)

        label_or = ttk.Label(mainframe, text="OR", width=35, anchor=tk.W)
        label_or.grid(column=0, row=1)

        label_append = ttk.Label(mainframe, text="Select the Zipfile you want to append to.", width=35, anchor=tk.W)
        label_append.grid(column=0, row=2)

        button_select_folder = ttk.Button(mainframe, text="Select Folder", command=self.open_folder)
        button_select_folder.grid(column=1, row=0, padx=(10, 0))

        button_compress = ttk.Button(mainframe, text="Compress", command=self.compress)
        button_compress.grid(column=2, row=0, padx=(10,0))

        button_select_zip = ttk.Button(mainframe, text="Select Zipfile", command=self.open_zipfile)
        button_select_zip.grid(column=1, row=2, padx=(10, 0))

        button_add = ttk.Button(mainframe, text="Add", command=self.append_zip)  
        button_add.grid(column=2, row=2, padx=(10,0))
        # make button as "Add File" and make 2nd button to "Add Folder"


    def open_folder(self):
        folderpath = filedialog.askdirectory() 
        global filepath 
        filepath = os.path.abspath(folderpath)
        self.label_response["text"] = f"Folder {os.path.split(filepath)[1]} selected. Press Compress to zip."



    def compress(self):
        compress_data(filepath)
        self.label_response["text"] = "Folder succesfully zipped."


    def open_zipfile(self):
        filename = filedialog.askopenfilename()
        global filepath 
        filepath = os.path.abspath(filename)
        self.label_response["text"] = f"Zipfile {os.path.split(filepath)[1]} selected. Press Add to select you additions."


    def append_zip(self):
        filename = filedialog.askopenfilename()
        append_path = os.path.abspath(filename)
        add_to_zip(filepath, append_path)
        self.label_response["text"] = "Files succesfully added to zipfile."



ZipFrame()





# PDF stuff below
pdf_frame = ttk.Frame(nb, padding= (45, 30, 45, 15))
pdf_frame.grid(column=0, row=0)

nb.add(pdf_frame, text="Merge PDFs")
nb.grid(column=0, row=0)

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
