#include <cassert>
#include <vector>

//g++-10 -ggdb3 -O0 -std=c++20 -Wall -Wextra -pedantic -o main.out Zad1.cpp

void swap(int* a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void sortuj(std::vector<int>& lista)
{
    for (long unsigned int i = 0; i < lista.size(); i++) {
        for (long unsigned int j = i + 1; j < lista.size(); j++) {
            if (lista[i] > lista[j])
                swap(&lista[i], &lista[j]);
        }
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
