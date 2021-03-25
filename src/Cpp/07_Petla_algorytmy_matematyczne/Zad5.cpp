#include <cassert>

//Napisz funkcje, ktora dla otrzymanych dwoch liczb zwroci
//ich najwiekszy wspolny dzielnik.

int nwdV1(int a, int b)
{

    if (b == 0)
        return a;

    return nwdV1(b, a % b);
}

int nwdV2(int a, int b)
{

    int c;

    while (b != a % b) {
        c = b;
        b = a % b;
        a = c;

        if (b == 0)
            break;
    }

    return a;
}

void test1()
{
    int a = 14;
    int b = 21;
    int wynik = 7;

    assert(nwdV1(a, b) == wynik);
}

void test2()
{
    int a = 14;
    int b = 21;
    int wynik = 7;

    assert(nwdV2(a, b) == wynik);
}

int main()
{

    test1();
    test2();

    return 0;
}
