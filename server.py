import PyPDF2


#Funcion que lee el archivo .pdf
pdf_reader = PyPDF2.PdfReader("Ing-de-Soft.pdf")
#pages = len(pdf_reader.pages)
pages = 50


pdf_writer = PyPDF2.PdfWriter()
for page in range(pages):
    pdf_writer.add_page(pdf_reader.pages[page])

new_file = f"page-{page}.pdf"

with open(new_file, "wb")as new_file:
    pdf_writer.write(new_file)
print(f"Se ha creado un nuevo archivo")


#Write a pdf file
