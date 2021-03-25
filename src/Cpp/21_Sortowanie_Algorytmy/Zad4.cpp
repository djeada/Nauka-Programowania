#include <cassert>
#include <functional>
#include <vector>

//g++-10 -ggdb3 -O0 -std=c++20 -Wall -Wextra -pedantic -o main.out Zad4.cpp
void merge(std::vector<int>& lista, unsigned int p, unsigned int q, unsigned int r)
{
    unsigned int rozmiarLewy = q - p + 1;
    unsigned int rozmiarPrawy = r - q;
    std::vector<int> lewaLista(rozmiarLewy);
    std::vector<int> prawaLista(rozmiarPrawy);

    for (unsigned int i = 0; i < rozmiarLewy; i++)
        lewaLista[i] = lista[p + i];

    for (unsigned int j = 0; j < rozmiarPrawy; j++)
        prawaLista[j] = lista[q + j + 1];

    unsigned int i = 0;
    unsigned int j = 0;
    unsigned int k = p;

    for (; k <= r && i < rozmiarLewy && j < rozmiarPrawy; k++) {

        if (lewaLista[i] <= prawaLista[j]) {
            lista[k] = lewaLista[i];
            i++;
        }

        else {
            lista[k] = prawaLista[j];
            j++;
        }
    }

    for (i = i; i < rozmiarLewy; ++i) {
        lista[k] = lewaLista[i];
        k++;
    }

    for (j = j; j < rozmiarPrawy; j++) {
        lista[k] = prawaLista[j];
        k++;
    }
}

void sortuj(std::vector<int>& lista)
{
    std::function<void(std::vector<int>&, int, int)> _sortuj;
    _sortuj = [&_sortuj](std::vector<int>& lista, int p, int r) {
        if (p < r) {
            int q = (p + r) / 2;
            _sortuj(lista, p, q);
            _sortuj(lista, q + 1, r);
            merge(lista, p, q, r);
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
