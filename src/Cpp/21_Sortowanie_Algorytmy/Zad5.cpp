#include <cassert>
#include <functional>
#include <vector>

//g++-10 -ggdb3 -O0 -std=c++20 -Wall -Wextra -pedantic -o main.out Zad4.cpp
int rozdziel(std::vector<int>& lista, int indeksPocz, int indeksKonc)
{
    int wartosc = lista[indeksKonc];
    int i = indeksPocz - 1;
    for (int j = indeksPocz; j < indeksKonc; j++) {
        if (lista[j] <= wartosc) {
            i++;
            std::swap(lista[i], lista[j]);
        }
    }

    std::swap(lista[i + 1], lista[indeksKonc]);

    return i + 1;
}

void sortuj(std::vector<int>& lista)
{
    std::function<void(std::vector<int>&, int, int)> _sortuj;
    _sortuj = [&_sortuj](std::vector<int>& lista, int p, int r) {
        if (p < r) {
            int q = rozdziel(lista, p, r);
            _sortuj(lista, p, q - 1);
            _sortuj(lista, q + 1, r);
        }
    };

    _sortuj(lista, 0, lista.size() - 1);
}

void test1()
{
    std::vector<int> lista({ 4, 2, 5, 3, 1 });
    std::vector<int> wynik({ 1, 2, 3, 4, 5 });

    sortuj(lista);

    assert(lista == wynik);
}

int main()
{

    test1();

    return 0;
}
