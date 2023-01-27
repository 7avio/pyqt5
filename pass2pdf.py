from PyPDF2 import PdfWriter, PdfReader
import getpass
import sys

pdfwriter = PdfWriter()
pdf = PdfReader("example.pdf")
for page_num in range(len(pdf.pages)):
	pdfwriter.add_page(pdf.pages[page_num])
# passw = getpass.getpass(prompt = 'Enter your desired passwprd: ')
passw = getpass.win_getpass(prompt='Password: ', stream=None)
pdfwriter.encrypt(passw)
with open("new.pdf", "wb") as f:
	pdfwriter.write(f)
