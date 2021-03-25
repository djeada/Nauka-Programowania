#include <cassert>
#include <vector>

//Otrzymujesz liste 2d. Obroc otrzymana liste o 90 stopni.
//Tzn. zamien miejscami ostatnia kolumne, z ostatnim wierszem,
//przedostatnią kolumnę z przedostatnim wierszem itd.

void obroc(std::vector<std::vector<int>>& macierz)
{

    int N = macierz.size();

    for (int i = 0; i < N / 2; i++) {
        int first = i + 1;
        int last = N - 1 - i;

        for (int j = first; j < last; j++) {
            int pom = macierz[i][j];
            macierz[i][j] = macierz[N - 1 - j][i];
            macierz[N - 1 - j][i] = macierz[N - 1 - i][N - 1 - j];
            macierz[N - 1 - i][N - 1 - j] = macierz[j][N - 1 - i];
            macierz[j][N - 1 - i] = pom;
        }

        int pom = macierz[i][i];
        macierz[i][i] = macierz[N - 1 - i][i];
        macierz[N - 1 - i][i] = macierz[N - 1 - i][N - 1 - i];
        macierz[N - 1 - i][N - 1 - i] = macierz[i][N - 1 - i];
        macierz[i][N - 1 - i] = pom;
    }
}

void test1()
{
    std::vector<std::vector<int>> macierz{ { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
    std::vector<std::vector<int>> wynik{ { 7, 4, 1 }, { 8, 5, 2 }, { 9, 6, 3 } };

    obroc(macierz);
    assert(macierz == wynik);
}

int main()
{

    test1();

    return 0;
}
