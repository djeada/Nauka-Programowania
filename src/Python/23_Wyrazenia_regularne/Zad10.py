"""
Otrzymujesz dwie listy rownej dlugosci. Elementy pierwszej listy stanowia slowa, ktore nalezy podmienic na odpowiadajace im slowa z drugiej listy.
"""

import re

# Wersja 1
def zamienAnaBV1(tekst, listaA, listaB):

    for napisA, napisB in zip(listaA, listaB):
        tekst = re.sub(r"\b{0}\b".format(napisA), napisB, tekst)

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
    listaA = ["or", "be", "he"]
    listaB = ["and", "off", "she"]

    wynik = """Whole every miles as tiled at seven and. 
	Wished she entire esteem mr oh by.
	He prevent request by if in pleased. 
	Picture too and concern has was comfort. 
	Ten difficult resembled eagerness nor. 
	Same park bore on off. 
	Warmth his law design say are person. 
	Pronounce suspected in belonging conveying ye repulsive.
"""

    assert zamienAnaBV1(tekst, listaA, listaB) == wynik
