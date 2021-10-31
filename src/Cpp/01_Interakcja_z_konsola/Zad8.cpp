#include <cmath>
#include <iostream>

/*
Otrzymujesz cenę i wymiary płytki oraz wymiary podłogi.
Oblicz ile będzie wynosiła cena podłogi o podanych wymiarach.
W zadaniu przyjmujemy, że podłoga jest prostokątem, a płytka kwadratem.
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
