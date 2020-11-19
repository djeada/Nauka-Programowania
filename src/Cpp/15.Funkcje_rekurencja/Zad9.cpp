#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

/*
Napisz funkcje, ktora sprawdzi czy otrzymane slowo jest elfickie. 
Elfickie slowo to takie, w ktorym co najmniej raz wystepuje kazda 
z liter slowa elf.
*/

bool czyElfickieSlowoV1(string slowo, string elf = "elf", int i = 0) {

	if (i >= slowo.size())
		return false;
		
	auto litera = slowo[i];

	if (elf.find(litera) != string::npos) {
			elf.erase(remove(elf.begin(), elf.end(), litera), elf.end());
	 		if (elf.empty())
	 			return true;
	}
	
	return czyElfickieSlowoV1(slowo, elf, i + 1);
}

int main () {

	string slowo = "reflektor";
	bool wynik = true;
	
	assert(czyElfickieSlowoV1(slowo) == wynik);
	
	slowo = "elzbieta";
	wynik = false;
	
	assert(czyElfickieSlowoV1(slowo) == wynik);
	
	return 0;
}


