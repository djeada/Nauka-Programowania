/*
Usun pierwsze wystapienie klucza w liscie.
Kolejnosc elementow w liscie powinna zostac zachowana.
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

void usunPierwszeWystapienieV1(vector<int>& lista, int klucz) {
	vector<int>::iterator it = lista.begin();
	while (it != lista.end()) {
		if (*it == klucz) {
		    it = lista.erase(it);
		    return;
		}
		else
		    it++;
	}
}

/*
Usun wszystkie wystapienia klucza z listy.
Kolejnosc elementow w liscie powinna zostac zachowana.
*/

//Zlozonosc Czasowa O(n^2)
//erase przesuwa wszystkie elementy wiec sam ma zlozonosc O(n)
void usunWszystkieWystapieniaV1(vector<int>& lista, int klucz) {
	vector<int>::iterator it = lista.begin();
	while (it != lista.end()) {
		if (*it == klucz)
		    it = lista.erase(it);
		    
		else
		    it++;
	}
}

//Zlozonosc Czasowa O(n)
void usunWszystkieWystapieniaV2(vector<int>& lista, int klucz)
{
   lista.erase(remove(lista.begin(), lista.end(), klucz), lista.end());
}

int main() {
    vector<int> lista({6, 7, 2, 1, 8});
	vector<int> wynik({6, 7, 1, 8});
	int klucz = 2;
	
	usunPierwszeWystapienieV1(lista, klucz);
	
	assert(lista == wynik);
	
	lista = vector<int>({6, 2, 7, 2, 1, 2, 8, 2, 2, 2, 2});
	usunWszystkieWystapieniaV1(lista, klucz);

	lista = vector<int>({6, 2, 7, 2, 1, 2, 8, 2, 2, 2, 2});
	usunWszystkieWystapieniaV2(lista, klucz);

    return 0;
}

//g++ -std=c++14 Zad5.cpp -o exe

