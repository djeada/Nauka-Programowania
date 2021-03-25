#include <cassert>

//Znajdz min/maks dwoch liczb bez uzycia instrukcji warunkowej.

int znak(int n)
{
    return (n >> 31) & 0x01;
}

// a >= b : znakA = 1, znakB = 0;
// a < b : znakA = 0, znakB = 1;
int maks(int a, int b)
{
    int znakB = znak(a - b);
    int znakA = znakB ^ 1;
    return znakA * a + znakB * b;
}

int min(int a, int b)
{
    int znakB = znak(a - b);
    int znakA = znakB ^ 1;
    return znakB * a + znakA * b;
}

void test1()
{
    int a = 10;
    int b = 8;
    int wynik = a;

    assert(maks(a, b) == wynik);
}

void test2()
{
    int a = 10;
    int b = 8;
    int wynik = b;

    assert(min(a, b) == wynik);
}

int main()
{

    test1();
    test2();

    return 0;
}
