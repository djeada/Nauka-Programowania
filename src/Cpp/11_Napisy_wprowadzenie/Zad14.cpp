#include <cassert>
#include <string>
#include <algorithm>

using namespace std;

//Otrzymujesz liczbę n. Zwroc napis skladajacy 
//sie z liczb naturalnych od 1 do n.

string liczby(int n) {
	string wynik = "";
	
	for (int i = 1; i <= n; i++)
		wynik += to_string(i);

	return wynik;
}

void test1() {
	int n = 5;
	string wynik = "12345";
	assert(liczby(n) == wynik);
}

void test2() {
	int n = -1;
	string wynik = "";
	assert(liczby(n) == wynik);
}

int main() {
	test1();
	test2();
	return 0;
}


