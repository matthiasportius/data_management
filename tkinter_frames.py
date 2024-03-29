import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from to_zip import compress_data, add_to_zip
from to_pdf import merge_pdfs



class ZipFrame:
    def __init__(self, notebook: ttk.Notebook) -> None:
        self.mainframe = ttk.Frame(notebook, padding= (45, 30, 45, 15))
        self.mainframe.grid(column=0, row=0)        
        self.populate_frame(notebook, self.mainframe)
        self.label_response = ttk.Label(self.mainframe, text="")
        self.label_response.grid(column=0, row=3, columnspan=3, pady=(10,0))


    def populate_frame(self, notebook: ttk.Notebook, mainframe):
        notebook.add(mainframe, text="Zip Data")
        notebook.grid(column=0, row=0)

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
        # make these buttons unselectable if no folder/file is selected first
        # unselectable = default; if file: selectable

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
        compress_data(filepath)  # add option (button/selector etc.) to give integer value from 0-9 to compress_data (default: give no value / optional)
        self.label_response["text"] = "Folder succesfully zipped." # if not aborted before, make if case for all cases/occurences


    def open_zipfile(self):
        filename = filedialog.askopenfilename()
        global filepath 
        filepath = os.path.abspath(filename)
        # forgot to test for .zip extension, if its not a zip then print out fail message and dont allow add (make it not clickable)
        self.label_response["text"] = f"Zipfile {os.path.split(filepath)[1]} selected. Press Add to select you additions."


    def append_zip(self):
        filename = filedialog.askopenfilename()  # add option to add folder with askdirectory
        append_path = os.path.abspath(filename)
        add_to_zip(filepath, append_path)
        self.label_response["text"] = "Files succesfully added to zipfile."


class PdfFrame:
    def __init__(self, notebook: ttk.Notebook) -> None:
        self.mainframe = ttk.Frame(notebook, padding= (45, 30, 45, 15))
        self.mainframe.grid(column=0, row=0)
        self.populate_frame(notebook, self.mainframe)

    def populate_frame(self, notebook: ttk.Notebook, mainframe):
        notebook.add(mainframe, text="Merge PDFs")
        notebook.grid(column=0, row=0)

        merge_label = ttk.Label(mainframe, text="Select the pdf files you want to merge.")
        merge_label.grid(column=0, row=0)

        merge_button = ttk.Button(mainframe, text="Merge", command=self.combine_pdf)
        merge_button.grid(column=1, row=0, padx=(10,0))


    def combine_pdf(self):
        files = filedialog.askopenfilenames()
        merge_pdfs(files)
