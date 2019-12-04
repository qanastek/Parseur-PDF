# -*- coding: utf-8 -*-

import time
import re
import os
import sys

reload(sys)  
sys.setdefaultencoding('utf-8')

from xml.etree.ElementTree import Element, SubElement, Comment, tostring

if len(sys.argv) != 2:
	sys.exit("Erreur argument manquant !")


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

def getAuthors(data):
    	
	return data.split('\n')[1:2]

def getReferences(data):

	if re.search("references",data):
		rslt = data.split('references')[1]

	elif re.search("References",data):
		rslt = data.split("References")[1]

	elif re.search("REFERENCES",data):
		rslt = data.split("REFERENCES")[1]

	# Get each line of the page
	page = rslt.split("\n")

	for line in page:

		if line == "\n" or len(line) <= 15 or re.match("^[\[\]0-9\.\ \|]+$",line):
			page.remove(line)

		previousLine = line

	# .split("\n\n")[0]
	return "\n".join(page)

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

# Read the args
if sys.argv[1] == "-t":
    out='txt'
elif sys.argv[1] == "-x":
    out='xml'
else:
    print("argument incorrect") 

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
		author = getAuthors(data)
		resume = getResume(data)
		bibliographie = getReferences(data)

		# If the user want to export as TXT
		if out == "txt":
    			
			# Create the output file
			os.system('touch resultat.txt')

			# Write informations inside the file
			with open("resultat.txt", 'a') as res:
				res.write("\n")
				res.write("File name: " + fileName)
				res.write("\n\n")
				res.write("Title: " + title)
				res.write("\n\n")
				res.write("Résumé: " + resume)
				res.write("\n\n")
				res.write("Biblio: " + bibliographie)
				res.write("\n\n-------------------------------------------------------------\n")
			res.close()

		# If the user want to export as XML
		elif out == "xml":
    			
			root = Element('article')

			preamble = SubElement(root, 'preamble')
			preamble.text = str(fileName)

			titre = SubElement(root, 'titre')
			titre.text = str(title)

			auteur = SubElement(root, 'auteur')
			auteur.text = str(author)

			abstract = SubElement(root, 'abstract')
			abstract.text = str(resume)

			biblio = SubElement(root, 'biblio')
			biblio.text = str(bibliographie)

			xml = tostring(root)

			# Create the output file
			os.system('touch resultat.xml')

			# Write the XML object inside
			with open("resultat.xml", 'a') as res:
				res.write(xml)
			res.close()


	f.close()
