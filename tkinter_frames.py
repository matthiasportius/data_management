import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from to_zip import compress_data, add_fileto_zip, add_folderto_zip
from to_pdf import merge_pdfs
from images import process_images



class ZipFrame:
    def __init__(self, notebook: ttk.Notebook) -> None:
        self.zip_path = None
        self.folder_path = None
        self.compression_level = 6
        
        self.mainframe = ttk.Frame(notebook, padding= (45, 30, 45, 15))
        self.mainframe.grid(column=0, row=0)        
        self.populate_frame(notebook, self.mainframe)
        self.label_response = ttk.Label(self.mainframe, text="")
        self.label_response.grid(column=0, row=5, columnspan=3, pady=(10,0))


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

        button_select_zip = ttk.Button(mainframe, text="Select Zipfile", command=self.open_zipfile)
        button_select_zip.grid(column=1, row=2, padx=(10, 0))

        button_add_file = ttk.Button(mainframe, text="Add File", command=self.append_fileto_zip)  
        button_add_file.grid(column=2, row=2, padx=(10,0))

        button_add_folder = ttk.Button(mainframe, text="Add Folder", command=self.append_folderto_zip)  
        button_add_folder.grid(column=2, row=3, padx=(10,0))

        compression_label = ttk.Label(mainframe, text="Compression level", width=35, anchor=tk.W)
        compression_label.grid(column=0, row=4)
        compression_level_slider = ttk.Scale(mainframe, from_=0, to=9, command=self.set_compression_level)
        compression_level_slider.set(6)
        compression_level_slider.grid(column=1, row=4)
        self.compression_level_label = ttk.Label(mainframe, text=f"{self.compression_level}")
        self.compression_level_label.grid(column=2, row=4)
        

    def open_folder(self):
        folderpath = filedialog.askdirectory() 
        self.folder_path = os.path.abspath(folderpath)
        self.label_response["text"] = f"Folder {os.path.split(self.folder_path)[1]} selected. Press Compress to zip."


    def compress(self):
        if not self.folder_path:
            self.label_response["text"] = "No folder selected."
        else:
            file_exists = compress_data(self.folder_path, self.compression_level)
            if file_exists:
                self.label_response["text"] = "ZIP file already exists."
            else:    
                self.label_response["text"] = "Folder succesfully zipped."


    def open_zipfile(self):
        filename = filedialog.askopenfilename(filetypes=[("ZIP files", "*.zip")])
        self.zip_path = os.path.abspath(filename)
        self.label_response["text"] = f"Zipfile {os.path.split(self.zip_path)[1]} selected. Press Add to select you additions."


    def append_fileto_zip(self):
        if not self.zip_path:
            self.label_response["text"] = "No zipfile selected"
        else:
            filename = filedialog.askopenfilename()
            append_path = os.path.abspath(filename)
            failed = add_fileto_zip(self.zip_path, append_path, self.compression_level)
            if failed:
                self.label_response["text"] = "File could not be added."
            else:
                self.label_response["text"] = "File succesfully added to zipfile."


    def append_folderto_zip(self):
        if not self.zip_path:
            self.label_response["text"] = "No zipfile selected"
        else:
            folderpath = filedialog.askdirectory() 
            append_path = os.path.abspath(folderpath)
            failed = add_folderto_zip(self.zip_path, append_path, self.compression_level)
            if failed:
                self.label_response["text"] = "Folder could not be added."
            else:
                self.label_response["text"] = "Folder succesfully added to zipfile."


    def set_compression_level(self, val):
        self.compression_level = int(float(val))
        if hasattr(self, 'compression_level_label'):
            self.compression_level_label.config(text=f"{self.compression_level}")



