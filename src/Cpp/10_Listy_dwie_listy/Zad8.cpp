#include <vector>
#include <cassert>
#include <algorithm>
#include <unordered_set>

using namespace std;

//Otrzymujesz dwie posortowane listy. 
//Polacz je w posortowana liste.

//Zlozonosc obliczeniowa O(n)
//Zlozonosc pamieciowa O(n)
vector<int> polaczV1(vector<int>& listaA, vector<int>& listaB) {

	if (listaA.empty())
		return listaB;
	
	if (listaB.empty())
		return listaA;
	
	vector<int> wynik;
	
	int i = 0;
	int j = 0;
	
	while (i < listaA.size() && j < listaB.size()) {
		if (listaA[i] < listaB[j]) {
			wynik.push_back(listaA[i]);
			i++;
		}
		else {
			wynik.push_back(listaB[j]);
			j++;
		}
	}

	for (int k = i; k < listaA.size(); k++)
		wynik.push_back(listaA[k]);
	
	for (int k = j; k < listaB.size(); k++)
		wynik.push_back(listaB[k]);	

	return wynik;
}

int main() {

	vector<int> listaA({5, 7, 11});
	vector<int> listaB({1, 3, 8, 14});

	vector<int> wynik({1, 3, 5, 7, 8, 11, 14});
	assert(polaczV1(listaA, listaB) == wynik);

	return 0;
}

