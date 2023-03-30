/*
Tytul:  Sprawdz warunek
Napisz funkcje, ktora sprawdzi nastepujace warunki dla otrzymanych dwoch liczb:
a) Czy pierwsza liczba jest wieksza od drugiej liczby?
b) Czy suma liczb jest mniejsza niz 10?
c) Czy obie liczby sa nieparzyste?
d) Czy wieksza liczba jest mniejsza od pierwszej liczby podniesionej do
kwadratu? Dane wejsciowe: dwie liczby naturalne Dane wyjsciowe: cztery wartosci
logiczne, odpowiadajace na kazde z pytan Przyklad: Dla pobranych liczb 3 i 2,
funkcja powinna zwrocic nastepujace wartosci logiczne: a) Prawda b) Prawda c)
Falsz d) Prawda

*/
#include <cassert>
#include <cmath>

bool pierwszaWieksza(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba > drugaLiczba;
}

bool sumaMniejsza10(int pierwszaLiczba, int drugaLiczba) {
  int suma = pierwszaLiczba + drugaLiczba;
  return suma < 10;
}

bool obieNieparzyste(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba % 2 == 1 && drugaLiczba % 2 == 1;
}

int wieksza(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba > drugaLiczba ? pierwszaLiczba : drugaLiczba;
}

bool wiekszaMniejszaPierwszaKwadrat(int pierwszaLiczba, int drugaLiczba) {
  return wieksza(pierwszaLiczba, drugaLiczba) < pow(pierwszaLiczba, 2);
}

void testPierwszaWieksza() {
  assert(!pierwszaWieksza(1, 2));
  assert(pierwszaWieksza(2, 1));
}

void testSumaMniejsza10() {
  assert(!sumaMniejsza10(1, 2));
  assert(sumaMniejsza10(1, 9));
  assert(sumaMniejsza10(9, 1));
}

void testObieNieparzyste() {
  assert(!obieNieparzyste(1, 2));
  assert(obieNieparzyste(1, 1));
  assert(obieNieparzyste(2, 2));
}

void testWiekszaMniejszaPierwszaKwadrat() {
  assert(!wiekszaMniejszaPierwszaKwadrat(1, 2));
  assert(wiekszaMniejszaPierwszaKwadrat(2, 1));
  assert(wiekszaMniejszaPierwszaKwadrat(2, 2));
}

int main() {

  testPierwszaWieksza();
  testSumaMniejsza10();
  testObieNieparzyste();
  testWiekszaMniejszaPierwszaKwadrat();

  return 0;
}

