#include <iostream>

using namespace std;

void pascal(int n) {

	for (int i = 1; i <= n; ++i) {
		int k = 1;
		for(int j = 1; j <= n-i; ++j)
			cout << " ";

		for (int j = 1; j <= i; j++) { 
			cout << k << " ";  
			k *= (i - j) / j;  
		} 

		cout << endl;
	}
}

int main () {

	int a = 5;
	pascal(a);
	
	return 0;
}


