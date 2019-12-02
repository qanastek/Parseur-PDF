# -*- coding: utf-8 -*-

import time
import re
import os
import sys

c=os.popen('ls *.pdf').read()

os.system('rm *.txt')

splitted = c.split("\n")

if sys.argv[1] == "-t":
    out='txt'
elif sys.argv[1] == "-x":
    out='xml'
else:
    print("argument incorrect") 

for item in splitted[0:len(splitted)-1]:
	# print (item.split(".")[0])
	
	name = item.split(".")[0]

	# pdftotext -enc UTF-8 'x.pdf' 'x.txt'
	rst = "pdftotext -enc UTF-8 '%s.pdf' '%s.%s'" % (name,name,out)
	os.system(rst)

os.system('touch resultat.txt')

splitted1 = c.split("\n")

for item in splitted1[0:len(splitted)-1]:
	
	name = item.split(".")[0]
	
	#print (name)

	with open(name + ".txt", 'r') as f:

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
