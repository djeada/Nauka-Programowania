'''
Znajdz i usun duplikaty z listy.
'''

#Wersja 1
def usunDuplikatyV1(lista):
	pom = []

	for x in lista:
		if x not in pom:
			pom.append(x)
			
	return pom

#Wersja 2
def usunDuplikatyV2(lista):
	return list(set(lista))

#Testy Poprawnosci
lista = [3, 5, 3, 3, 2]
wynik = [3, 5, 2]

assert(sorted(usunDuplikatyV1(lista)) == sorted(wynik))
assert(sorted(usunDuplikatyV2(lista)) == sorted(wynik))

