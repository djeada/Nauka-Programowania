/*
Tytul: Napis skladajacy sie z liczb od 1 do n.
Tresc: Otrzymasz liczbe naturalna n. Zwroc napis skladajacy sie z liczb naturalnych od 1 do n.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanej liczby n rownej 3 powinien zostac zwrocony napis: "123".

*/
#include <algorithm>
#include <cassert>
#include <string>

std::string liczby(int n) {
  std::string wynik = "";

  for (int i = 1; i <= n; i++)
    wynik += std::to_string(i);

  return wynik;
}

void test1() {
  int n = 5;
  std::string wynik = "12345";
  assert(liczby(n) == wynik);
}

void test2() {
  int n = -1;
  std::string wynik = "";
  assert(liczby(n) == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}

