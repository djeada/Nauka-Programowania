#include <cassert>
#include <cmath>

//Napisz funkcje, ktora dla otrzymanej liczby
//zwroci jej pierwiastek.

const float dokladnosc = 0.0001;

float pierwiastek(int a)
{

    float wynik = a;

    while (abs(a - wynik * wynik) > dokladnosc)
        wynik = (wynik + a / wynik) / 2;

    return wynik;
}

void test1()
{
    int a = 16;
    int wynik = 4;

    assert(abs(pierwiastek(a) - wynik) <= dokladnosc);
}

int main()
{

    test1();

    return 0;
}
