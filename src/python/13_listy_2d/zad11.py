"""
Tytul: Macierz z parami elementow odpowiadajacych sobie z dwoch list.
Tresc: Dla otrzymanych dwoch list, stworz dwukolumnowa macierz, ktorej pierwsza kolumna sklada sie z elementow pierwszej listy, a druga kolumna z elementow drugiej listy. Jesli otrzymane listy nie sa rownej dlugosci, zwroc pusta macierz.
Dane wejsciowe: Dwie listy.
Dane wyjsciowe: Lista list liczb naturalnych lub pusta macierz (w przypadku nierownych dlugosci list).
Przyklad:
Dla otrzymanych dwoch list: [3, 5, 2] oraz [2, 8, 1], powinna zostac zwrocona macierz: [[3, 2], [5, 8], [2, 1]

"""

import enum
import random

class Stale(enum.Enum):
    """
    Stale uzywane do reprezentacji stanu gry na planszy.
    """

    puste_pule = enum.auto()
    statek = enum.auto()

class Symbole:
    """
    Klasa definiujaca znaki wykorzystywane w grze.
    """

    puste_pule = "."
    statek = "$"
    chybiony_statek = "o"
    zatopiony_statek = "x"

def inicjalizuj_plansze(znak, n=10):
    """
    Funkcja inicjalizujaca plansze gry.
    """
    plansza = []
    for i in range(n):
        plansza.append([])
        for _ in range(n):
            plansza[i].append(znak)
    return plansza

def rysuj_plansze(plansza_gracza):
    """
    Funkcja rysujaca plansze.
    """
    print("   ", end="")
    for i in range(len(plansza_gracza)):
        print(i, end=" ")
    print()

    for i in range(len(plansza_gracza)):
        print(i, end=" ")
        for j in range(len(plansza_gracza)):
            print(plansza_gracza[i][j], end=" ")
        print()

def rysuj_obie_plansze(plansza_gracza, widoczna_plansza_komputera):
    """
    Funkcja rysujaca plansze.
    """

    # on left side plasza_gracza
    # on right side widoczna_plansza_komputera
    # indices shown on the top and left side of the board

    print("   ", end="")
    for i in range(len(plansza_gracza)):
        print(i, end=" ")
    print()

    for i in range(len(plansza_gracza)):
        print(i, end=" ")
        for j in range(len(plansza_gracza)):
            print(plansza_gracza[i][j], end=" ")
        print(widoczna_plansza_komputera[i], end=" ")
        print()

def rozmiesc_statki_komputera(plansza):
    """
    Funkcja rozmieszczajaca statki na planszy.
    """

    def losuj_wspolrzedne(plansza, rozmiar_statku):
        """
        Funkcja losujaca wspolrzedne na planszy.
        """
        kierunek = random.randint(0, 1)

        if kierunek == 0:
            x = random.randint(0, len(plansza) - 1 - rozmiar_statku)
            y = random.randint(0, len(plansza) - 1)
        else:
            x = random.randint(0, len(plansza) - 1)
            y = random.randint(0, len(plansza) - 1 - rozmiar_statku)

        while plansza[x][y] != Stale.puste_pule:
            # losujemy wspolrzedne zanim znajdziemy puste pole
            # wspolrzedne musza byc w zakresie planszy
            # wspolrzedne musza uwzglednic rozmiar statku
            # jesli kierunek == 0 to statki musza sie rozmieszac w pionie i x musi byc w zakresie planszy - rozmiar statku
            # jesli kierunek == 1 to statki musza sie rozmieszac w poziomie i y musi byc w zakresie planszy - rozmiar statku

            if kierunek == 0:
                x = random.randint(0, len(plansza) - 1 - rozmiar_statku)
                y = random.randint(0, len(plansza) - 1)
            else:
                x = random.randint(0, len(plansza) - 1)
                y = random.randint(0, len(plansza) - 1 - rozmiar_statku)

        if kierunek == 0:
            for i in range(rozmiar_statku):
                print(x + i, y, kierunek)
                plansza[x + i][y] = Stale.statek
        else:
            for i in range(rozmiar_statku):
                print(x, y + i, kierunek)
                plansza[x][y + i] = Stale.statek

    statki = {1: 5, 2: 3, 3: 2, 4: 1}
    liczba_statkow_do_rozmieszczenia = sum(statki.values())

    while liczba_statkow_do_rozmieszczenia > 0:
        for rozmiar_statku in statki:
            while statki[rozmiar_statku] > 0:
                losuj_wspolrzedne(plansza, rozmiar_statku)
                statki[rozmiar_statku] -= 1
                liczba_statkow_do_rozmieszczenia -= 1

    return plansza

