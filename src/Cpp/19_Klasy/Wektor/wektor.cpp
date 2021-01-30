#include <cmath>
#include "wektor.h"

Wektor::Wektor(double _x, double _y, double _z) :
	x(_x),
	y(_y),
	z(_z) {
}

void Wektor::setX(double _x) {
	x = _x; 
}

void Wektor::setY(double _y) {
	y = _y;
}

void Wektor::setZ(double _z) {
	z = _z;
}

double Wektor::getX() {
	return x;
}

double Wektor::getY() {
	return y;
}

double Wektor::getZ() {
	return z;
}

double Wektor::modul() {
	double kwadratX = pow(x, 2);
	double kwadratY = pow(y, 2);
	double kwadratZ = pow(z, 2);
		
	return sqrt(kwadratX + kwadratY + kwadratZ);
}

Wektor operator + (const Wektor& w1, const Wektor& w2){
	Wektor w3(w1.x + w2.x, w1.y + w2.y, w1.z + w2.z);
	return w3;
}

Wektor operator - (const Wektor& w1, const Wektor& w2){
	Wektor w3(w1.x - w2.x, w1.y - w2.y, w1.z - w2.z);
	return w3;
}

Wektor operator * (const Wektor& w1, const Wektor& w2){
	double x = w1.y * w2.z - w1.z * w2.y; 
	double y = w1.z * w2.x - w1.x * w2.z; 
	double z = w1.x * w2.y - w1.y * w2.x; 

	return Wektor(x, y, z);
}

std::ostream& operator << (std::ostream& out, Wektor& w){
	std::cout << "X = " << w.x << std::endl; 
	std::cout << "Y = " << w.y << std::endl;
	std::cout << "Z = " << w.z << std::endl; 
	return out;
}

bool operator == (const Wektor& w1, const Wektor& w2){
	return w1.x == w2.x && w1.y == w2.y && w1.z == w2.z;
}

bool operator != (const Wektor& w1, const Wektor& w2){
	return w1.x != w2.x || w1.y != w2.y || w1.z != w2.z;
}

