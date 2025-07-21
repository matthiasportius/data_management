# Data Conversion and Management UI

This project is a selfmade UI, made with Tkinter, to convers and manage files.  
As of now, zipping files, adding files to existing zipfiles and merging single pdf files is supported, but more is planned.

## compression

ZIP (and similar algorithms like GZIP or DEFLATE):
* work best on raw, repetitive, or text-based data (.txt, .csv, .json, .docx, .xlsx, .bmp, .wav, .tiff)
* are ineffective on data that’s already compressed (.jpg, .png, .mp3, .mp4, .zip)
This is why compression of image files like .jpg or .png shows no change, even at compression level 9, since they are already compressed.


## Usage

Run the tkinter_gui.py file and use the GUI for everything else.

## Issues to address

Following issues are addressed next:

* There could be a superclass for the frames holding the `__init__`, since this should always be the same (response label to Pdf class needs to be added)
* add option to insert pdf in existing one see [here](https://pypdf.readthedocs.io/en/stable/user/merging-pdfs.html)
* add option to reduce size of existing pdf see [here](https://pypdf.readthedocs.io/en/stable/user/file-size.html)
* add option to remove metadata of images to shrink them
* make tkinter more beautiful
* make it deployable / installable
* bind certain keys with root.bind() for more functionality?
* option to create new files and folder?
* in create folder if action cancelled dont show anything (not it shows: folder data management selected)
* prevent duplicate files in zip
* handle overwrites gracefully
* show a progress bar
* add more failsafe tests:
    * isdir option in to_zip and run that if true, ...
* option to extract zipfiles (zipfile.Zipfile.extractall(out_path))?

* next: 
