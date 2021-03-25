#include <cassert>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

//Otrzymujesz liste par. Pierwszym elementem pary jest napis reprezentujacy imie i nazwikso
//pracownika, drugim zysk z transakcji jaka dany pracownik przeprowadzil. Znajdz pracownika,
//ktory przyniosl firmie najwiecej zysku.

void wypelnijSlownik(const std::vector<std::pair<std::string, int>>& lista, std::unordered_map<std::string, int>& slownik)
{

    for (const auto& rekord : lista)
        slownik[rekord.first] += rekord.second;
}

std::string znajdzMaxZysk(std::unordered_map<std::string, int>& slownik)
{
    std::string najlepszyPracownik;
    int maxZysk = -1;

    for (auto it = slownik.begin(); it != slownik.end(); it++) {
        if (it->second > maxZysk) {
            najlepszyPracownik = it->first;
            maxZysk = it->second;
        }
    }

    return najlepszyPracownik;
}

std::string pracownik(std::vector<std::pair<std::string, int>>& lista)
{

    if (lista.empty())
        return "";

    std::unordered_map<std::string, int> slownik;
    wypelnijSlownik(lista, slownik);

    return znajdzMaxZysk(slownik);
}

void test1()
{

    std::vector<std::pair<std::string, int>> lista{ { "Barnaba Barabash", 120 }, { "Jon Snow", 100 }, { "Kira Summer", 300 },
        { "Barnaba Barabash", 200 }, { "Bob Marley", 110 } };

    std::string wynik = "Barnaba Barabash";

    assert(pracownik(lista) == wynik);
}

void test2()
{
    std::vector<std::pair<std::string, int>> lista;
    std::string wynik;

    assert(pracownik(lista) == wynik);
}

int main()
{

    test1();
    test2();

    return 0;
}
