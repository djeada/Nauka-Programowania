/*
Tytul: Slownik z kluczami bedacymi liczbami naturalnymi i wartosciami ich
kwadratami. Tresc: Dostajesz liczbe naturalna. Stworz slownik, w ktorym kluczami
beda kolejne liczby naturalne mniejsze od otrzymanej liczby, a wartosciami beda
ich kwadraty. Dane wejsciowe: Liczba naturalna. Dane wyjsciowe: Slownik z
kluczami i wartosciami bedacymi liczbami naturalnymi. Przyklad: Dla liczby 5,
slownik powinien wygladac nastepujaco: {1: 1, 2: 4, 3: 9, 4: 16}.

*/
#include <cassert>
#include <cmath>
#include <unordered_map>

std::unordered_map<int, int> budujSlownik(int liczba) {
  /*
   * Funkcja tworzy slownik zawierajacy klucze bedace kolejnymi
   * liczbami naturalnymi mniejszymi od podanej liczby n
   * oraz wartosci bedacymi kwadratami kluczy.
   */
  std::unordered_map<int, int> slownik;

  for (int i = 1; i < liczba; i++)
    slownik[i] = pow(i, 2);

  return slownik;
}

void test1() {
  int liczba = 5;
  std::unordered_map<int, int> wynik{{1, 1}, {2, 4}, {3, 9}, {4, 16}};

  assert(budujSlownik(liczba) == wynik);
}

void test2() {
  int liczba = -1;
  std::unordered_map<int, int> wynik;

  assert(budujSlownik(liczba) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

