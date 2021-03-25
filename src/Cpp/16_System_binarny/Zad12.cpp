#include <algorithm>
#include <cassert>

//Znajdz dlugosc najdluzszego ciagu zer w liczbie binarnej.

int najdluzszyCiagZer(int liczba)
{
    if (liczba == 0)
        return 1;

    int wynik = 0;
    int pom = 0;

    while (liczba != 0) {
        int reszta = liczba % 2;
        liczba /= 2;
        if (reszta == 1) {
            wynik = std::max(wynik, pom);
            pom = 0;
        } else
            pom++;
    }
    return std::max(wynik, pom);
}

void test1()
{
    int liczba = 111;
    int wynik = 1;

    assert(najdluzszyCiagZer(liczba) == wynik);
}

void test2()
{
    int liczba = 8219;
    int wynik = 8;

    assert(najdluzszyCiagZer(liczba) == wynik);
}

int main()
{

    test1();
    test2();

    return 0;
}
