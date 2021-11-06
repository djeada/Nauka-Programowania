#include <cassert>
#include <cmath>
#include <vector>

/*
Otrzymujesz dziesiętną reprezentację liczby naturalnej. 

a) Oblicz z ilu zer składa się binarna reprezentacja otrzymanej liczby.
b) Oblicz z ilu jedynek składa się binarna reprezentacja otrzymanej liczby.
*/

int policzUstawioneBity(int liczba) {
  /*
  * Funkcja zwraca ilosc ustawionych bitow w liczbie.
  */
  int suma = 0;

  while (liczba > 0) {
    if (liczba & 1)
      suma++;
    liczba >>= 1;
  }

  return suma;
}

void przygotujTablice(std::vector<int> &tablica) {
  /*
  * Funkcja wypelnia tablice zawierajaca ilosc ustawionych bitow dla kazdej liczby w zakresie 0-255.
  */
  tablica.clear();

  for (int i = 0; i < 256; i++)
    tablica.push_back(policzUstawioneBity(i));
}

int liczbaBitow(int liczba) { 
  /*
  * Funkcja zwraca ilosc bitow w liczbie.
  */
  return (int)log2(liczba) + 1;
}

int zera(int liczba, std::vector<int> &tablica) {
  /*
  * Funkcja zwraca ilosc zer w binarnej reprezentacji liczby.
  */
  return liczbaBitow(liczba) - tablica[liczba & 0xff] +
         tablica[(liczba >> 8) & 0xff] + tablica[(liczba >> 16) & 0xff] +
         tablica[(liczba >> 24) & 0xff];
}

int jedynki(int liczba, std::vector<int> &tablica) {
  /*
  * Funkcja zwraca ilosc jedynek w binarnej reprezentacji liczby.
  */
  return tablica[liczba & 0xff] + tablica[(liczba >> 8) & 0xff] +
         tablica[(liczba >> 16) & 0xff] + tablica[(liczba >> 24) & 0xff];
}

void test1(std::vector<int> &tablica) {
  int liczba = 10;
  int wynik = 2;

  assert(jedynki(liczba, tablica) == wynik);
}

void test2(std::vector<int> &tablica) {
  int liczba = 7;
  int wynik = 3;

  assert(jedynki(liczba, tablica) == wynik);
}

void test3(std::vector<int> &tablica) {
  int liczba = 10;
  int wynik = 2;

  assert(zera(liczba, tablica) == wynik);
}

void test4(std::vector<int> &tablica) {
  int liczba = 7;
  int wynik = 0;

  assert(zera(liczba, tablica) == wynik);
}

int main() {

  std::vector<int> tablica;
  przygotujTablice(tablica);

  test1(tablica);
  test2(tablica);
  test3(tablica);
  test4(tablica);

  return 0;
}
