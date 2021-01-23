#include <cassert>
#include <string>

using namespace std;

// Przy uzyciu operatorow bitowych:
//a) Zamien wielkie litery na male.
string wielkieNaMale(string slowo) {
	string wynik = "";
	
	for (const int& litera : slowo)
		wynik += (char)(litera | (int)' ');
		
	return wynik;
}


//b) Zamien male litery na wielkie.
string maleNaWielkie(string slowo) {
	string wynik = "";

	for (const int& litera : slowo)
		wynik += (char)(litera & (int)'_');
		
	return wynik;
}

//c) Zamien male litery na wielkie i wielkie na male.
string odwrocWielkoscLiter(string slowo) {

	string wynik = "";

	for (const int& litera : slowo) {

		if (litera >= 'a' and litera <= 'z')
			wynik += (char)(litera ^ (int)' ');
			
		else if (litera >= 'A' and litera <= 'Z')
			wynik += (char)(litera ^ (int)' ');
		
		else
			wynik += (char)litera;
	}
		
	return wynik;
}

void test1() {
	string slowo = "KURCZAKU";
	string wynik = "kurczaku";

	assert(wielkieNaMale(slowo) == wynik);
}

void test2() {
	string slowo = "piesek";
	string wynik = "PIESEK";

	assert(maleNaWielkie(slowo) == wynik);
}

void test3() {
	string slowo = "wszedl Kotek na PloteK i mrUga";
	string wynik = "WSZEDL kOTEK NA pLOTEk I MRuGA";

	assert(odwrocWielkoscLiter(slowo) == wynik);
}


int main() {

	test1();
	test2();
	test3();

	return 0;
}

