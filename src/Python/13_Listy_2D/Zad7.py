"""
Otrzymujesz liste par liczb. Liczby w parze reprezentuja poczatek i koniec przedzialu. 
Niektore przedzialy moga na siebie nachodzic. 
W takim przypadku polacz je ze soba i zwroc liste niepokrywajacych sie przedzialow.
"""

# Wersja 1
def polaczPrzedzialyV1(lista):
    lista = sorted(lista)
    wynik = []
    pocz, koniec = lista[0][0], lista[0][1]

    for x in lista[1:]:
        if koniec >= x[0]:
            if koniec < x[1]:
                koniec = x[1]

        else:
            wynik.append((pocz, koniec))
            pocz, koniec = x[0], x[1]

    wynik.append((pocz, koniec))

    return wynik


# Testy Poprawnosci
lista = [(23, 67), (23, 53), (45, 88), (77, 88), (10, 22), (11, 12), (42, 45)]
wynik = [(10, 22), (23, 88)]

assert polaczPrzedzialyV1(lista) == wynik
