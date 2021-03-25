#include <algorithm>
#include <cassert>
#include <string>

/*
Napisz funkcje, ktora sprawdzi czy otrzymane slowo jest elfickie. 
Elfickie slowo to takie, w ktorym co najmniej raz wystepuje kazda 
z liter slowa elf.
*/

bool czyElfickieSlowoV1(std::string slowo, std::string elf = "elf", int i = 0)
{

    if (i >= slowo.size())
        return false;

    auto litera = slowo[i];

    if (elf.find(litera) != std::string::npos) {
        elf.erase(remove(elf.begin(), elf.end(), litera), elf.end());
        if (elf.empty())
            return true;
    }

    return czyElfickieSlowoV1(slowo, elf, i + 1);
}

void test1()
{
    std::string slowo = "reflektor";
    bool wynik = true;

    assert(czyElfickieSlowoV1(slowo) == wynik);
}

void test2()
{
    std::string slowo = "elzbieta";
    bool wynik = false;

    assert(czyElfickieSlowoV1(slowo) == wynik);
}

int main()
{

    test1();
    test2();

    return 0;
}
