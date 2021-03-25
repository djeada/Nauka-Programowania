#include <cassert>
#include <vector>

//g++-10 -ggdb3 -O0 -std=c++20 -Wall -Wextra -pedantic -o main.out Zad2.cpp

void sortuj(std::vector<int>& lista)
{
    for (unsigned int i = 1; i < lista.size(); i++) {
        int klucz = lista[i];
        int j = i - 1;

        while (j >= 0 && lista[j] > klucz) {
            lista[j + 1] = lista[j];
            j--;
        }

        lista[j + 1] = klucz;
    }
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
