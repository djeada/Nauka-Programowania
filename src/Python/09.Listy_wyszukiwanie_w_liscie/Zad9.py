
'''
Znajdz element dominujacy. Inaczej znajdz lidera w liscie.
'''

import random

#Wersja 1
#bez uzycia slownika
def znajdzLideraV1(lista):
	if not lista:
		return False

	listaPomocniczna = [0]*(max(lista) + 1)
	for x in lista:
		assert(type(x) == int)
		listaPomocniczna[x] += 1
		if listaPomocniczna[x] > len(lista)//2:
			return x
	return False

#Wersja 2
#z uzyciem slownika
def znajdzLideraV2(lista):
	if not lista:
		return False

	histo = {}
	for x in lista:
		assert(type(x) == int)
		
		if x in histo:
			histo[x] += 1
		else:
			histo[x] = 1
		
		if histo[x] > len(lista)//2:
			return x
			
	return False
	
#Testy Poprawnosci
lista = [3, 5, 3, 3, 2]
assert(znajdzLideraV1(lista) == 3)
assert(znajdzLideraV2(lista) == 3)

lista = [0, 0, 2, 1, 9]
assert(not znajdzLideraV1(lista))
assert(not znajdzLideraV2(lista))

lista = []
assert(not znajdzLideraV1(lista))
assert(not znajdzLideraV2(lista))


