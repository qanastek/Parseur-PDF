# -*- coding: utf-8 -*-

import time

path = 'fichierTest.txt'

somme = 0
ligne = 0
word = 0

for i in range(10000):

	with open(path, 'r') as f:
		data = f.read()
		somme += data.count('is')
		word += len(data.split(" "))
		ligne += data.count('\n')

print(somme)
print(word)
print(ligne)