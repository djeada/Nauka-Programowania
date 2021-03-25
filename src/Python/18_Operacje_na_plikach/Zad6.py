"""
Znajdz wszystkie pliki tekstowe (rozszerzenie .txt) znajdujace sie w podanym folderze, badz w podfolderach. W znalezionych plikach podmien litery 'a' na litery 'x'.
"""

import os

# Wersja 1
szukanyNapis = "a"
napisDoPodmiany = "x"
rozszerzenie = ".txt"
folder = os.getcwd()


def plikiWFolderze(folder):
    pliki = []
    for item in os.listdir(folder):
        sciezka = os.path.join(folder, item)
        if not os.path.isdir(sciezka):
            pliki.append(sciezka)

    return pliki


def modyfikujPlik(plik, szukanyNapis, napisDoPodmiany):
    with open(plik, "r") as otwartyPlik:
        dane = otwartyPlik.read()

    with open(plik, "w") as otwartyPlik:
        otwartyPlik.write(dane.replace(szukanyNapis, napisDoPodmiany))


def znajdzOrazModyfikuj(folder, rozszerzenie, szukanyNapis, napisDoPodmiany):
    for plik in plikiWFolderze(folder):
        if rozszerzenie in plik:
            modyfikujPlik(plik, szukanyNapis, napisDoPodmiany)


znajdzOrazModyfikuj(folder, rozszerzenie, szukanyNapis, napisDoPodmiany)
