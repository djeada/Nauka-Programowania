/*
Tytul: Wybieranie minimum i maksimum.
Tresc: Otrzymujesz dwie liczby naturalne.
a) Zwroc mniejsza z nich. Zabronione jest uzycie instrukcji warunkowej oraz zewnetrznych bibliotek.
b) Zwroc wieksza z nich. Zabronione jest uzycie instrukcji warunkowej oraz zewnetrznych bibliotek.
Dane wejsciowe: Dwie liczby naturalne w obu podpunktach.
Dane wyjsciowe: Liczba naturalna w obu podpunktach.
Przyklad:
a) Dla otrzymanych liczb: 3 i 2, powinna zostac zwrocona liczba: 2.
b) Dla otrzymanych liczb: 3 i 2, powinna zostac zwrocona liczba: 3.

*/
#include <cassert>

int znak(int n) {
  /*
   * Funkcja zwraca znak liczby n.
   */
  return (n >> 31) & 0x01;
}

int maks(int a, int b) {
  /*
   * Funkcja zwraca maksimum dwoch liczb.
   * dla a >= b: znak_a = 1, znak_b = 0;
   * dla a < b: znak_a = 0, znak_b = 1;
   */
  int znakB = znak(a - b);
  int znakA = znakB ^ 1;
  return znakA * a + znakB * b;
}

int min(int a, int b) {
  /*
   * Funkcja zwraca minimum dwoch liczb.
   * dla a >= b: znak_a = 0, znak_b = 1;
   * dla a < b: znak_a = 1, znak_b = 0;
   */
  int znakB = znak(a - b);
  int znakA = znakB ^ 1;
  return znakB * a + znakA * b;
}

void testMaks() {
  int a = 10;
  int b = 8;
  int wynik = a;

  assert(maks(a, b) == wynik);
}

void testMin() {
  int a = 10;
  int b = 8;
  int wynik = b;

  assert(min(a, b) == wynik);
}

int main() {

  testMaks();
  testMin();

  return 0;
}

