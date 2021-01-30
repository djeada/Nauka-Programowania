#ifndef zespolona_h
#define zespolona_h

#include <iostream>

using namespace std;

class Zespolona {
	private:
		double Re;
		double Im;
	public:
		Zespolona();
		Zespolona(double a, double b);
		
		double Modul();
		void Sprzezenie();
		
		friend Zespolona operator + (const Zespolona &z1, const Zespolona &z2);
		friend Zespolona operator - (const Zespolona &z1, const Zespolona &z2);
		friend Zespolona operator * (const Zespolona &z1, const Zespolona &z2);
		friend Zespolona operator / (const Zespolona &z1, const Zespolona &z2);
		friend bool operator == (const Zespolona &z1, const Zespolona &z2);
		
		friend ostream& operator << (ostream& out, const Zespolona &z);
		
};


#endif

