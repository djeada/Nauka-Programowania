import os

"""
Wypisz nazwy plikow znajdujacych sie w folderze.
"""

# Wersja 1
def pliki_w_folderze(folder):
    pod_foldery = []
    pliki = []
    for item in os.listdir(folder):
        sciezka = os.path.join(folder, item)
        if os.path.isdir(sciezka):
            pod_foldery.append(sciezka)
        else:
            pliki.append(sciezka)

    return pod_foldery, pliki


def sciezka_do_nazwy(sciezka):
    return sciezka[sciezka.rfind(os.sep) + 1 :]


podFoldery, pliki = pliki_w_folderze(os.getcwd())

if podFoldery:
    print(
        "W folderze "
        + sciezka_do_nazwy(os.getcwd())
        + "znajduja sie nastepujace podfoldery: "
    )
    for folder in podFoldery:
        print(folder)

if pliki:
    print(
        "W folderze "
        + sciezka_do_nazwy(os.getcwd())
        + "znajduja sie nastepujace pliki: "
    )
    for plik in pliki:
        print(sciezka_do_nazwy(plik))
