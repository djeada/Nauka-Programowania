#include <numbers> 
#include <cmath>
#include "kolo.h"

Kolo::Kolo(double r)  {
	if (r <= 0) {
		std::cout << "Promien nie moze byc liczba ujemna." <<std::endl; 
		std::cout << "Promien ustawiono na 1" << std::endl; 
		promien = 1.0; 
	}

	else 
		promien = r;
}

void Kolo::setPromien(double r) {
	promien =r; 
}

double Kolo::getPromien() {
	return promien; 
}

double Kolo::pole() {
	return std::numbers::pi*pow(promien, 2);
}

double Kolo::obwod() {
	return 2*std::numbers::pi*promien; 
}

double Kolo::srednica() {
	return 2*promien;
}

std::ostream& operator << (std::ostream& out, Kolo& k){
	std::cout << "Promien = " << k.promien << std::endl; 
	std::cout << "Srednica = " << k.srednica() << std::endl; 
	std::cout << "Pole = " << k.pole() << std::endl;
	std::cout << "Obwod = " << k.obwod() << std::endl; 

	return out;
} 
