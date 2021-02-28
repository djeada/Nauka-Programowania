#include <vector>
#include <cassert>

//Otrzymujesz liste skladajaca sie z ciagu liter A i B. 
//Litery A reprezentuja samochod jadacy na wschod, a 
//litery B jadacy na zachid.  Samochody jadace w przeciwna 
//stronw mijaja sie. Policz mijajace sie samochody.

int policzSamochodyV1(std::vector<char>& lista) {

	int licznik = 0;
	for (unsigned int i = 0; i < lista.size(); i++) {
		if (lista[i] == 'A') {
			for (unsigned int j = i + 1; j < lista.size(); j++) {
				if (lista[j] == 'B')
					licznik++;
			}
		}
		
		else if (lista[i] == 'B') {
			for (int j = i - 1; j > -1; j--) {
				if (lista[j] == 'A')
					licznik++;
			}
		}
	}

	return licznik/2;
}

int policzSamochodyV2(std::vector<char>& lista) {
	int licznik = 0;
	int pom = 0;

	for (auto x : lista) {
		if (x == 'A')
			pom++;

		else if (x == 'B')
			licznik += pom;
	}

	return licznik;
}

void test1() {
	std::vector<char> lista {'A', 'B', 'A', 'B', 'B'};
    	int wynik = 5;
 	assert(policzSamochodyV1(lista) == wynik);
	assert(policzSamochodyV2(lista) == wynik);
}

void test2() {
	std::vector<char> lista {'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A'};
    	int wynik = 15;
 	assert(policzSamochodyV1(lista) == wynik);
	assert(policzSamochodyV2(lista) == wynik);
}

int main() {
    	
	test1();
	test2();

	return 0;
}
