#include <cassert>
#include <functional>

//Otrzymujesz dwie liczby. Uzywając jedynie operatorow bitowych zaimplementuj:

//a) dodawanie.
int suma(int a, int b)
{

    while (b != 0) {
        int pom = a & b;
        a = a ^ b;
        b = pom << 1;
    }

    return a;
}

//b) odejmowanie.
int roznica(int a, int b)
{

    while (b != 0) {
        int pom = (~a) & b;
        a = a ^ b;
        b = pom << 1;
    }

    return a;
}

//c) mnozenie.
int iloczyn(int a, int b)
{

    int znak = (a < 0 && b >= 0) || (b < 0 && a >= 0) ? -1 : 1;

    if (a < 0)
        a *= -1;

    if (b < 0)
        b *= -1;

    int pom = 0;

    while (b != 0) {
        if (b & 1)
            pom += a;
        a <<= 1;
        b >>= 1;
    }

    return znak * pom;
}

//d) dzielenie.
int iloraz(int a, int b)
{
    std::function<int(int, int, int, int*)> wew_iloczyn;
    wew_iloczyn = [&wew_iloczyn](int dzielna, int dzielnik, int org_b, int* reszta) -> int {
        int wynik = 1;

        if (dzielna == dzielnik) {
            *reszta = 0;
            return 1;
        }

        else if (dzielna < dzielnik) {
            *reszta = dzielna;
            return 0;
        }

        while (dzielnik <= dzielna) {
            dzielnik = dzielnik << 1;
            wynik = wynik << 1;
        }

        if (dzielna < dzielnik) {
            dzielnik >>= 1;
            wynik >>= 1;
        }

        wynik = wynik + wew_iloczyn(dzielna - dzielnik, org_b, org_b, reszta);

        return wynik;
    };

    int znak = (a < 0 && b >= 0) || (b < 0 && a >= 0) ? -1 : 1;

    if (a < 0)
        a *= -1;

    if (b < 0)
        b *= -1;

    int reszta = 0;

    return znak * wew_iloczyn(a, b, b, &reszta);
}

void test1()
{
    int a = -2;
    int b = 2;
    int wynik = 0;
    assert(suma(a, b) == wynik);
}

void test2()
{
    int a = 3;
    int b = 2;
    int wynik = 5;
    assert(suma(a, b) == wynik);
}

void test3()
{
    int a = 3;
    int b = 2;
    int wynik = 1;
    assert(roznica(a, b) == wynik);
}

void test4()
{
    int a = 10;
    int b = 15;
    int wynik = -5;
    assert(roznica(a, b) == wynik);
}

void test5()
{
    int a = 3;
    int b = 2;
    int wynik = 6;
    assert(iloczyn(a, b) == wynik);
}

void test6()
{
    int a = 10;
    int b = -2;
    int wynik = -20;
    assert(iloczyn(a, b) == wynik);
}

void test7()
{
    int a = 9;
    int b = 3;
    int wynik = 3;
    assert(iloraz(a, b) == wynik);
}

void test8()
{
    int a = 25;
    int b = -5;
    int wynik = -5;
    assert(iloraz(a, b) == wynik);
}

int main()
{

    test1();
    test2();
    test3();
    test4();
    test5();
    test6();
    test7();
    test8();

    return 0;
}
