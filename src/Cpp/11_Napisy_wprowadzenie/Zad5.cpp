#include <iostream>

//Otrzymujesz napis oraz liczbe k. 
//a) wypisz poziomo co k-ty znak. Znaki powinny byc oddzielone spacjami.
void wypiszPoziomo(const std::string& napis, int k) {


	for (unsigned int i = 0; i < napis.size(); i += k)
		std::cout << napis[i] << ", ";
	
	std::cout << std::endl;
}

//b) wypisz pionowo co k-ty znak. Znaki powinny byc oddzielone enterami.
void wypiszPionowo(const std::string& napis, int k) {

	for (unsigned int i = 0; i < napis.size(); i += k)
		std::cout << napis[i] << std::endl;
}

int main() {
	std::string napis = "hej dzieci jesli chcecie zobaczyc smerfow las";
	int k = 3;
	wypiszPoziomo(napis, k);
	wypiszPionowo(napis, k);

	return 0;
}


