#include <iostream>
using namespace std;

int main() {
	//Na farmie mamy a glow i b nog, znajdz liczbe kur oraz owieczek.
	
	cout << "Podaj dwie liczby: " << endl;
	int g, n;
	cin >> g >> n;
	
 	for (int i = 0; i < g; i++) {
		int o = g - i;
		if (2*i + 4*o == n) {
			cout << i << " " << o << endl;
			break;
		}
	}
}
