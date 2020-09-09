/*
Znajdz i zamien wszystkie wystapienia slowa w zdaniu na inne podane slowo.
*/

#include <iostream>
#include <string>
#include <cassert>

using namespace std;

string zamienWszystkoV1(string zdanie, string napisA, string napisB) {

    auto k = zdanie.find(napisA);

    while (k != string::npos) {
        zdanie.replace(k, napisA.size(), napisB);
        k = zdanie.find(napisA, k  + napisB.size());
    }
    
    return zdanie;
}

int main() {

	//Testy Poprawnosci
    string zdanie = "Lezy jezy na wiezy";
	string napisA = "zy";
    string napisB = "rzy";
	string wynik = "Lerzy jerzy na wierzy";
	
	
	assert(zamienWszystkoV1(zdanie, napisA, napisB) == wynik);

    return 0;
}

