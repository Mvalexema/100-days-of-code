import PyPDF2

# Reading pdf file (Mosaic press release with 4q24 results)
file = open('Press-Release.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(file)

page_one = pdf_reader.pages[0]

page_one_text = page_one.extract_text()
print(page_one_text)
file.close()


# Writing(copying) into the pdf file
file = open('Press-Release.pdf','rb')
pdf_reader = PyPDF2.PdfReader(file)
first_page = pdf_reader.pages[0]
#first_page_text = first_page.extract_text()
pdf_writer = PyPDF2.PdfWriter()

pdf_writer.add_page(first_page)

pdf_output = open("New_doc.pdf", 'wb')
pdf_writer.write(pdf_output)
#print()
pdf_output.close()
file.close()
