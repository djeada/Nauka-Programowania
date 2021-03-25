#include <cassert>
#include <limits>
#include <vector>

//Otrzymujesz liste 2d. Znajdz w niej klepsydre o najwiekszej sumie.
//Klepsydra sklada sie z dokladnie 7 elementow. Trzy pierwsze elementy
//są kolejnymi elementami dowolnego wiersza listy 2d. Nastepny element
//znajduje sie w tej samej kolumnie co drugi element i w dokladnie
//jednym wierszu nizej. Trzy nastepne znajduja sie w tych samych
//kolumnach co trzy pierwsze i dokladnie dwie wiersze nizej.

int klepsydraV1(std::vector<std::vector<int>>& macierz)
{
    int wynik = __WINT_MIN__;

    int N = macierz.size();

    for (int wiersz = 0; wiersz < N; wiersz++) {
        for (int kolumna = 0; kolumna < N; kolumna++) {
            if (!(wiersz == 0 || wiersz == N - 1 || kolumna == 0 || kolumna == N - 1))
                wynik = std::max(wynik, (macierz[wiersz - 1][kolumna - 1] + macierz[wiersz - 1][kolumna] + macierz[wiersz - 1][kolumna + 1] + macierz[wiersz][kolumna] + macierz[wiersz + 1][kolumna - 1] + macierz[wiersz + 1][kolumna] + macierz[wiersz + 1][kolumna + 1]));
        }
    }

    return wynik;
}

int test1()
{
    std::vector<std::vector<int>> macierz{ { 10, 99, 28, 21, 78 }, { 35, 78, 31, 56, 24 },
        { 7, 18, 2, 50, 87 }, { 59, 67, 9, 82, 53 },
        { 23, 26, 76, 62, 36 } };

    int wynik = 395;
    assert(klepsydraV1(macierz) == wynik);
}

int main()
{
    test1();
    return 0;
}
