#include <string>
#include <algorithm>
#include <cassert>
#include <vector>

//Znajdz wszystkie wyjatkowe palindromy jakie mozna utworzyc ze znakow 
//w slowie (bez zmiany kolejnosci).		
//Wyjatkowy palindrom spelnia jeden z dwoch warunkow:
//1. Wszystkie znaki sa identyczne, np. “xxx”.
//2. Wszystkie znaki poza srodkowym znakiem są identyczne, np. “ccdcc”.
//Pojedynczy znak jest rowniez uznawany za wyjatkowy palindrom.
//Nie uwzgledniaj duplikatow w liscie.

std::vector<std::string> wyjatkowePalindromy(const std::string& slowo) {
	std::vector<std::string> wynik;
	
	for (unsigned int i = 0; i < slowo.size(); i++) {
		wynik.push_back(std::string(1, slowo[i]));

		unsigned int j = i + 1;
	 	unsigned int k = 0;
		while (j < slowo.size() && slowo[i] == slowo[j])
			j++;

		if (j > i + 1)
			wynik.push_back(slowo.substr(i,i-j));

		if (j + 1 < slowo.size() && slowo[i] == slowo[j + 1])
			k = j + 1;

		while (k > i && slowo[i] == slowo[k])
			k--;

		if (i + 1 == k)
			wynik.push_back(slowo.substr(i, 2*(j-i) + 1));
	}

	return wynik;
}

bool wektoryRowne(std::vector<std::string> v1, std::vector<std::string> v2) {
	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());
	return v1 == v2;
}

void test1() {
	std::string slowo = "xxxx";
	std::vector<std::string> wynik {"x", "xxxx", "x", "xxx", "x", "xx", "x"};
	assert(wektoryRowne(wyjatkowePalindromy(slowo), wynik)); 
}

void test2() {
	std::string slowo;
	std::vector<std::string> wynik;
	assert(wektoryRowne(wyjatkowePalindromy(slowo), wynik)); 
}

int main() {
	test1();
	test2();
	return 0;
}

