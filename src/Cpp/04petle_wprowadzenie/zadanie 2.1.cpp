#include <iostream>
using namespace std;

int main(){
	int a;
	cin>>a;
	int liczba = 0;
	for(int i=1; i<a; i++){
		liczba += i;
	}
	cout<<liczba;
}
