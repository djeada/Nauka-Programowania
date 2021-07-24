"""
Dla dwoch slow, ile minimalnie znakow musimy usunac aby uzyskac anagramy.
Zwroc -1 dla slow, o roznych dlugosciach.	
"""

# Wersja 1
def buduj_histogram_znakow(slowo):
    histo = {}

    for znak in slowo:
        if znak in histo:
            histo[znak] += 1
        else:
            histo[znak] = 0

    return histo


def min_znakow_do_zmiany_v1(slowo_a, slowo_b):
    if len(slowo_a) != len(slowo_b):
        return -1

    histo_slowa_a = buduj_histogram_znakow(slowo_a)
    histo_slowa_b = buduj_histogram_znakow(slowo_b)
    licznik = 0

    for klucz, wartosc in histo_slowa_a.items():
        if klucz not in histo_slowa_b.keys():
            licznik += 1
        else:
            licznik += wartosc - histo_slowa_b[klucz]

    for klucz, wartosc in histo_slowa_b.items():
        if klucz not in histo_slowa_a.keys():
            licznik += 1
        else:
            licznik += wartosc - histo_slowa_a[klucz]

    return licznik


# Testy Poprawnosci
slowo_a = "grazyna"
slowo_b = "razynax"
assert min_znakow_do_zmiany_v1(slowo_a, slowo_b) == 2

slowo_a = "pancytryna"
slowo_b = "panpomarancza"
assert min_znakow_do_zmiany_v1(slowo_a, slowo_b) == -1

slowo_a = "20ejdy0978oa"
slowo_b = "akv81w39j1o7"
assert min_znakow_do_zmiany_v1(slowo_a, slowo_b) == 10
