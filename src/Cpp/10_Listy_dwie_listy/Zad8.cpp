#include <vector>
#include <cassert>
#include <algorithm>

//Otrzymujesz dwie posortowane listy. 
//Polacz je w posortowana liste.

//Zlozonosc obliczeniowa O(n)
//Zlozonosc pamieciowa O(n)
std::vector<int> polaczV1(std::vector<int>& listaA, std::vector<int>& listaB) {

	if (listaA.empty())
		return listaB;
	
	if (listaB.empty())
		return listaA;
	
	std::vector<int> wynik;
	
	unsigned int i = 0;
	unsigned int j = 0;
	
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

	for (unsigned int k = i; k < listaA.size(); k++)
		wynik.push_back(listaA[k]);
	
	for (unsigned int k = j; k < listaB.size(); k++)
		wynik.push_back(listaB[k]);	

	return wynik;
}

void test1() {
	std::vector<int> listaA {5, 7, 11};
	std::vector<int> listaB {1, 3, 8, 14};

	std::vector<int> wynik {1, 3, 5, 7, 8, 11, 14};
	assert(polaczV1(listaA, listaB) == wynik);
}

int main() {

	test1();

	return 0;
}

