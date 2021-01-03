#include <vector>
#include <cassert>

using namespace std;

//Otrzymujesz dwie listy liczb reprezentujacych 
//wspolrzedne dwoch wektorow. Zrealizuj:
//a) mnozenie sklarne.
int mnozenieSkalarne(vector<int>& listaA, vector<int>& listaB) {

	assert(listaA.size() == listaB.size());

	int wynik = 0; 

	for (int i = 0; i < listaA.size(); i++) 
		wynik += listaA[i] * listaB[i]; 
	
	return wynik; 
}

//b) mnozenie wektorowe.
vector<int> mnozenieWektorowe(vector<int>& listaA, vector<int>& listaB) {

	assert(listaA.size() == listaB.size() && listaA.size() == 3);

	vector<int> wynik;
	wynik.push_back(listaA[1] * listaB[2] - listaA[2] * listaB[1]); 
	wynik.push_back(listaA[2] * listaB[0] - listaA[0] * listaB[2]); 
	wynik.push_back(listaA[0] * listaB[1] - listaA[1] * listaB[0]); 

	return wynik;
}

int main() {

	vector<int> listaA({3, -5, 4});
	vector<int> listaB({2, 6, 5});

	int iloczynSkalar = -4;
	assert(mnozenieSkalarne(listaA, listaB) == iloczynSkalar);

	vector<int> iloczynWekt({-49, -7, 28});
	assert(mnozenieWektorowe(listaA, listaB) == iloczynWekt);

	return 0;
}

