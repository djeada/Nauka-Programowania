/*
Tytul: Rotacje napisow.
Tresc: Dostajesz dwa napisy. Sprawdz, czy jeden z nich jest rotacja drugiego.
Dane wejsciowe: Dwa napisy.
Dane wyjsciowe: Wartosc logiczna.
Przyklad:
Dla napisow "malpka" i "pkamal" powinno zostac zwrocone "Prawda".

*/
#include <algorithm>
#include <cassert>
#include <string>

bool czyRotacjaV1(std::string &s1, std::string &s2) {

  if (s1.length() != s2.length())
    return false;

  std::string pom = s1 + s1;

  return (pom.find(s2) != std::string::npos);
}

// Testy Poprawnosci
void test1() {
  std::string slowoA = "malpka";
  std::string slowoB = "kamapl";

  assert(!czyRotacjaV1(slowoA, slowoB));
}

void test2() {
  std::string slowoA = "malpka";
  std::string slowoB = "pkamal";

  assert(czyRotacjaV1(slowoA, slowoB));
}

int main() {

  test1();
  test2();

  return 0;
}

