"""
Policz mijajace sie samochody.
Otrzymujesz liste skladajaca sie z ciagu liter A i B. Litery A reprezentuja samochod jadacy na wschod, a litery B jadacy na zachod. 
"""

# Wersja 1
def policzSamochodyV1(lista):

    licznik = 0
    for i in range(len(lista)):
        if lista[i] == "A":
            for j in range(i + 1, len(lista)):
                if lista[j] == "B":
                    licznik += 1

        elif lista[i] == "B":
            for j in range(i - 1, -1, -1):
                if lista[j] == "A":
                    licznik += 1

    return licznik // 2


# Wersja 2
def policzSamochodyV2(lista):
    licznik = 0
    pom = 0

    for x in lista:
        if x == "A":
            pom += 1

        elif x == "B":
            licznik += pom

    return licznik


# Testy Poprawnosci
lista = ["A", "B", "A", "B", "B"]
wynik = 5

assert policzSamochodyV1(lista) == wynik
assert policzSamochodyV2(lista) == wynik

lista = ["A", "A", "A", "B", "B", "A", "B", "A", "B", "A", "A", "A"]
wynik = 15

assert policzSamochodyV1(lista) == wynik
assert policzSamochodyV2(lista) == wynik
