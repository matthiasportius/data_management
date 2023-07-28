# Data Conversion and Management UI

This project is a selfmade UI, made with Tkinter, to convers and manage files.  
As of now, zipping files, adding files to existing zipfiles and merging single pdf files is supported, but more is planned.

## Usage

Run the tkinter_gui.py file and use the GUI for everything else.

## Issues to address

Following issues are addressed next:

* There could be a superclass for the frames holding the `__init__`, since this should always be the same (response label to Pdf class needs to be added)
* add a button to zipfile class which selects folder that can be appended to a zipfile (for that at a isdir option in to_zip and run that if true)
* add option to determine zip compression level (0-9)
* add option to insert pdf in existing one see [here](https://pypdf.readthedocs.io/en/stable/user/merging-pdfs.html)
* add option to reduce size of existing pdf see [here](https://pypdf.readthedocs.io/en/stable/user/file-size.html
