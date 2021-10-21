#include <cmath>
#include <iostream>

class Punkt {
public:
  Punkt(double _x, double _y) : x(_x), y(_y) {}

  void setX(double _x) { x = _x; }

  void setY(double _y) { y = _y; }

  double getX() { return x; }

  double getY() { return y; }

  double odleglosc(Punkt &innyPunkt) {
    double odlegloscX = x - innyPunkt.getX();
    double odlegloscY = y - innyPunkt.getY();

    return sqrt(pow(odlegloscX, 2) + pow(odlegloscY, 2));
  }

  friend std::ostream &operator<<(std::ostream &out, Punkt &p) {
    std::cout << "X = " << p.x << std::endl;
    std::cout << "Y = " << p.y << std::endl;
    return out;
  }

  friend bool operator==(const Punkt &p1, const Punkt &p2) {
    return p1.x == p2.x && p1.y == p2.y;
  }

  friend bool operator!=(const Punkt &p1, const Punkt &p2) {
    return p1.x != p2.x || p1.y != p2.y;
  }

private:
  double x, y;
};

int main() {

  Punkt punktA(5, 5);
  Punkt punktB(-3, -3);

  std::cout << "Odleglosc miedzy punktem A \n"
            << punktA << "a punktem B \n"
            << punktB << "wynosi: " << punktA.odleglosc(punktB) << std::endl;

  return 0;
}
