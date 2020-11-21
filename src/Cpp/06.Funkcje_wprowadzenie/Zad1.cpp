#include <cassert>
#include <string>

using namespace std;

//Napisz funkcje ktora zwroci
//a) liczbe 3

int funkcja1() {
	return 3;
}

//b) napis "Tak"
string funkcja2() {
	return "Tak";
}

//c) wartosc logiczna prawda
bool funkcja3() {
	return true;
}

int main() {
	assert(funkcja1() == 3);
	assert(funkcja2() == "Tak");
	assert(funkcja3());

	return 0;
}
