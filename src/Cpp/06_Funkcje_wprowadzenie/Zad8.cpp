#include <cassert>
#include <limits>
//Napisz funkcje realizujaca zaokraglanie ilorazu bez uzycia '/' i '%'.

int podziel(int a, int b)
{

    int znak = 1;
    int licznik = 0;

    if (b == 0)
        return std::numeric_limits<int>::signaling_NaN();

    if (a == 0)
        return 0;

    if (a < 0) {
        znak = -1;
        a = -a;
    }

    if (b < 0) {
        znak *= -1;
        b = -b;
    }

    if (znak == 1) {
        licznik = 0;
        while (a >= b) {
            a -= b;
            licznik += 1;
        }
    }

    else {
        licznik = 1;
        while (a > b) {
            a -= b;
            licznik += 1;
        }
    }

    return licznik * znak;
}

void test1()
{

    int a = 15;
    int b = 5;
    int wynik = 3;

    assert(podziel(a, b) == wynik);
}

void test2()
{

    int a = 8;
    int b = -4;
    int wynik = -2;

    assert(podziel(a, b) == wynik);
}

int main()
{

    test1();
    test2();

    return 0;
}
