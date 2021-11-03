"""
Otrzymujesz listę par liczb. Liczby w parze reprezentują początek i koniec przedziału. 
Niektóre przedziały mogą na siebie nachodzić. W takim przypadku połącz je ze sobą 
i zwróć listę niepokrywających się przedziałów.
"""

def polacz_pokrywajace_sie_przedzialy(lista_przedzialow):
    """
    Funkcja zwraca listę niepokrywających się przedziałów.
    """
    # sortujemy listę przedziałów
    lista_przedzialow.sort()

    lista_napotkanych_przedzialow = []
    lista_napotkanych_przedzialow.append(lista_przedzialow[0])

    # przechodzimy po wszystkich przedziałach i sprawdzamy czy nie nachodza na siebie
    # jeśli nie to dodajemy do listy napotkanych przedziałów
    # jeśli tak to sprawdzamy czy to zmieniamy początek przedziału na koniec poprzedniego przedziału

    for przedzial in lista_przedzialow:
        if przedzial[0] <= lista_napotkanych_przedzialow[-1][1]:
            lista_napotkanych_przedzialow[-1][1] = max(przedzial[1], lista_napotkanych_przedzialow[-1][1])
        else:
            lista_napotkanych_przedzialow.append(przedzial)
    return lista_napotkanych_przedzialow

 
def test_polacz_pokrywajace_sie_przedzialy():
    lista_przedzialow = [[23, 67], [23, 53], [45, 88], [77, 88], [10, 22], [11, 12], [42, 45]]
    wynik = [[10, 22], [23, 88]]
    assert polacz_pokrywajace_sie_przedzialy(lista_przedzialow) == wynik


if __name__ == "__main__":
    test_polacz_pokrywajace_sie_przedzialy()
