#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>

using namespace std;

/*
Znajdz najdluzsze powtorzenie w napisie.
*/

string nwp(string& slowoA, string& slowoB)
{

    int N = slowoA.length() < slowoB.length() ? slowoA.length() : slowoB.length();

    for (int i = 0; i < N; i++) {
        if (slowoA[i] != slowoB[i])
            return slowoA.substr(0, i);
    }

    return slowoA.substr(0, N);
}

string najdluzszePowtorzenieV1(string& slowo)
{

    string maks;

    int N = slowo.length();

    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            string slowoA = slowo.substr(i, N);
            string slowoB = slowo.substr(j, N);
            string podslowo = nwp(slowoA, slowoB);

            if (podslowo.length() > maks.length())
                maks = podslowo;
        }
    }

    return maks;
}

int main()
{

    //Testy Poprawnosci
    string slowo = "98432934021742343230";
    string wynik = "432";

    assert(najdluzszePowtorzenieV1(slowo) == wynik);

    return 0;
}
