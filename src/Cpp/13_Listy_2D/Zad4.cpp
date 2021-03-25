#include <cassert>
#include <vector>

//Otrzymujesz dwie macierze o tych samych wymiarach, zwroc macierz bedaca:

//a) wynikiem dodawania otrzymanych macierzy;
bool wymiaryRowne(std::vector<std::vector<int>> macierzA, std::vector<std::vector<int>> macierzB)
{

    if (macierzA.size() != macierzB.size())
        return false;

    for (unsigned int i = 0; i < macierzA.size(); i++) {
        if (macierzA[i].size() != macierzB[i].size())
            return false;
    }

    return true;
}

std::vector<std::vector<int>> dodaj(std::vector<std::vector<int>> macierzA, std::vector<std::vector<int>> macierzB)
{

    std::vector<std::vector<int>> wynik;

    if (!wymiaryRowne(macierzA, macierzB))
        return wynik;

    for (unsigned int i = 0; i < macierzA.size(); ++i) {
        std::vector<int> wiersz;
        for (unsigned int j = 0; j < macierzA[i].size(); ++j)
            wiersz.push_back(macierzA[i][j] + macierzB[i][j]);
        wynik.push_back(wiersz);
    }

    return wynik;
}

//b) odejmowania pierwszej macierzy od drugiej.
std::vector<std::vector<int>> odejmij(std::vector<std::vector<int>> macierzA, std::vector<std::vector<int>> macierzB)
{

    std::vector<std::vector<int>> wynik;

    if (!wymiaryRowne(macierzA, macierzB))
        return wynik;

    for (unsigned int i = 0; i < macierzA.size(); ++i) {
        std::vector<int> wiersz;
        for (unsigned int j = 0; j < macierzA[i].size(); ++j)
            wiersz.push_back(macierzA[i][j] - macierzB[i][j]);
        wynik.push_back(wiersz);
    }

    return wynik;
}

void test1()
{
    std::vector<std::vector<int>> macierzA{ { 1, 2 }, { -2, 0 } };
    std::vector<std::vector<int>> macierzB{ { 5, -3 }, { 1, 7 } };
    std::vector<std::vector<int>> wynik{ { 6, -1 }, { -1, 7 } };
    assert(dodaj(macierzA, macierzB) == wynik);
}

void test2()
{
    std::vector<std::vector<int>> macierzA{ { 1, 2 }, { -2, 0 } };
    std::vector<std::vector<int>> macierzB{ { 5, -3 }, { 1, 7 } };
    std::vector<std::vector<int>> wynik{ { -4, 5 }, { -3, -7 } };
    assert(odejmij(macierzA, macierzB) == wynik);
}

int main()
{
    test1();
    test2();
    return 0;
}
