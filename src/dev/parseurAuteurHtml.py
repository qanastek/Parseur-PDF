from bs4 import BeautifulSoup
import re
import os







file = "../../corpus/Lin_2004_Rouge.html"

htmlData = open(file, 'r')

soup = BeautifulSoup(htmlData, "html.parser")

font_spans = [ data for data in soup.select('span') if 'font-size:12px' in str(data) ]



print( font_spans )