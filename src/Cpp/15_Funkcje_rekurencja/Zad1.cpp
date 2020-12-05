#include <iostream>
#include <cassert>

using namespace std;

/*
Liczby naturalne mniejsze rowne N.	
*/

string mniejszeLiczbyV1(int n) {
		
	if (n < 0)
		return "";

	if (n == 0)
		return to_string(n);

	return to_string(n) + ", " + mniejszeLiczbyV1(n-1);
}

int main() {
	int n = 10;
	string wynik = "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0";
	cout << mniejszeLiczbyV1(n);
	
    return 0;
}

