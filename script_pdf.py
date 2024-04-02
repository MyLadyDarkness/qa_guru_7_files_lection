# for pdf files: pip install pypdf
import os.path

from pypdf import PdfReader

reader = PdfReader("tmp/Python Notes.pdf")

#print(reader.pages)
#print(len(reader.pages))

#print(reader.pages[1].extract_text())

print(os.path.getsize("tmp/Python Notes.pdf")) # size 267167

assert os.path.getsize("tmp/Python Notes.pdf") == 267167

