#include <cassert>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

//Otrzymujesz napis oraz liczbe k. 
//a) wypisz poziomo co k-ty znak. Znaki powinny byc oddzielone spacjami.
void wypiszPoziomo(const string& napis, int k) {

	assert(k > 0);

	for (int i = 0; i < napis.size(); i += k)
		cout << napis[i] << ", ";
	
	cout << endl;
}

//b) wypisz pionowo co k-ty znak. Znaki powinny byc oddzielone enterami.
void wypiszPionowo(const string& napis, int k) {

	assert(k > 0);

	for (int i = 0; i < napis.size(); i += k)
		cout << napis[i] << endl;
}

int main() {
	string napis = "hej dzieci jesli chcecie zobaczyc smerfow las";
	int k = 3;
	wypiszPoziomo(napis, k);
	wypiszPionowo(napis, k);

	return 0;
}