class PdfFrame:
    def __init__(self, notebook: ttk.Notebook) -> None:
        self.mainframe = ttk.Frame(notebook, padding= (45, 30, 45, 15))
        self.mainframe.grid(column=0, row=0)
        self.populate_frame(notebook, self.mainframe)
        self.label_response = ttk.Label(self.mainframe, text="")
        self.label_response.grid(column=0, row=5, columnspan=3, pady=(10,0))


    def populate_frame(self, notebook: ttk.Notebook, mainframe):
        notebook.add(mainframe, text="Merge PDFs")
        notebook.grid(column=0, row=0)

        merge_label = ttk.Label(mainframe, text="Select the pdf files you want to merge.")
        merge_label.grid(column=0, row=0)

        merge_button = ttk.Button(mainframe, text="Merge", command=self.combine_pdf)
        merge_button.grid(column=1, row=0, padx=(10,0))


    def combine_pdf(self):
        files = filedialog.askopenfilenames()
        no_files = merge_pdfs(files)
        if no_files:
            self.label_response["text"] = "No files selected."
        else: 
            self.label_response["text"] = "PDF files succesfully merged"



class ImgFrame:
    def __init__(self, notebook: ttk.Notebook) -> None:
        self.reduce_filesize = False
        self.reduce_filesize = tk.BooleanVar(value=False)
        self.preserve_dpi = tk.BooleanVar(value=False)
        self.reduce_quality = tk.BooleanVar(value=False)
        self.jpg_quality = 70


        self.mainframe = ttk.Frame(notebook, padding= (45, 30, 45, 15))
        self.mainframe.grid(column=0, row=0)
        self.populate_frame(notebook, self.mainframe)
        self.label_response = ttk.Label(self.mainframe, text="")
        self.label_response.grid(column=0, row=5, columnspan=3, pady=(10,0))


    def populate_frame(self, notebook: ttk.Notebook, mainframe):
        notebook.add(mainframe, text="Process IMGs")
        notebook.grid(column=0, row=0)

        merge_label = ttk.Label(mainframe, text="Select the image files you want to process and remove metadata from.")
        merge_label.grid(column=0, row=0)

        merge_button = ttk.Button(mainframe, text="Select images", command=self.process_img)
        merge_button.grid(column=1, row=0, padx=(10,0))

        check_reduce_filesize = ttk.Checkbutton(mainframe, text='Reduce filesize?', 
	    variable=self.reduce_filesize, onvalue=True, offvalue=False)
        check_reduce_filesize.grid(column=1, row=1)

        check_preserve_dpi = ttk.Checkbutton(mainframe, text='Preserve DPI for printing?', 
	    variable=self.preserve_dpi, onvalue=True, offvalue=False)
        check_preserve_dpi.grid(column=1, row=2, padx=(50,0))  

        check_reduce_quality = ttk.Checkbutton(mainframe, text='Reduce .jpg quality?', 
	    variable=self.reduce_quality, onvalue=True, offvalue=False, command=self.toggle_quality_level)
        check_reduce_quality.grid(column=1, row=3, padx=(23,0)) 

        self.quality_label = ttk.Label(mainframe, text="Quality level", width=35, anchor=tk.W)
        self.quality_label.grid(column=0, row=4)
        self.quality_level_slider = ttk.Scale(mainframe, from_=0, to=100, command=self.set_jpg_quality)
        self.quality_level_slider.set(70)
        self.quality_level_slider.grid(column=1, row=4)
        self.quality_level_label = ttk.Label(mainframe, text=f"{self.jpg_quality}")
        self.quality_level_label.grid(column=2, row=4)
        self.toggle_quality_level()


    def process_img(self):
        filenames = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg *.jpeg *.png *.webp *.bmp *.tiff *.tif"),
                                                          ("JPEG files", "*.jpg *.jpeg"),
                                                          ("PNG files", "*.png"),])
        if not filenames:
            self.label_response["text"] = "No image files selected."
        else:
            error = process_images(input_files=filenames, reduce_filesize=self.reduce_filesize.get(),
                                reduce_quality=self.reduce_quality.get(), jpg_quality=self.jpg_quality,
                                preserve_DPI=self.preserve_dpi.get())
            if error:
                self.label_response["text"] = f"{error}"
            else:
                self.label_response["text"] = "Image files succesfully processed"


    def toggle_quality_level(self):
        state = 'normal' if self.reduce_quality.get() else 'disabled'
        self.quality_label.configure(state=state)
        self.quality_level_slider.configure(state=state)
        self.quality_level_label.configure(state=state)


    def set_jpg_quality(self, val):
        self.jpg_quality = int(float(val))
        if hasattr(self, 'quality_level_label'):
            self.quality_level_label.config(text=f"{self.jpg_quality}")
