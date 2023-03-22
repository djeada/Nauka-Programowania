"""
Otrzymujesz liste skladajaca sie wylacznie z liter A i B. 
Litera A reprezentuje samochod jadacy na wschod, a litera B 
jadacy na zachod. Samochody jadace w przeciwna strone mijaja sie. 
Policz mijajace sie samochody.
"""


def policz_samchody(lista):
    licznik = 0
    pom = 0
    for samochod in lista:
        if samochod == "A":
            pom += 1
        elif samochod == "B":
            licznik += pom

    return licznik


def test_policz_samochody():
    assert policz_samchody(["A", "B", "A", "B", "B"]) == 5
    assert (
        policz_samchody(["A", "A", "A", "B", "B", "A", "B", "A", "B", "A", "A", "A"])
        == 15
    )


if __name__ == "__main__":

    test_policz_samochody()