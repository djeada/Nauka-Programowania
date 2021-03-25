#include <algorithm>
#include <cassert>
#include <string>
#include <utility>
#include <vector>

//Otrzymujesz liste par napisow i liczb. Posortuj pary w liscie wzgledem:
//a) wartosci liczb;
void sortujWartosci(std::vector<std::pair<std::string, int>>& lista)
{
    std::sort(lista.begin(), lista.end(), [](auto rhs, auto lhs) {
        return rhs.second < lhs.second;
    });
}

//b) dlugosci napisow;
void sortujDlugosci(std::vector<std::pair<std::string, int>>& lista)
{
    std::sort(lista.begin(), lista.end(), [](auto rhs, auto lhs) {
        return rhs.first.size() < lhs.first.size();
    });
}

void test1()
{
    std::vector<std::pair<std::string, int>> lista{ { "abc", 3 }, { "bca", 1 }, { "cab", 2 } };
    std::vector<std::pair<std::string, int>> wynik{ { "bca", 1 }, { "cab", 2 }, { "abc", 3 } };

    sortujWartosci(lista);

    assert(lista == wynik);
}

void test2()
{
    std::vector<std::pair<std::string, int>> lista{ { "ab", 3 }, { "abc", 1 }, { "a", 2 } };
    std::vector<std::pair<std::string, int>> wynik{ { "a", 2 }, { "ab", 3 }, { "abc", 1 } };

    sortujDlugosci(lista);

    assert(lista == wynik);
}

int main()
{

    test1();
    test2();

    return 0;
}
