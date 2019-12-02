import os

c=os.popen('ls *.pdf').read()

os.system('rm *.txt')

splitted = c.split("\n")

for item in splitted[0:len(splitted)-1]:
	# print (item.split(".")[0])
	
	string=item.split(".")[0]

	rst="pdftotext -layout -enc UTF-8 "+"'"+item+"'"+" "+"'"+string+".txt"+"'"
	os.system(rst)
