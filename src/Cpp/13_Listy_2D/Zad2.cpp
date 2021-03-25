#include <cassert>
#include <utility>
#include <vector>

//Dla otrzymanej liczby, stworz macierz kwadratowa skladajaca
//się z liczby kolumn i wierszy rownej otrzymanej liczbie
//ktorej kazdy element jest iloczynem jego wspolrzednych.

std::vector<std::vector<int>> macierz(int n)
{

    std::vector<std::vector<int>> macierz;
    macierz.reserve(n);

    for (int i = 0; i < n; i++) {
        std::vector<int> wiersz;
        for (int j = 0; j < n; j++)
            wiersz.push_back(i * j);
        macierz.push_back(wiersz);
    }

    return macierz;
}

void test1()
{
    int n = 4;
    std::vector<std::vector<int>> wynik{ { 0, 0, 0, 0 }, { 0, 1, 2, 3 },
        { 0, 2, 4, 6 }, { 0, 3, 6, 9 } };
    assert(macierz(n) == wynik);
}

int main()
{
    test1();
    return 0;
}
