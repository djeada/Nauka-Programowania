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

void zamienV1(std::string &napis) {

  for (auto &znak : napis) {
    if (znak == 'a')
      znak = '?';
  }
}

void zamienV2(std::string &napis) {
  replace(napis.begin(), napis.end(), 'a', '?');
}

void test1() {
  std::string napis = "pacZka!";
  std::string wynik = "p?cZk?!";

  zamienV1(napis);
  assert(napis == wynik);
}

void test2() {
  std::string napis = "pacZka!";
  std::string wynik = "p?cZk?!";

  zamienV2(napis);
  assert(napis == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}

