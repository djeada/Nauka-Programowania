#include <cassert>
#include <cmath>
#include <vector>

//Otrzymujesz liste n wspolczynnikow wielomianu postaci
//a_nx^n + a_(n-1)x^(n-1) + ... + a_0 oraz liczbe x.
//Oblicz wartosc wspolczynnikow wielomianu po
//przemnozeniu przez liczbe x.
std::vector<int> iloczyn(std::vector<int>& lista, int x)
{

    std::vector<int> wynik;

    for (auto& liczba : lista)
        wynik.push_back(liczba * x);

    return wynik;
}

void test1()
{
    std::vector<int> lista{ 3, 2, 1 };
    int x = 2;
    std::vector<int> wynik{ 6, 4, 2 };
    assert(iloczyn(lista, x) == wynik);
}

int main()
{

    test1();

    return 0;
}
