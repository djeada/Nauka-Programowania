/*
Sprawdz czy slowoA rozpoczyna sie od slowaB. Zignoruj roznice miedzy malymi i wielkimi literami.
*/

#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>

using namespace std;

bool rozpoczynaSieV1(string slowoA, string slowoB)
{
    transform(slowoA.begin(), slowoA.end(), slowoA.begin(), ::tolower);
    transform(slowoB.begin(), slowoB.end(), slowoB.begin(), ::tolower);

    return !slowoA.find(slowoB);
}

int main()
{

    //Testy Poprawnosci
    string slowoA = "Dinozaur jest zly";
    string slowoB = "Dino";

    assert(rozpoczynaSieV1(slowoA, slowoB) == true);

    slowoA = "Dinozaur jest zly";
    slowoB = "Pies";

    assert(rozpoczynaSieV1(slowoA, slowoB) == false);

    return 0;
}
