"""
Otrzymujesz napis reprezentujacy sciezke pliku. Odfiltruj nazwe pliku ze sciezki.
Zwroc sama nazwe pliku, bez rozszerzen.
"""

import re


def nazwa_pliku(sciezka):
    """
    Funkcja zwraca nazwe pliku z podanej sciezki.
    """
    nazwa = re.search(r'[^\\/:*?"<>|]+$', sciezka).group(0)

    # usun rozszerzenie pliku
    while re.sub(r'\.[^.]+$', '', nazwa) is not nazwa:
        nazwa = re.sub(r'\.[^.]+$', '', nazwa)
    return nazwa


def test_nazwa_pliku():
    assert nazwa_pliku("C:\\Windows\\explorer.exe") == "explorer"
    assert nazwa_pliku("/home/user/var/log/syslog") == "syslog"
    assert nazwa_pliku("test.jpg.png.mp3.mp5.html.txt") == "test"
    assert nazwa_pliku("test") == "test"


if __name__ == "__main__":
    test_nazwa_pliku()
