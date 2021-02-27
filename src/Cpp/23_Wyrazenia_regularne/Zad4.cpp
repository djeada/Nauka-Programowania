#include <string>
#include <cassert>
#include <regex> 

//Otrzymujesz dwa napisy. Sprawdz czy drugi wystepuje w pierwszym.

bool nalezyDoZdania(std::string& zdanie, std::string& napis)
{
	return regex_search(zdanie, std::regex(napis));
}

void test1() 
{
	std::string zdanie = "Mozart gra na skrzypcach";
	std::string napis = "skrzyp";
	assert(nalezyDoZdania(zdanie, napis));
}

void test2() 
{
	std::string zdanie = "Lezy jerzy na wiezy";
	std::string napis = "nan";
	assert(!nalezyDoZdania(zdanie, napis));
}

int main() {

	test1();
	test2();

	return 0;
}
