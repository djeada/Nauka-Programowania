#include <cassert>

/*
Otrzymujesz dwie liczby naturalne. 

a) Zwróć mniejszą liczbę. Zabronione jest użycie instrukcji 
warunkowej i zewnętrznych bibliotek.
b) Zwróć większą liczbę. Zabronione jest użycie instrukcji 
warunkowej i zewnętrznych bibliotek.
*/

int znak(int n) { 
  /*
  * Funkcja zwraca znak liczby n.
  */
 return (n >> 31) & 0x01; 
}

int maks(int a, int b) {
  /*
  * Funkcja zwraca maksimum dwóch liczb.
  * dla a >= b: znak_a = 1, znak_b = 0;
  * dla a < b: znak_a = 0, znak_b = 1;
  */
  int znakB = znak(a - b);
  int znakA = znakB ^ 1;
  return znakA * a + znakB * b;
}

int min(int a, int b) {
  /*
  * Funkcja zwraca minimum dwóch liczb.
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
