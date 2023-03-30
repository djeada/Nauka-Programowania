/*
Tytul: Zamien litery "a" na znaki zapytania.
Tresc: Otrzymasz napis. Zmien litery "a" na znaki zapytania.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "Latarnik", powinien zostac zwrocony napis: "L?t?rnik".

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

