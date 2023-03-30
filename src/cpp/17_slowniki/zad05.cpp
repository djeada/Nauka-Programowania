/*
Tytul: Lista pracownikow z najwiekszymi zyskami.
Tresc: Otrzymujesz liste par. Pierwszym elementem pary jest napis reprezentujacy imie i nazwisko pracownika, drugim zysk z transakcji, jaka dany pracownik przeprowadzil. Znajdz pracownika, ktory przyniosl firmie najwiecej zysku.
Dane wejsciowe: Lista par napisow i liczb naturalnych.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanej listy:
[["Barnaba Barabash", 120],
["Jon Snow", 100],
["Kira Summer", 300],
["Barnaba Barabash", 200],
["Bob Marley", 110]]
zostanie zwrocony napis: “Barnaba Barabash”.

*/
#include <cassert>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

void wypelnijSlownik(const std::vector<std::pair<std::string, int>> &lista,
                     std::unordered_map<std::string, int> &slownik) {
  /*
   * Funkcja wypelnia slownik. W slowniku kluczem jest imie i nazwisko
   * pracownika, a wartoscia zysk.
   */

  for (const auto &rekord : lista)
    slownik[rekord.first] += rekord.second;
}

std::string znajdzMaxZysk(std::unordered_map<std::string, int> &slownik) {
  /*
   * Funkcja zwraca imie i nazwisko pracownika, ktory przyniosl najwiecej zysku.
   */
  std::string najlepszyPracownik;
  int maxZysk = -1;

  for (auto it = slownik.begin(); it != slownik.end(); it++) {
    if (it->second > maxZysk) {
      najlepszyPracownik = it->first;
      maxZysk = it->second;
    }
  }

  return najlepszyPracownik;
}

std::string pracownik(std::vector<std::pair<std::string, int>> &lista) {
  /*
   * Funkcja jest wrapper'em do funkcji znajdzMaxZysk.
   */

  if (lista.empty())
    return "";

  std::unordered_map<std::string, int> slownik;
  wypelnijSlownik(lista, slownik);

  return znajdzMaxZysk(slownik);
}

void test1() {

  std::vector<std::pair<std::string, int>> lista{{"Barnaba Barabash", 120},
                                                 {"Jon Snow", 100},
                                                 {"Kira Summer", 300},
                                                 {"Barnaba Barabash", 200},
                                                 {"Bob Marley", 110}};

  std::string wynik = "Barnaba Barabash";

  assert(pracownik(lista) == wynik);
}

void test2() {
  std::vector<std::pair<std::string, int>> lista;
  std::string wynik;

  assert(pracownik(lista) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

