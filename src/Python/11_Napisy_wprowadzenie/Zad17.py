"""
Zamien liste na napis.
"""

# Wersja 1
def zamienListeNaNapisV1(lista):
    return "".join(str(x) for x in lista)


# Testy Poprawnosci
lista = [2, 3, 10]
napis = "2310"

assert zamienListeNaNapisV1(lista) == napis

lista = ["ab", "hu", "czo"]
napis = "abhuczo"

assert zamienListeNaNapisV1(lista) == napis