def rozmiesc_statki_gracza(plansza):
    """
    Funkcja realziujaca rozmieszczenie statkow gracza. Gracz pytany jest o podanie wspolrzednych dla swoich statkow.
    """

    def podaj_wspolrzedne(plansza, rozmiar_statku):
        """
        Funkcja pobierajaca wspolrzedne statku.
        """
        rysuj_plansze(plansza)
        print(f"Masz do umieszczenia statki o rozmiarze: {rozmiar_statku}")
        print("Pamietaj, nie mozna umieszczac statku na ukos.")

        x_poczatkowe = int(input("Podaj wspolrzedna x poczatkowa: "))
        y_poczatkowe = int(input("Podaj wspolrzedna y poczatkowa: "))

        x_koncowe = (
            int(input("Podaj wspolrzedna x koncowa: "))
            if rozmiar_statku != 1
            else x_poczatkowe
        )
        y_koncowe = (
            int(input("Podaj wspolrzedna y koncowa: "))
            if rozmiar_statku != 1
            else y_poczatkowe
        )

        # napraw kolejnosc wspolrzednych
        if x_poczatkowe > x_koncowe:
            x_poczatkowe, x_koncowe = x_koncowe, x_poczatkowe
        if y_poczatkowe > y_koncowe:
            y_poczatkowe, y_koncowe = y_koncowe, y_poczatkowe

        # sprawdz czy wspolrzedne wychodza poza plansze
        if (
            x_poczatkowe < 0
            or y_poczatkowe < 0
            or x_koncowe > len(plansza) - 1
            or y_koncowe > len(plansza) - 1
        ):
            print("Podane wspolrzedne wychodza poza plansze.")
            return False

        # sprawdz czy wspolrzedne pasuja do rozmiaru statku
        if not (
            (
                x_koncowe - x_poczatkowe + 1 == rozmiar_statku
                and y_koncowe == y_poczatkowe
            )
            or (
                y_koncowe - y_poczatkowe + 1 == rozmiar_statku
                and x_koncowe == x_poczatkowe
            )
        ):
            print("Wspolrzedne statku nie pasuja do rozmiaru statku.")
            return False

        # sprawdz czy wszystkie pola miedzy podanymi wspolrzednymi sa puste
        for i in range(x_poczatkowe, x_koncowe + 1):
            for j in range(y_poczatkowe, y_koncowe + 1):
                if plansza[i][j] != Symbole.puste_pule:
                    print("Jakis statek znajduje sie na podanych wspolrzednych.")
                    return False

        # zapis wspolrzednych statku
        for i in range(x_poczatkowe, x_koncowe + 1):
            for j in range(y_poczatkowe, y_koncowe + 1):
                plansza[i][j] = Symbole.statek

        return True

    statki = {1: 5, 2: 3, 3: 2, 4: 1}
    liczba_statkow_do_rozmieszczenia = sum(statki.values())

    while liczba_statkow_do_rozmieszczenia > 0:
        for rozmiar_statku in statki:
            while statki[rozmiar_statku] > 0:
                if podaj_wspolrzedne(plansza, rozmiar_statku):
                    statki[rozmiar_statku] -= 1
                    liczba_statkow_do_rozmieszczenia -= 1

    return plansza

def ruch_uzytkownika(widoczna_plansza_komputera, ukryta_plansza_komputera):
    """
    Funkcja wykonujaca ruch uzytkownika.
    """
    x = int(input("Podaj wiersz: "))
    y = int(input("Podaj kolumne: "))
    if ukryta_plansza_komputera[x][y] == Stale.statek:
        widoczna_plansza_komputera[x][x] = Symbole.zatopiony_statek
        print("Trafiony!")
    else:
        widoczna_plansza_komputera[x][y] = Symbole.chybiony_statek
        print("Pudlo!")

def ruch_komputera(plansza_gracza):
    """
    Funkcja wykonujaca ruch komputera.
    """
    x = random.randint(0, len(plansza_gracza) - 1)
    y = random.randint(0, len(plansza_gracza) - 1)
    if plansza_gracza[x][y] == Symbole.statek:
        plansza_gracza[x][y] = Symbole.zatopiony_statek
    else:
        plansza_gracza[x][y] = Symbole.chybiony_statek

def sprawdz_czy_gracz_wygral(widoczna_plansza_komputera, ukryta_plansza_komputera):
    """
    Funkcja sprawdzajaca czy wygral gracz.
    """
    return widoczna_plansza_komputera.count(
        Symbole.zatopiony_statek
    ) == ukryta_plansza_komputera.count(Stale.statek)

def sprawdz_czy_komputer_wygral(plansza_gracza):
    """
    Funkcja sprawdzajaca czy wygral komputer.
    """
    return plansza_gracza.count(Symbole.statek) == 0

def gra():
    """
    Funkcja rozpoczynajaca gre.
    """
    plansza_gracza = inicjalizuj_plansze(Symbole.puste_pule)
    # plansza_gracza = rozmiesc_statki_gracza(plansza_gracza)

    widoczna_plansza_komputera = inicjalizuj_plansze(Symbole.puste_pule)
    ukryta_plansza_komputera = inicjalizuj_plansze(Stale.puste_pule)
    ukryta_plansza_komputera = rozmiesc_statki_komputera(ukryta_plansza_komputera)

    while not sprawdz_czy_komputer_wygral(
        widoczna_plansza_komputera
    ) and not sprawdz_czy_gracz_wygral(
        widoczna_plansza_komputera, ukryta_plansza_komputera
    ):
        rysuj_obie_plansze(widoczna_plansza_komputera, ukryta_plansza_komputera)
        ruch_uzytkownika(widoczna_plansza_komputera, ukryta_plansza_komputera)
        ruch_komputera(plansza_gracza)

    if sprawdz_czy_komputer_wygral(widoczna_plansza_komputera):
        print("Wygral komputer!")

    else:
        print("Wygral gracz!")

if __name__ == "__main__":

    gra()

