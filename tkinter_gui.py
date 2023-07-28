import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pypdf import PdfWriter

from tkinter_frames import ZipFrame



root = tk.Tk()
nb = ttk.Notebook(root)

# for resizing the window:
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# generates frame for zipping files:
ZipFrame(nb)


# PDF stuff below
pdf_frame = ttk.Frame(nb, padding= (45, 30, 45, 15))
pdf_frame.grid(column=0, row=0)

nb.add(pdf_frame, text="Merge PDFs")
nb.grid(column=0, row=0)

def merge_pdf():
    files = filedialog.askopenfilenames()
    merger = PdfWriter()
    files_pdf = [file for file in files if file.endswith(".pdf")]
    for pdf in files_pdf:
        merger.append(pdf)
    folder_path = os.path.split(files_pdf[0])[0]
    merger.write(os.path.join(folder_path, "merged_pdf.pdf"))
    merger.close()
    # works, gives list:
    # ('C:/Users/User/Documents/test/test_pdf/pdf1.pdf', 'C:/Users/User/Documents/test/test_pdf/pdf2.pdf', ...)

merge_label = ttk.Label(pdf_frame, text="Select the pdf files you want to merge.")
merge_label.grid(column=0, row=0)

merge_button = ttk.Button(pdf_frame, text="Merge", command=merge_pdf)
merge_button.grid(column=1, row=0, padx=(10,0))




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
