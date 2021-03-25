#include <cassert>
#include <string>

//Znajdz i zamien wszystkie wystapienia slowa w zdaniu na inne podane slowo.

std::string zamienWszystkoV1(std::string zdanie, std::string napisA, std::string napisB)
{

    auto k = zdanie.find(napisA);

    while (k != std::string::npos) {
        zdanie.replace(k, napisA.size(), napisB);
        k = zdanie.find(napisA, k + napisB.size());
    }

    return zdanie;
}

int main()
{

    //Testy Poprawnosci
    std::string zdanie = "Lezy jezy na wiezy";
    std::string napisA = "zy";
    std::string napisB = "rzy";
    std::string wynik = "Lerzy jerzy na wierzy";

    assert(zamienWszystkoV1(zdanie, napisA, napisB) == wynik);

    return 0;
}

//Compiled with g++ -std=c++17 Zad1.cpp -lstdc++fs -o exe
