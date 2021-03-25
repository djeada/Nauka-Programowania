#include <cassert>
#include <cmath>
#include <iostream>

int czyPierwsza(int n)
{

    if (!(n % 2) && n != 2)
        return false;

    for (int i = 3; i <= sqrt((double)n); i += 2) {
        if (!(n % i))
            return false;
    }

    return true;
}

void liczbyPierwszeV1(int n)
{
    for (int i = 2; i <= n; i++) {
        if (czyPierwsza(i))
            std::cout << i << " ";
    }
}

void sitoEratostenesa(int pierwsze[], int liczba)
{
    for (int p = 2; p <= liczba; p++) {
        if (pierwsze[p] == -1)
            continue;

        int n = 2;

        for (int i = p * n; i <= liczba; n++, i = p * n)
            pierwsze[i] = -1;
    }
}

void liczbyPierwszeV2(int liczba)
{

    int pierwsze[liczba + 1] = { 0 };

    sitoEratostenesa(pierwsze, liczba);

    for (int i = 2; i <= liczba; i++) {
        if (pierwsze[i] == 0)
            std::cout << i << " ";
    }
}

int main()
{

    int a = 15;

    liczbyPierwszeV1(a);

    std::cout << std::endl;
    liczbyPierwszeV2(a);

    return 0;
}
