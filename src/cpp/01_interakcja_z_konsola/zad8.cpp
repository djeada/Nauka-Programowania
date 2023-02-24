#include <cmath>
#include <iostream>

/*
Otrzymujesz cene i wymiary plytki oraz wymiary podlogi.
Oblicz ile bedzie wynosila cena podlogi o podanych wymiarach.
W zadaniu przyjmujemy, ze podloga jest prostokatem, a plytka kwadratem.
*/

int main() {

  std::cout << "podaj: cene plytki, dlugosc boku plytki i wymiary podlogi"
            << std::endl;

  int cena;
  int bokPlytki;
  int szerokoscPodlogi;
  int dlugoscPodlogi;

  std::cin >> cena;
  std::cin >> bokPlytki;
  std::cin >> szerokoscPodlogi;
  std::cin >> dlugoscPodlogi;

  int szerokoscKonieczna =
      szerokoscPodlogi + bokPlytki - szerokoscPodlogi % bokPlytki;
  int dlugoscKonieczna =
      dlugoscPodlogi + bokPlytki - dlugoscPodlogi % bokPlytki;

  int polePlytki = pow(bokPlytki, 2);
  int polePodlogi = szerokoscKonieczna * dlugoscKonieczna;

  float calkowityKoszt = cena * (float)polePodlogi / polePlytki;

  std::cout << "Dla plytki o dlugosci boku " << bokPlytki << "i ceny " << cena
            << " calkowity koszt wylozenia podlogi o wymiarach "
            << szerokoscPodlogi << "x" << dlugoscPodlogi << " wynosi "
            << calkowityKoszt << std::endl;

  return 0;
}
