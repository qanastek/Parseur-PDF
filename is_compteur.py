import time


start_time = time.time()

path = './Papers/fichierTest.txt'

for i in range(1):
	somme = 0
	with open(path, 'r') as f:
		data = f.read()
		somme = data.count('is')
print(somme)


print("--- %s seconds ---" % (time.time() - start_time))
