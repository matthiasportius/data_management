import os
import zipfile




def compress_data(in_path: str | os.PathLike, compression_level: int = 0) -> None:
    out_path = os.path.splitext(in_path)[0] + ".zip"
    with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=compression_level) as zipf:  # deflate is most common method to zip, better use 'x' instead of 'w' as it exclusively creates and writes new file
        for root, folder, files in os.walk(in_path):  # os.walk also goes to subfolder
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, in_path))
    # make this as one
    try:
        with zipfile.ZipFile(file=out_path, mode='w', compression=zipfile.ZIP_DEFLATED,
                             compresslevel=compression_level, strict_timestamps=False) as zipf:  
            for root, folder, files in os.walk(in_path): 
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, in_path))
    except FileExistsError:
        pass  # add sth like returning a phrase which is outputted by tkinter






def add_fileto_zip(zip_path: str | os.PathLike, file_path: str | os.PathLike, compression_level) -> None:
    if zipfile.is_zipfile(zip_path):
        with zipfile.ZipFile(zip_path, 'a', zipfile.ZIP_DEFLATED, compresslevel=compression_level) as zipf:
            zipf.write(file_path, os.path.split(file_path)[1])  
# add this:             if os.path.isdir(add_path) and isfile to the function:


def add_folderto_zip(zip_path, folder_path, compression_level):
    if zipfile.is_zipfile(zip_path):
        with zipfile.ZipFile(zip_path, 'a', zipfile.ZIP_DEFLATED, compresslevel=compression_level) as zipf:     
            for root, folder, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))
