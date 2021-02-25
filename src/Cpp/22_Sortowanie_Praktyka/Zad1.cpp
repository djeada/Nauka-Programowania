#include <string>
#include <algorithm>
#include <cassert>

//g++-10 -ggdb3 -O0 -std=c++20 -Wall -Wextra -pedantic -o main.out Zad1.cpp

void sortuj (std::string& napis)
{
    std::sort(napis.begin(), napis.end());
}

void test1() 
{
	std::string napis = "bcda";
	std::string wynik = "abcd";

	sortuj(napis);

	assert(napis == wynik);
}

int main() {

	test1();

	return 0;
}
