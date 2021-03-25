#include <cassert>
#include <cmath>
#include <vector>

//Otrzymujesz liste n wspolczynnikow wielomianu postaci
//a_nx^n + a_(n-1)x^(n-1) + ... + a_0 oraz liczbe x.
//Znajdz wartosc wielomianu w punkcie.
int wartoscWielomianu(std::vector<int>& lista, int x)
{

    int n = lista.size();
    int wynik = 0;

    for (int i = 0; i < n; i++)
        wynik += lista[i] * pow(x, n - i);

    return wynik;
}

void test1()
{
    std::vector<int> lista{ 3, 2, 1 };
    int x = 1;
    int wynik = 6;
    assert(wartoscWielomianu(lista, x) == wynik);
}

int main()
{

    test1();

    return 0;
}
