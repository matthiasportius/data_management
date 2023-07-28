import os
import zipfile


def compress_data(in_path):
    out_path = os.path.splitext(in_path)[0] + ".zip"
    with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as zipf:  # deflate is most common method to zip, better use 'x' instead of 'w' as it exclusively creates and writes new file
        for root, folder, files in os.walk(in_path):  # os.walk also goes to subfolder
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, in_path))


def add_to_zip(zip_path, in_path):
    if zipfile.is_zipfile(zip_path):
        with zipfile.ZipFile(zip_path, 'a', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(in_path, os.path.split(in_path)[1])
# works not with single files, to do for folders, change following:
            # for root, folder, files in os.walk(in_path):
            #     # stops here, walk not for files?
            #     print(3)
            #     for file in files:
            #         file_path = os.path.join(in_path, file)
            #         zipf.write(file_path, os.path.relpath(file_path, in_path))
    # deletes all previous files in zip and does not add extra files, something with relpath?




# for compress_data --> ZipFile also accepts compresslevel=<value from 0 to 9> with 9 having the best compression and 0 having no compression

# extract zipfiles:
# zipfile.Zipfile.extractall(out_path)
