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

#### combine_pdf

`filedialog.askopenfilenames` returns the filenames of the selected files as a tuple of string. If no file is selected and the dialogue is aborted, an empty string is returned. If a file was selected and the dialogue is aborted, an empty tuple is returned. The filenames are given to `merge_pdfs`, a function in `to_pdf.py`.
> The filenames are the files full path as string.

#### merge_pdfs

Accepts full file paths as a tuple of strings. All files in the tuple are checked for their `.pdf` extension. The pdfs are then merged into one file which is then stored as `merged_pdf.pdf` in the same file directory. 

#### compress_data

Compresses a selected folder and creates that folder as a zip file. The most common method to zip files, *deflate*, is used. The *mode* parameter is `'x'` to exclusively create and write a new file. If the file `outpath` already exists, a `FileExistsError` is returned which is catched.
`os.walk` is used to get all the files in the selected folder, as it also goes to subfolders. With the `ZipFile.write()` method, the file is added to the zip archive with its initial name.  
Compression level can be selected between integers of 0 to 9. 0 beeing no compression and 9 the most compression, but also the slowest. The dafault value is -1 which is a compromise between speed and compression (equivalent to ~6).  
`strict_timestamps` is set to `False` to allow files with timestapms before 1980 and after 2107 (setting the timestamp to this limit value).  

#### add_to_zip

Adds a file or folder to an existing zip file. First checks if the given path is a valid zip file and if not returns an error message. If a folder should be added, `os.walk` goes over all the files in the folder and writes them to the zip archive. The files in the selected folder are unpacked into the zip file. For a single file, it is simply directly written to the archive.

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
* add some error handling, e.g. when user closes dialogue windows before submitting etc. (often this just crashed program)

* next: 
