/*
Tytul: Sznurek.
Tresc: Masz do sprzedania sznurek o dlugosci n, a takze liste cen dla sznurkow o dlugosciach od 1 do n. Ceny moga byc rozne dla roznych dlugosci. Znajdz maksymalny zysk, ktory mozna osiagnac poprzez sprzedaz danego sznurka.
Dane wejsciowe: Lista n liczb calkowitych reprezentujacych ceny dla sznurkow o dlugosciach od 1 do n, oraz liczba naturalna n reprezentujaca dlugosc sznurka, ktory chcesz sprzedac.
Dane wyjsciowe: Najwieksza mozliwa wartosc, jaka mozna uzyskac ze sprzedazy danego sznurka.
Przyklad:
Dla listy cen: [1, 5, 8, 9, 10, 17, 17, 20] oraz dlugosci sznurka 4, powinna zostac zwrocona liczba 10.

*/
#include <cassert>
#include <stdexcept>
#include <vector>

// Zlozonosc czasowa O(n^n)
// Zlozonosc pamieciowa O(1)
int podzielSznurekV1(std::vector<int> &ceny, int n) {

  if (ceny.size() < n)
    throw std::invalid_argument("Dlugosc sznurka do sprzedazy nie moze byc "
                                "wieksza od liczby elementow listy ceny.");

  if (n == 0)
    return 0;

  auto maks = 0;

  for (auto i = 0; i < n; i++) {
    auto cena = ceny[i] + podzielSznurekV1(ceny, n - i - 1);

    if (cena > maks)
      maks = cena;
  }

  return maks;
}

// Zlozonosc czasowa O(n^2)
// Zlozonosc pamieciowa O(n)
int podzielSznurekV2(std::vector<int> &ceny, int n) {

  if (ceny.size() < n)
    throw std::invalid_argument("Dlugosc sznurka do sprzedazy nie moze byc "
                                "wieksza od liczby elementow listy ceny.");

  std::vector<int> pom(n + 1, 0);

  for (auto i = 0; i < n; i++) {
    for (auto j = 0; j < i + 1; j++)
      pom[i + 1] = std::max(pom[i + 1], ceny[j] + pom[i - j]);
  }

  return pom[n];
}

// Testy Poprawnosci
void test1() {
  std::vector<int> lista{1, 5, 8, 9, 10, 17, 17, 20};
  auto n = 4;
  auto wynik = 10;

  assert(podzielSznurekV1(lista, n) == wynik);
  assert(podzielSznurekV2(lista, n) == wynik);
}

void test2() {
  std::vector<int> lista{3, 9, 10, 20};
  auto n = 5;

  for (auto funkcja : std::vector<int (*)(std::vector<int> &, int)>(
           {podzielSznurekV1, podzielSznurekV2})) {
    try {
      funkcja(lista, n);
      assert(false);
    } catch (...) {
      assert(true);
    }
  }
}

void test3() {
  std::vector<int> lista{5};
  auto n = 1;
  auto wynik = 5;

  assert(podzielSznurekV1(lista, n) == wynik);
  assert(podzielSznurekV2(lista, n) == wynik);
}

int main() {

  test1();
  test2();
  test3();

  return 0;
}

