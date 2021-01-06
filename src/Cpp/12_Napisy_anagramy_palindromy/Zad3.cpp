#include <string>
#include <cassert>

using namespace std;

/*
Dla podanych dwóch napisów sprawdź czy są swoimi anagramami. 
Dwa napisy są anagramami jesli jeden z nich można zbudować 
poprzez przestawienie znakow w drugim.
*/

//Zlozonosc czasowa O(n)
//Zlozonosc pamieciowa O(1)
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

void test1() {
	string s1 = "adam";
	string s2 = "mada";
	assert(anagram(s1, s2));
}

void test2() {
	string s1 = "adam";
	string sw = "dame";
	assert(!anagram(s1, sw));
}

int main() {
	test1();
	test2();
	return 0;
}

