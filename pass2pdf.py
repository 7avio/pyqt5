from PyPDF2 import PdfWriter, PdfReader
import getpass
import sys

def encrypt_document():
	pdf_file = str(input('insert the name of your pdf file: '))
	pdf_pass = str(input('insert the name of your document with password'))
	pdfwriter = PdfWriter()
	pdf = PdfReader(pdf_file)
	for page_num in range(len(pdf.pages)):
		pdfwriter.add_page(pdf.pages[page_num])
	# passw = getpass.getpass(prompt = 'Enter your desired passwprd: ')
	passw = getpass.win_getpass(prompt='Password: ', stream=None)
	pdfwriter.encrypt(passw)
	with open(pdf_pass, 	"wb") as f:
		pdfwriter.write(f)
