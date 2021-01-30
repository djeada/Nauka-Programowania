#include <cmath>
#include "punkt.h"

Punkt::Punkt(double _x, double _y) :
	x(_x),
	y(_y) {
}

void Punkt::setX(double _x) {
	x = _x; 
}

void Punkt::setY(double _y) {
	y = _y;
}

double Punkt::getX() {
	return x;
}

double Punkt::getY() {
	return y;
}

double Punkt::odleglosc(Punkt& innyPunkt) {
	double odlegloscX = x - innyPunkt.getX();
	double odlegloscY = y - innyPunkt.getY();

	return sqrt(pow(odlegloscX,2) + pow(odlegloscY,2));
}

std::ostream& operator << (std::ostream& out, Punkt& p){
	std::cout << "X = " << p.x << std::endl; 
	std::cout << "Y = " << p.y << std::endl; 
	return out;
}

bool operator == (const Punkt &p1, const Punkt &p2){
	return p1.x == p2.x && p1.y == p2.y;
}

bool operator != (const Punkt &p1, const Punkt &p2){
	return p1.x != p2.x || p1.y != p2.y;
}

