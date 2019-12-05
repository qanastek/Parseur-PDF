# -*- coding: utf-8 -*-

import time
import re
import os
import sys

reload(sys)  
sys.setdefaultencoding('utf-8')

from xml.etree.ElementTree import Element, SubElement, Comment, tostring

def convertPdfToTxt(splitted):
    	
	for name in splitted[0:-1]:
		
		nameRaw = name.split(".")[0]
		rst = "pdftotext -enc UTF-8 '%s' '%s.txt'" % (name,nameRaw)
		os.system(rst)

def getResume(data):
    	
	if re.search("Abstract",data):
			splitted = data.split("Abstract")[1]
	elif re.search("ABSTRACT",data):
		splitted = data.split("ABSTRACT")[1]

	# Get first paragraphe
	splitted2 = splitted.split("\n\n")[0]

	# Cut after Keywords
	splitted2 = splitted2.split("Keywords")[0]

	# Replace jump line by spaces
	splitted2 = splitted2.replace("\n"," ")

	# Delete characters which aren't Alpha and Space
	splitted2 = re.sub('[^a-zA-Z ]+', '', splitted2[:5]) + splitted2[5:]

	return splitted2

def getTitle(data):
    	
	return data.split('\n')[0]

os.system("rm *.txt")
os.system("rm *.xml")

# Delete spaces in files names
os.system("""
for file in *.pdf; do mv "$file" "$(echo $file | sed 's/ /_/g')"; done
""")

# List all the PDF available
ls = "ls *.pdf"
c = os.popen(ls).read()

splitted = c.split("\n")

# Convert each PDF to TXT
convertPdfToTxt(splitted)

# For each converted PDF
for item in splitted[0:-1]:
	
	# Cut the extension and keep the name only
	nameFile = item.split(".")[0]

	# Open the converted PDF
	with open(nameFile + ".txt", 'r') as f:

		data = f.read().decode('utf-8')

		# Documents Informations
		fileName = nameFile
		title = getTitle(data)
		resume = getResume(data)

		# Create the output file
		os.system('touch resultat.txt')

		# Write informations inside the file
		with open("resultat.txt", 'a') as res:
			res.write("\n")
			res.write("File name: " + str(fileName))
			res.write("\n\n")
			res.write("Title: " + str(title))
			res.write("\n\n")
			res.write("Résumé: " + str(resume))
			res.write("\n\n")
			res.write("\n\n-------------------------------------------------------------\n")
		res.close()


	f.close()
