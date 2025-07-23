import os
from PIL import Image, ExifTags



ORIENTATION_TAG = 274
ROTATION_MAP = {
    3: 180,
    6: 270,
    8: 90
}


def process_images(input_folder: str | os.PathLike, reduce_filesize: bool = False, reduce_quality: bool = False, 
                   jpg_quality: int = 70, remove_metadata: bool = False) -> None:
    supported_formats = ('.jpg', '.jpeg', '.png')

    output_folder = os.path.join(os.path.dirname(input_folder), 'processed_images')
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, folder, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(supported_formats):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_folder, os.path.relpath(input_path, input_folder))
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                try:
                    img = Image.open(input_path)

                    # rotate
                    exif = img.getexif()
                    orientation = exif.get(ORIENTATION_TAG)
                    if orientation in ROTATION_MAP:
                        angle = ROTATION_MAP[orientation]
                        img = img.rotate(angle, expand=True)

                    # strip metadata
                    if remove_metadata:
                        img_no_meta = Image.new(img.mode, img.size)
                        img_no_meta.putdata(img.getdata())
                        img = img_no_meta

                    if reduce_filesize:
                        img.save(output_path, format=img.format, optimize=True)
                    if reduce_quality and img.format == 'JPEG':
                        img.save(output_path, format=img.format, quality=jpg_quality)
                    else:
                        img.save(output_path, format=img.format, optimize=False)

                except Exception as e:
                    return f"Error processing {file}: {e}"

# add checkbox for reduce quality or reduce filesize
# add slider for quality reduction setting to compress images (default = 0 reduction)
# add checkbox for metadata removal
# add button for "Process Image"
# add info: only for .jpg and .png
