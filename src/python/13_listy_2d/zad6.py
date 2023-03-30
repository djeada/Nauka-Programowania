"""
Tytul: Wypisanie elementow macierzy spiralnie.
Tresc: Otrzymujesz liste list liczb naturalnych. Zbierz elementy otrzymanej macierzy spiralnie i zapisz je w liscie.
Dane wejsciowe: Lista list liczb naturalnych.
Dane wyjsciowe: Lista.
Przyklad:
Dla otrzymanej macierzy: [[1,2,3], [4,5,6], [7,8,9]], powinna zostac zwrocona lista: [1, 2, 3, 6, 9, 8, 7, 4, 5].

"""


def polacz_pokrywajace_sie_przedzialy(lista_przedzialow):
    """
    Funkcja zwraca liste niepokrywajacych sie przedzialow.
    """
    # sortujemy liste przedzialow
    lista_przedzialow.sort()

    lista_napotkanych_przedzialow = []
    lista_napotkanych_przedzialow.append(lista_przedzialow[0])

    # przechodzimy po wszystkich przedzialach i sprawdzamy czy nie nachodza na siebie
    # jesli nie to dodajemy do listy napotkanych przedzialow
    # jesli tak to sprawdzamy czy to zmieniamy poczatek przedzialu na koniec poprzedniego przedzialu

    for przedzial in lista_przedzialow:
        if przedzial[0] <= lista_napotkanych_przedzialow[-1][1]:
            lista_napotkanych_przedzialow[-1][1] = max(
                przedzial[1], lista_napotkanych_przedzialow[-1][1]
            )
        else:
            lista_napotkanych_przedzialow.append(przedzial)
    return lista_napotkanych_przedzialow


def test_polacz_pokrywajace_sie_przedzialy():
    lista_przedzialow = [
        [23, 67],
        [23, 53],
        [45, 88],
        [77, 88],
        [10, 22],
        [11, 12],
        [42, 45],
    ]
    wynik = [[10, 22], [23, 88]]
    assert polacz_pokrywajace_sie_przedzialy(lista_przedzialow) == wynik


if __name__ == "__main__":
    test_polacz_pokrywajace_sie_przedzialy()

