#include <cassert>
#include <cmath>
#include "prostokat.h"

void test1() {
	Prostokat prostokatA(2, 5, 7, 2);
	Prostokat prostokatB(3, 6, 9, 4);
	double wynik = 6.00;

	assert(prostokatA.poleCzesciWspolnej(prostokatB) == wynik);
}

void test2() {
	Prostokat prostokatA(-9.5, 10.5, 6, 2);
	Prostokat prostokatB(-4.5, 2.3, 3.8, -3.3);
	double wynik = 12.24;

	assert(abs(prostokatA.poleCzesciWspolnej(prostokatB) - wynik) < 0.01);
}

int main() {

	test1();
	test2();

	return 0;
}
