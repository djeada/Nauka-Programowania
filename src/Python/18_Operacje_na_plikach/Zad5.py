import os

"""
Wypisz nazwy plikow znajdujacych sie w folderze.
"""

# Wersja 1
def plikiWFolderze(folder):
    podFoldery = []
    pliki = []
    for item in os.listdir(folder):
        sciezka = os.path.join(folder, item)
        if os.path.isdir(sciezka):
            podFoldery.append(sciezka)
        else:
            pliki.append(sciezka)

    return podFoldery, pliki


def sciezkaDoNazwy(sciezka):
    return sciezka[sciezka.rfind(os.sep) + 1 :]


podFoldery, pliki = plikiWFolderze(os.getcwd())

if podFoldery:
    print(
        "W folderze "
        + sciezkaDoNazwy(os.getcwd())
        + "znajduja sie nastepujace podfoldery: "
    )
    for folder in podFoldery:
        print(folder)

if pliki:
    print(
        "W folderze " + sciezkaDoNazwy(os.getcwd()) + "znajduja sie nastepujace pliki: "
    )
    for plik in pliki:
        print(sciezkaDoNazwy(plik))
