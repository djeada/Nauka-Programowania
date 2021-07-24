"""
Otrzymujesz dwie listy rownej dlugosci. Elementy pierwszej listy stanowia slowa, ktore nalezy podmienic na odpowiadajace im slowa z drugiej listy.
"""

import re

# Wersja 1
def zamien_ana_bv1(tekst, lista_a, lista_b):

    for napis_a, napisB in zip(lista_a, lista_b):
        tekst = re.sub(r"\b{0}\b".format(napis_a), napisB, tekst)

    return tekst


if __name__ == "__main__":

    # Testy Poprawnosci
    tekst = """Whole every miles as tiled at seven or. 
	Wished he entire esteem mr oh by.
	He prevent request by if in pleased. 
	Picture too and concern has was comfort. 
	Ten difficult resembled eagerness nor. 
	Same park bore on be. 
	Warmth his law design say are person. 
	Pronounce suspected in belonging conveying ye repulsive.
"""
    lista_a = ["or", "be", "he"]
    lista_b = ["and", "off", "she"]

    wynik = """Whole every miles as tiled at seven and. 
	Wished she entire esteem mr oh by.
	He prevent request by if in pleased. 
	Picture too and concern has was comfort. 
	Ten difficult resembled eagerness nor. 
	Same park bore on off. 
	Warmth his law design say are person. 
	Pronounce suspected in belonging conveying ye repulsive.
"""

    assert zamien_ana_bv1(tekst, lista_a, lista_b) == wynik
