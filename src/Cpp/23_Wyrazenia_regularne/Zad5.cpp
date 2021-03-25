#include <cassert>
#include <regex>
#include <string>

//Otrzymujesz napis. Odfiltruj z niego cyfry.

std::string odfiltrujCyfry(std::string& napis)
{
    return std::regex_replace(napis, std::regex("[^0-9]*"), "");
}

void test1()
{
    std::string napis = "numer 32.19 wyzej niz 31.17";
    std::string wynik = "32193117";
    assert(odfiltrujCyfry(napis) == wynik);
}

void test2()
{
    std::string napis = "Lezy jerzy na wiezy";
    std::string wynik;
    assert(odfiltrujCyfry(napis) == wynik);
}

int main()
{

    test1();
    test2();

    return 0;
}
