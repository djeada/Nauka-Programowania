#include "punkt.h"

int main() {

	Punkt punktA(5, 5);
	Punkt punktB(-3, -3);

	std::cout << "Odleglosc miedzy punktem A \n" << punktA << "a punktem B \n" << punktB
		<< "wynosi: " << punktA.odleglosc(punktB) << std::endl;

	return 0;
}
