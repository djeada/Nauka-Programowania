
"""
Otrzymujesz listę list liczb naturalnych. Obróć otrzymaną listę o 90 stopni. 
Tzn. zamień miejscami ostatnią kolumnę z ostatnim wierszem, przedostatnią 
kolumnę z przedostatnim wierszem itd.
"""

def obroc_o_90(macierz):
    """
    Funkcja obraca macierz o 90 stopni.
    """
    
    if len(macierz) != len(macierz[0]):
        raise ValueError("Macierz nie jest kwadratowa")
    
    n = len(macierz)

    for i in range(n//2 +1):
        ostatni = n - 1 - i

        for j in range(i + 1, ostatni):
            pom = macierz[i][j]
            macierz[i][j] = macierz[n - 1 - j][i]
            macierz[n - 1 - j][i] = macierz[n - 1 - i][n - 1 - j]
            macierz[n - 1 - i][n - 1 - j] = macierz[j][n - 1 - i]
            macierz[j][n - 1 - i] = pom
    
        pom = macierz[i][i]
        macierz[i][i] = macierz[n - 1 - i][i]
        macierz[n - 1 - i][i] = macierz[n - 1 - i][n - 1 - i]
        macierz[n - 1 - i][n - 1 - i] = macierz[i][n - 1 - i]
        macierz[i][n - 1 - i] = pom

    return macierz
    
def test_obroc_o_90():
    macierz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    wynik = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert obroc_o_90(macierz) == wynik

if __name__ == "__main__":
    
    test_obroc_o_90()
