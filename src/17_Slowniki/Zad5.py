"""
Otrzymujesz listę par. Pierwszym elementem pary jest napis reprezentujący 
imię i nazwisko pracownika, drugim zysk z transakcji jaką dany pracownik 
przeprowadził. Znajdź pracownika, który przyniósł firmie najwięcej zysku.
"""

def pracownik_z_najwiekszym_zyskiem(lista_par):
    """
    Funkcja zwraca napis reprezentujący imię i nazwisko pracownika, który 
    przyniósł firmie najwięcej zysku.
    """

    zyski = {}
    for para in lista_par:
        if para[0] in zyski:
            zyski[para[0]] += para[1]
        else:
            zyski[para[0]] = para[1]
    
    return max(zyski, key=zyski.get)

def test_pracownik_z_najwiekszym_zyskiem():

    assert(pracownik_z_najwiekszym_zyskiem([("Barnaba Barabash", 120), ("Jon Snow", 100),("Kira Summer", 300),("Barnaba Barabash", 200), ("Bob Marley", 110)]) == "Barnaba Barabash")

if __name__ == "__main__":
    
    test_pracownik_z_najwiekszym_zyskiem()