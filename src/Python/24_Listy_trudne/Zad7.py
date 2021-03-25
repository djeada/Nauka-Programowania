"""
Ile wody znajduje sie miedzy slupkami?
Lista reprezentuje wysokosci slupkow.
"""

# Zlozonosc czasowa O(n)
# Zlozonosc obliczeniowa O(n)
# Znajdz najwyzsze graniczne slupki
# Ilosc wody rowna sie mniejszemu z dwoch granicznych slupkow minus wysokosci aktualnego
def ileWodyV1(slupki):

    n = len(slupki)
    woda = 0

    lewy = [float("-inf")]

    for i in range(n):
        lewy.append(max(lewy[i], slupki[i]))

    prawy = float("-inf")

    for i in range(n - 1, -1, -1):
        prawy = max(prawy, slupki[i])

        if min(lewy[i], prawy) > slupki[i]:
            woda += min(lewy[i], prawy) - slupki[i]

    return woda


if __name__ == "__main__":

    slupki = [3, 0, 1, 0, 2]
    wynik = 5

    assert ileWodyV1(slupki) == wynik
