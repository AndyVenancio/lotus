import PyPDF2 as pdf2

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_file_path = '432-632-Syllabus-Fall23-draft2.pdf'

# Open the PDF file in read-binary mode
with open(pdf_file_path, 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = pdf2.PdfFileReader(pdf_file)

    # Get the number of pages in the PDF
    num_pages = pdf_reader.numPages
    print(f'Total number of pages: {num_pages}')

    # Extract and print text from each page
    page = pdf_reader.getPage(0)
    page_text = page.extractText()
    print(page_text[127:146])
    x = page_text.find('Dr Sergey Kushnarev')
    print(x)
