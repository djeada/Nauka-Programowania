#include <cassert>
#include <regex>
#include <sstream>
#include <string>
#include <vector>

//Otrzymujesz dwa napisy. Znajdz wiersze w pierwszym napisie konczace
//sie drugim napisem. Wiersz może byc zakonczony dowolnym znakiem interpunkcyjnym.

std::vector<std::string> rozdziel(const std::string& napis)
{
    std::vector<std::string> wynik;
    std::string wiersz;
    std::istringstream strumien(napis);
    while (std::getline(strumien, wiersz, '\n'))
        wynik.push_back(wiersz);

    return wynik;
}

std::vector<std::string> wiersze(std::string& tekst, std::string& napis)
{
    std::vector<std::string> wynik;
    std::regex wzorzec(std::string(".*" + napis + "[;,!?\\.]?"));

    auto _wiersze = rozdziel(tekst);

    for (auto& wiersz : _wiersze) {
        if (regex_match(wiersz, wzorzec))
            wynik.push_back(wiersz);
    }

    return wynik;
}

void test1()
{
    std::string tekst = "Folgujmy paniom nie sobie, ma rada;\nMilujmy wiernie nie jest w nich przysada.\nGodnosci trzeba nie za nic tu cnota,\nMilosci pragna nie pragna tu zlota";
    std::string napis = "ada";
    std::vector<std::string> wynik{ "Folgujmy paniom nie sobie, ma rada;", "Milujmy wiernie nie jest w nich przysada." };

    assert(wiersze(tekst, napis) == wynik);
}

int main()
{

    test1();

    return 0;
}
