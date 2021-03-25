#include <cassert>
#include <cmath>

//Napisz funkcje, ktora dla otrzymanych dwoch liczb
//przy pomocy petli obliczy ile wynosi a podniesione do b.

double potega(int a, int b)
{
    int wynik = 1;
    for (int i = 0; i < abs(b); i++)
        wynik *= a;

    if (b < 0)
        return 1 / wynik;

    return wynik;
}

void test1()
{
    int a = 2;
    int b = 3;
    double wynik = 8.00;

    assert(abs(potega(a, b) - wynik) < 0.01);
}

void test2()
{
    int a = 10;
    int b = -5;
    double wynik = 0.00001;

    assert(abs(potega(a, b) - wynik) < 0.01);
}

int main()
{

    test1();
    test2();

    return 0;
}
