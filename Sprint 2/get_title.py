import os
import sys


file_name = sys.argv[1]
if(os.path.exists(file_name)):
	print file_name
	os.system("pdftotext -layout "+file_name)
	txt_file = file_name[:-3]+"txt"
	f= open( txt_file )
	f1 = f.readlines()
	print(f1[:3])
	



else:
	print('file doesnt exist')

