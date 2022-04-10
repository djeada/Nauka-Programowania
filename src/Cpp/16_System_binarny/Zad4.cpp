#include <cassert>
#include <cmath>
#include <vector>

/*
Otrzymujesz dziesietna reprezentacje liczby naturalnej.

a) Oblicz z ilu zer sklada sie binarna reprezentacja otrzymanej liczby.
b) Oblicz z ilu jedynek sklada sie binarna reprezentacja otrzymanej liczby.
*/

int zera(int n) {
    int licznik = 0;
    while (n > 0) {
        if (n % 2 == 0) {
            licznik++;
        }
        n /= 2;
    }
    return licznik;
}

int jedynki(int n) {
    int licznik = 0;
    while (n > 0) {
        if (n % 2 == 1) {
            licznik++;
        }
        n /= 2;
    }
    return licznik;
}

void test1() {
    int a = -2;
    int oczekiwane = 0;
    int wynik = zera(a);
    assert(wynik == oczekiwane);
}

void test2() {
    int a = 3;
    int oczekiwane = 2;
    int wynik = jedynki(a);
    assert(wynik == oczekiwane);
}

void test3() {
    int a = 3;
    int oczekiwane = 0;
    int wynik = zera(a);
    assert(wynik == oczekiwane);
}

void test4() {
    int a = 7;
    int oczekiwane = 3;
    int wynik = jedynki(a);
    assert(wynik == oczekiwane);
}

int main() {

  test1();
  test2();
  test3();
  test4();

  return 0;
}
