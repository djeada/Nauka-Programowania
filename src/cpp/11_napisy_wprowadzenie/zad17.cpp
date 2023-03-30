/*
Tytul: Wczytaj i rozdziel informacje o pracowniku.
Tresc: Otrzymasz rekord z bazy danych reprezentujacy dane pracownika. Sa to
kolejno: imie, nazwisko, miejsce urodzenia, stanowisko i zarobki. Informacje sa
rozdzielone srednikami. Zapisz je w osobnych zmiennych i wypisz je razem z
odpowiednimi komunikatami. Dane wejsciowe: Napis. Dane wyjsciowe: Lista napisow.
Przyklad:
Dla otrzymanego napisu:
"Jan; Kowalski; Warszawa; Programista; 1000;",
powinna zostac zwrocona lista:
["Imie: Jan", "Nazwisko: Kowalski", "Miejsce urodzenia: Warszawa", "Zawod:
Programista", "Zarobki: 1000"].

*/
#include <algorithm>
#include <cassert>
#include <string>
#include <vector>

std::string liczby(const std::vector<int> &lista) {
  std::string wynik = "";

  for (auto liczba : lista)
    wynik += std::to_string(liczba);

  return wynik;
}

void test1() {
  std::vector<int> lista({2, 4, 7});
  std::string wynik = "247";
  assert(liczby(lista) == wynik);
}

void test2() {
  std::vector<int> lista;
  std::string wynik = "";
  assert(liczby(lista) == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}

