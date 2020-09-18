'''
Znajdz w macierzy klepsydre o najwiekszej sumie.
'''

import random

#Wersja 1
def maksKlepsydra(macierz):
	maks = -float('Inf')
	
	for wiersz in range(len(macierz)):
		assert(len(wiersz) == len(macierz))
		for kolumna in wiersz:
			 if not (wiersz == 0 or wiersz == len(macierz) - 1 or kolumna == 0 or kolumna == len(macierz) - 1):
			 	maks = max(maks, (macierz[wiersz - 1][kolumna - 1] + macierz[wiersz - 1][kolumna]+ macierz[wiersz-1][kolumna + 1] + macierz[wiersz][kolumna] + macierz[wiersz + 1][kolumna - 1] + macierz[wiersz + 1][kolumna] + macierz[wiersz + 1][kolumna + 1]))
           		
	return maks
     
#Testy Poprawnosci
N = 5
macierz = [[random.randint(0, 100) for i in range(N)] for j in range(N)]
print(macierz)
print(maksKlepsydra(macierz))
