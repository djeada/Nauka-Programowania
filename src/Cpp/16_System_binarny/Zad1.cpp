#include <cassert>
#include <string>
#include <cmath>

#define naLiczbe(c) (c-'0')

using namespace std;

//Otrzymujesz liczbe, zamien ja na:
//a) jej odpowiednik w systemie binarnym.
int naDec(string liczba) {
	int dec = 0;
   	int n = liczba.size();
	for (int i = 0; i < n; i++)
		dec += pow(2, n - i - 1) * naLiczbe(liczba[i]);

	return dec;
}

//b) jej odpowiednik w systemie dziesiętnym.
string naBin(int liczba) {
	
	string bin;

	while (liczba > 0) {
		bin.insert(0, to_string(liczba % 2));
		liczba /= 2;
	}
	
	return bin;
}

void test1() {
	string liczba = "0011";
	int wynik = 3;

	assert(naDec(liczba) == wynik);
}

void test2() {
	string liczba = "1111100";
	int wynik = 124;

	assert(naDec(liczba) == wynik);
}

void test3() {
	int liczba = 124;
	string wynik = "1111100";

	assert(naBin(liczba) == wynik);
}

void test4() {
	int liczba = 3;
	string wynik = "11";

	assert(naBin(liczba) == wynik);
}

int main() {

	test1();
	test2();
	test3();
	test4();

	return 0;
}

