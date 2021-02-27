#include <string>
#include <vector>
#include <cassert>
#include <regex>
#include <sstream>

//Otrzymujesz napis reprezentujacy zdanie. Zapisz w liscie cyfry bedace 
//czescia slow. Cyfry odseparowane od liter spacjami pomin.

std::vector<std::string> cyfry(const std::string& napis)
{
	std::string slowo;
	std::stringstream ss(napis);

	std::vector<std::string> wynik;

    	while (ss >> slowo) {
		if (std::regex_search(slowo, std::regex("[0-9]+")) && std::regex_search(slowo, std::regex("[^0-9]+")))
	        		wynik.push_back(std::regex_replace(slowo, std::regex("[^0-9]*"), ""));
	}

	return wynik;
}

void test1() 
{
	std::string napis = "jerzy29 i an37a s3uc8ali91 lekcji 22 2 jezyka polki3go";
	std::vector<std::string> wynik {"29", "37", "3891", "3"};

	assert(cyfry(napis) == wynik);
}

int main() {

	test1();

	return 0;
}
