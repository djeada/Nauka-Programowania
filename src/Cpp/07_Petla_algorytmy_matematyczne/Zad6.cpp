#include <cassert>

//Napisz funkcje, ktora dla otrzymanych dwoch liczb zwroci
//ich najmniejsza wspolna wielokrotnosc.

int nwd(int a, int b)
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

int nww(int a, int b)
{
    return a * b / nwd(a, b);
}

void test1()
{
    int a = 14;
    int b = 21;
    int wynik = 42;

    assert(nww(a, b) == wynik);
}

int main()
{

    test1();

    return 0;
}
