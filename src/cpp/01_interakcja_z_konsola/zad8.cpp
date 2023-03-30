/*
Tytul: Obliczenie ceny podlogi.
Tresc: Otrzymasz cene pojedynczej plytki, wymiary plytki w postaci kwadratu oraz
wymiary podlogi w postaci prostokata. Oblicz, ile kosztowac bedzie podloga o
podanych wymiarach. Jednostki sa umowne. Dane wejsciowe: Cztery liczby
naturalne: cena plytki, dlugosc boku plytki, dlugosc podlogi oraz szerokosc
podlogi. Dane wyjsciowe: Liczba naturalna oznaczajaca cene podlogi. Przyklad:
Dla pobranych liczb: 2 (cena plytki), 3 (dlugosc boku plytki), 20 (dlugosc
podlogi) oraz 40 (szerokosc podlogi), powinna zostac wypisana liczba: 196.

*/
#include <cmath>
#include <iostream>

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

