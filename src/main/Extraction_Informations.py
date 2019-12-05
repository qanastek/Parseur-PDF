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

def convertPdfToTxt(name):
    	
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
			# print(line)
			page.remove(line)

	# .split("\n\n")[0]
	return "\n".join(page)

def getAuthors(data):

	return data.split('\n')[1]

def getConclusion(data):

	# Geteverything after the keyword "Conclusion"
	if re.search("Conclusion",data):

		if data.count("Conclusion")>1:
			rslt = data.split('Conclusion')[2]
		else:
			rslt = data.split('Conclusion')[1]

	elif re.search("CONCLUSION",data):
		rslt = data.split("CONCLUSION")[1]

	if re.search("Acknowledgments",data):
		rslt = rslt.split("Acknowledgments")[0]

	elif re.search("ACKNOWLEDGEMNTS",data):
		rslt = rslt.split("ACKNOWLEDGMENTS")[0]

	if re.search("Acknowledgements",data):
		rslt = rslt.split("Acknowledgements")[0]

	elif re.search("ACKNOWLEDGEMENTS",data):
		rslt = rslt.split("ACKNOWLEDGEMENTS")[0]	

	if re.search("References",data):
		rslt = rslt.split("References")[0]

	elif re.search("REFERENCES",data):
		rslt = rslt.split("REFERENCES")[0]

	# Get each line of the page

	conclu = rslt.split("\n")

	# print(conclu)
	for line in conclu:

		if line == "\n" or len(line) <= 15 or re.match("^[\[\]0-9\.\ \|]+$",line) or re.match("^[0-9]+$",line):
			# print(line)
			conclu.remove(line)

	# .split("\n\n")[0]
	return "\n".join(conclu)	

def getIntroduction(data):
	return ""

def getDiscution(data):
	return ""

def getCorps(data):
	start = 'introduction\n'
	s = data
	s = s[s.lower().find(start) + len(start):s.lower().rfind('conclusion')]

	if len(s) <= 10:
		s = s[s.lower().rfind(start) + len(start):s.lower().rfind('references\n')]
	return s

def showChoices(ls):

	id = 0

	for item in ls[:-1]:
		print("[%d] %s") % (id,item)
		id += 1

	print("Chosisez un document:")
	choice = input()

	return (choice, ls[choice])

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

choice,item = showChoices(splitted)

# Convert each PDF to TXT
convertPdfToTxt(item)

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
	conclusion = getConclusion(data)
	introduction = getIntroduction(data)
	discution = getDiscution(data)
	corps = getCorps(data)

	# If the user want to export as TXT
	if out == "txt":
			
		# Create the output file
		os.system('touch resultat.txt')

		# Write informations inside the file
		with open("resultat.txt", 'a') as res:
			res.write("\n")
			res.write("File name: " + str(fileName))
			res.write("\n\n")
			res.write("Authors: " + str(author))
			res.write("\n\n")
			res.write("Title: " + str(title))
			res.write("\n\n")
			res.write("Résumé: " + str(resume))
			res.write("\n\n")
			res.write("Conclusion: " + str(conclusion))
			res.write("\n\n")
			res.write("Biblio: " + str(bibliographie))
			res.write("\n\n")
			res.write("Corps:" + str(corps))
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