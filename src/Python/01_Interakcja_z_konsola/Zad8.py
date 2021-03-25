"""
Otrzymujesz cene oraz wymiary pojedynczej plytki. Oblicz ile bedzie wynosila cena
za podloge o podanych wymiarach. Podloga jest prostokatem, a plytka kwadratem
"""

if __name__ == "__main__":

    print("podaj: cene plytki, dlugosc boku plytki i wymiary podlogi")

    cena = int(input())
    bokPlytki = int(input())
    szerokoscPodlogi = int(input())
    dlugoscPodlogi = int(input())

    szerokoscKonieczna = szerokoscPodlogi + bokPlytki - szerokoscPodlogi % bokPlytki
    dlugoscKonieczna = dlugoscPodlogi + bokPlytki - dlugoscPodlogi % bokPlytki

    polePlytki = bokPlytki ** 2
    polePodlogi = szerokoscKonieczna * dlugoscKonieczna

    calkowityKoszt = cena * polePodlogi // polePlytki

    print(
        "Dla plytki o dlugosci boku ",
        bokPlytki,
        "i ceny ",
        cena,
        " calkowity koszt wylozenia podlogi o wymiarach ",
        szerokoscPodlogi,
        "x",
        dlugoscPodlogi,
        " wynosi ",
        calkowityKoszt,
    )
