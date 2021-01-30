#include <iostream>

class Kolo {
	public:
		Kolo(double r = 1); 
		void setPromien(double r); 
		double getPromien();
		double pole();
		double obwod();
		double srednica();
		friend std::ostream& operator << (std::ostream& out, Kolo& z);

	private:
		double promien;
};
