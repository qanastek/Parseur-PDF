# -*- coding: utf-8 -*-

import time
import cStringIO
import getopt
import os
import re
import string
import sys

from pyPdf import PdfFileReader
from pyPdf.utils import PdfReadError

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf, PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFSyntaxError

if len(sys.argv) != 3:
	sys.exit("Erreur argument manquant !")

path = sys.argv[2]

rm = "rm %s *.txt" % (path)
os.system(rm)

ls = "ls %s *.pdf" % (path)
c = os.popen(ls).read()

splitted = c.split("\n")

if sys.argv[1] == "-t":
    out='txt'
elif sys.argv[1] == "-x":
    out='xml'
else:
    print("argument incorrect") 

for item in splitted[0:-1]:
	# print (item.split(".")[0])
	
	name = item.split(".")[0]

	# pdftotext -enc UTF-8 'x.pdf' 'x.txt'
	rst = "pdftotext -enc UTF-8 '%s%s.pdf' '%s%s.%s'" % (path,name,path,name,out)
	print(rst)
	os.system(rst)

os.system('touch resultat.txt')

splitted1 = c.split("\n")

for item in splitted1[0:-1]:
	
	name = item.split(".")[0]
	
	#print (name)

	with open(path + name + ".txt", 'r') as f:

		data = f.read()

		if re.search("Abstract",data):
			splitted = data.split("Abstract")[1]
		elif re.search("ABSTRACT",data):
			splitted = data.split("ABSTRACT")[1]

		splitted2 = splitted.split("\n\n")[0]
		splitted2 = splitted2.split("Keywords")[0]

		with open("resultat.txt", 'a') as res:
			res.write(name)
			res.write("\n\n")
			res.write(splitted2)
			res.write("\n")
			res.write("-------------------------------------------------------------")
			res.write("\n")
		res.close()

	f.close()
