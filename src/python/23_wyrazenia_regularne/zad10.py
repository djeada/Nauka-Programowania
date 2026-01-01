"""
ZAD-10 — Podmień napisy z listy A na napisy z listy B

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `zamiana`

### Treść

Otrzymujesz:

* tekst,
* listę A (napisy do znalezienia),
* listę B (napisy do podmiany), tej samej długości co A.

Zastąp w tekście wszystkie wystąpienia słów z listy A odpowiadającymi im słowami z listy B (ten sam indeks). Zamieniaj tylko **całe słowa**, nie fragmenty innych słów.

### Wejście

1. Tekst (jedna lub wiele linii)
2. Liczba naturalna `n` — długość list
3. `n` wierszy: elementy listy A
4. `n` wierszy: elementy listy B

### Wyjście

Zmodyfikowany tekst.

### Przykład

*(jak w treści — z listami A/B)*

"""

import re


def zamien_a_na_b(tekst, lista_a, lista_b):
    """
    Funkcja zamienia w tekscie napisy z listy_a na napisy z listy_b.
    """

    for napis_a, napis_b in zip(lista_a, lista_b):
        tekst = re.sub(r"\b{0}\b".format(napis_a), napis_b, tekst)

    return tekst


def test_zamien_a_na_b():
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

    oczekiwane = """Whole every miles as tiled at seven and. 
	Wished she entire esteem mr oh by.
	He prevent request by if in pleased. 
	Picture too and concern has was comfort. 
	Ten difficult resembled eagerness nor. 
	Same park bore on off. 
	Warmth his law design say are person. 
	Pronounce suspected in belonging conveying ye repulsive.
"""

    assert zamien_a_na_b(tekst, lista_a, lista_b) == oczekiwane


if __name__ == "__main__":
    test_zamien_a_na_b()
