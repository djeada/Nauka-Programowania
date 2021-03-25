#include <cassert>
#include <cmath>
#include <vector>

//Otrzymujesz dwie listy n wspolczynnikow wielomianu postaci
//a_nx^n + a_(n-1)x^(n-1) + ... + a_. Oblicz wartosc wspolczynnikow
//wielomianu bedacego iloczynem otrzymanych wielomianow.
std::vector<int> iloczyn(std::vector<int>& listaA, std::vector<int>& listaB)
{

    std::vector<int> wynik(listaA.size() + listaB.size() - 1, 0);

    for (unsigned int i = 0; i < listaA.size(); i++) {
        for (unsigned int j = 0; j < listaB.size(); j++)
            wynik[i + j] += listaA[i] * listaB[j];
    }

    return wynik;
}

void test1()
{
    std::vector<int> listaA{ 5, 0, 10, 6 };
    std::vector<int> listaB{ 1, 2, 4 };
    std::vector<int> wynik{ 5, 10, 30, 26, 52, 24 };
    assert(iloczyn(listaA, listaB) == wynik);
}

int main()
{
    test1();
    return 0;
}
