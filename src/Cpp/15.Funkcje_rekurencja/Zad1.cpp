/*
Liczby naturalne mniejsze od N.	
*/

#include <iostream>

using namespace std;

void liczbyNaturalneMniejszeOdN(int N) { 
	
	if (N < 0)
		return;

	cout << N << endl;
	liczbyNaturalneMniejszeOdN(N-1);
}

int main() {
	int N = 10;
	
	liczbyNaturalneMniejszeOdN(N);
	
    return 0;
}

