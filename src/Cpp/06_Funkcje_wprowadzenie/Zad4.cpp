#include <cassert>
#include <cmath>

//Napisz funkcje, ktora:

//a) dla podanych dwoch liczb, zwroci mniejsza
int min2(int a, int b)
{
    return a < b ? a : b;
}

//b) dla podanych dwoch liczb, zwroci wieksza
int maks2(int a, int b)
{
    return a > b ? a : b;
}

//c) dla podanych trzech liczb, zwroci najmniejsza
int min3(int a, int b, int c)
{
    int minAB = a < b ? a : b;
    return minAB < c ? minAB : c;
}

//d) dla podanych trzech liczb, zwroci najwieksza
int maks3(int a, int b, int c)
{
    int maksAB = a > b ? a : b;
    return maksAB > c ? maksAB : c;
}

void test1()
{
    int a = 7;
    int b = 5;
    int wynik = a;

    assert(maks2(a, b) == wynik);
    assert(maks2(b, a) == wynik);
}

void test2()
{
    int a = 7;
    int b = 5;
    int wynik = b;

    assert(min2(a, b) == wynik);
    assert(min2(b, a) == wynik);
}

void test3()
{
    int a = 7;
    int b = 5;
    int c = 11;
    int wynik = c;

    assert(maks3(a, b, c) == wynik);
    assert(maks3(b, a, c) == wynik);
}

void test4()
{
    int a = 7;
    int b = 5;
    int c = 11;
    int wynik = b;

    assert(min3(a, b, c) == wynik);
    assert(min3(b, a, c) == wynik);
}

int main()
{
    test1();
    test2();
    test3();
    test4();

    return 0;
}
