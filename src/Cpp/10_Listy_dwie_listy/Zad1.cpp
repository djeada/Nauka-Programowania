#include <vector>
#include <iostream>

using namespace std;

//Dla otrzymanych dwoch list wypisz na przemian elemnty pierwszej
//i drugiej listy. Jesli listy nie sa rownej dlugosci, po wyczerpaniu 
//elementow krotszej listy, wypisuj tylko elementy dluzszej listy.

void wypisz(vector<int>& listaA, vector<int>& listaB) {

	int n = listaA.size() < listaB.size() ? listaA.size() : listaB.size();

	for (int i = 0; i < n; i++) {
		cout << listaA[i] << ", ";
		cout << listaB[i] << ", ";
	}
	
	for (int i = n; i < listaA.size(); i++)
		cout << listaA[i] << ", ";

	for (int i = n; i < listaB.size(); i++)
		cout << listaB[i] << ", ";
}

int main() {

	vector<int> listaA({5, 3, 7, 2});
	vector<int> listaB({1, -2, 3});
	
	wypisz(listaA, listaB);

	return 0;
}
