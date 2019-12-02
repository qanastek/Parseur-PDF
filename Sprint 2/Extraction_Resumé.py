# -*- coding: utf-8 -*-

import time

import os

c=os.popen('ls *.pdf').read()

os.system('rm *.txt')
os.system('touch resultat.txt')

splitted = c.split("\n")


for item in splitted[0:len(splitted)-1]:
	
	name = item.split(".")[0]

	rst = "pdftotext -enc UTF-8 "+"'"+item+"'"+" "+"'"+name+".txt"+"'"
	os.system(rst)

	with open(name + ".txt", 'r') as f:

		data = f.read()

		splitted = data.split("Abstract")[1]

		splitted2 = splitted.split(".\n\n")[0]
		

		with open("resultat.txt", 'a') as res:
			res.write(name)
			res.write("\n")
			res.write(splitted2)
			res.write("\n")
			res.write("---------------------------------------------------------------------")
			res.write("\n")
		res.close()

	f.close()