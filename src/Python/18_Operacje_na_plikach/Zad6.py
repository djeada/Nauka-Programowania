"""
Znajdz wszystkie pliki tekstowe (rozszerzenie .txt) znajdujace sie w podanym folderze, badz w podfolderach. W znalezionych plikach podmien litery 'a' na litery 'x'.
"""

import os

# Wersja 1
szukany_napis = "a"
napis_do_podmiany = "x"
rozszerzenie = ".txt"
folder = os.getcwd()


def pliki_w_folderze(folder):
    pliki = []
    for item in os.listdir(folder):
        sciezka = os.path.join(folder, item)
        if not os.path.isdir(sciezka):
            pliki.append(sciezka)

    return pliki


def modyfikuj_plik(plik, szukany_napis, napis_do_podmiany):
    with open(plik, "r") as otwartyPlik:
        dane = otwartyPlik.read()

    with open(plik, "w") as otwartyPlik:
        otwartyPlik.write(dane.replace(szukany_napis, napis_do_podmiany))


def znajdz_oraz_modyfikuj(folder, rozszerzenie, szukany_napis, napis_do_podmiany):
    for plik in pliki_w_folderze(folder):
        if rozszerzenie in plik:
            modyfikuj_plik(plik, szukany_napis, napis_do_podmiany)


znajdz_oraz_modyfikuj(folder, rozszerzenie, szukany_napis, napis_do_podmiany)
