#include <algorithm>
#include <cassert>
#include <string>
#include <vector>

//Znajdz wszystkie permutacje slowa bedace palindromami.

bool palindrom(std::string& slowo)
{
    int N = slowo.length() - 1;
    for (int i = 0; i <= N / 2; i++) {
        if (slowo[i] != slowo[N - i])
            return false;
    }

    return true;
}

void permutacja(std::string& slowoWej, std::string& slowoWyj, std::vector<std::string>& wynik)
{
    if (slowoWej.empty() && palindrom(slowoWyj) && find(wynik.begin(), wynik.end(), slowoWyj) == wynik.end()) {
        wynik.push_back(slowoWyj);
        return;
    }

    for (unsigned int i = 0; i < slowoWej.length(); ++i) {
        std::string noweSlowoWej = slowoWej;
        std::string noweSlowoWyj = slowoWyj;
        noweSlowoWej.erase(i, 1);
        noweSlowoWyj += slowoWej.at(i);
        permutacja(noweSlowoWej, noweSlowoWyj, wynik);
    }
}

std::vector<std::string> permutacje(std::string& slowoWej)
{

    std::vector<std::string> wynik;

    std::string slowoWyj;
    permutacja(slowoWej, slowoWyj, wynik);

    return wynik;
}

bool wektoryRowne(std::vector<std::string> v1, std::vector<std::string> v2)
{
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    return v1 == v2;
}

void test1()
{
    std::string slowo = "adamm";
    std::vector<std::string> wynik{ "madam", "amdma" };
    assert(wektoryRowne(permutacje(slowo), wynik));
}

int main()
{
    test1();
    return 0;
}
