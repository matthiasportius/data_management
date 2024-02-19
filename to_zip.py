import os
import zipfile



def compress_data(in_path: str | os.PathLike, compression_level: int = -1) -> None:
    out_path = os.path.splitext(in_path)[0] + ".zip"
    try:
        with zipfile.ZipFile(file=out_path, mode='w', compression=zipfile.ZIP_DEFLATED,
                             compresslevel=compression_level, strict_timestamps=False) as zipf:  
            for root, folder, files in os.walk(in_path): 
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, in_path))
    except FileExistsError:
        pass  # add sth like returning a phrase which is outputted by tkinter


def add_to_zip(zip_path: str | os.PathLike, add_path: str | os.PathLike) -> None:
    if zipfile.is_zipfile(zip_path):
        with zipfile.ZipFile(zip_path, 'a', zipfile.ZIP_DEFLATED) as zipf:
            if os.path.isdir(add_path):
                # works not with single files only folders
                # "unpacks" files in the selected folder into zipfile
                for root, folder, files in os.walk(add_path):
                    for file in files:
                        file_path = os.path.join(add_path, file)
                        zipf.write(file_path, os.path.relpath(file_path, add_path))
            else:
                zipf.write(add_path, os.path.split(add_path)[1])
    else:
        pass  # add returning phrase: is not a zipfile


# test this and make button for it
def extract_zip(zip_path):
    if zipfile.is_zipfile(zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            zipf.extractall(path=os.path.split(zip_path)[0])
    else:
        pass  # add returning phrase: is no a zipfile
# according to the docs, decompression has a lot of pitfalls 
    # (incorrect zip format, usupported compression method, incorrect password, ...)
    # later only allow for certain compression types, no passwords, specific zip format
