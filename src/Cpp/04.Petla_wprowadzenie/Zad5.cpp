#include <iostream>
using namespace std;

int main(){
	int a, b;
	cin>>a>>b;
	if(b<a){
		int pom=a;
		a = b;
		b = pom;
	}

for(int i=a+1; i<b; i++){
			cout<<i<<" ";
		}
		cout<<endl;
for(int i=a+1; i<b; i++){
			if(i%3==0)
			cout<<i<<" ";
		}
}
