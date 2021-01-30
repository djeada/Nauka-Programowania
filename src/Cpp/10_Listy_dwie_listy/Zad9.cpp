#include <vector>
#include <cassert>
#include <algorithm>

//Otrzymujesz dwie listy. Usun z pierwszej listy te 
//elementy, ktore wystepuja rowniez w drugiej liscie.

//Zlozonosc obliczeniowa O(n^2)
//Zlozonosc pamieciowa O(n)
void usunCzescWspolnaV1(std::vector<int>& listaA, std::vector<int>& listaB) {

	auto it = listaA.begin();

	while (it != listaA.end()) {
		if (find(listaB.begin(), listaB.end(), *it) != listaB.end())
			it = listaA.erase(it);
		else
			it++;
	}
}


int main() {

	std::vector<int> listaA({3, 6, 2, 7, 9});
	std::vector<int> listaB({4, 2, 3, 5, 6});
	std::vector<int> wynik({7, 9});
	
	usunCzescWspolnaV1(listaA, listaB);

	assert(listaA == wynik);

	return 0;
}

