"""
Zamien liste na napis.
"""

# Wersja 1
def zamien_liste_na_napis_v1(lista):
    return "".join(str(x) for x in lista)


# Testy Poprawnosci
lista = [2, 3, 10]
napis = "2310"

assert zamien_liste_na_napis_v1(lista) == napis

lista = ["ab", "hu", "czo"]
napis = "abhuczo"

assert zamien_liste_na_napis_v1(lista) == napis
