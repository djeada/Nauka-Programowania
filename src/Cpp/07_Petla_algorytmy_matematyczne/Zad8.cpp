#include <cassert>
#include <cmath>

//Napisz funkcje, ktora dla otrzymanej liczby sprawdzi
//czy jest ona liczba pierwsza.

bool czyPierwsza(int n)
{

    if (n <= 1)
        return false;

    if (n % 2 == 0 && n != 2)
        return false;

    for (int i = 3; i <= sqrt((double)n); i += 2) {
        if (n % i == 0)
            return false;
    }

    return true;
}

void test1()
{
    int a = 15;
    assert(!czyPierwsza(a));
}

void test2()
{
    int a = 7;
    assert(czyPierwsza(a));
}

void test3()
{
    int a = -15;
    assert(!czyPierwsza(a));
}

int main()
{

    test1();
    test2();
    test3();

    return 0;
}
