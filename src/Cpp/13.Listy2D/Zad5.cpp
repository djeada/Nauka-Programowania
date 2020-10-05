#include <iostream>
#include <cassert>

using namespace std;

vector<vector<int>> pomnozV1(vector<vector<int>> a, vector<vector<int>> b)
{
	vector<vector<int>> c;

	for (int i = 0; i < a.size(); i++)
		for (int j = 0; j < b.size(); j++)
			for (int k = 0; k < a[0].size(); k++)
				c[i][j] = a[i][k]*b[k][j];
	
	return c;	
}

vector<vector<int>> pomnozV2(vector<vector<int>> a, vector<vector<int>> b) {
	static int i = 0, j = 0, k = 0;

	if(i < M1) {
		if(j < N2) {
			if(k < N1) {
				c[i][j] += a[i][k]*b[k][j];
				k++;
				matmulr(a,b,c);
			}
			k = 0;
		        j++;
			matmulr(a,b,c);
		}
		j = 0;
		i++;
		matmulr(a,b,c);
	}

	return c;
}

int main()
{


	
	
	return 0;	 	
}
