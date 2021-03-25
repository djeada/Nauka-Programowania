#include <cassert>
#include <cmath>
#include <string>

//Otrzymujesz liczbe, zamien ja na jej binarny odpowiednik jesli:

//a) jest liczba parzysta.
std::string naBin(int liczba)
{

    std::string bin;

    while (liczba > 0) {
        bin.insert(0, std::to_string(liczba % 2));
        liczba /= 2;
    }

    return bin;
}

std::string zamienLiczbeParzysta(int liczba)
{
    if (liczba % 2 == 0)
        return naBin(liczba);

    return "";
}

//b) jest liczba pierwsza.
bool czyPierwsza(int n)
{

    if (n <= 1)
        return false;

    if (n % 2 == 0 && n != 2)
        return false;

    for (int i = 3; i <= std::sqrt((double)n); i += 2) {
        if (n % i == 0)
            return false;
    }

    return true;
}

std::string zamienLiczbePierwsza(int liczba)
{
    if (czyPierwsza(liczba))
        return naBin(liczba);

    return "";
}

void test1()
{
    int liczba = 3;
    std::string wynik;

    assert(zamienLiczbeParzysta(liczba) == wynik);
}

void test2()
{
    int liczba = 124;
    std::string wynik = "1111100";

    assert(zamienLiczbeParzysta(liczba) == wynik);
}

void test3()
{
    int liczba = 124;
    std::string wynik;

    assert(zamienLiczbePierwsza(liczba) == wynik);
}

void test4()
{
    int liczba = 3;
    std::string wynik = "11";

    assert(zamienLiczbePierwsza(liczba) == wynik);
}

int main()
{

    test1();
    test2();
    test3();
    test4();

    return 0;
}
