#include <cassert>
#include <string>

/*
Gracz A oraz gracz B graja w kapsle.
Na poczatku gry otrzymuja pewna liczbe kapsli.
W kazdej turze grac moze z puli kapsli zabrac 1, 2 badz 4 kapsle.
Gracz, ktory zabral ostatni kapsel wygyrwa.
Gre rozpoczyna gracz A.
Znajdz liczbe mozliwych kombinacji wybrania liczby kapsli w danej turze
prowadzaca do zwyciestwa kazdego z graczy.
*/

void oblicz(int n, int& wynikA, int& wynikB, std::string s = "AB")
{

    if (n <= 0)
        return;

    if (n == 1 || n == 2 || n == 4) {

        if (s[0] == 'A')
            wynikA++;

        else
            wynikB++;

        return;
    }

    else {
        auto temp = s[0];
        s[0] = s[1];
        s[1] = temp;

        oblicz(n - 1, wynikA, wynikB, s);
        oblicz(n - 2, wynikA, wynikB, s);
        oblicz(n - 4, wynikA, wynikB, s);
    }
}

void test1()
{
    int wynikA = 0;
    int wynikB = 0;

    oblicz(1, wynikA, wynikB);
    assert(wynikA == 1);
    assert(wynikB == 0);
}

void test2()
{
    int wynikA = 0;
    int wynikB = 0;
    oblicz(3, wynikA, wynikB);
    assert(wynikA == 0);
    assert(wynikB == 2);
}

void test3()
{
    int wynikA = 0;
    int wynikB = 0;
    oblicz(10, wynikA, wynikB);
    assert(wynikA == 33);
    assert(wynikB == 27);
}

int main()
{

    test1();
    test2();
    test3();

    return 0;
}
