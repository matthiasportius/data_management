import os
import zipfile



def compress_data(in_path: str | os.PathLike, compression_level: int = 0) -> None | bool:
    out_path = os.path.splitext(in_path)[0] + ".zip"
    try:
        with zipfile.ZipFile(file=out_path, mode='x', compression=zipfile.ZIP_DEFLATED, 
                             compresslevel=compression_level, strict_timestamps=False) as zipf:
            for root, folder, files in os.walk(in_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, in_path))
    except FileExistsError:
        return True


def add_fileto_zip(zip_path: str | os.PathLike, file_path: str | os.PathLike, compression_level: int = 0) -> None | bool:
    if zipfile.is_zipfile(zip_path) and os.path.isfile(file_path):
        with zipfile.ZipFile(zip_path, 'a', zipfile.ZIP_DEFLATED, compresslevel=compression_level) as zipf:
            zipf.write(file_path, os.path.split(file_path)[1])  
    else:
        return True


def add_folderto_zip(zip_path: str | os.PathLike, folder_path: str | os.PathLike, compression_level: int = 0) -> None | bool:
    if zipfile.is_zipfile(zip_path) and os.path.isdir(folder_path):
        with zipfile.ZipFile(zip_path, 'a', zipfile.ZIP_DEFLATED, compresslevel=compression_level) as zipf:     
            for root, folder, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))
    else:
        return True
