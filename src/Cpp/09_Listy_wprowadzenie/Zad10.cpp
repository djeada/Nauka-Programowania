#include <vector>
#include <cassert>
#include <cmath>

using namespace std;

//Otrzymujesz dokladnie 6 liczb. Otrzymane liczby stanowia 
//odpowienio wspolrzedne xA, yA, xB, yB, xC, yC. Sprawdz
//czy punkty A, B oraz C moga stanowic wierzcholki trojkata.

int odleglosc(int x1, int y1, int x2, int y2) {
	int roznicaX = x1 - x2;
	int roznicaY = y1 - y2;
	int sumaKwadratow = pow(roznicaX, 2) + pow(roznicaY, 2);
	return sqrt(sumaKwadratow);
}

bool czyTrojkatV1(vector<int>& wsplX, vector<int>& wsplY) {

	assert(wsplX.size() == wsplY.size() && wsplX.size() == 3);

	int odlegloscAB = odleglosc(wsplX[0], wsplY[0], wsplX[1], wsplY[1]);
	int odlegloscBC = odleglosc(wsplX[2], wsplY[2], wsplX[1], wsplY[1]);
	int odlegloscAC = odleglosc(wsplX[0], wsplY[0], wsplX[2], wsplY[2]);

	return (odlegloscAB + odlegloscBC) > odlegloscAC && (odlegloscAB + odlegloscAC) > odlegloscBC
		&& (odlegloscAC + odlegloscBC) > odlegloscAB;
}

bool czyTrojkatV2(vector<int>& wsplX, vector<int>& wsplY) {

	assert(wsplX.size() == wsplY.size() && wsplX.size() == 3);

	int a = wsplX[0]*(wsplY[1] - wsplY[2]) + wsplX[1]*(wsplY[2] - wsplY[0]) +  
            	wsplX[2]*(wsplY[0] - wsplY[1]); 
	
	return a != 0;
}

int main() {
    	vector<int> wsplX({-2, 7, 8});
    	vector<int> wsplY({4, 5, -8});
	assert(czyTrojkatV1(wsplX, wsplY));
	assert(czyTrojkatV2(wsplX, wsplY));

	wsplX = {0, 2, 5};
    	wsplY = {0, -2, -5};
	assert(!czyTrojkatV2(wsplX, wsplY));
	assert(!czyTrojkatV2(wsplX, wsplY));

	return 0;
}
