/*
Tytul: Sortowanie wzgledem kluczy/wartosci
Otrzymujesz slownik skladajacy sie z par napisow i liczb calkowitych. Twoim
zadaniem jest wypisanie par posortowanych wzgledem napisow oraz wzgledem liczb.
Dane wejsciowe: Slownik par: napis, liczba calkowita.
Dane wyjsciowe: Lista par.
Przyklad:
Dla otrzymanego slownika: {"c": 3, "x": 5, "a": -2, "b": 4}, powinien zostac
zwrocony slownik: [("a", -2), ("b", 4), ("c", 3), ("x", 5)]. Dla otrzymanego
slownika: {"c": 3, "x": 5, "a": -2, "b": 4}, powinien zostac zwrocony slownik:
[("a", -2), ("c", 3), ("b", 4), ("x", 5)].

*/
#include <cassert>
#include <string>
#include <unordered_map>

std::unordered_map<char, int> budujSlownik(const std::string &slowo) {
  /*
   * Tworzymy slownik, ktory bedzie przechowywal informacje o ilosci wystapien
   * liter w slowie.
   */
  std::unordered_map<char, int> slownik;

  for (const auto &znak : slowo)
    if (tolower(isalpha(znak)))
      slownik[znak]++;

  return slownik;
}

char litera(const std::string &slowo) {
  /*
   * Zwraca najczesciej wystepujaca litere w napisie.
   */
  std::unordered_map<char, int> histogram = budujSlownik(slowo);

  int max = -1;
  char maxLitera = '\0';

  for (auto &litera : slowo) {
    if (histogram[litera] > max) {
      maxLitera = litera;
      max = histogram[litera];
    }
  }

  return maxLitera;
}

void test1() {
  std::string slowo = "lezy jerzy na wiezy";
  char wynik = 'e';

  assert(litera(slowo) == wynik);
}

void test2() {
  std::string slowo = "The most intelligent people disguise the fact that they "
                      "are intelligent. Wise men do not wear name tags., "
                      "The more people talk about their own skills, the more "
                      "desperate they are--their work should speak for itself.";
  char wynik = 'e';

  assert(litera(slowo) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

