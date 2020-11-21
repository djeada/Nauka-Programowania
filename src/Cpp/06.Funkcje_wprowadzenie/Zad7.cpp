#include <string>
#include <iostream>

using namespace std;

//Napisz dwie funkcje. Pierwsza powinna porsic uzytkownika o podanie 
//nazwy i hasla oraz zwracac otrzymane dane.

void inicjalizacjaDanych(string& nazwa, string& haslo) {
	cout << "podaj nazwe oraz haslo do zapamietania" << endl;
	cin >> nazwa >> haslo;
}

//Druga powinna otrzymywac dane od pierwszej i ponownie prosic o
//podanie nazwy oraz hasla, dopoki dane nie beda identyczne z tymi
//podanymi za pierwszym razem.

void czyDanePoprawne(string& nazwa, string& haslo) {
	
	string nowaNazwa;
	string noweHaslo;

	while (nowaNazwa != nazwa || noweHaslo != haslo) {
		cout << "Aby zalogowac sie do systemu: podaj nazwe oraz haslo" << endl;
		cin >> nowaNazwa >> noweHaslo;
	}

	cout << "Logowanie do systemu przebieglo pomyslnie" << endl;
}


int main() {
	string nazwa;
	string haslo;
	inicjalizacjaDanych(nazwa, haslo);
	czyDanePoprawne(nazwa, haslo);

	return 0;
}
