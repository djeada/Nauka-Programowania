#include <iostream>

class Wektor {
public:
  Wektor(double x = 0, double y = 0, double z = 0);
  void setX(double x);
  void setY(double y);
  void setZ(double z);
  double getX();
  double getY();
  double getZ();
  double modul();
  friend Wektor operator+(const Wektor &w1, const Wektor &w2);
  friend Wektor operator-(const Wektor &w1, const Wektor &w2);
  friend Wektor operator*(const Wektor &w1, const Wektor &w2);
  friend std::ostream &operator<<(std::ostream &out, Wektor &w);
  friend bool operator==(const Wektor &p1, const Wektor &p2);
  friend bool operator!=(const Wektor &p1, const Wektor &p2);

private:
  double x, y, z;
};
