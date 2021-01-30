#include "macierz.h"

Macierz::Macierz(const std::vector<std::vector<int>> _macierz) :
	macierz(_macierz) {
}

void Macierz::setElement(unsigned int wiersz, unsigned int kolumna, int wartosc) {
	if (wiersz >= wiersze() || kolumna >= kolumny())
		throw std::invalid_argument("Nieprawidlowy indeks.");

	macierz[wiersz][kolumna] = wartosc;
}

int Macierz::element(unsigned int wiersz, unsigned int kolumna) const {

	if (wiersz >= wiersze() || kolumna >= kolumny())
		throw std::invalid_argument("Nieprawidlowy indeks.");

	return macierz[wiersz][kolumna];
}

unsigned int Macierz::wiersze() const {
	return macierz.size();
}

unsigned int Macierz::kolumny() const {
	if (wiersze() >= 1)
		return macierz.front().size();
	else
		return 0;
}

Macierz Macierz::operator + (const Macierz &innaMacierz) {
	
	if (wiersze() != innaMacierz.wiersze() || kolumny() != innaMacierz.kolumny())
		throw std::invalid_argument("Wymiary macierzy musza byc jednakowe.");


	Macierz pom(std::vector<std::vector<int>>(wiersze(), std::vector<int>(kolumny())));

	for (unsigned int i = 0; i < pom.wiersze(); i++)
		for (unsigned int j = 0; j < pom.kolumny(); j++)
			pom.setElement(i,j, element(i, j) + innaMacierz.element(i, j));

	return pom;
}

Macierz Macierz::operator - (const Macierz &innaMacierz) {
	
	if (wiersze() != innaMacierz.wiersze() || kolumny() != innaMacierz.kolumny())
		throw std::invalid_argument("Wymiary macierzy musza byc jednakowe.");


	Macierz pom(std::vector<std::vector<int>>(wiersze(), std::vector<int>(kolumny())));

	for (unsigned int i = 0; i < pom.wiersze(); i++)
		for (unsigned int j = 0; j < pom.kolumny(); j++)
			pom.setElement(i,j, element(i, j) - innaMacierz.element(i, j));

	return pom;
}


Macierz Macierz::operator * (const Macierz &innaMacierz) {
	
	if (kolumny() != innaMacierz.wiersze())
		throw std::invalid_argument("Liczba kolumn mnoznej musi sie rownac liczbie wierszy mnoznika.");

 	const unsigned int n = wiersze();
    	const unsigned int m = kolumny();
    	const unsigned int p = innaMacierz.kolumny();

	Macierz pom(std::vector<std::vector<int>>(n, std::vector<int>(p)));

	for (unsigned int j = 0; j < p; j++) {
		for (unsigned int k = 0; k < m; k++) {
			for (unsigned int i = 0; i < n; i++) 
				pom.setElement(i,j, pom.element(i,j) + element(i, k) * innaMacierz.element(k, j));
		}
	}

	return pom;
}

std::ostream& operator << (std::ostream& out, Macierz& p){

	for (const auto& wiersz : p.macierz) {
		for (const auto& wartosc : wiersz)
			std::cout << wartosc << " ";
		std::cout << std::endl;
	}

	return out;
}

bool operator == (const Macierz &p1, const Macierz &p2){
	return p1.macierz == p2.macierz;
}

bool operator != (const Macierz &p1, const Macierz &p2){
	return p1.macierz != p2.macierz;
}

