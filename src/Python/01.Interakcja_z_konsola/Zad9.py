
'''
Otrzymujesz roczna stope procentowa, liczbe lat na splacenie kredytu oraz wysokosc
udzielonego kredytu. Oblicz miesieczna rate oraz calkowity koszt kredytu.
''' 

print("podaj stope procentowa, liczbe lat oraz wysokosc udzielonego kredytu")

stopa = int(input())
lat = int(input())
kredyt = int(input())

print(kredyt * ((1 + stopa) ^ lat)/(12 * lat))


