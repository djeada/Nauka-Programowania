#include <iostream>

class Punkt {
	public:
		Punkt(double x = 0, double y = 0); 
		void setX(double x);
		void setY(double y);
		double getX();
		double getY();
		double odleglosc(Punkt& innyPunkt);
		friend std::ostream& operator << (std::ostream& out, Punkt& z);
		friend bool operator == (const Punkt& p1, const Punkt& p2);
		friend bool operator != (const Punkt& p1, const Punkt& p2);

	private:
		double x, y;
};
