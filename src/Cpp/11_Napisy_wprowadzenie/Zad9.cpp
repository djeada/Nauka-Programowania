#include <cassert>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>

using namespace std;

//Otrzymujesz rekord z bazy danych reprezentujacy dane pracownika. 
//Sa to kolejno: imie, nazwisko, miejsce urodzenia, stanowisko i zarobki. 
//Informacje rozdzielone sa srednikami. Zapisz je w osobnych zmiennych 
//i wypisz wraz z komunikatem.

vector<string> dane(string& napis) {

	vector<string> wynik;
	stringstream ss(napis);

	for (string slowo; ss >> slowo;) {
		if (slowo.size() > 1) {
			wynik.push_back(slowo.substr(0, slowo.size()-1));    
			if (ss.peek() == ';')
				ss.ignore();
		}	
	}

	return wynik;
}

void wypiszDane(string& napis) {
	
	vector<string> wynik = dane(napis);
	assert(wynik.size() == 5);

	cout << "Imie: " << wynik[0] << endl;
	cout << "Nazwisko: " << wynik[1] << endl;
	cout << "Miejsce urodzenia: " << wynik[2] << endl;
	cout << "Zawod: " << wynik[3] << endl;
	cout << "Zarobki: " << wynik[4] << endl;
}
	
int main() {
	string napis = "Jan; Kowalski; Warszawa; Programista; 1000";
	wypiszDane(napis);
	return 0;
}


