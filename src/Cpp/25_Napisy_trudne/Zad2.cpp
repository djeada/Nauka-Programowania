/*
Znajdz i usun wszystkie wystapienia slowa w zdaniu.
*/

#include <cassert>
#include <iostream>
#include <string>

using namespace std;

string usunWszystkieV1(string zdanie, const string slowo)
{
    auto k = zdanie.find(slowo);

    while (k != string::npos) {
        zdanie.erase(k, slowo.length());
        k = zdanie.find(slowo);
    }

    return zdanie;
}

int main()
{

    //Testy Poprawnosci
    string zdanie = "Lezy jezy na wiezy";
    string slowo = "zy";
    string wynik = "Le je na wie";

    assert(usunWszystkieV1(zdanie, slowo) == wynik);

    return 0;
}
