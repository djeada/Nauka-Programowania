#include <algorithm>
#include <cassert>
#include <string>
#include <vector>

//Otrzymujesz napis reprezentujacy zdanie oraz slowo.
//Znajdz wszystkie anagramy otrzymanego slowa w zdaniu.
//Roznice miedzy wielkimi i malymi literami powinny byc zignorowane.

void naMale(std::string& slowo)
{
    transform(slowo.begin(), slowo.end(), slowo.begin(), ::tolower);
}

bool anagram(std::string s1, std::string s2)
{

    unsigned int N = s1.length();
    unsigned int M = s2.length();

    if (N != M)
        return false;

    int pom[256] = { 0 };

    for (const auto& znak : s1)
        pom[znak]++;

    for (const auto& znak : s2)
        pom[znak]--;

    for (const auto& x : pom) {
        if (x != 0)
            return false;
    }

    return true;
}

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

std::vector<std::string> anagramyV1(const std::string& zdanie, const std::string& napis)
{
    std::vector<std::string> wynik;
    unsigned int pocz = 0;
    unsigned int konc = 0;
    while ((konc = zdanie.find(' ', pocz)) != std::string::npos) {
        if (konc != pocz) {
            auto slowo = zdanie.substr(pocz, konc - pocz);
            wyczysc(slowo);
            naMale(slowo);
            if (!slowo.empty() && anagram(slowo, napis))
                wynik.push_back(slowo);
        }
        pocz = konc + 1;
    }
    if (konc != pocz) {
        auto slowo = zdanie.substr(pocz);
        wyczysc(slowo);
        naMale(slowo);
        if (!slowo.empty() && anagram(slowo, napis))
            wynik.push_back(slowo);
    }

    return wynik;
}

void test1()
{
    std::string zdanie = "Za jego nikczemne uczynki, spotakla go wysoce sroga kara.";
    std::string slowo = "arak";
    std::vector<std::string> wynik({ "kara" });
    assert(anagramyV1(zdanie, slowo) == wynik);
}

int main()
{
    test1();

    return 0;
}
