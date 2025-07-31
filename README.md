# Data Conversion and Management UI

This project is a selfmade UI, made with Tkinter, to convers and manage files.  
As of now, zipping files, adding files to existing zipfiles and merging single pdf files is supported, but more is planned.

## compression

ZIP (and similar algorithms like GZIP or DEFLATE):
* work best on raw, repetitive, or text-based data (.txt, .csv, .json, .docx, .xlsx, .bmp, .wav, .tiff)
* are ineffective on data that’s already compressed (.jpg, .png, .mp3, .mp4, .zip)
This is why compression of image files like .jpg or .png shows no change, even at compression level 9, since they are already compressed.

## remove metadata from images

Image metadata includes several informations how, when and where the image was taken. Timestamps, camera model, gps location and software are infos collected in the image's metadata. 
Although size reduction from removing this data is minimal, the privacy gain is far greater.

## Usage

Run the tkinter_gui.py file and use the GUI for everything else.

### to_pdf.py

#### merge_pdfs

Accepts full file paths as a tuple of strings. All files in the tuple are checked for their `.pdf` extension. The pdfs are then merged into one file which is then stored as `merged_pdf.pdf` in the same file directory. 

## to_zip.py

#### compress_data

Compresses a selected folder and creates that folder as a zip file. The most common method to zip files, *deflate*, is used. The *mode* parameter is `'x'` to exclusively create and write a new file. If the file `outpath` already exists, a `FileExistsError` is returned which is catched.
`os.walk` is used to get all the files in the selected folder, as it also goes to subfolders. With the `ZipFile.write()` method, the file is added to the zip archive with its initial name.  
Compression level can be selected between integers of 0 to 9. 0 beeing no compression and 9 the most compression, but also the slowest. The dafault value is -1 which is a compromise between speed and compression (equivalent to ~6).  
`strict_timestamps` is set to `False` to allow files with timestapms before 1980 and after 2107 (setting the timestamp to this limit value).  

#### add_fileto_zip

Adds a file to an existing zip file. First checks if the given path is a valid zip file and if not returns an error message. If a folder should be added, `os.walk` goes over all the files in the folder and writes them to the zip archive. The files in the selected folder are unpacked into the zip file. For a single file, it is simply directly written to the archive.

#### add_folderto_zip

## images.py

The 'Orientation' tag tells how to properly rotate image before viewing. Therefore it is better retain that info. Because of that I rotate images before removing that tag. The `ORIENTATION_TAG` value of 274 represents the EXIF 'Orientation' tag mapped to an int. This is a standardized value. However, to dynamically get the int representation of the EXIF tag one could use: `next((k for k, v in ExifTags.TAGS.items() if v == 'Orientation'), None)` (in the very unlikely case that the tag number ever changes this would still work). Since PIL's `rotate()` rotates CCW the values of `ROTATION_MAP` are e.g. 6: 270° CCW = 90° CW which again fits the EXIF tag standard values.
`img.getdata()` copies only pixel data, so any metadata or tags are not transferred this way. By not passing any info to the save parameter like `exif=img.info['exif']` the metadata is lost.
By loosing the metadata, also the DPI info is lost. If there is no DPI info, the pillow library often assigns a DPI of 96 by default. For .tif files it is often retained when using pilow. If the user wants to explicitly retain the info, an option for that was added.
When not passing metadata to the `save` function, it is automatically omitted and therefore deleted in the new file. Retaining or finding specific metadata however is more difficult, since for different file formats, the metadata is also stored different. While .jpg files metadata can often be accessed via `img.info`, .png files store metadata in text chunks and so on.

## tkinter_frames.py

#### combine_pdf

`filedialog.askopenfilenames` returns the filenames of the selected files as a tuple of string. If no file is selected and the dialogue is aborted, an empty string is returned. If a file was selected and the dialogue is aborted, an empty tuple is returned. The filenames are given to `merge_pdfs`, a function in `to_pdf.py`.
> The filenames are the files full path as string.

## Issues to address

Following issues are addressed next:

* There could be a superclass for the frames holding the `__init__`, since this should always be the same (response label to Pdf class needs to be added)
* add option to insert pdf in existing one see [here](https://pypdf.readthedocs.io/en/stable/user/merging-pdfs.html)
* add option to reduce size of existing pdf see [here](https://pypdf.readthedocs.io/en/stable/user/file-size.html)
* make tkinter more beautiful
* bind certain keys with root.bind() for more functionality?
* prevent duplicate files in zip
* handle overwrites gracefully
* show a progress bar
* make buttons like compress unselectable if no folder was selected before (unselectable = default; if file: selectable)

* next: 
    2. finish remove metadata from pdfs (+ add it to to_pdf.py as option during merge + add GUI checkbox for it)
    3. For 'Select folder' and 'Select zipfile' if action cancelled dont show anything (now it shows: folder data_management selected)
    4. add typing to tkinter_frames
    5. make it deployable / installable
