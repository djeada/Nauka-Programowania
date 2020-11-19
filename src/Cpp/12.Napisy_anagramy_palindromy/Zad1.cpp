#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

/*
Sprawdz czy slowo jest palindromem.
*/

bool palindrom(string& slowo) {
	int N = slowo.length() - 1;
	for (int i = 0; i <= N/2; i++) {
		if (slowo[i] != slowo[N - i])
			return false;
	}

	return true;
}

int main() {
    string slowo = "kajak";
	assert(palindrom(slowo)); 
	
	slowo = "Pan";
	assert(!palindrom(slowo)); 

    return 0;
}

