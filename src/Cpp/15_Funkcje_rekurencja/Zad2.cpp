#include <cassert>

/*
Suma liczb naturalnych mniejszych od N.
*/

int sumaV1(int N)
{

    if (N <= 0)
        return 0;

    return N + sumaV1(N - 1);
}

void test1()
{
    int N = 10;
    int wynik = 55;

    assert(sumaV1(N) == wynik);
}

int main()
{

    test1();

    return 0;
}
