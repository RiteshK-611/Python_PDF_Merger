from PyPDF2 import PdfFileMerger, PdfFileReader
from tkinter.filedialog import askopenfilename, asksaveasfilename

merger = PdfFileMerger()

n = int(input("Enter no. of files you want to merge: "))

for file in range(n):
  file = PdfFileReader(askopenfilename())
  merger.append(file)

merger.write(asksaveasfilename()+".pdf")