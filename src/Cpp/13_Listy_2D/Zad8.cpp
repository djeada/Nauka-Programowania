#include <algorithm>
#include <cassert>
#include <vector>

//Otrzymujesz liste 2d. Zbierz spiralnie elementy
//otrzymanej listy i zapisz je w zwyklej liscie.

std::vector<int> spiralaV1(std::vector<std::vector<int>>& macierz)
{
    std::vector<int> wynik;

    int x = macierz[0].size();
    int y = macierz.size();
    int k = 0;
    int l = 0;

    while (k < y && l < x) {

        for (int i = l; i < x; i++)
            wynik.push_back(macierz[k][i]);

        k++;

        for (int i = k; i < y; i++)
            wynik.push_back(macierz[i][x - 1]);

        x--;

        if (k < x) {

            for (int i = x - 1; i > l - 1; i--)
                wynik.push_back(macierz[y - 1][i]);
            y--;
        }

        if (l < y) {

            for (int i = y - 1; i > k - 1; i--)
                wynik.push_back(macierz[i][l]);
            l++;
        }
    }

    return wynik;
}

void test1()
{
    std::vector<std::vector<int>> macierz{ { 1, 2, 3, 4, 5 },
        { 16, 17, 18, 19, 6 },
        { 15, 24, 25, 20, 7 },
        { 14, 23, 22, 21, 8 },
        { 13, 12, 11, 10, 9 } };

    std::vector<int> wynik{ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
        12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25 };

    assert(spiralaV1(macierz) == wynik);
}

void test2()
{
    std::vector<std::vector<int>> macierz{ { 1, 2, 3 },
        { 4, 5, 6 },
        { 7, 8, 9 } };

    std::vector<int> wynik{ 1, 2, 3, 6, 9, 8, 7, 4, 5 };

    assert(spiralaV1(macierz) == wynik);
}

int main()
{
    test1();
    test2();
    return 0;
}
