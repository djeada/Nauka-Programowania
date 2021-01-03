#include <vector>
#include <cassert>
#include <algorithm>
#include <unordered_set>

using namespace std;

//Otrzymujesz dwie listy. Usun z pierwszej listy te 
//elementy, ktore wystepuja rowniez w drugiej liscie.

//Zlozonosc obliczeniowa O(n^2)
//Zlozonosc pamieciowa O(n)
void usunCzescWspolnaV1(vector<int>& listaA, vector<int>& listaB) {

	auto it = listaA.begin();

	while (it != listaA.end()) {
		if (find(listaB.begin(), listaB.end(), *it) != listaB.end())
			listaA.erase(it);
		else
			it++;
	}
}


int main() {

	vector<int> listaA({3, 6, 2, 7, 9});
	vector<int> listaB({4, 2, 3, 5, 6});
	vector<int> wynik({7, 9});
	
	usunCzescWspolnaV1(listaA, listaB);

	assert(listaA == wynik);

	return 0;
}

