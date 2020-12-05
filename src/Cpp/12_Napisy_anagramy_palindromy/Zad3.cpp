#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

/*
Dla podanych dwóch napisów sprawdź czy są swoimi anagramami. 
Dwa napisy są anagramami jesli jeden z nich można zbudować 
poprzez przestawienie znakow w drugim.
*/

bool anagram(string s1, string s2) {

	int N = s1.length();
	int M = s2.length();

	if(N != M) return false;

	int pom[256] = {0};

	for (const auto& znak : s1)
		pom[znak]++;

	for (const auto& znak : s2)
		pom[znak]--;

	for (const auto& x : pom) {
		if (x != 0) 
			return false;
	}

	return true;
}

int main() {
    string s1 = "adam";
	string s2 = "mada";
	string s3 = "dame";

	assert(anagram(s1, s2));
	assert(!anagram(s1, s3));
    
	return 0;
}

//g++ -std=c++14 Zad3.cpp -o exe

