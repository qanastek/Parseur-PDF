from bs4 import BeautifulSoup
import re
import os



file = "test.html"

htmlData = open(file,encoding="utf8")

soup = BeautifulSoup(htmlData, "html.parser")

font_spans = soup.find_all("span", attrs={"style":re.compile("font-size:1[1-3]px")})


if(font_spans and font_spans!=[]):
	print( font_spans[0].text,font_spans[1].text,font_spans[2].text )
else:
	print(soup.find_all("span")[3:6].text)