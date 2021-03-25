#include <cassert>
#include <cmath>
#include <vector>

//Otrzymujesz dwie listy n wspolczynnikow wielomianu postaci
//a_nx^n + a_(n-1)x^(n-1) + ... + a_. Oblicz wartosc wspolczynnikow
//wielomianu bedacego suma otrzymanych wielomianow.
std::vector<int> suma(std::vector<int>& listaA, std::vector<int>& listaB)
{

    assert(listaA.size() == listaB.size());
    std::vector<int> wynik;

    for (unsigned int i = 0; i < listaA.size(); i++)
        wynik.push_back(listaA[i] + listaB[i]);

    return wynik;
}

void test1()
{
    std::vector<int> listaA{ 3, 2, 1 };
    std::vector<int> listaB{ 8, 9, 2 };
    std::vector<int> wynik{ 11, 11, 3 };
    assert(suma(listaA, listaB) == wynik);
}

int main()
{

    test1();

    return 0;
}
