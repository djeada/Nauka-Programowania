#include <cassert>

//Napisz funkcje, ktora przy pomocy petli obliczy silnie
//z otrzymanej liczby.

int silnia(int a)
{

    int wynik = 1;

    while (a > 0) {
        wynik *= a;
        a--;
    }

    return wynik;
}

void test1()
{
    int a = 4;
    int wynik = 24;
    assert(silnia(a) == wynik);
}

void test2()
{
    int a = -5;
    int wynik = 1;
    assert(silnia(a) == wynik);
}

int main()
{

    test1();
    test2();

    return 0;
}
