# -*- coding: utf-8 -*-

import time
import re
import os
import sys

if len(sys.argv) != 2:
	sys.exit("Erreur argument manquant !")

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

	# for line in data.split('\n'):
		
	# 	if not bool(re.search(r'\d', line)):
    			
	# 		return line


rm = "rm *.txt"
os.system(rm)

# Delete spaces from file names
os.system("""
for file in *.pdf; do mv "$file" "$(echo $file | sed 's/ /_/g')"; done
""")

ls = "ls *.pdf"
c = os.popen(ls).read()

splitted = c.split("\n")

if sys.argv[1] == "-t":
    out='txt'
elif sys.argv[1] == "-x":
    out='xml'
else:
    print("argument incorrect") 

# Convert each PDF to TXT
for name in splitted[0:-1]:

	nameRaw = name.split(".")[0]

	# pdftotext -enc UTF-8 'x.pdf' 'x.txt'
	rst = "pdftotext -enc UTF-8 '%s' '%s.%s'" % (name,nameRaw,out)
	# print(rst)
	os.system(rst)

os.system('touch resultat.txt')

# Summarize
for item in splitted[0:-1]:
	
	name = item.split(".")[0]

	# For each converted PDF
	with open(name + ".txt", 'r') as f:

		data = f.read()

		title = getTitle(data)
		resume = getResume(data)

		# Write in the file
		with open("resultat.txt", 'a') as res:
			res.write("\n")
			res.write("File name: " + name)
			res.write("\n\n")
			res.write("Title: " + title)
			res.write("\n\n")
			res.write("Résumé: " + resume)
			res.write("\n\n-------------------------------------------------------------\n")
		res.close()

	f.close()
