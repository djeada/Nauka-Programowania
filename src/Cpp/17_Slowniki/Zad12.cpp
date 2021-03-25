#include <algorithm>
#include <cassert>
#include <unordered_map>
#include <vector>

//Otrzymujesz dwa slowniki skladajace się z par napisow i list liczb.
//Listy sa nieuporzadkowane. Sprawdz czy slowniki skladaja sie z tych samych par.
//Dwie listy uznajemy za identyczne jesli zawieraja te same elementy, przy czym
//kolejnosc elementow moze byc zmieniona.

bool wektoryRowne(std::vector<int> v1, std::vector<int> v2)
{
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    return v1 == v2;
}

bool identyczne(std::unordered_map<std::string, std::vector<int>>& slownikA, std::unordered_map<std::string, std::vector<int>>& slownikB)
{

    if (slownikA.size() != slownikB.size())
        return false;

    for (auto& [klucz, wektorA] : slownikA) {
        if (slownikB.count(klucz) == 0)
            return false;

        auto wektorB = slownikB[klucz];
        if (!wektoryRowne(wektorA, wektorB))
            return false;
    }

    return true;
}

void test1()
{
    std::unordered_map<std::string, std::vector<int>> slownikA{ { "c", { 3, 2, 1 } },
        { "x", { -2, 9, 11 } },
        { "a", { 4, 6, 7 } } };

    std::unordered_map<std::string, std::vector<int>> slownikB{ { "a", { 7, 4, 6 } },
        { "c", { 2, 3, 1 } },
        { "x", { -2, 11, 9 } } };

    assert(identyczne(slownikA, slownikB));
}

void test2()
{
    std::unordered_map<std::string, std::vector<int>> slownikA{ { "abc", { 1, 2, 3 } },
        { "123", { 9, 0, 0 } },
        { "xxx", { 5, 5, 5 } } };
    std::unordered_map<std::string, std::vector<int>> slownikB{ { "abc", { 1, 2, 3 } },
        { "xxx", { 0, 0, 9 } },
        { "123", { 5, 5, 5 } } };

    assert(!identyczne(slownikA, slownikB));
}

int main()
{

    test1();
    test2();

    return 0;
}
