import os
from pypdf import PdfWriter



def merge_pdfs(files: tuple[str, ...]) -> None:
    if not files:
        return
    
    merger = PdfWriter()
    files_pdf = [file for file in files if file.endswith(".pdf")]
    for pdf in files_pdf:
        merger.append(pdf)
    folder_path = os.path.split(files_pdf[0])[0]
    merger.write(os.path.join(folder_path, "merged_pdf.pdf"))
    merger.close()


# insert pdf into existing (combine/merge)

# reduce pdf size