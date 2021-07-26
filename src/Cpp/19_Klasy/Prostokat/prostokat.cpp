#include "prostokat.h"
#include <cmath>

Prostokat::Prostokat(double _lewo, double _prawo, double _gora, double _dol)
    : lewo(_lewo), prawo(_prawo), gora(_gora), dol(_dol) {}

double Prostokat::getLewo() { return lewo; }

double Prostokat::getPrawo() { return prawo; }

double Prostokat::getGora() { return gora; }

double Prostokat::getDol() { return dol; }

double Prostokat::poleCzesciWspolnej(Prostokat &innyProstokat) {
  double poleX = std::max(0.00, std::min(prawo, innyProstokat.getPrawo()) -
                                    std::max(lewo, innyProstokat.getLewo()));
  double poleY = std::max(0.00, std::min(gora, innyProstokat.getGora()) -
                                    std::max(dol, innyProstokat.getDol()));
  return poleX * poleY;
}
