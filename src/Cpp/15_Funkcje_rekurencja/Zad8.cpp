#include <cassert>
#include <vector>

using namespace std;

/*
Wieza Hanoi.
*/

void hanoiWew(int n, char a, char b, char c, vector<pair<char,char>>& wynik) {

	if (n == 1) {
		wynik.emplace_back(a, b);
		return;
	}

	hanoiWew(n - 1, a, c, b, wynik);
	wynik.emplace_back(a, b);
	hanoiWew(n - 1, c, b, a, wynik);
}

vector<pair<char,char>> hanoi(int n) { 
	vector<pair<char,char>> wynik;
	hanoiWew(n, 'A', 'B', 'C', wynik);
	return wynik;
}

int main() {
	int n = 3;
	vector<pair<char, char>> wynik = { {'A', 'B'}, {'A', 'C'}, {'B', 'C'}, 
		{'A', 'B'}, {'C', 'A'}, {'C', 'B'}, {'A', 'B'}};
	
	assert(hanoi(n) == wynik);
		
    return 0;
}

