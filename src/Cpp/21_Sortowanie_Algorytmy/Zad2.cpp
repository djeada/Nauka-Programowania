#include <cassert>
#include <vector>

//g++-10 -ggdb3 -O0 -std=c++20 -Wall -Wextra -pedantic -o main.out Zad2.cpp

void sortuj(std::vector<int>& lista)
{
    auto it = lista.begin();

    while (it != lista.end()) {

        auto it_min = it;

        for (auto i = it + 1; i != lista.end(); i++) {

            if (*i < *it_min)
                it_min = i;
        }

        std::iter_swap(it, it_min);
        it++;
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
