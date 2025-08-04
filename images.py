import os
from PIL import Image, ExifTags



ORIENTATION_TAG = 274
ROTATION_MAP = {
    3: 180,
    6: 270,
    8: 90
}


def process_images(input_files: tuple[str | os.PathLike], reduce_filesize: bool = False, reduce_quality: bool = False, 
                   jpg_quality: int = 70, preserve_DPI: bool = False) -> None | str:
    supported_formats = ('.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff', '.tif')
    output_folder = os.path.join(os.path.dirname(input_files[0]), 'processed_images')
    output_folder = os.path.normpath(output_folder)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in input_files:
        if file.lower().endswith(supported_formats):
            output_path = os.path.join(output_folder, os.path.relpath(file, os.path.dirname(input_files[0])))
            output_path = os.path.normpath(output_path)
            try:
                img = Image.open(file)

                # rotate
                exif = img.getexif()
                orientation = exif.get(ORIENTATION_TAG)
                if orientation in ROTATION_MAP:
                    angle = ROTATION_MAP[orientation]
                    img = img.rotate(angle, expand=True)
                
                # retian DPI info
                dpi = None
                if preserve_DPI:
                    dpi = img.info.get("dpi")
                    if not dpi and "jpeg" in img.format.lower():
                        exif = img.getexif()
                        x_dpi = exif.get(282)
                        y_dpi = exif.get(283)
                        if x_dpi and y_dpi:
                            dpi = (int(x_dpi), int(y_dpi))

                save_kwargs = {}
                if dpi:
                    save_kwargs["dpi"] = dpi
                if reduce_filesize:
                    save_kwargs["optimize"] = True
                else:
                    save_kwargs["optimize"] = False
                if reduce_quality and img.format == 'JPEG':
                    save_kwargs["quality"] = jpg_quality
                img.save(output_path, format=img.format, **save_kwargs)

            except Exception as e:
                return f"Error processing {file}: {e}"
        
        else: 
            return "Image format not supported."
