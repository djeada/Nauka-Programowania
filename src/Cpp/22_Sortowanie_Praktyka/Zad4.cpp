#include <algorithm>
#include <cassert>
#include <string>
#include <vector>

//Otrzymujesz liste napisow. Posortuj wzgledem dlugosci napisy w liscie.

void sortuj(std::vector<std::string>& lista)
{
    std::sort(lista.begin(), lista.end(), [](auto lhs, auto rhs) {
        return lhs.size() < rhs.size();
    });
}

void test1()
{
    std::vector<std::string> lista{ "abcd", "ab", "a", "abc" };
    std::vector<std::string> wynik{ "a", "ab", "abc", "abcd" };

    sortuj(lista);

    assert(lista == wynik);
}

int main()
{

    test1();

    return 0;
}
