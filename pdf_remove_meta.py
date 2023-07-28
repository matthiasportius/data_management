# meta data contains (private) info related to the file (title, author, keywords, ...)
# it can be deleted to get "safe" pdfs

# strg + d with open pdf lets you see pdf metadata

from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("name_of_pdf.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.add_metadate({})  # empty dict added to metadata leads to no metadata in the end

with open("meta_pdf.pdf", 'wb') as new_pdf:
    writer.write(new_pdf)  # new pdf file without metadata which contains all info of the old file
