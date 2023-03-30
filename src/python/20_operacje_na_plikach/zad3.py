"""
Tytul: Statystyki dla pliku tekstowego.
Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do pliku tekstowego. Oblicz:
a) Liczbe wierszy w pliku.
b) Liczbe slow w pliku (slowa oddzielone sa spacjami i moga skladac sie wylacznie z liter).
c) Srednia dlugosc wiersza.
d) Srednia liczbe slow na wiersz.
e) Czestosc wystepowania kazdego ze slow w pliku.
Dane wejsciowe: Napis reprezentujacy sciezke do pliku.
Dane wyjsciowe:
a) Liczba naturalna reprezentujaca liczbe wierszy.
b) Liczba naturalna reprezentujaca liczbe slow.
c) Liczba zmiennoprzecinkowa reprezentujaca srednia dlugosc wiersza.
d) Liczba zmiennoprzecinkowa reprezentujaca srednia liczbe slow na wiersz.
e) Slownik par: napis (slowo), liczba naturalna (czestotliwosc wystepowania slowa).
Przyklad:
Dla otrzymanego napisu: "C:\Users\Username\Documents\text_file.txt" powinno zostac zwrocone:
a) Liczba naturalna reprezentujaca liczbe wierszy, np. 6
b) Liczba naturalna reprezentujaca liczbe slow, np. 25
c) Liczba zmiennoprzecinkowa reprezentujaca srednia dlugosc wiersza, np. 41.5
d) Liczba zmiennoprzecinkowa reprezentujaca srednia liczbe slow na wiersz, np. 4.2
e) Slownik par: napis (slowo), liczba naturalna (czestotliwosc wystepowania slowa): {'The': 2, 'quick': 2, 'brown': 2, 'fox': 2, 'jumped': 1, 'over': 1, 'the': 1, 'lazy': 1, 'dog.': 1, 'cat': 1, 'sat': 1, 'on': 1, 'mat.': 1, 'Foxes': 1, 'are': 1, 'known': 1, 'for': 1, 'their': 2, 'cunning': 1, 'and': 1, 'intelligence.': 1, 'Dogs': 1, 'loyalty': 1, 'kindness.': 1, 'Cats': 1, 'independent': 1, 'animals': 1, 'but': 1, 'can': 1, 'be': 1, 'affectionate.': 1, 'This': 1, 'text': 1, 'file': 1, 'contains': 1, 'ten': 1, 'lines': 1, 'and': 1, 'words.': 1}
Tekst pliku:
"The quick brown fox jumped over the lazy dog.
The quick brown cat sat on the mat.
Foxes are known for their cunning and intelligence.
Dogs are known for their loyalty and kindness.
Cats are independent animals but can be affectionate.
This text file contains six lines and 25 words."

"""

import pathlib

def znajdz_sciezki(nazwa_pliku):
    """
    Funkcja zwraca liste sciezek do plikow o podanej nazwie.
    """
    sciezki = []
    for plik in pathlib.Path.home().glob("**/*"):
        if plik.name == nazwa_pliku:
            sciezki.append(str(plik.absolute()))
    return sciezki

def test_znajdz_sciezki():

    # stworz foldery testowe
    sciezka1 = "test"
    sciezka2 = "test/test1"
    sciezka3 = "test/test2"
    pathlib.Path(sciezka1).mkdir()
    pathlib.Path(sciezka2).mkdir()
    pathlib.Path(sciezka3).mkdir()

    # utworz pliki testowe
    nazwa_pliku = "test.txt"
    plik_1 = pathlib.Path(f"{sciezka1}/{nazwa_pliku}")
    plik_1.touch()
    plik_2 = pathlib.Path(f"{sciezka2}/{nazwa_pliku}")
    plik_2.touch()
    plik_3 = pathlib.Path(f"{sciezka3}/{nazwa_pliku}")
    plik_3.touch()

    wynik = znajdz_sciezki(nazwa_pliku)
    assert str(plik_1.absolute()) in wynik
    assert str(plik_2.absolute()) in wynik
    assert str(plik_3.absolute()) in wynik

    # usun foldery testowe
    import shutil

    shutil.rmtree(sciezka1)

if __name__ == "__main__":
    test_znajdz_sciezki()

