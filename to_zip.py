import os
import zipfile



def compress_data(in_path, compression_level):
    out_path = os.path.splitext(in_path)[0] + ".zip"
    with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=compression_level) as zipf:  # deflate is most common method to zip, better use 'x' instead of 'w' as it exclusively creates and writes new file
        for root, folder, files in os.walk(in_path):  # os.walk also goes to subfolder
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, in_path))


def add_fileto_zip(zip_path, file_path, compression_level):
    if zipfile.is_zipfile(zip_path):
        with zipfile.ZipFile(zip_path, 'a', zipfile.ZIP_DEFLATED, compresslevel=compression_level) as zipf:
            zipf.write(file_path, os.path.split(file_path)[1])  


def add_folderto_zip(zip_path, folder_path, compression_level):
    if zipfile.is_zipfile(zip_path):
        with zipfile.ZipFile(zip_path, 'a', zipfile.ZIP_DEFLATED, compresslevel=compression_level) as zipf:     
            for root, folder, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))
