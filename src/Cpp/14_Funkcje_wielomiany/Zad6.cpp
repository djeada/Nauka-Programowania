#include <cassert>
#include <cmath>
#include <utility>
#include <vector>

//Otrzymujesz liste wspolczynnikow a, b, c rownania
//kwadratowego ax^2 + bx + c.
//Znajdz rzeczywiste miejsca zerowe rownania kwadratowego.
std::pair<double, double> pierwiastki(std::vector<int>& lista)
{

    assert(lista.size() == 3);

    std::pair<double, double> wynik;

    int delta = lista[1] * lista[1] - 4 * lista[0] * lista[2];

    if (delta > 0) {
        wynik.first = (-lista[1] + sqrt(delta)) / (2 * lista[0]);
        wynik.second = (-lista[1] - sqrt(delta)) / (2 * lista[0]);
    }

    else if (delta == 0) {
        wynik.first = -lista[1] / (2 * lista[0]);
        wynik.second = -lista[1] / (2 * lista[0]);
    }

    return wynik;
}

void test1()
{
    std::vector<int> lista{ 1, 2, 1 };
    std::pair<double, double> wynik{ -1, -1 };
    assert(pierwiastki(lista) == wynik);
}

void test2()
{
    std::vector<int> lista{ 1, -4, 5 };
    std::pair<double, double> wynik;
    assert(pierwiastki(lista) == wynik);
}

int main()
{

    test1();
    test2();
    return 0;
}
