#include <iostream>
#include <cmath>
using namespace std;

int main(){
	int n;
	cin>>n;
	float suma=0;
	for(float i=1; i<=n; i++){
		float a = i/(i+1);
		suma += a;
	}
	cout<<suma<<endl;

suma=0;
	for(float i=1; i<=n; i++){
		float a = (pow(i, 2)+5)/i;
		suma += a;
	}
	cout<<suma<<endl;

suma=0;
	for(float i=1; i<=n; i++){
		float a = i+pow(2, i);
		suma += a;
	}
	cout<<suma<<endl;
}
