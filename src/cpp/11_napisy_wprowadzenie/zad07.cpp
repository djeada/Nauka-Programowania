/*
Tytul: Zamien znaki na kody ASCII.
Tresc: Otrzymasz napis. Zmien wszystkie znaki w napisie na odpowiadajace im numery w tablicy ASCII. Zastap otrzymany napis napisem skladajacym sie z otrzymanych numerow, oddzielonych przecinkami.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "Robot", powinien zostac zwrocony napis: "82, 111, 98, 111, 116".

*/
#include <algorithm>
#include <cassert>
#include <string>

void zamienV1(std::string &napis) {

  if (napis.empty())
    return;

  std::string wynik = "";

  for (int numer : napis)
    wynik += std::to_string(numer) + ", ";

  napis = wynik.substr(0, wynik.size() - 2);
}

void test1() {
  std::string napis = "pacZka!";
  std::string wynik = "112, 97, 99, 90, 107, 97, 33";

  zamienV1(napis);
  assert(napis == wynik);
}

void test2() {
  std::string napis = "";
  std::string wynik = "";

  zamienV1(napis);
  assert(napis == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}

