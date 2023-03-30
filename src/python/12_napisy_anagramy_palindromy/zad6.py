"""
Tytul: Permutacje slowa, ktore sa palindromami.
Tresc: Napisz program, ktory znajdzie permutacje danego slowa, ktore sa palindromami.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla otrzymanego napisu: “taco”, powinna zostac zwrocona lista: ["taco", "toca"].

"""

def permutacje(napis):
    """
    Funkcja zwraca liste wszystkich permutacji danego napisu.
    """
    if len(napis) == 1:
        return [napis]
    else:
        permutacje = []
        for i in range(len(napis)):
            for permutacja in permutacje(napis[:i] + napis[i + 1 :]):
                permutacje.append(napis[i] + permutacja)
        return permutacje

def czy_palindrom(napis):
    """
    Funkcja sprawdza czy dany napis jest palindromem.
    """
    return napis == napis[::-1]

def permutacje_palindromiczne(napis):
    """
    Funkcja zwraca liste wszystkich permutacji danego napisu, ktore sa palindromami.
    """
    return [permutacja for permutacja in permutacje(napis) if czy_palindrom(permutacja)]

def test_permutacje_palindromiczne():
    assert sorted(permutacje_palindromiczne("adamm")) == sorted(["madam", "amdma"])

if __name__ == "__main__":
    test_permutacje_palindromiczne()

