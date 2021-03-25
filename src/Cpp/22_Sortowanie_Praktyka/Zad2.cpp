#include <algorithm>
#include <cassert>
#include <string>
#include <vector>

//Otrzymujesz napis reprezentujacy zdanie.
//Podziel zdanie na słowa skladowe.
//Nastepnie posortuj słowa alfabetycznie i
//zapisz je w liscie. Znaki interpunkcyjne
//nie sa liczone jako slowa.

void wyczysc(std::string& napis)
{
    auto it = napis.begin();

    while (it != napis.end()) {
        if (ispunct(*it))
            napis.erase(it);
        else
            it++;
    }
}

std::vector<std::string> slowa(std::string& napis)
{
    std::vector<std::string> wynik;
    int pocz = 0;
    int konc = 0;
    while ((konc = napis.find(' ', pocz)) != std::string::npos) {
        if (konc != pocz) {
            auto slowo = napis.substr(pocz, konc - pocz);
            wyczysc(slowo);
            if (!slowo.empty())
                wynik.push_back(slowo);
        }
        pocz = konc + 1;
    }
    if (konc != pocz) {
        auto slowo = napis.substr(pocz);
        wyczysc(slowo);
        if (!slowo.empty())
            wynik.push_back(slowo);
    }

    return wynik;
}

void sortuj(std::vector<std::string>& lista)
{
    std::sort(lista.begin(), lista.end());
}

void test1()
{
    std::string napis = "Lemur wygina smialo cialo";
    std::vector<std::string> wynik{ "Lemur", "cialo", "smialo", "wygina" };
    auto napisy = slowa(napis);
    sortuj(napisy);

    assert(napisy == wynik);
}

int main()
{

    test1();

    return 0;
}
