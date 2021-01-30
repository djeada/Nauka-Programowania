#include <iostream>
#include "zespolona.h"

int main(){

	Zespolona z1;
	Zespolona z2(9, 12);
	
	std::cout << z1;
	std::cout << z2;
	
	std::cout << z1 * z2;
	
	Zespolona z3(-3,-3);
	
	std::cout << z3 + z2;
	std::cout << z3 / z2;
	
	z2.Sprzezenie();
	
	std::cout << z2;
	
	std::cout << z3.Modul() << std::endl;
	
	return 0;
}
