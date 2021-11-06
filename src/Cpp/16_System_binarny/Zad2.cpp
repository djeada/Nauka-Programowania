#include <cassert>
#include <cmath>
#include <string>

/*
Otrzymujesz liczbę naturalną. Zwróć binarną 
reprezentację otrzymanej liczby jeśli:

a) Otrzymana liczba jest liczbą parzystą.
b) Otrzymana liczba jest liczbą pierwszą.
*/

std::string naBinarny(int liczba) {
  /*
  * Funkcja zamienia liczbę dziesiętną na binarną.
  */
  std::string bin;

  while (liczba > 0) {
    bin.insert(0, std::to_string(liczba % 2));
    liczba /= 2;
  }

  return bin;
}

std::string zamienLiczbeParzysta(int liczba) {
  /*
  * Funkcja zamienia liczbę parzystą na liczbę binarną.
  */
  if (liczba % 2 == 0)
    return naBinarny(liczba);

  return "";
}

bool czyPierwsza(int n) {
  /*
  *  Funkcja sprawdza czy liczba jest pierwsza.
  */
  if (n <= 1)
    return false;

  if (n % 2 == 0 && n != 2)
    return false;

  for (int i = 3; i <= std::sqrt((double)n); i += 2) {
    if (n % i == 0)
      return false;
  }

  return true;
}

std::string zamienLiczbePierwsza(int liczba) {
  /*
  * Funkcja zamienia liczbę pierwszą na liczbę binarną.
  */
  if (czyPierwsza(liczba))
    return naBinarny(liczba);

  return "";
}

void test1() {
  int liczba = 3;
  std::string wynik;

  assert(zamienLiczbeParzysta(liczba) == wynik);
}

void test2() {
  int liczba = 124;
  std::string wynik = "1111100";

  assert(zamienLiczbeParzysta(liczba) == wynik);
}

void test3() {
  int liczba = 124;
  std::string wynik;

  assert(zamienLiczbePierwsza(liczba) == wynik);
}

void test4() {
  int liczba = 3;
  std::string wynik = "11";

  assert(zamienLiczbePierwsza(liczba) == wynik);
}

int main() {

  test1();
  test2();
  test3();
  test4();

  return 0;
}
