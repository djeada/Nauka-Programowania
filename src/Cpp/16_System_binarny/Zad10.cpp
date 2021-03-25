#include <cassert>

//Policz ile bitow nalezy odwrocic,
//aby zamien liczbe A w liczbe B.

int bityDoZmiany(int liczbaA, int liczbaB)
{

    int n = liczbaA ^ liczbaB;

    int licznik = 0;
    while (n != 0) {
        n &= (n - 1);
        licznik++;
    }

    return licznik;
}

void test1()
{
    int liczbaA = 34;
    int liczbaB = 73;
    int wynik = 5;

    assert(bityDoZmiany(liczbaA, liczbaB) == wynik);
}

int main()
{

    test1();

    return 0;
}
