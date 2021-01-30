#include <vector>
#include <cassert>
#include <numeric>

//Otrzymujesz dwie listy: wagi oraz wartosci. 
//Znajdz srednia wazona wartosci.
double sredniaWazona(std::vector<double>& wagi, std::vector<double>& wartosci) {

	assert(wagi.size() == wartosci.size());

	double suma = accumulate(wartosci.begin(), wartosci.end(), 0);
	double sumaIloczynow = 0;

	for (unsigned int i = 0; i < wartosci.size(); i++)
		sumaIloczynow += (wartosci[i]*wagi[i]);

	return sumaIloczynow/suma;
}

int main() {

	std::vector<double> wartosci({0, -23, -5, 2, -3, 4, 9});
	std::vector<double> wagi({1, 2, 3, 4, 5, 6, 7});
	
	double wynik = -1.1875;
	assert(sredniaWazona(wagi, wartosci) == wynik);

	wartosci = {2, 5, 0, 2, 1};
	wagi = {0.2, 0.4, 0.1, 0.2, 0.1};
	wynik = 0.29;
	assert(sredniaWazona(wagi, wartosci) == wynik);

	return 0;
}
